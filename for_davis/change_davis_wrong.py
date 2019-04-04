from PIL import Image
import numpy as np
import os

# DAVIS数据集中的tennis项网球本应是背景0，但被标注成了255，用此函数来更改。

def change_wrong_pixel(mask_fol_rp):
    mask_set = os.listdir(mask_fol_rp)  #
    mask_set.sort()  # 每个文件夹下所有mask

    for mask_name in mask_set:
        mask_rp = mask_fol_rp +mask_name
        mask = Image.open(mask_rp)
        mask_np = np.asarray(mask, dtype=np.uint8)
        obj_ind = list(np.unique(mask_np))
        print(obj_ind)
        # res_img = np.where(mask_np == 255, 0, mask_np)
        # res_img = res_img.astype(np.uint8)
        # res_img = Image.fromarray(res_img, mode='L')
        # os.remove(mask_rp)
        # res_img.save(mask_rp)

change_wrong_pixel('/data1/guoxi/p3d/p3d_evaluation/DAVIS/Annotations/480p/tennis/')
change_wrong_pixel('/data1/guoxi/p3d/p3d_evaluation/DAVIS/Results/Segmentations/480p/my_method/tennis/')








