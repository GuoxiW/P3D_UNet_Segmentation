from PIL import Image
import numpy as np
import os

count = 0


def remove_wrong_pixel(mask_rp, obj):
    global count
    mask = Image.open(mask_rp)
    mask_np = np.asarray(mask, dtype=np.uint8)
    obj_ind = list(np.unique(mask_np))
    # print(obj_ind)
    for obj_tem in obj_ind:
        if obj == obj_tem:
            count += 1
            mask_np = np.where(mask_np == obj, 0, mask_np)
            mask_np = mask_np.astype(np.uint8)
            res_img = Image.fromarray(mask_np, mode='L')
            os.remove(mask_rp)
            res_img.save(mask_rp)
            print(mask_rp + ' ' + str(obj))
# mask_rp = '/home/guoxi/Desktop/00060.png'
# remove_wrong_pixel(mask_rp, 2)

mask_fol_rp = '/data1/guoxi/YouTube-VOS/pretreatment_after_correct/train/Annotations/'
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
            tem_mask_pixel_num = np.sum(mask_np == obj)
            if tem_mask_pixel_num < 15:
                count += 1
                mask_np = np.where(mask_np == obj, 0, mask_np)
                os.remove(mask_rp + mask_name)
                print(mask_rp + ' ' + mask_name + ' ' + str(obj) + ' ' + str(tem_mask_pixel_num))
                res_img = Image.fromarray(mask_np, mode='L')
                res_img.save(mask_rp + mask_name)

print(count)

# 删除了72个，结果正确,剩余755个



