import torch
import torchvision
import torch.nn as nn
import torch.optim as optim
import os
import shutil
import time

import dataset
from transforms.spatial_transforms import Compose, Normalize, Scale, ToTensor
from transforms.temporal_transforms import LoopPadding
import network_cla
import network_seg
import utils
import experiment


def main():

    save_path = '/disk2/guoxi/p3d/result/masks/'
    batch_size = 1
    n_threads = 16
    # 'Temporal duration of inputs'
    sample_duration = 16
    # the data for devison
    norm_value = 255
    # Height and width of inputs
    sample_size = 224
    # Number of validation samples for each activity
    n_val_samples = 3
    video_path = '../dataset/'
    mean = [0.485, 0.456, 0.406]
    std = [0.229, 0.224, 0.225]

    norm_method = Normalize(mean, std)
    spatial_transform = Compose([Scale((sample_size, sample_size)), ToTensor(norm_value=norm_value), norm_method])
    temporal_transform = LoopPadding(sample_duration)
    target_transform = Compose([Scale((sample_size, sample_size)), ToTensor(norm_value=norm_value)])
    opt = [video_path, sample_duration]

    test_data = dataset.get_test_set(opt, spatial_transform, target_transform, split='val')
    test_loader = torch.utils.data.DataLoader(test_data, batch_size=batch_size, shuffle=False, num_workers=n_threads, pin_memory=True)

    # inputs, name_video, names_frames = next(iter(test_loader))
    # print('type(name_video):', type(name_video[0]), len(name_video))
    # print(name_video[0])
    # print('type(names_frames):', type(names_frames), len(names_frames))
    # print(names_frames[0])
    # print('inputs.size(), targets.size():', inputs.size(), targets.size())

    model = network_seg.P3D199()
    weight_path = '/disk2/guoxi/p3d/result/model/P3D_saliency/weights/best_weights.pth'
    state_dict = torch.load(weight_path)
    model.load_state_dict(state_dict['state_dict'])
    model = model.cuda()
    model.eval()

    for clip_sets, name_video, names_frames in test_loader:
        # count = 0
        for iord, clip in enumerate(clip_sets[:-1]):
            # print('clip.size(), clip.max(), clip.min():', clip.size(), clip.max(), clip.min())
            with torch.no_grad():
                masks = model(clip.cuda())
            masks.squeeze_()
            # print('masks.size(), masks.max(), masks.min():')
            # print(masks.size(), masks.max(), masks.min())
            for j in range(sample_duration):
                order = iord*sample_duration + j
                mask_name = name_video[0] + '-' + names_frames[order][0] + '.png'
                print(mask_name)
                mask_path = save_path + mask_name
                mask = masks[j, :, :]
                mask.unsqueeze_(dim=0)
                mask.unsqueeze_(dim=0)
                # mask *= 255
                print('masks.size(), masks.max(), masks.min():')
                print(mask.size(), mask.max(), mask.min())
                torchvision.utils.save_image(mask, mask_path)
        # dispose the last clip
        clip = clip_sets[-1]
        with torch.no_grad():
            masks = model(clip.cuda())
        masks.squeeze_()
        for j in range(-1, -1-sample_duration, -1):
            mask_name = name_video[0] + '-' + names_frames[j][0] + '.png'
            print(mask_name)
            mask_path = save_path + mask_name
            torchvision.utils.save_image(masks[j, :, :], mask_path)



if __name__ == '__main__':
    main()
