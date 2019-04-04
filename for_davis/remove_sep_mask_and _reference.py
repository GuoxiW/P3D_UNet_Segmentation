import os

# 删除ground truth中的reference.txt,refer_num.txt,00000_1.png等等影响evaluation的文件。

mask_fol_rp = '/data1/guoxi/p3d/p3d_evaluation/DAVIS/Annotations/480p/'
fol_set = os.listdir(mask_fol_rp)  # 读取所有的mask,即所有的文件夹名称 mask文件夹 0000001521243214
fol_set.sort()
for fol_name in fol_set:   # 每个文件夹下
    mask_rp = mask_fol_rp + fol_name + '/'  # 获得文件夹路径
    mask_set = os.listdir(mask_rp)  #
    mask_set.sort()  # 每个文件夹下所有mask

    for mask_name in mask_set:  # 所有mask
        if len(mask_name) != 9:
            os.remove(mask_rp + mask_name)