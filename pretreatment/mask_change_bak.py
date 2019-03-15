import os
from PIL import Image
import numpy as np


def evaluate_mask_change(mask_rp):

    mask_set = os.listdir(mask_rp)
    mask_set.sort()   # 每个文件夹下所有mask
    mask_num = []

    for mask_name in mask_set:  # 所有mask
        if mask_name[-4:] != '.png':
            continue
        mask = Image.open(mask_rp + mask_name)
        mask_np = np.asarray(mask, dtype=np.uint8)
        obj_ind = list(np.unique(mask_np))  # mask为彩色数据，读取出每个物体的id 0为背景，1 2 3 分别为要分割的物体
        obj_ind = max(obj_ind)
        if not len(mask_num):
            mask_num.append(obj_ind)
        if obj_ind > max(mask_num):
            return 1

    return 0

# print(evaluate_mask_change('/disk2/guoxi/YouTube-VOS/train/Annotations/003234408d/'))
# print(evaluate_mask_change('/disk2/guoxi/YouTube-VOS/train/Annotations/0043f083b5/'))
# print(evaluate_mask_change('/disk2/guoxi/YouTube-VOS/train/Annotations/00a23ccf53/'))
# print(evaluate_mask_change('/disk2/guoxi/YouTube-VOS/train/Annotations/013099c098/'))
# print(evaluate_mask_change('/disk2/guoxi/YouTube-VOS/train/Annotations/02f3a5c4df/'))

def get_mask_change(mask_rp):
    mask_set = os.listdir(mask_rp)
    mask_set.sort()  # 每个文件夹下所有mask
    mask_order = []
    mask_num = []
    number = -1

    for mask_name in mask_set:  # 所有mask
        number += 1
        if mask_name[-4:] != '.png':
            continue
        mask = Image.open(mask_rp + mask_name)
        mask_np = np.asarray(mask, dtype=np.uint8)
        obj_ind = list(np.unique(mask_np))  # mask为彩色数据，读取出每个物体的id 0为背景，1 2 3 分别为要分割的物体
        obj_ind = max(obj_ind)
        if not len(mask_num):
            mask_num.append(obj_ind)
        if obj_ind > max(mask_num):
            mask_num.append(obj_ind)
            mask_order.append(number)

    return mask_order, mask_num[1:]

print(get_mask_change('/disk2/guoxi/YouTube-VOS/train/Annotations/003234408d/'))
# print(get_mask_change(''))
# print(get_mask_change(''))
# print(get_mask_change(''))
# print(get_mask_change(''))
