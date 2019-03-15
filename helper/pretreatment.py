# 对数据进行预处理
# 1.定义函数实现所有真值的分类，生成每类只有一个需要分割物体的数据集
# mask_sep_ele
# handle_mask_sep
# mask_total_num 减去背景
# 2.对不满16帧的数据进行复制，达到16帧
# pad_data
# padding共144张，选取复制最后一张图n次，
# 双边时因为从00000开始，容易出现命名的问题，解决方案：
# 1. 00000 00001 00002 00003 这样命名，对于只有4帧的数据集 添加 1 2 3 4 6 7
# 2. 将第一帧放在最后，丧失了一些时空信息
# 最终选择双边padding,第一帧的复制放在最后
# 还未做测试

import os
from PIL import Image
import numpy as np
import shutil


def mask_total_num(mask):  # 有些没有mask
    obj_ind = list(np.unique(mask))
    obj_ind_len = len(obj_ind)
    obj_ind_len -= 1
    return obj_ind_len


def mask_sep_ele(mask, mask_rp, name):  # mask是原始的彩色数据
    obj_ind = list(np.unique(mask))  # mask为彩色数据，读取出每个物体的id 0为背景，1 2 3 分别为要分割的物体
    templet = np.zeros(mask.shape, dtype=np.uint8)
    for ind in obj_ind[1:]:  # 除去背景黑色的0
        res = templet.copy()
        res = np.where(mask == ind, 255, res)  # 如果是对应的物体，则标白255，负责标黑0
        order = str(ind)  # 得出顺序
        mask_name = name[:-4] + '_' + order + '.png'  # 标识出这是第几个物体的灰度值
        res_img = Image.fromarray(res, mode='L')
        res_img.save(mask_rp + mask_name)


def handle_mask_sep(mask_fol_rp):
    # mask_fol_rp = '/disk2/guoxi/YouTube-VOS/train/Annotations/'
    fol_set = os.listdir(mask_fol_rp)  # 读取所有的mask,即所有的文件夹名称
    fol_set.sort()

    for fol_name in fol_set:
        mask_rp = mask_fol_rp + fol_name + '/'  # 获得文件夹路径
        mask_set = os.listdir(mask_rp)
        mask_set.sort()

        for mask_name in mask_set:
            if mask_name[-4:] != '.png':
                continue
            mask = Image.open(mask_rp + mask_name)
            mask_np = mask.asarray(mask, dtype=np.uint8)
            mask_sep_ele(mask_np, mask_rp, mask_name)


def pad_data_single(img_fol_rp, mask_fol_rp):  # 共有144张图片需要padding,最多15张，最少4张，选取复制最后一张图N次的方法
    fol_set = os.listdir(mask_fol_rp)  # 读取所有的mask,即所有的文件夹名称
    fol_set.sort()

    for fol_name in fol_set:
        mask_rp = mask_fol_rp + fol_name + '/'  # 文件夹
        img_rp = img_fol_rp + fol_name + '/'
        mask_set = os.listdir(mask_rp)          # 文件
        mask_set.sort()

        if len(mask_set) < 16:
            # img_rp = img_fol_rp + fol_name + '/'
            # print(len(mask_set), mask_rp)
            last_name = mask_set[-1]  # 最后一张图
            last_order = int(last_name[:-4])  # 最后一张图的标签
            for _ in range(len(mask_set), 16):  # 临时变量，长度到16迭代
                last_order += 5  # 向后加5
                name = str(last_order).zfill(5)  # 长度为5
                shutil.copyfile(mask_rp+last_name, mask_rp+name+'.png')
                print('file copy', mask_rp+last_name, mask_rp+name+'.png')
                shutil.copyfile(img_rp+last_name[:-4]+'.jpg', img_rp+name+'.jpg')


def pad_data_double(img_fol_rp, mask_fol_rp):  # 共有144张图片需要padding,最多15张，最少4张，同时复制第一张和最后一张，第一张的复制放在最后
    fol_set = os.listdir(mask_fol_rp)  # 读取所有的mask,即所有的文件夹名称
    fol_set.sort()

    for fol_name in fol_set:
        mask_rp = mask_fol_rp + fol_name + '/'  # 文件夹
        img_rp = img_fol_rp + fol_name + '/'
        mask_set = os.listdir(mask_rp)          # 文件
        mask_set.sort()

        if len(mask_set) < 16:
            # img_rp = img_fol_rp + fol_name + '/'
            # print(len(mask_set), mask_rp)
            padding_num_first = (16 - len(mask_set)) // 2  # 第一张图复制次数
            padding_num_last = 16 - len(mask_set) - padding_num_first  # 最后一张图复制次数
            first_name = mask_set[0]  # 第一张图
            last_name = mask_set[-1]  # 最后一张图
            last_order = int(last_name[:-4])  # 最后一张图的标签
            for _ in range(padding_num_last):  # 复制最后一张图
                last_order += 5  # 向后加5
                name = str(last_order).zfill(5)  # 长度为5
                shutil.copyfile(mask_rp+last_name, mask_rp+name+'.png')
                print('file copy', mask_rp+last_name, mask_rp+name+'.png')
                shutil.copyfile(img_rp+last_name[:-4]+'.jpg', img_rp+name+'.jpg')

            for _ in range(padding_num_first):  # 复制第一张图
                last_order += 5  # 向后加5
                name = str(last_order).zfill(5)  # 长度为5
                shutil.copyfile(mask_rp + first_name, mask_rp + name + '.png')
                print('file copy', mask_rp + first_name, mask_rp + name + '.png')
                shutil.copyfile(img_rp + first_name[:-4] + '.jpg', img_rp + name + '.jpg')





