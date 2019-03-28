import torch
import torchvision
import torch.nn as nn
import torch.optim as optim
import os
import shutil
import time
import numpy as np
from PIL import Image

import dataset
from transforms.spatial_transforms import Compose, Normalize, Scale, ToTensor
from transforms.temporal_transforms import LoopPadding
import network_cla
import network_seg
import utils
import experiment

# 因为数据预处理中已进行了相关操作，故取消了resize和padding
# 为了防止出错 n_threads=1

def main():

    save_path = '../result/mask_all/'
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

    # inputs, name_video, names_frames = next(iter(test_loader))
    # print('type(name_video):', type(name_video[0]), len(name_video))
    # print(name_video[0])
    # print('type(names_frames):', type(names_frames), len(names_frames))
    # print(names_frames[0])
    # print('inputs.size(), targets.size():', inputs.size(), targets.size())

    model = network_seg.P3D199()
    model = torch.nn.DataParallel(model)
    weight_path = '../result/model/P3D_saliency/weights/best_weights.pth'
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


        # count = -1
        for iord, clip_set in enumerate(clip_sets[:-1]):  #i_order
            # print(' ')
            # count += 1
            # print(clip_sets[count])
            # print(iord)
            # print(clip)
            # print('clip.size(), clip.max(), clip.min():', clip.size(), clip.max(), clip.min())
            # torch.Size([1, 3, 16, 224, 224])
            for mask_tol_num, clip in enumerate(clip_set):
                # print(clip.size())
                with torch.no_grad():
                    masks = model(clip.cuda())
                    # print(masks.size())
                masks.squeeze_()
                # print(masks.size())
                # print('masks.size(), masks.max(), masks.min():')
                # print(masks.size(), masks.max(), masks.min())
                for j in range(sample_duration):
                    order = iord * sample_duration + j
                    mask_name = name_video[0] + '_' + names_frames[order][0] + '_' + str(mask_tol_num + 1) + '_' + str(int(total_mask)) + '.png'
                    # print(mask_name)
                    mask_path = save_path + mask_name
                    mask = masks[j, :, :]
                    # print(mask.size())
                    # mask.unsqueeze_(dim=0)
                    # print(mask.size())
                    # mask.unsqueeze_(dim=0)
                    # print(mask.size())
                    # mask *= 255
                    # print('masks.size(), masks.max(), masks.min():')
                    # print(mask.size(), mask.max(), mask.min())
                    torchvision.utils.save_image(mask, mask_path)
        # dispose the last clip
        clip_set = clip_sets[-1]
        for mask_tol_num, clip in enumerate(clip_set):

            with torch.no_grad():
                masks = model(clip.cuda())
            masks.squeeze_()
            for j in range(-1, -1-sample_duration, -1):
                mask_name = name_video[0] + '_' + names_frames[j][0] + '_' + str(mask_tol_num + 1) + '_' + str(int(total_mask)) + '.png'
                # print(mask_name)
                mask_path = save_path + mask_name
                torchvision.utils.save_image(masks[j, :, :], mask_path)
    # print('Done with evaluation')
    # print('make data now')
    # fol_set = os.listdir(save_path)
    # fol_set.sort()
    #
    # for fol_name in fol_set:
    #     img_rp = save_path + fol_name + '/'
    #     img_set = os.listdir(img_rp)
    #     img_set.sort()
    #
    #     img_orl = [img_name[0:6] for img_name in img_set]
    #     img_orl =list(set(img_orl))
    #     for img_name in img_set[0:6]
    #
    #         img = Image.open(img_rp + img_name)
    #         img = img.resize((size, size), Image.BILINEAR)
    #         img_save_rp = out_rp + fol_name + '/' + img_name
    #         img.save(img_save_rp)


if __name__ == '__main__':
    main()
