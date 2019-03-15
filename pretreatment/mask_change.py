import os
from PIL import Image
import numpy as np


mask_fol_rp = '/data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/'
fol_set = os.listdir(mask_fol_rp)  # 读取所有的mask,即所有的文件夹名称 mask文件夹 0000001521243214
fol_set.sort()
for fol_name in fol_set:   # 每个文件夹下
    mask_rp = mask_fol_rp + fol_name + '/'  # 获得文件夹路径
    mask_set = os.listdir(mask_rp)   #
    mask_set.sort()   # 每个文件夹下所有mask
    mask_num = []
    reference_list = []
    image_count = -1
    change_count = -1

    for mask_name in mask_set:  # 所有mask
        if len(mask_name) != 9:
            continue
        image_count += 1
        mask = Image.open(mask_rp + mask_name)
        mask_np = np.asarray(mask, dtype=np.uint8)
        obj_ind = list(np.unique(mask_np))  # mask为彩色数据，读取出每个物体的id 0为背景，1 2 3 分别为要分割的物体
        obj_tem = max(obj_ind)
        if not len(mask_num):
            mask_num.append(obj_tem)
            change_count += 1
        if obj_tem > max(mask_num):
            mask_num.append(obj_tem)
            change_count = image_count
        reference_list.append(change_count)

    file_name = mask_rp + 'reference.txt'
    file = open(file_name, 'a', encoding='UTF-8')
    file.write(str(reference_list))
    file.close()

            # mask_num.append(obj_ind)
            # mask_order.append(number)

        # return mask_order, mask_num
#
# print(get_mask_change('/data1/guoxi/YouTube-VOS/train/Annotations/00a23ccf53/'))
# # print(get_mask_change(''))
# # print(get_mask_change(''))
# # print(get_mask_change(''))
# # print(get_mask_change(''))
