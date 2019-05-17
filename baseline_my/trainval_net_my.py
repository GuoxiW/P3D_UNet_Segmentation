import _init_paths
import numpy as np
import argparse
import pprint
import time
import torch
import torch.nn as nn
import torch.backends.cudnn as cudnn

from lib.dataset.roi_data_loader.roi_batch_loader import RoiBatchLoader
from model.utils.config import cfg, cfg_from_file, cfg_from_list, get_output_dir
from model.utils.net_utils import adjust_learning_rate, save_checkpoint, get_roidb, create_folder, save_model, resume_model

from model.tcnn.c3d import C3D, c3d_tcnn


def parse_args(is_show=False):
    """
    Parse input arguments
    """
    parser = argparse.ArgumentParser(description='Train a R-C3D network')
    parser.add_argument('--dataset', dest='dataset',default='thumos14', type=str, choices=['thumos14', 'activitynet'],
                      help='training dataset')
    parser.add_argument('--net', dest='net',default='c3d', type=str, choices=['c3d', 'res18', 'res34', 'res50', 'eco'],
                      help='main network c3d, i3d, res34, res50')
    parser.add_argument('--start_epoch', dest='start_epoch', default=1, type=int,
                      help='starting epoch')
    parser.add_argument('--epochs', dest='max_epochs', default=8, type=int,
                      help='number of epochs to train')
    parser.add_argument('--disp_interval', default=100, type=int,
                      help='number of iterations to display')
    parser.add_argument('--save_dir', default="./models",nargs=argparse.REMAINDER,
                      help='directory to save models')
    parser.add_argument('--output_dir',default="./output",nargs=argparse.REMAINDER,
                      help='directory to save log file')
    parser.add_argument('--nw', dest='num_workers', default=12, type=int,
                      help='number of worker to load data')
    parser.add_argument('--gpus', dest='gpus', nargs='+', type=int, default=0,
                      help='gpu ids.')
    parser.add_argument('--bs', dest='batch_size', default=1, type=int,
                      help='batch_size')
    parser.add_argument('--roidb_dir', dest='roidb_dir',default="./experiments/dataset",
                      help='roidb_dir')

    # config optimization
    parser.add_argument('--o', dest='optimizer',default="sgd", type=str,
                      help='training optimizer')
    parser.add_argument('--lr', dest='lr', default=0.0001, type=float,
                      help='starting learning rate')
    parser.add_argument('--lr_decay_step', dest='lr_decay_step', default=6, type=int,
                      help='step to do learning rate decay, unit is epoch')
    parser.add_argument('--lr_decay_gamma', dest='lr_decay_gamma', default=0.1, type=float,
                      help='learning rate decay ratio')

    # set training session
    parser.add_argument('--s', dest='session', default=1, type=int,
                      help='training session')

    # resume trained model
    parser.add_argument('--resume',default=False, action='store_true',
                      help='resume checkpoint or not')
    parser.add_argument('--checksession', default=1, type=int,
                      help='checksession to load model')
    parser.add_argument('--checkepoch', default=8, type=int,
                      help='checkepoch to load model')
    parser.add_argument('--checkpoint', default=9388, type=int,
                      help='checkpoint to load model')
    # log and display
    parser.add_argument('--use_tfboard',default=False, action='store_true',
                      help='whether use tensorflow tensorboard')

    args = parser.parse_args()
    if is_show:
        print('Called with args:')
        print(args)
    return args


def train_net(tcnn_model, dataloader, optimizer, args):
    tcnn_model.train()
    loss_temp = 0
    start = time.time()

    data_start = time.time()
    for step, (video_data, gt_twins, num_gt) in enumerate(dataloader):
        video_data = video_data.cuda()
        gt_twins = gt_twins.cuda()
        data_time = time.time() - data_start

        tcnn_model.zero_grad()
        rois, cls_prob, twin_pred, rpn_loss_cls, rpn_loss_twin, \
        RCNN_loss_cls, RCNN_loss_twin, rois_label = tcnn_model(video_data, gt_twins)
        loss = rpn_loss_cls.mean() + rpn_loss_twin.mean() \
               + RCNN_loss_cls.mean() + RCNN_loss_twin.mean()
        loss_temp += loss.item()

        # backward
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if step % args.disp_interval == 0:
            end = time.time()
            if step > 0:
                loss_temp /= args.disp_interval

            loss_rpn_cls = rpn_loss_cls.mean().item()
            loss_rpn_twin = rpn_loss_twin.mean().item()
            loss_rcnn_cls = RCNN_loss_cls.mean().item()
            loss_rcnn_twin = RCNN_loss_twin.mean().item()
            fg_cnt = torch.sum(rois_label.data.ne(0))
            bg_cnt = rois_label.data.numel() - fg_cnt
            gt_cnt = num_gt.sum().item()

            print("[session %d][epoch %2d][iter %4d/%4d] loss: %.4f, lr: %.2e" \
                  % (args.session, args.epoch, step + 1, len(dataloader), loss_temp, args.lr))
            print("\t\t\tfg/bg=(%d/%d), gt_twins: %d, time cost: %f" % (fg_cnt, bg_cnt, gt_cnt, end - start))
            print("\t\t\trpn_cls: %.4f, rpn_twin: %.4f, rcnn_cls: %.4f, rcnn_twin %.4f" \
                  % (loss_rpn_cls, loss_rpn_twin, loss_rcnn_cls, loss_rcnn_twin))
            print("one step data time: %.4f" % (data_time))

            loss_temp = 0
            start = time.time()
        data_start = time.time()

    end = time.time()
    print(end - start)