remove_wrong_pixel('/data1/guoxi/YouTube-VOS/pretreatment_after_correct/train/Annotations/d301ca58cc/00025.png', 4)
remove_wrong_pixel('/data1/guoxi/YouTube-VOS/pretreatment_after_correct/train/Annotations/df365282c6/00150.png', 3)
remove_wrong_pixel('/data1/guoxi/YouTube-VOS/pretreatment_after_correct/train/Annotations/5e1ce354fd/00060.png', 6)
remove_wrong_pixel('/data1/guoxi/YouTube-VOS/pretreatment_after_correct/train/Annotations/7584129dc3/00045.png', 1)
remove_wrong_pixel('/data1/guoxi/YouTube-VOS/pretreatment_after_correct/train/Annotations/b2edc76bd2/00095.png', 6)
remove_wrong_pixel('/data1/guoxi/YouTube-VOS/pretreatment_after_correct/train/Annotations/c6d9526e0d/00065.png', 6)
remove_wrong_pixel('/data1/guoxi/YouTube-VOS/pretreatment_after_correct/train/Annotations/df365282c6/00140.png', 3)
remove_wrong_pixel('/data1/guoxi/YouTube-VOS/pretreatment_after_correct/train/Annotations/c55784c766/00085.png', 3)
remove_wrong_pixel('/data1/guoxi/YouTube-VOS/pretreatment_after_correct/train/Annotations/c6d9526e0d/00060.png', 5)
remove_wrong_pixel('/data1/guoxi/YouTube-VOS/pretreatment_after_correct/train/Annotations/ee316eaed6/00010.png', 3)
remove_wrong_pixel('/data1/guoxi/YouTube-VOS/pretreatment_after_correct/train/Annotations/c6d9526e0d/00070.png', 5)
remove_wrong_pixel('/data1/guoxi/YouTube-VOS/pretreatment_after_correct/train/Annotations/c8d79e3163/00100.png', 5)
remove_wrong_pixel('/data1/guoxi/YouTube-VOS/pretreatment_after_correct/train/Annotations/c6d9526e0d/00075.png', 5)
remove_wrong_pixel('/data1/guoxi/YouTube-VOS/pretreatment_after_correct/train/Annotations/90c7a87887/00000.png', 1)
remove_wrong_pixel('/data1/guoxi/YouTube-VOS/pretreatment_after_correct/train/Annotations/59323787d5/00070.png', 10)
remove_wrong_pixel('/data1/guoxi/YouTube-VOS/pretreatment_after_correct/train/Annotations/203594a418/00030.png', 3)
remove_wrong_pixel('/data1/guoxi/YouTube-VOS/pretreatment_after_correct/train/Annotations/dfdbf91a99/00010.png', 2)
remove_wrong_pixel('/data1/guoxi/YouTube-VOS/pretreatment_after_correct/train/Annotations/ff66152b25/00120.png', 1)
remove_wrong_pixel('/data1/guoxi/YouTube-VOS/pretreatment_after_correct/train/Annotations/b6ec609f7b/00015.png', 3)
remove_wrong_pixel('/data1/guoxi/YouTube-VOS/pretreatment_after_correct/train/Annotations/c6d9526e0d/00065.png', 5)
remove_wrong_pixel('/data1/guoxi/YouTube-VOS/pretreatment_after_correct/train/Annotations/c6d9526e0d/00175.png', 5)
remove_wrong_pixel('/data1/guoxi/YouTube-VOS/pretreatment_after_correct/train/Annotations/afe1a35c1e/00065.png', 11)
remove_wrong_pixel('/data1/guoxi/YouTube-VOS/pretreatment_after_correct/train/Annotations/79e9db913e/00055.png', 5)
remove_wrong_pixel('/data1/guoxi/YouTube-VOS/pretreatment_after_correct/train/Annotations/90c7a87887/00065.png', 1)
remove_wrong_pixel('/data1/guoxi/YouTube-VOS/pretreatment_after_correct/train/Annotations/90c7a87887/00090.png', 1)
remove_wrong_pixel('/data1/guoxi/YouTube-VOS/pretreatment_after_correct/train/Annotations/76a75f4eee/00000.png', 5)
remove_wrong_pixel('/data1/guoxi/YouTube-VOS/pretreatment_after_correct/train/Annotations/90c7a87887/00085.png', 1)
remove_wrong_pixel('/data1/guoxi/YouTube-VOS/pretreatment_after_correct/train/Annotations/90c7a87887/00005.png', 1)
remove_wrong_pixel('/data1/guoxi/YouTube-VOS/pretreatment_after_correct/train/Annotations/90c7a87887/00080.png', 1)
remove_wrong_pixel('/data1/guoxi/YouTube-VOS/pretreatment_after_correct/train/Annotations/90c7a87887/00075.png', 1)
remove_wrong_pixel('/data1/guoxi/YouTube-VOS/pretreatment_after_correct/train/Annotations/90c7a87887/00070.png', 1)
remove_wrong_pixel('/data1/guoxi/YouTube-VOS/pretreatment_after_correct/train/Annotations/4f601d255a/00060.png', 2)

print(count)

