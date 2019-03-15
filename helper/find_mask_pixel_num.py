import os
from PIL import Image
import numpy as np
import csv

# out1 = open('result.csv', 'a', newline='')
# out2 = open('result_pixel_num', 'a', newline='')
# csv_write = csv.writer(out1, dialect='excel')
# csv_write_pixel = csv.writer(out2, dialect='excel')

total_num = 0
error_num = 0
error_mask_rp = '/data1/guoxi/YouTube-VOS/test_wrong/'

def find_mask_pixel_num(total_num, error_num, mask_fol_rp):
    fol_set = os.listdir(mask_fol_rp)  # 读取所有的mask,即所有的文件夹名称 mask文件夹 0000001521243214
    fol_set.sort()



    for fol_name in fol_set:  # 每个文件夹下
        mask_rp = mask_fol_rp + fol_name + '/'  # 获得文件夹路径
        mask_set = os.listdir(mask_rp)  #
        mask_set.sort()  # 每个文件夹下所有mask


        for mask_name in mask_set:  # 所有mask
            if mask_name[-4:] != '.png':
                continue
            mask = Image.open(mask_rp + mask_name)
            mask_np = np.asarray(mask, dtype=np.uint8)
            obj_ind = list(np.unique(mask_np))

            for obj in obj_ind:
                total_num += 1
                tem_mask_pixel_num = np.sum(mask_np == obj)
                if tem_mask_pixel_num < 255:
                    # error_num += 1
                    print(mask_rp + mask_name + ' ' + str(obj) + ' ' + str(tem_mask_pixel_num))

    # print(total_num)  # 242422
    # print(error_num)  # 827

mask_fol_rp = '/data1/guoxi/YouTube-VOS/train/Annotations/'
find_mask_pixel_num(total_num, error_num, mask_fol_rp)
