import os
import shutil
# 生成用于检测densecrf正确性的数据，即把groundtruth当作预测值，检验J与F

mask_fol_rp = '/data1/guoxi/p3d_floder/resized_dataset/dataset/valannot/'
mask_save_rp = '/data1/guoxi/p3d/result/mask_test_densecrf/'
fol_set = os.listdir(mask_fol_rp)  # 读取所有的mask,即所有的文件夹名称 mask文件夹 0000001521243214
fol_set.sort()
for fol_name in fol_set:   # 每个文件夹下
    mask_rp = mask_fol_rp + fol_name + '/'  # 获得文件夹路径
    mask_set = os.listdir(mask_rp)  #
    mask_set.sort()  # 每个文件夹下所有mask

    for mask_name in mask_set:  # 所有mask
        if len(mask_name) != 11:
            continue
        order = mask_name[-5]
        save_rp = mask_save_rp + fol_name + '/' + str(order) + '/'
        if not os.path.exists(save_rp):
            os.makedirs(save_rp)
        mask_fol_name = mask_rp + mask_name
        mask_save_name = save_rp + mask_name[:-6] + '.png'
        shutil.copyfile(mask_fol_name, mask_save_name)