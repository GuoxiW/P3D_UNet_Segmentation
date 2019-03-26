# 早期的用于检测错误mask的代码。
import os
from PIL import Image
import numpy as np

# mask_fol_rp = '/disk2/guoxi/YouTube-VOS/test_wrong/'
# mask_set = os.listdir(mask_fol_rp)   #
# mask_set.sort()   # 每个文件夹下所有mask
# mask_num = []
#
# for mask_name in mask_set:  # 所有mask
#     if mask_name[-4:] != '.png':
#         continue
#     mask = Image.open(mask_fol_rp + mask_name)
#     mask_np = np.asarray(mask, dtype=np.uint8)
#     obj_ind = list(np.unique(mask_np))  # mask为彩色数据，读取出每个物体的id 0为背景，1 2 3 分别为要分割的物体
#         # obj_ind = max(obj_ind)
#         # if not len(mask_num):
#         #     mask_num.append(obj_ind)
#         # if obj_ind > max(mask_num):
#         #     mask_num.append(obj_ind)
#         #     # if mask_name != '00000.png':
#     print(mask_fol_rp + mask_name + ' ' + str(obj_ind))
#         # print(mask_num)
#     # if len(mask_num) > 1:
#     #     print(mask_rp)
#     #     shutil.rmtree(mask_rp)
#     #     shutil.rmtree(image_rp)


mask_fol_rp = '/disk2/guoxi/YouTube-VOS/train/Annotations/'
fol_name = '59323787d5'


mask_rp = mask_fol_rp + fol_name + '/'  # 获得文件夹路径
mask_set = os.listdir(mask_rp)   #
mask_set.sort()   # 每个文件夹下所有mask
mask_num = []

for mask_name in mask_set:  # 所有mask
    if mask_name[-4:] != '.png':
        continue
    mask = Image.open(mask_rp + mask_name)
    mask_np = np.asarray(mask, dtype=np.uint8)
    obj_ind = list(np.unique(mask_np))  # mask为彩色数据，读取出每个物体的id 0为背景，1 2 3 分别为要分割的物体
    # obj_ind = max(obj_ind)
    # if not len(mask_num):
    #     mask_num.append(obj_ind)
    # if obj_ind > max(mask_num):
    #     mask_num.append(obj_ind)
            # if mask_name != '00000.png':
    print(mask_rp + mask_name + ' ' + str(obj_ind))
        # print(mask_num)
    # if len(mask_num) > 1:
    #     print(mask_rp)
    #     shutil.rmtree(mask_rp)
    #     shutil.rmtree(image_rp)