# 删除了32个，结果正确,剩余723个
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/02d28375aa/ 00150.png 2 1
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/07129e14a4/ 00140.png 4 2
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/07913cdda7/ 00010.png 3 4
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/106242403f/ 00015.png 3 8
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/11a0c3b724/ 00050.png 3 2
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/1f7d31b5b2/ 00075.png 3 8
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/1f8014b7fd/ 00000.png 3 1
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/43326d9940/ 00075.png 1 4
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/43a6c21f37/ 00105.png 3 2
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/4804ee2767/ 00020.png 1 2
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/57bfb7fa4c/ 00000.png 3 1
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/6afd692f1a/ 00110.png 4 2
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/733824d431/ 00085.png 2 7
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/76b90809f7/ 00065.png 2 2
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/76b90809f7/ 00135.png 1 12
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/78f1a1a54f/ 00000.png 2 2
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/78f1a1a54f/ 00010.png 2 6
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/78f1a1a54f/ 00015.png 2 1
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/78f1a1a54f/ 00025.png 2 1
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/78f1a1a54f/ 00030.png 2 1
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/78f1a1a54f/ 00035.png 2 1
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/7d1333fcbe/ 00030.png 3 2
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8749369ba0/ 00065.png 3 1
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8749369ba0/ 00070.png 3 1
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/909dbd1b76/ 00050.png 12 3
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/909dbd1b76/ 00060.png 3 1
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/94209c86f0/ 00045.png 4 1
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/958073d2b0/ 00030.png 2 2
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/958073d2b0/ 00080.png 2 1
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/958073d2b0/ 00100.png 2 6
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/958073d2b0/ 00105.png 2 3
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/958073d2b0/ 00115.png 2 2
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/958073d2b0/ 00120.png 2 2
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/958073d2b0/ 00125.png 2 14
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/958073d2b0/ 00130.png 2 5
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/958073d2b0/ 00135.png 2 13
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/958073d2b0/ 00140.png 2 1
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/958073d2b0/ 00145.png 2 7
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/acf44293a2/ 00090.png 3 7
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/af8ad72057/ 00140.png 4 1
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b2edc76bd2/ 00095.png 7 8
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b2edc76bd2/ 00095.png 9 3
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b2edc76bd2/ 00095.png 10 8
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b6ec609f7b/ 00115.png 2 7
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/bb1c770fe7/ 00145.png 9 3
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/c31fa6c598/ 00065.png 1 7
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/c6d9526e0d/ 00045.png 5 8
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/c6d9526e0d/ 00050.png 5 4
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/c6d9526e0d/ 00055.png 5 6
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/c6d9526e0d/ 00125.png 5 9
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/cef824a1e1/ 00040.png 2 8
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/d454e8444f/ 00020.png 4 3
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/d6476cad55/ 00020.png 2 1
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/d6476cad55/ 00025.png 2 4
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/d7135cf104/ 00095.png 3 8
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/df365282c6/ 00135.png 3 10
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/df365282c6/ 00145.png 3 3
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/df365282c6/ 00155.png 3 14
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/df365282c6/ 00160.png 3 1
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e2b608d309/ 00160.png 1 12
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e33c18412a/ 00045.png 4 1
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e39e3e0a06/ 00090.png 4 1
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/eaab4d746c/ 00000.png 2 10
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/eb383cb82e/ 00055.png 4 11
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/ec28252938/ 00095.png 3 2
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/ed8f814b2b/ 00040.png 3 2
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/f46c364dca/ 00170.png 5 2
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/f659251be2/ 00055.png 2 1
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/f659251be2/ 00060.png 2 1
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/f659251be2/ 00120.png 2 1
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/f659251be2/ 00130.png 2 3
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/ffc43fc345/ 00135.png 1 1
# 72
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/d301ca58cc/00025.png 4
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/df365282c6/00150.png 3
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/5e1ce354fd/00060.png 6
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/7584129dc3/00045.png 1
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b2edc76bd2/00095.png 6
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/c6d9526e0d/00065.png 6
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/df365282c6/00140.png 3
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/c55784c766/00085.png 3
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/c6d9526e0d/00060.png 5
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/ee316eaed6/00010.png 3
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/c6d9526e0d/00070.png 5
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/c8d79e3163/00100.png 5
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/c6d9526e0d/00075.png 5
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/90c7a87887/00000.png 1
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/59323787d5/00070.png 10
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/203594a418/00030.png 3
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/dfdbf91a99/00010.png 2
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/ff66152b25/00120.png 1
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b6ec609f7b/00015.png 3
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/c6d9526e0d/00065.png 5
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/c6d9526e0d/00175.png 5
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/afe1a35c1e/00065.png 11
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/79e9db913e/00055.png 5
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/90c7a87887/00065.png 1
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/90c7a87887/00090.png 1
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/76a75f4eee/00000.png 5
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/90c7a87887/00085.png 1
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/90c7a87887/00005.png 1
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/90c7a87887/00080.png 1
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/90c7a87887/00075.png 1
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/90c7a87887/00070.png 1
# /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/4f601d255a/00060.png 2
# 104