if __name__ == '__main__':
    args = parse_args(is_show=True)

    cfg.CUDA = True
    cfg.USE_GPU_NMS = True
    cudnn.benchmark = True

    if args.dataset == "thumos14":
        args.imdb_name = "train_data_25fps_flipped.pkl"
        args.imdbval_name = "val_data_25fps.pkl"
        args.num_classes = 21
        args.set_cfgs = ['ANCHOR_SCALES', '[2,4,5,6,8,9,10,12,14,16]', 'NUM_CLASSES', args.num_classes]
    else:
        raise ValueError('Current only do experiment on THUMOS14')

    args.cfg_file = "./lib/model/cfgs/{}_{}.yml".format(args.net, args.dataset)
    if args.cfg_file is not None:
        cfg_from_file(args.cfg_file)
    if args.set_cfgs is not None:
        cfg_from_list(args.set_cfgs)
    print('Using config:')
    pprint.pprint(cfg)

    # for reproduce
    np.random.seed(cfg.RNG_SEED)
    torch.manual_seed(cfg.RNG_SEED)
    if cfg.CUDA:
        torch.cuda.manual_seed_all(cfg.RNG_SEED)

    # train set
    roidb_path = args.roidb_dir + "/" + args.dataset + "/" + args.imdb_name
    roidb = get_roidb(roidb_path)
    print('{:d} roidb entries'.format(len(roidb)))

    model_dir = create_folder(args)

    dataset = RoiBatchLoader(roidb)
    dataloader = torch.utils.data.DataLoader(dataset, batch_size=args.batch_size,
                                             num_workers=args.num_workers, shuffle=True)

    # initilize the network here.
    if args.net == 'c3d':
        tcnn_model = c3d_tcnn(pretrained=True)
    else:
        raise ValueError('Current only use C3D backbone')

    tcnn_model.create_architecture()
    print(tcnn_model)

    params = []
    for key, value in dict(tcnn_model.named_parameters()).items():
        if value.requires_grad:
            print(key)
            if 'bias' in key:
                params += [{'params': [value], 'lr': args.lr * (cfg.TRAIN.DOUBLE_BIAS + 1),
                            'weight_decay': cfg.TRAIN.BIAS_DECAY and cfg.TRAIN.WEIGHT_DECAY or 0}]
            else:
                params += [{'params': [value], 'lr': args.lr, 'weight_decay': cfg.TRAIN.WEIGHT_DECAY}]

    if args.optimizer == "adam":
        args.lr = args.lr * 0.1
        optimizer = torch.optim.Adam(params)
    elif args.optimizer == "sgd":
        optimizer = torch.optim.SGD(params, momentum=cfg.TRAIN.MOMENTUM)

    if args.resume:
        tcnn_model, optimizer, args = resume_model(args, model_dir, tcnn_model, params)

    if torch.cuda.is_available():
        tcnn_model = tcnn_model.cuda()
        if isinstance(args.gpus, int):
            args.gpus = [args.gpus]
        tcnn_model = nn.parallel.DataParallel(tcnn_model, device_ids=args.gpus)

    for epoch in range(args.start_epoch, args.max_epochs + 1):
        if epoch % (args.lr_decay_step + 1) == 0:
            adjust_learning_rate(optimizer, args.lr_decay_gamma)
            args.lr *= args.lr_decay_gamma

        args.epoch = epoch
        train_net(tcnn_model, dataloader, optimizer, args)

        save_model(args, model_dir, epoch, tcnn_model, optimizer, len(dataloader))


