# 用于将val中所有的image和mask放在一个文件夹里，在evaluation中进行比对

import os
import shutil


def make_val_data(val_fol_rp, write_fol_rp):
    fol_set = os.listdir(val_fol_rp)  # 读取所有的mask,即所有的文件夹名称 mask文件夹 0000001521243214
    fol_set.sort()

    for fol_name in fol_set:   # 每个文件夹下
        val_rp = val_fol_rp + fol_name + '/'  # 获得文件夹路径
        val_set = os.listdir(val_rp)   #
        val_set.sort()   # 每个文件夹下所有mask
    
        for val_name in val_set:  # 所有mask
            if val_name[-4:] != '.jpg':
                continue
            read_rp = val_rp + val_name
            write_rp = write_fol_rp + fol_name + '_' + val_name
            shutil.copy(read_rp, write_rp)


def make_valannot_data(val_fol_rp, write_fol_rp):
    fol_set = os.listdir(val_fol_rp)  # 读取所有的mask,即所有的文件夹名称 mask文件夹 0000001521243214
    fol_set.sort()

    for fol_name in fol_set:  # 每个文件夹下
        val_rp = val_fol_rp + fol_name + '/'  # 获得文件夹路径
        val_set = os.listdir(val_rp)  #
        val_set.sort()  # 每个文件夹下所有mask

        for val_name in val_set:  # 所有mask
            if val_name[-4:] != '.png':
                continue
            read_rp = val_rp + val_name
            write_rp = write_fol_rp + fol_name + '_' + val_name
            shutil.copy(read_rp, write_rp)
make_val_data('/data1/guoxi/p3d_floder/resized_dataset/dataset/val/', '/data1/guoxi/p3d_floder/resized_dataset/val_dataset_all/')
make_valannot_data('/data1/guoxi/p3d_floder/resized_dataset/dataset/valannot/', '/data1/guoxi/p3d_floder/resized_dataset/val_dataset_all/')