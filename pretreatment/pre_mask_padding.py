import numpy as np
from PIL import Image
import os


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


mask_fol_rp = '/data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/'
image_fol_rp = '/data1/guoxi/YouTube-VOS/pretreatment_data/train/JPEGImages/'

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
        mask_np = np.asarray(mask, dtype=np.uint8)
        print(mask_name)
        mask_sep_ele(mask_np, mask_rp, mask_name)



