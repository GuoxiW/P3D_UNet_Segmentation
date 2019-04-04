import os
# 生成用于DAVIS matlab计算的train.txt,val.txt为空。
# /data1/guoxi/p3d/p3d_evaluation/DAVIS/ImageSets/2017/train.txt
# /data1/guoxi/p3d/p3d_evaluation/DAVIS/ImageSets/2017/val.txt
mask_fol_rp = '/data1/guoxi/p3d_floder/resized_dataset/reference_dataset/val/'
fol_set = os.listdir(mask_fol_rp)  # 读取所有的mask,即所有的文件夹名称 mask文件夹 0000001521243214
fol_set.sort()
for fol_name in fol_set:   # 每个文件夹下
    print(fol_name)