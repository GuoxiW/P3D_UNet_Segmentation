import os
from PIL import Image
import numpy as np
import json

mask_fol_rp = '/data1/guoxi/YouTube-VOS/test_wrong/train/'
fol_set = os.listdir(mask_fol_rp)  # 读取所有的mask,即所有的文件夹名称 mask文件夹 0000001521243214
fol_set.sort()
for fol_name in fol_set:   # 每个文件夹下
    mask_rp = mask_fol_rp + fol_name + '/'  # 获得文件夹路径
    mask_set = os.listdir(mask_rp)   #
    mask_set.sort()   # 每个文件夹下所有mask
    # file_name = fol_name + reference.txt
    file = open(mask_rp + 'reference.txt', "r", encoding='UTF-8')
    list = file.read()
    list = json.loads(list)
    print(list)
