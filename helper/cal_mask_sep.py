import os
from PIL import Image
import numpy as np

mask_fol_rp = '/data1/guoxi/YouTube-VOS/train/Annotations/'
# mask_fol_rp = '/data1/guoxi/YouTube-VOS/test_for_order/'
fol_set = os.listdir(mask_fol_rp)  # 读取所有的mask,即所有的文件夹名称 mask文件夹 0000001521243214
fol_set.sort()
mask_nam = []
mask_num = []
mask_nam_sort = []

for fol_name in fol_set:   # 每个文件夹下
    mask_rp = mask_fol_rp + fol_name + '/'  # 获得文件夹路径
    mask_set = os.listdir(mask_rp)   #
    mask_set.sort()   # 每个文件夹下所有mask
    tem_num = 0

    for mask_name in mask_set:  # 所有mask
        if mask_name[-4:] != '.png':
            continue
        mask = Image.open(mask_rp + mask_name)
        mask_np = np.asarray(mask, dtype=np.uint8)
        obj_ind = list(np.unique(mask_np))  # mask为彩色数据，读取出每个物体的id 0为背景，1 2 3 分别为要分割的物体
        obj_ind = max(obj_ind)
        if obj_ind > tem_num:
            tem_num = obj_ind

    mask_nam.append(fol_name)
    mask_num.append(tem_num)
    # print(mask_nam)
    # print(mask_num)
file_nam = open('cal_mask_name.txt', 'w')
file_num = open('cal_mask_num.txt', 'w')
mask_num_sort = np.sort(mask_num)
order = np.argsort(mask_num)
for i in range(len(order)):
    mask_nam_sort.append(mask_nam[order[i]])
# print(mask_num_sort)
# print(mask_nam_sort)
file_nam.write(str(mask_nam_sort))
file_nam.close()
file_num.write(str(mask_num_sort))
file_num.close()
print(mask_num_sort[-1])
print(mask_num_sort[0])
print(list(mask_num_sort).count(0))
print(list(mask_num_sort).count(1))
print(list(mask_num_sort).count(2))
print(list(mask_num_sort).count(3))
print(list(mask_num_sort).count(4))
print(list(mask_num_sort).count(5))
print(list(mask_num_sort).count(6))
print(list(mask_num_sort).count(7))
print(list(mask_num_sort).count(8))
print(list(mask_num_sort).count(9))
print(list(mask_num_sort).count(10))
print(list(mask_num_sort).count(11))
print(list(mask_num_sort).count(12))
print(list(mask_num_sort).count(13))
print(list(mask_num_sort).count(14))
print(list(mask_num_sort).count(15))
print(list(mask_num_sort).count(16))
print(list(mask_num_sort).count(17))
print(list(mask_num_sort).count(18))

