import torch
import torch.nn as nn
import torch.optim as optim
import os
import shutil
import time

import dataset
from transforms.spatial_transforms import Compose, Normalize, Scale, ToTensor
import network_cla
import network_seg
import utils
import experiment
import joint_transforms


def main():

    # parameters
    # ???should we adjust the learning rate during the training process? ???
    learn_rate = 1e-4
    num_epochs = 600  # 最大迭代次数
    max_patience = 60  # 停止训练的参数
    result_rp = '/data1/guoxi/p3d_floder/result/model/'
    exp_name = 'P3D_saliency'

    batch_size = 4
    n_threads = 16
    # 'Temporal duration of inputs'
    sample_duration = 16
    # the data for devison
    norm_value = 255
    # Height and width of inputs
    sample_size = 224
    # Number of validation samples for each activity
    n_val_samples = 3
    video_path = '/data1/guoxi/p3d_floder/dataset/'
    mean = [0.485, 0.456, 0.406]
    std = [0.229, 0.224, 0.225]

    norm_method = Normalize(mean, std)
    train_joint_transform = Compose([  # 图像预处理一般用Compose把多个步骤整合到一起
        # mask_loader????
        joint_transforms.JointResize(256),  # 把给定的图片resize到given size 'JpegImageFile' object is not iterable
        joint_transforms.JointRandomCrop(224),  # 在一个随机的位置进行裁剪  'JpegImageFile' object does not support indexing
        joint_transforms.JointRandomHorizontalFlip(),  # 以0.5的概率水平翻转给定的PIL图像
    ])

    spatial_transform = Compose([
                                 # Scale((sample_size, sample_size)),
                                 ToTensor(norm_value=norm_value),
                                 norm_method
    ])  # 空间变换

    target_transform = Compose([
                                # Scale((sample_size, sample_size)),
                                ToTensor(norm_value=norm_value)
    ])

    clip_transform = Compose([
         joint_transforms.RandomErase(probability=0.5, sh=0.4, r1=0.3)
    ])

    opt = [video_path, sample_duration]

    train_data = dataset.get_training_set(opt, spatial_transform, target_transform, train_joint_transform, clip_transform)
    train_loader = torch.utils.data.DataLoader(train_data, batch_size=batch_size, shuffle=True, num_workers=n_threads, pin_memory=True)  # 使用多进程加载的进程数 是否将数据保存在pin memory区，pin memory中的数据转到GPU会快一些
    validation_data = dataset.get_validation_set(opt, spatial_transform, target_transform)
    val_loader = torch.utils.data.DataLoader(validation_data, batch_size=batch_size, shuffle=False, num_workers=n_threads, pin_memory=True)


    inputs, targets = next(iter(train_loader))
    print('inputs.size(), inputs.min(), inputs.max()', inputs.size(), inputs.min(), inputs.max())
    print('targets.size(), targets.min(), targets.max():', targets.size(), targets.min(), targets.max())

    # every time we load weights, which may be slow
    model_cla = network_cla.P3D199(pretrained=True, num_classes=400)
    cla_dict = model_cla.state_dict()

    model = network_seg.P3D199()
    # model.apply(utils.weights_init)
    seg_dict = model.state_dict()

    pretrained_dict = {k: v for k, v in cla_dict.items() if k in seg_dict}
    seg_dict.update(pretrained_dict)
    model.load_state_dict(seg_dict)
    model.cuda()

    commen_layers = ['conv1_custom','bn1','relu','maxpool','maxpool_2','layer1','layer2','layer3']
    # seperate layers, to set different lr
    param_exist = []
    param_add = []
    for k, (name, module) in enumerate(model.named_children()):
        # existing layers
        if name in commen_layers:
            # print('existing layer: ', name)
            for param in module.parameters():
                param_exist.append(param)
        # adding layers
        else:
            # print('adding layer: ', name)
            for param in module.parameters():
                param_add.append(param)
    print('  + Number of params: {}'.format(
        sum([p.data.nelement() for p in model.parameters()])))

    optimizer = optim.Adam([{'params': param_exist, 'lr': learn_rate * 0.1}, {'params': param_add}])
    criterion = nn.BCELoss().cuda()

    exp_dir = result_rp + exp_name
    ##!!! existing directory will be removed
    if os.path.exists(exp_dir):
        shutil.rmtree(exp_dir)

    exp = experiment.Experiment(exp_name, result_rp)
    exp.init()

    for epoch in range(num_epochs):

        since = time.time()

        # ### Train ###
        trn_loss = utils.train(model, train_loader, optimizer, criterion)
        print('Epoch {:d}: Train - Loss: {:.4f}'.format(epoch, trn_loss))
        time_elapsed = time.time() - since
        print('Train Time {:.0f}m {:.0f}s'.format(
            time_elapsed // 60, time_elapsed % 60))

        ### Test ###
        val_loss = utils.test(model, val_loader, criterion)
        print('Val - Loss: {:.4f}'.format(val_loss))
        time_elapsed = time.time() - since
        print('Total Time {:.0f}m {:.0f}s\n'.format(
            time_elapsed // 60, time_elapsed % 60))

        ### Save Metrics ###
        exp.save_history('train', trn_loss)
        exp.save_history('val', val_loss)

        ### Checkpoint ###
        exp.save_weights(model, trn_loss, val_loss)
        exp.save_optimizer(optimizer, val_loss)

        ## Early Stopping ##
        if (epoch - exp.best_val_loss_epoch) > max_patience:
            print(("Early stopping at epoch %d since no "
                   + "better loss found since epoch %.3").format(epoch, exp.best_val_loss))
            break

        exp.epoch += 1



if __name__ == '__main__':
    main()
