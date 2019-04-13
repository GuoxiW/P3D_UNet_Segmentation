import torch
import torch.nn as nn
import os
import numpy as np
from PIL import Image

import dataset
from transforms.spatial_transforms import Compose, Normalize, ToTensor
import network_seg

# save_path
# model

weights_fol_rp = '../result/model/P3D_saliency/weights/'
weights_set = os.listdir(weights_fol_rp)
weights_set.sort()

for weights in weights_set:

    if len(weights) < 27:  # 用于除去optimizer以及best.pth
        continue
    weights_order = weights.split('-')[2]
    save_path = '../result/mask_matlab_all_list/' + str(weights_order) + '/'
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    weight_path = weights_fol_rp + weights
    batch_size = 1
    n_threads = 1
    # 'Temporal duration of inputs'
    sample_duration = 16
    # the data for devision
    norm_value = 255
    # Height and width of inputs
    # sample_size = 224
    # 因为dataset已经resize过，不用resize了
    # Number of validation samples for each activity
    n_val_samples = 3
    video_path = '/data1/guoxi/p3d_floder/resized_dataset/dataset/'
    mean = [0.485, 0.456, 0.406]
    std = [0.229, 0.224, 0.225]

    norm_method = Normalize(mean, std)
    spatial_transform = Compose([ToTensor(norm_value=norm_value), norm_method])
    # temporal_transform = LoopPadding(sample_duration)  # padding transform 如果不够16帧扩容到16帧
    target_transform = Compose([ToTensor(norm_value=norm_value)])
    opt = [video_path, sample_duration]

    test_data = dataset.get_test_set(opt, spatial_transform, target_transform, split='val')
    test_loader = torch.utils.data.DataLoader(test_data, batch_size=batch_size, shuffle=False, num_workers=n_threads, pin_memory=True)



    model = network_seg.P3D199()
    model = torch.nn.DataParallel(model)
    state_dict = torch.load(weight_path)
    model.load_state_dict(state_dict['state_dict'])
    model = model.cuda()
    model.eval()

    for clip_sets, name_video, names_frames, total_mask in test_loader:
        # print('clip_sets = ')
        # print(clip_sets)
        # print('name_video = ')
        # print(name_video)
        # print('names_frames = ')
        # print(names_frames)

        # result

        # clip_sets =[tensor([[[[[0.6049, 0.9817, 1.2214, ..., -0.9534, -0.9705, -1.0562],....
        # name_video =['d2857f0faa']
        # names_frames =[['00000'], ['00005'], ['00010'], ['00015'], ['00020'], ['00025'], ['00030'], ['00035'], ['00040'], ['00045'],
        #  ['00050'], ['00055'], ['00060'], ['00065'], ['00070'], ['00075'], ['00080'], ['00085'], ['00090'], ['00095'],
        #  ['00100'], ['00105'], ['00110'], ['00115'], ['00120'], ['00125'], ['00130'], ['00135'], ['00140'], ['00145'],
        #  ['00150'], ['00155'], ['00160'], ['00165'], ['00170'], ['00175']]


        for iord, clip_set in enumerate(clip_sets[:-1]):  #i_order

            for mask_tol_num, clip in enumerate(clip_set):

                with torch.no_grad():
                    masks = model(clip.cuda())

                masks.squeeze_()

                for j in range(sample_duration):
                    order = iord * sample_duration + j
                    mask_path = save_path + name_video[0] + '/' + str(mask_tol_num + 1) + '/'
                    if not os.path.exists(mask_path):
                        os.makedirs(mask_path)
                    mask_save_path = mask_path + names_frames[order][0] + '.png'
                    mask = masks[j, :, :]
                    mask_numpy = mask.data.cpu().numpy()
                    mask_numpy = mask_numpy * 255
                    mask_numpy = mask_numpy.astype(np.uint8)
                    pure_mask = Image.fromarray(mask_numpy, mode='L')
                    pure_mask.save(mask_save_path)
        # dispose the last clip
        clip_set = clip_sets[-1]
        for mask_tol_num, clip in enumerate(clip_set):

            with torch.no_grad():
                masks = model(clip.cuda())
            masks.squeeze_()
            for j in range(-1, -1-sample_duration, -1):
                mask_path = save_path + name_video[0] + '/' + str(mask_tol_num + 1) + '/'
                if not os.path.exists(mask_path):
                    os.makedirs(mask_path)
                mask_save_path = mask_path + names_frames[j][0] + '.png'
                mask = masks[j, :, :]
                mask_numpy = mask.data.cpu().numpy()
                mask_numpy = mask_numpy * 255
                mask_numpy = mask_numpy.astype(np.uint8)
                pure_mask = Image.fromarray(mask_numpy, mode='L')
                pure_mask.save(mask_save_path)
    print(weights)