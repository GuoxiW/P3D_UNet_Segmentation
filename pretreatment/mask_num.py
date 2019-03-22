import os
from PIL import Image
import numpy as np


def make_mask_num(mask_fol_rp):
    fol_set = os.listdir(mask_fol_rp)  # 读取所有的mask,即所有的文件夹名称 mask文件夹 0000001521243214
    fol_set.sort()
    for fol_name in fol_set:   # 每个文件夹下
        mask_rp = mask_fol_rp + fol_name + '/'  # 获得文件夹路径
        mask_set = os.listdir(mask_rp)   #
        mask_set.sort()   # 每个文件夹下所有mask
        refer_num_list = []

        for mask_name in mask_set:  # 所有mask
            if len(mask_name) != 9:
                continue
            mask = Image.open(mask_rp + mask_name)
            mask_np = np.asarray(mask, dtype=np.uint8)
            obj_ind = list(np.unique(mask_np))  # mask为彩色数据，读取出每个物体的id 0为背景，1 2 3 分别为要分割的物体
            obj_tem = max(obj_ind)
            refer_num_list.append(obj_tem)

        file_name = mask_rp + 'refer_num.txt'
        file = open(file_name, 'a', encoding='UTF-8')
        file.write(str(refer_num_list))
        file.close()

# make_mask_num('/data1/guoxi/p3d_floder/resized_dataset/dataset/trainannot/')
# print('done with train')
# make_mask_num('/data1/guoxi/p3d_floder/resized_dataset/dataset/valannot/')
# print('done with val')

make_mask_num('/data1/guoxi/p3d_floder/resized_dataset/reference_dataset/trainannot/')
print('done with train')
make_mask_num('/data1/guoxi/p3d_floder/resized_dataset/reference_dataset/valannot/')
print('done with val')