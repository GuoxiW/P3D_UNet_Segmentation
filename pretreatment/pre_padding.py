# 用于将不够16帧的视频padding到16帧，采取最后一帧的单边padding。
import os
import shutil


mask_fol_rp = '/data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/'
image_fol_rp = '/data1/guoxi/YouTube-VOS/pretreatment_data/train/JPEGImages/'
fol_set = os.listdir(mask_fol_rp)  # 读取所有的mask,即所有的文件夹名称 mask文件夹 0000001521243214
fol_set.sort()

for fol_name in fol_set:
    mask_rp = mask_fol_rp + fol_name + '/'  # 获得文件夹路径
    image_rp = image_fol_rp + fol_name + '/'
    mask_set = os.listdir(mask_rp)
    mask_set.sort()

    if len(mask_set) < 16:
        # img_rp = img_fol_rp + fol_name + '/'
        # print(len(mask_set), mask_rp)
        print(mask_set)
        last_name = mask_set[-1]  # 最后一张图
        last_order = int(last_name[:-4])  # 最后一张图的标签
        for _ in range(len(mask_set), 16):  # 临时变量，长度到16迭代
            last_order += 5  # 向后加5
            name = str(last_order).zfill(5)  # 长度为5
            shutil.copyfile(mask_rp + last_name, mask_rp + name + '.png')
            print('file copy', mask_rp + last_name, mask_rp + name + '.png')
            shutil.copyfile(image_rp + last_name[:-4] + '.jpg', image_rp + name + '.jpg')


#  ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/01b80e8e1a/00060.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/01b80e8e1a/00065.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/01b80e8e1a/00060.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/01b80e8e1a/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/01b80e8e1a/00060.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/01b80e8e1a/00075.png
# ['00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/02f3a5c4df/00060.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/02f3a5c4df/00065.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/02f3a5c4df/00060.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/02f3a5c4df/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/02f3a5c4df/00060.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/02f3a5c4df/00075.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/02f3a5c4df/00060.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/02f3a5c4df/00080.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/02f3a5c4df/00060.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/02f3a5c4df/00085.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/02f3a5c4df/00060.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/02f3a5c4df/00090.png
# ['00070.png', '00075.png', '00080.png', '00085.png', '00090.png', '00095.png', '00100.png', '00105.png', '00110.png', '00115.png', '00120.png', '00125.png', '00130.png', '00135.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/05fdbbdd7a/00135.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/05fdbbdd7a/00140.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/05fdbbdd7a/00135.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/05fdbbdd7a/00145.png
# ['00120.png', '00125.png', '00130.png', '00135.png', '00140.png', '00145.png', '00150.png', '00155.png', '00160.png', '00165.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/07b6e8fda8/00165.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/07b6e8fda8/00170.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/07b6e8fda8/00165.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/07b6e8fda8/00175.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/07b6e8fda8/00165.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/07b6e8fda8/00180.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/07b6e8fda8/00165.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/07b6e8fda8/00185.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/07b6e8fda8/00165.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/07b6e8fda8/00190.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/07b6e8fda8/00165.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/07b6e8fda8/00195.png
# ['00055.png', '00060.png', '00065.png', '00070.png', '00075.png', '00080.png', '00085.png', '00090.png', '00095.png', '00100.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/11e53de6f2/00100.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/11e53de6f2/00105.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/11e53de6f2/00100.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/11e53de6f2/00110.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/11e53de6f2/00100.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/11e53de6f2/00115.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/11e53de6f2/00100.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/11e53de6f2/00120.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/11e53de6f2/00100.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/11e53de6f2/00125.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/11e53de6f2/00100.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/11e53de6f2/00130.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/1232b2f1d4/00035.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/1232b2f1d4/00040.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/1232b2f1d4/00035.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/1232b2f1d4/00045.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/1232b2f1d4/00035.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/1232b2f1d4/00050.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/1232b2f1d4/00035.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/1232b2f1d4/00055.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/1232b2f1d4/00035.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/1232b2f1d4/00060.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/1232b2f1d4/00035.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/1232b2f1d4/00065.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/1232b2f1d4/00035.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/1232b2f1d4/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/1232b2f1d4/00035.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/1232b2f1d4/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00050.png', '00055.png', '00060.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/17b0d94172/00060.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/17b0d94172/00065.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/17b0d94172/00060.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/17b0d94172/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/17b0d94172/00060.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/17b0d94172/00075.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/17b0d94172/00060.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/17b0d94172/00080.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/1ab27ec7ea/00055.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/1ab27ec7ea/00060.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/1ab27ec7ea/00055.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/1ab27ec7ea/00065.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/1ab27ec7ea/00055.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/1ab27ec7ea/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/1ab27ec7ea/00055.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/1ab27ec7ea/00075.png
# ['00085.png', '00090.png', '00095.png', '00100.png', '00105.png', '00110.png', '00115.png', '00120.png', '00125.png', '00130.png', '00135.png', '00140.png', '00145.png', '00150.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/1bd87fe9ab/00150.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/1bd87fe9ab/00155.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/1bd87fe9ab/00150.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/1bd87fe9ab/00160.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/20c6d8b362/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/20c6d8b362/00050.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/20c6d8b362/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/20c6d8b362/00055.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/20c6d8b362/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/20c6d8b362/00060.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/20c6d8b362/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/20c6d8b362/00065.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/20c6d8b362/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/20c6d8b362/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/20c6d8b362/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/20c6d8b362/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2120d9c3c3/00065.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2120d9c3c3/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2120d9c3c3/00065.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2120d9c3c3/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2268e93b0a/00060.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2268e93b0a/00065.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2268e93b0a/00060.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2268e93b0a/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2268e93b0a/00060.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2268e93b0a/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/238d947c6b/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/238d947c6b/00050.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/238d947c6b/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/238d947c6b/00055.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/238d947c6b/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/238d947c6b/00060.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/238d947c6b/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/238d947c6b/00065.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/238d947c6b/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/238d947c6b/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/238d947c6b/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/238d947c6b/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/260dd9ad33/00065.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/260dd9ad33/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/260dd9ad33/00065.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/260dd9ad33/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png', '00070.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/26b895d91e/00070.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/26b895d91e/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2ac9ef904a/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2ac9ef904a/00050.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2ac9ef904a/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2ac9ef904a/00055.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2ac9ef904a/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2ac9ef904a/00060.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2ac9ef904a/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2ac9ef904a/00065.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2ac9ef904a/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2ac9ef904a/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2ac9ef904a/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2ac9ef904a/00075.png
# ['00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png', '00070.png', '00075.png', '00080.png', '00085.png', '00090.png', '00095.png', '00100.png', '00105.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2b659a49d7/00105.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2b659a49d7/00110.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2b659a49d7/00105.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2b659a49d7/00115.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2c11fedca8/00055.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2c11fedca8/00060.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2c11fedca8/00055.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2c11fedca8/00065.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2c11fedca8/00055.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2c11fedca8/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2c11fedca8/00055.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2c11fedca8/00075.png
# ['00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png', '00070.png', '00075.png', '00080.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2d9a1a1d49/00080.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2d9a1a1d49/00085.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2d9a1a1d49/00080.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2d9a1a1d49/00090.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2d9a1a1d49/00080.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2d9a1a1d49/00095.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2d9a1a1d49/00080.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2d9a1a1d49/00100.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2d9a1a1d49/00080.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2d9a1a1d49/00105.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2d9a1a1d49/00080.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2d9a1a1d49/00110.png
# ['00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png', '00070.png', '00075.png', '00080.png', '00085.png', '00090.png', '00095.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2e00393d96/00095.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2e00393d96/00100.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2e00393d96/00095.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2e00393d96/00105.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2e00393d96/00095.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2e00393d96/00110.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/30176e3615/00055.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/30176e3615/00060.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/30176e3615/00055.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/30176e3615/00065.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/30176e3615/00055.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/30176e3615/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/30176e3615/00055.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/30176e3615/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/3245e049fb/00065.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/3245e049fb/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/3245e049fb/00065.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/3245e049fb/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/3e2845307e/00060.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/3e2845307e/00065.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/3e2845307e/00060.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/3e2845307e/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/3e2845307e/00060.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/3e2845307e/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/3e91f10205/00025.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/3e91f10205/00030.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/3e91f10205/00025.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/3e91f10205/00035.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/3e91f10205/00025.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/3e91f10205/00040.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/3e91f10205/00025.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/3e91f10205/00045.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/3e91f10205/00025.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/3e91f10205/00050.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/3e91f10205/00025.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/3e91f10205/00055.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/3e91f10205/00025.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/3e91f10205/00060.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/3e91f10205/00025.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/3e91f10205/00065.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/3e91f10205/00025.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/3e91f10205/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/3e91f10205/00025.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/3e91f10205/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/3f45a470ad/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/3f45a470ad/00050.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/3f45a470ad/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/3f45a470ad/00055.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/3f45a470ad/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/3f45a470ad/00060.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/3f45a470ad/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/3f45a470ad/00065.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/3f45a470ad/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/3f45a470ad/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/3f45a470ad/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/3f45a470ad/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/420caf0859/00055.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/420caf0859/00060.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/420caf0859/00055.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/420caf0859/00065.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/420caf0859/00055.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/420caf0859/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/420caf0859/00055.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/420caf0859/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/46630b55ae/00055.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/46630b55ae/00060.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/46630b55ae/00055.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/46630b55ae/00065.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/46630b55ae/00055.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/46630b55ae/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/46630b55ae/00055.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/46630b55ae/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/49058178b8/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/49058178b8/00050.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/49058178b8/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/49058178b8/00055.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/49058178b8/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/49058178b8/00060.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/49058178b8/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/49058178b8/00065.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/49058178b8/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/49058178b8/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/49058178b8/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/49058178b8/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/4a8af115de/00020.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/4a8af115de/00025.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/4a8af115de/00020.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/4a8af115de/00030.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/4a8af115de/00020.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/4a8af115de/00035.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/4a8af115de/00020.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/4a8af115de/00040.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/4a8af115de/00020.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/4a8af115de/00045.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/4a8af115de/00020.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/4a8af115de/00050.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/4a8af115de/00020.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/4a8af115de/00055.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/4a8af115de/00020.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/4a8af115de/00060.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/4a8af115de/00020.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/4a8af115de/00065.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/4a8af115de/00020.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/4a8af115de/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/4a8af115de/00020.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/4a8af115de/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/4e49c2a9c7/00055.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/4e49c2a9c7/00060.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/4e49c2a9c7/00055.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/4e49c2a9c7/00065.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/4e49c2a9c7/00055.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/4e49c2a9c7/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/4e49c2a9c7/00055.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/4e49c2a9c7/00075.png
# ['00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png', '00070.png', '00075.png', '00080.png', '00085.png', '00090.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/4e7a28907f/00090.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/4e7a28907f/00095.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/4e7a28907f/00090.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/4e7a28907f/00100.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/51a597ee04/00050.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/51a597ee04/00055.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/51a597ee04/00050.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/51a597ee04/00060.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/51a597ee04/00050.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/51a597ee04/00065.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/51a597ee04/00050.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/51a597ee04/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/51a597ee04/00050.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/51a597ee04/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/598935ef05/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/598935ef05/00050.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/598935ef05/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/598935ef05/00055.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/598935ef05/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/598935ef05/00060.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/598935ef05/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/598935ef05/00065.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/598935ef05/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/598935ef05/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/598935ef05/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/598935ef05/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/5b07b4229d/00050.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/5b07b4229d/00055.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/5b07b4229d/00050.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/5b07b4229d/00060.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/5b07b4229d/00050.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/5b07b4229d/00065.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/5b07b4229d/00050.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/5b07b4229d/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/5b07b4229d/00050.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/5b07b4229d/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/5de9b90f24/00060.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/5de9b90f24/00065.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/5de9b90f24/00060.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/5de9b90f24/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/5de9b90f24/00060.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/5de9b90f24/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/61d08ef5a1/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/61d08ef5a1/00050.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/61d08ef5a1/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/61d08ef5a1/00055.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/61d08ef5a1/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/61d08ef5a1/00060.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/61d08ef5a1/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/61d08ef5a1/00065.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/61d08ef5a1/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/61d08ef5a1/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/61d08ef5a1/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/61d08ef5a1/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/61ed178ecb/00060.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/61ed178ecb/00065.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/61ed178ecb/00060.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/61ed178ecb/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/61ed178ecb/00060.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/61ed178ecb/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/6406c72e4d/00060.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/6406c72e4d/00065.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/6406c72e4d/00060.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/6406c72e4d/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/6406c72e4d/00060.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/6406c72e4d/00075.png
# ['00060.png', '00065.png', '00070.png', '00075.png', '00080.png', '00085.png', '00090.png', '00095.png', '00100.png', '00105.png', '00110.png', '00115.png', '00120.png', '00125.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/678a2357eb/00125.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/678a2357eb/00130.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/678a2357eb/00125.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/678a2357eb/00135.png
# ['00165.png', '00170.png', '00175.png', '00180.png', '00185.png', '00190.png', '00195.png', '00200.png', '00205.png', '00210.png', '00215.png', '00220.png', '00225.png', '00230.png', '00235.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/6a37a91708/00235.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/6a37a91708/00240.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/6c623fac5f/00035.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/6c623fac5f/00040.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/6c623fac5f/00035.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/6c623fac5f/00045.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/6c623fac5f/00035.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/6c623fac5f/00050.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/6c623fac5f/00035.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/6c623fac5f/00055.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/6c623fac5f/00035.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/6c623fac5f/00060.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/6c623fac5f/00035.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/6c623fac5f/00065.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/6c623fac5f/00035.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/6c623fac5f/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/6c623fac5f/00035.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/6c623fac5f/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/72690ef572/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/72690ef572/00050.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/72690ef572/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/72690ef572/00055.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/72690ef572/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/72690ef572/00060.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/72690ef572/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/72690ef572/00065.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/72690ef572/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/72690ef572/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/72690ef572/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/72690ef572/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/7435690c8c/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/7435690c8c/00050.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/7435690c8c/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/7435690c8c/00055.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/7435690c8c/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/7435690c8c/00060.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/7435690c8c/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/7435690c8c/00065.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/7435690c8c/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/7435690c8c/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/7435690c8c/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/7435690c8c/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/7660005554/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/7660005554/00050.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/7660005554/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/7660005554/00055.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/7660005554/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/7660005554/00060.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/7660005554/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/7660005554/00065.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/7660005554/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/7660005554/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/7660005554/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/7660005554/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png', '00070.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/76962c7ed2/00070.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/76962c7ed2/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/77610860e0/00055.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/77610860e0/00060.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/77610860e0/00055.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/77610860e0/00065.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/77610860e0/00055.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/77610860e0/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/77610860e0/00055.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/77610860e0/00075.png
# ['00055.png', '00060.png', '00065.png', '00070.png', '00075.png', '00080.png', '00085.png', '00090.png', '00095.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/77c834dc43/00095.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/77c834dc43/00100.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/77c834dc43/00095.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/77c834dc43/00105.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/77c834dc43/00095.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/77c834dc43/00110.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/77c834dc43/00095.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/77c834dc43/00115.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/77c834dc43/00095.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/77c834dc43/00120.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/77c834dc43/00095.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/77c834dc43/00125.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/77c834dc43/00095.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/77c834dc43/00130.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png', '00070.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/7c37d7991a/00070.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/7c37d7991a/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/7cec7296ae/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/7cec7296ae/00050.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/7cec7296ae/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/7cec7296ae/00055.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/7cec7296ae/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/7cec7296ae/00060.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/7cec7296ae/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/7cec7296ae/00065.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/7cec7296ae/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/7cec7296ae/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/7cec7296ae/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/7cec7296ae/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/7e9b6bef69/00065.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/7e9b6bef69/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/7e9b6bef69/00065.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/7e9b6bef69/00075.png
# ['00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png', '00070.png', '00075.png', '00080.png', '00085.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8088bda461/00085.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8088bda461/00090.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8088bda461/00085.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8088bda461/00095.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8088bda461/00085.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8088bda461/00100.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8088bda461/00085.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8088bda461/00105.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8088bda461/00085.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8088bda461/00110.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8088bda461/00085.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8088bda461/00115.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8200245704/00040.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8200245704/00045.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8200245704/00040.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8200245704/00050.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8200245704/00040.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8200245704/00055.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8200245704/00040.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8200245704/00060.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8200245704/00040.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8200245704/00065.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8200245704/00040.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8200245704/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8200245704/00040.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8200245704/00075.png
# ['00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png', '00070.png', '00075.png', '00080.png', '00085.png', '00090.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8345358fb8/00090.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8345358fb8/00095.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/83d3130ba0/00035.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/83d3130ba0/00040.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/83d3130ba0/00035.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/83d3130ba0/00045.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/83d3130ba0/00035.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/83d3130ba0/00050.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/83d3130ba0/00035.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/83d3130ba0/00055.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/83d3130ba0/00035.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/83d3130ba0/00060.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/83d3130ba0/00035.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/83d3130ba0/00065.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/83d3130ba0/00035.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/83d3130ba0/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/83d3130ba0/00035.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/83d3130ba0/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/84a4bf147d/00065.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/84a4bf147d/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/84a4bf147d/00065.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/84a4bf147d/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8647d06439/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8647d06439/00050.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8647d06439/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8647d06439/00055.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8647d06439/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8647d06439/00060.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8647d06439/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8647d06439/00065.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8647d06439/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8647d06439/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8647d06439/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8647d06439/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8b0cfbab97/00020.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8b0cfbab97/00025.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8b0cfbab97/00020.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8b0cfbab97/00030.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8b0cfbab97/00020.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8b0cfbab97/00035.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8b0cfbab97/00020.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8b0cfbab97/00040.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8b0cfbab97/00020.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8b0cfbab97/00045.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8b0cfbab97/00020.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8b0cfbab97/00050.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8b0cfbab97/00020.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8b0cfbab97/00055.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8b0cfbab97/00020.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8b0cfbab97/00060.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8b0cfbab97/00020.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8b0cfbab97/00065.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8b0cfbab97/00020.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8b0cfbab97/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8b0cfbab97/00020.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8b0cfbab97/00075.png
# ['00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png', '00070.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8b4fb018b7/00070.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8b4fb018b7/00075.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8b4fb018b7/00070.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8b4fb018b7/00080.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8bffc4374b/00065.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8bffc4374b/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8bffc4374b/00065.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8bffc4374b/00075.png
# ['00190.png', '00195.png', '00200.png', '00205.png', '00210.png', '00215.png', '00220.png', '00225.png', '00230.png', '00235.png', '00240.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/9047bf3222/00240.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/9047bf3222/00245.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/9047bf3222/00240.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/9047bf3222/00250.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/9047bf3222/00240.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/9047bf3222/00255.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/9047bf3222/00240.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/9047bf3222/00260.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/9047bf3222/00240.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/9047bf3222/00265.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/923137bb7f/00060.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/923137bb7f/00065.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/923137bb7f/00060.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/923137bb7f/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/923137bb7f/00060.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/923137bb7f/00075.png
# ['00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png', '00070.png', '00075.png', '00080.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/93ff35e801/00080.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/93ff35e801/00085.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/93ff35e801/00080.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/93ff35e801/00090.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/93ff35e801/00080.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/93ff35e801/00095.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/93ff35e801/00080.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/93ff35e801/00100.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/93ff35e801/00080.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/93ff35e801/00105.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/93ff35e801/00080.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/93ff35e801/00110.png
# ['00055.png', '00060.png', '00065.png', '00070.png', '00075.png', '00080.png', '00085.png', '00090.png', '00095.png', '00100.png', '00105.png', '00110.png', '00115.png', '00120.png', '00125.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/9582e0eb33/00125.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/9582e0eb33/00130.png
# ['00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png', '00070.png', '00075.png', '00080.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/9966f3adac/00080.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/9966f3adac/00085.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/9966f3adac/00080.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/9966f3adac/00090.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/9966f3adac/00080.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/9966f3adac/00095.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/9966f3adac/00080.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/9966f3adac/00100.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/9966f3adac/00080.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/9966f3adac/00105.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/9966f3adac/00080.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/9966f3adac/00110.png
# ['00055.png', '00060.png', '00065.png', '00070.png', '00075.png', '00080.png', '00085.png', '00090.png', '00095.png', '00100.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/9ecec5f8ea/00100.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/9ecec5f8ea/00105.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/9ecec5f8ea/00100.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/9ecec5f8ea/00110.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/9ecec5f8ea/00100.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/9ecec5f8ea/00115.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/9ecec5f8ea/00100.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/9ecec5f8ea/00120.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/9ecec5f8ea/00100.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/9ecec5f8ea/00125.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/9ecec5f8ea/00100.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/9ecec5f8ea/00130.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png', '00070.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/9f30bfe61e/00070.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/9f30bfe61e/00075.png
# ['00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png', '00070.png', '00075.png', '00080.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/a2554c9f6d/00080.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/a2554c9f6d/00085.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/a2554c9f6d/00080.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/a2554c9f6d/00090.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/a2554c9f6d/00080.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/a2554c9f6d/00095.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/a2554c9f6d/00080.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/a2554c9f6d/00100.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/a2554c9f6d/00080.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/a2554c9f6d/00105.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/a2554c9f6d/00080.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/a2554c9f6d/00110.png
# ['00140.png', '00145.png', '00150.png', '00155.png', '00160.png', '00165.png', '00170.png', '00175.png', '00180.png', '00185.png', '00190.png', '00195.png', '00200.png', '00205.png', '00210.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/a36e8c79d8/00210.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/a36e8c79d8/00215.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/a800d85e88/00050.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/a800d85e88/00055.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/a800d85e88/00050.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/a800d85e88/00060.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/a800d85e88/00050.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/a800d85e88/00065.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/a800d85e88/00050.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/a800d85e88/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/a800d85e88/00050.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/a800d85e88/00075.png
# ['00175.png', '00180.png', '00185.png', '00190.png', '00195.png', '00200.png', '00205.png', '00210.png', '00215.png', '00220.png', '00225.png', '00230.png', '00235.png', '00240.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ad54468654/00240.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ad54468654/00245.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ad54468654/00240.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ad54468654/00250.png
# ['00150.png', '00155.png', '00160.png', '00165.png', '00170.png', '00175.png', '00180.png', '00185.png', '00190.png', '00195.png', '00200.png', '00205.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ae2cecf5f6/00205.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ae2cecf5f6/00210.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ae2cecf5f6/00205.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ae2cecf5f6/00215.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ae2cecf5f6/00205.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ae2cecf5f6/00220.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ae2cecf5f6/00205.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ae2cecf5f6/00225.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b4805ae9cd/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b4805ae9cd/00050.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b4805ae9cd/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b4805ae9cd/00055.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b4805ae9cd/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b4805ae9cd/00060.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b4805ae9cd/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b4805ae9cd/00065.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b4805ae9cd/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b4805ae9cd/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b4805ae9cd/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b4805ae9cd/00075.png
# ['00065.png', '00070.png', '00075.png', '00080.png', '00085.png', '00090.png', '00095.png', '00105.png', '00110.png', '00115.png', '00120.png', '00125.png', '00130.png', '00135.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b5a09a83f3/00135.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b5a09a83f3/00140.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b5a09a83f3/00135.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b5a09a83f3/00145.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b70a2c0ab1/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b70a2c0ab1/00050.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b70a2c0ab1/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b70a2c0ab1/00055.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b70a2c0ab1/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b70a2c0ab1/00060.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b70a2c0ab1/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b70a2c0ab1/00065.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b70a2c0ab1/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b70a2c0ab1/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b70a2c0ab1/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b70a2c0ab1/00075.png
# ['00105.png', '00110.png', '00115.png', '00120.png', '00125.png', '00130.png', '00135.png', '00140.png', '00145.png', '00150.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b7f675fb98/00150.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b7f675fb98/00155.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b7f675fb98/00150.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b7f675fb98/00160.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b7f675fb98/00150.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b7f675fb98/00165.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b7f675fb98/00150.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b7f675fb98/00170.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b7f675fb98/00150.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b7f675fb98/00175.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b7f675fb98/00150.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b7f675fb98/00180.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b7fb871660/00050.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b7fb871660/00055.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b7fb871660/00050.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b7fb871660/00060.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b7fb871660/00050.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b7fb871660/00065.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b7fb871660/00050.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b7fb871660/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b7fb871660/00050.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b7fb871660/00075.png
# ['00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png', '00070.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b871db031a/00070.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b871db031a/00075.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b871db031a/00070.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b871db031a/00080.png
# ['00220.png', '00225.png', '00230.png', '00235.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b938d79dff/00235.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b938d79dff/00240.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b938d79dff/00235.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b938d79dff/00245.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b938d79dff/00235.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b938d79dff/00250.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b938d79dff/00235.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b938d79dff/00255.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b938d79dff/00235.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b938d79dff/00260.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b938d79dff/00235.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b938d79dff/00265.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b938d79dff/00235.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b938d79dff/00270.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b938d79dff/00235.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b938d79dff/00275.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b938d79dff/00235.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b938d79dff/00280.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b938d79dff/00235.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b938d79dff/00285.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b938d79dff/00235.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b938d79dff/00290.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b938d79dff/00235.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b938d79dff/00295.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png', '00070.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b941aef1a0/00070.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b941aef1a0/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/bd321d2be6/00060.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/bd321d2be6/00065.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/bd321d2be6/00060.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/bd321d2be6/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/bd321d2be6/00060.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/bd321d2be6/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/bd5b2e2848/00040.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/bd5b2e2848/00045.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/bd5b2e2848/00040.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/bd5b2e2848/00050.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/bd5b2e2848/00040.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/bd5b2e2848/00055.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/bd5b2e2848/00040.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/bd5b2e2848/00060.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/bd5b2e2848/00040.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/bd5b2e2848/00065.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/bd5b2e2848/00040.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/bd5b2e2848/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/bd5b2e2848/00040.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/bd5b2e2848/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/c52bce43db/00065.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/c52bce43db/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/c52bce43db/00065.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/c52bce43db/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/c6a12c131f/00050.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/c6a12c131f/00055.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/c6a12c131f/00050.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/c6a12c131f/00060.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/c6a12c131f/00050.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/c6a12c131f/00065.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/c6a12c131f/00050.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/c6a12c131f/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/c6a12c131f/00050.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/c6a12c131f/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png', '00070.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ca91c69e3b/00070.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ca91c69e3b/00075.png
# ['00050.png', '00055.png', '00060.png', '00065.png', '00070.png', '00075.png', '00080.png', '00085.png', '00090.png', '00095.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ca91e99105/00095.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ca91e99105/00100.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ca91e99105/00095.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ca91e99105/00105.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ca91e99105/00095.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ca91e99105/00110.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ca91e99105/00095.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ca91e99105/00115.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ca91e99105/00095.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ca91e99105/00120.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ca91e99105/00095.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ca91e99105/00125.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/cff8191891/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/cff8191891/00050.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/cff8191891/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/cff8191891/00055.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/cff8191891/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/cff8191891/00060.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/cff8191891/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/cff8191891/00065.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/cff8191891/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/cff8191891/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/cff8191891/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/cff8191891/00075.png
# ['00065.png', '00070.png', '00075.png', '00080.png', '00085.png', '00090.png', '00095.png', '00100.png', '00105.png', '00110.png', '00115.png', '00120.png', '00125.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d107a1457c/00125.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d107a1457c/00130.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d107a1457c/00125.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d107a1457c/00135.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d107a1457c/00125.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d107a1457c/00140.png
# ['00000.png', '00005.png', '00010.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d2484bff33/00065.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d2484bff33/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d2484bff33/00065.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d2484bff33/00075.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d2484bff33/00065.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d2484bff33/00080.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d292a50c7f/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d292a50c7f/00050.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d292a50c7f/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d292a50c7f/00055.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d292a50c7f/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d292a50c7f/00060.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d292a50c7f/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d292a50c7f/00065.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d292a50c7f/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d292a50c7f/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d292a50c7f/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d292a50c7f/00075.png
# ['00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d3f5c309cc/00065.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d3f5c309cc/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d3f5c309cc/00065.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d3f5c309cc/00075.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d3f5c309cc/00065.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d3f5c309cc/00080.png
# ['00030.png', '00035.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png', '00070.png', '00075.png', '00080.png', '00085.png', '00090.png', '00095.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d44e6acd1d/00095.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d44e6acd1d/00100.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d44e6acd1d/00095.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d44e6acd1d/00105.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d44e6acd1d/00095.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d44e6acd1d/00110.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d7157a9f44/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d7157a9f44/00050.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d7157a9f44/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d7157a9f44/00055.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d7157a9f44/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d7157a9f44/00060.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d7157a9f44/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d7157a9f44/00065.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d7157a9f44/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d7157a9f44/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d7157a9f44/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d7157a9f44/00075.png
# ['00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png', '00070.png', '00075.png', '00080.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d9010348a1/00080.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d9010348a1/00085.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d9010348a1/00080.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d9010348a1/00090.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/df0638b0a0/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/df0638b0a0/00050.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/df0638b0a0/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/df0638b0a0/00055.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/df0638b0a0/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/df0638b0a0/00060.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/df0638b0a0/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/df0638b0a0/00065.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/df0638b0a0/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/df0638b0a0/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/df0638b0a0/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/df0638b0a0/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/df5e2152b3/00065.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/df5e2152b3/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/df5e2152b3/00065.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/df5e2152b3/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e0bdb5dfae/00035.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e0bdb5dfae/00040.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e0bdb5dfae/00035.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e0bdb5dfae/00045.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e0bdb5dfae/00035.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e0bdb5dfae/00050.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e0bdb5dfae/00035.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e0bdb5dfae/00055.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e0bdb5dfae/00035.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e0bdb5dfae/00060.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e0bdb5dfae/00035.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e0bdb5dfae/00065.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e0bdb5dfae/00035.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e0bdb5dfae/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e0bdb5dfae/00035.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e0bdb5dfae/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png', '00070.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e1194c2e9d/00070.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e1194c2e9d/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e16945b951/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e16945b951/00050.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e16945b951/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e16945b951/00055.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e16945b951/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e16945b951/00060.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e16945b951/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e16945b951/00065.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e16945b951/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e16945b951/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e16945b951/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e16945b951/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e3bf38265f/00050.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e3bf38265f/00055.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e3bf38265f/00050.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e3bf38265f/00060.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e3bf38265f/00050.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e3bf38265f/00065.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e3bf38265f/00050.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e3bf38265f/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e3bf38265f/00050.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e3bf38265f/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e3d60e82d5/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e3d60e82d5/00050.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e3d60e82d5/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e3d60e82d5/00055.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e3d60e82d5/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e3d60e82d5/00060.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e3d60e82d5/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e3d60e82d5/00065.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e3d60e82d5/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e3d60e82d5/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e3d60e82d5/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e3d60e82d5/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png', '00070.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e415093d27/00070.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e415093d27/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e495f32c60/00040.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e495f32c60/00045.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e495f32c60/00040.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e495f32c60/00050.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e495f32c60/00040.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e495f32c60/00055.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e495f32c60/00040.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e495f32c60/00060.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e495f32c60/00040.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e495f32c60/00065.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e495f32c60/00040.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e495f32c60/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e495f32c60/00040.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e495f32c60/00075.png
# ['00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e4e2983570/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e4e2983570/00050.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e4e2983570/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e4e2983570/00055.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e4e2983570/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e4e2983570/00060.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e4e2983570/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e4e2983570/00065.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e4e2983570/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e4e2983570/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e4e2983570/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e4e2983570/00075.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e4e2983570/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e4e2983570/00080.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png', '00070.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e4ffb6d0dd/00070.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e4ffb6d0dd/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e5ce96a55d/00060.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e5ce96a55d/00065.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e5ce96a55d/00060.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e5ce96a55d/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e5ce96a55d/00060.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e5ce96a55d/00075.png
# ['00150.png', '00155.png', '00160.png', '00165.png', '00170.png', '00175.png', '00180.png', '00185.png', '00190.png', '00195.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e6be243065/00195.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e6be243065/00200.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e6be243065/00195.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e6be243065/00205.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e6be243065/00195.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e6be243065/00210.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e6be243065/00195.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e6be243065/00215.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e6be243065/00195.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e6be243065/00220.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e6be243065/00195.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e6be243065/00225.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png', '00070.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e75a466eea/00070.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e75a466eea/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png', '00070.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e8f7904326/00070.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e8f7904326/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e92b6bfea4/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e92b6bfea4/00050.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e92b6bfea4/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e92b6bfea4/00055.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e92b6bfea4/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e92b6bfea4/00060.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e92b6bfea4/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e92b6bfea4/00065.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e92b6bfea4/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e92b6bfea4/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e92b6bfea4/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e92b6bfea4/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e99706b555/00040.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e99706b555/00045.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e99706b555/00040.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e99706b555/00050.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e99706b555/00040.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e99706b555/00055.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e99706b555/00040.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e99706b555/00060.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e99706b555/00040.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e99706b555/00065.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e99706b555/00040.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e99706b555/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e99706b555/00040.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e99706b555/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png', '00070.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ea444a37eb/00070.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ea444a37eb/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ef0a8e8f35/00055.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ef0a8e8f35/00060.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ef0a8e8f35/00055.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ef0a8e8f35/00065.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ef0a8e8f35/00055.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ef0a8e8f35/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ef0a8e8f35/00055.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ef0a8e8f35/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/f1d99239eb/00065.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/f1d99239eb/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/f1d99239eb/00065.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/f1d99239eb/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/f305a56d9f/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/f305a56d9f/00050.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/f305a56d9f/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/f305a56d9f/00055.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/f305a56d9f/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/f305a56d9f/00060.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/f305a56d9f/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/f305a56d9f/00065.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/f305a56d9f/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/f305a56d9f/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/f305a56d9f/00045.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/f305a56d9f/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png']
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/fe6c244f63/00065.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/fe6c244f63/00070.png
# file copy /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/fe6c244f63/00065.png /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/fe6c244f63/00075.png

# /home/guoxi/anaconda3/envs/pytorch/bin/python /data1/guoxi/p3d/P3D_UNet_Segmentation/pre_padding.py
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/01b80e8e1a/00060.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/01b80e8e1a/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/01b80e8e1a/00060.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/01b80e8e1a/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/01b80e8e1a/00060.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/01b80e8e1a/00075.png
# ['00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/02f3a5c4df/00060.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/02f3a5c4df/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/02f3a5c4df/00060.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/02f3a5c4df/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/02f3a5c4df/00060.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/02f3a5c4df/00075.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/02f3a5c4df/00060.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/02f3a5c4df/00080.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/02f3a5c4df/00060.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/02f3a5c4df/00085.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/02f3a5c4df/00060.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/02f3a5c4df/00090.png
# ['00070.png', '00075.png', '00080.png', '00085.png', '00090.png', '00095.png', '00100.png', '00105.png', '00110.png', '00115.png', '00120.png', '00125.png', '00130.png', '00135.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/05fdbbdd7a/00135.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/05fdbbdd7a/00140.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/05fdbbdd7a/00135.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/05fdbbdd7a/00145.png
# ['00120.png', '00125.png', '00130.png', '00135.png', '00140.png', '00145.png', '00150.png', '00155.png', '00160.png', '00165.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/07b6e8fda8/00165.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/07b6e8fda8/00170.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/07b6e8fda8/00165.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/07b6e8fda8/00175.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/07b6e8fda8/00165.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/07b6e8fda8/00180.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/07b6e8fda8/00165.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/07b6e8fda8/00185.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/07b6e8fda8/00165.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/07b6e8fda8/00190.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/07b6e8fda8/00165.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/07b6e8fda8/00195.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/0d9cc80d7e/00050.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/0d9cc80d7e/00055.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/0d9cc80d7e/00050.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/0d9cc80d7e/00060.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/0d9cc80d7e/00050.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/0d9cc80d7e/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/0d9cc80d7e/00050.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/0d9cc80d7e/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/0d9cc80d7e/00050.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/0d9cc80d7e/00075.png
# ['00055.png', '00060.png', '00065.png', '00070.png', '00075.png', '00080.png', '00085.png', '00090.png', '00095.png', '00100.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/11e53de6f2/00100.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/11e53de6f2/00105.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/11e53de6f2/00100.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/11e53de6f2/00110.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/11e53de6f2/00100.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/11e53de6f2/00115.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/11e53de6f2/00100.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/11e53de6f2/00120.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/11e53de6f2/00100.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/11e53de6f2/00125.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/11e53de6f2/00100.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/11e53de6f2/00130.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/1232b2f1d4/00035.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/1232b2f1d4/00040.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/1232b2f1d4/00035.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/1232b2f1d4/00045.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/1232b2f1d4/00035.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/1232b2f1d4/00050.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/1232b2f1d4/00035.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/1232b2f1d4/00055.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/1232b2f1d4/00035.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/1232b2f1d4/00060.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/1232b2f1d4/00035.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/1232b2f1d4/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/1232b2f1d4/00035.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/1232b2f1d4/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/1232b2f1d4/00035.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/1232b2f1d4/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00050.png', '00055.png', '00060.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/17b0d94172/00060.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/17b0d94172/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/17b0d94172/00060.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/17b0d94172/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/17b0d94172/00060.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/17b0d94172/00075.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/17b0d94172/00060.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/17b0d94172/00080.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/1ab27ec7ea/00055.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/1ab27ec7ea/00060.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/1ab27ec7ea/00055.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/1ab27ec7ea/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/1ab27ec7ea/00055.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/1ab27ec7ea/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/1ab27ec7ea/00055.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/1ab27ec7ea/00075.png
# ['00085.png', '00090.png', '00095.png', '00100.png', '00105.png', '00110.png', '00115.png', '00120.png', '00125.png', '00130.png', '00135.png', '00140.png', '00145.png', '00150.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/1bd87fe9ab/00150.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/1bd87fe9ab/00155.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/1bd87fe9ab/00150.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/1bd87fe9ab/00160.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/1d746352a6/00065.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/1d746352a6/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/1d746352a6/00065.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/1d746352a6/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/20c6d8b362/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/20c6d8b362/00050.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/20c6d8b362/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/20c6d8b362/00055.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/20c6d8b362/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/20c6d8b362/00060.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/20c6d8b362/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/20c6d8b362/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/20c6d8b362/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/20c6d8b362/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/20c6d8b362/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/20c6d8b362/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/2120d9c3c3/00065.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/2120d9c3c3/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/2120d9c3c3/00065.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/2120d9c3c3/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/22472f7395/00040.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/22472f7395/00045.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/22472f7395/00040.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/22472f7395/00050.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/22472f7395/00040.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/22472f7395/00055.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/22472f7395/00040.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/22472f7395/00060.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/22472f7395/00040.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/22472f7395/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/22472f7395/00040.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/22472f7395/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/22472f7395/00040.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/22472f7395/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/2268e93b0a/00060.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/2268e93b0a/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/2268e93b0a/00060.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/2268e93b0a/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/2268e93b0a/00060.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/2268e93b0a/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/238d947c6b/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/238d947c6b/00050.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/238d947c6b/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/238d947c6b/00055.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/238d947c6b/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/238d947c6b/00060.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/238d947c6b/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/238d947c6b/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/238d947c6b/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/238d947c6b/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/238d947c6b/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/238d947c6b/00075.png
# ['00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png', '00070.png', '00075.png', '00080.png', '00085.png', '00090.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/250116161c/00090.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/250116161c/00095.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/260dd9ad33/00065.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/260dd9ad33/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/260dd9ad33/00065.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/260dd9ad33/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png', '00070.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/26b895d91e/00070.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/26b895d91e/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/2ac9ef904a/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/2ac9ef904a/00050.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/2ac9ef904a/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/2ac9ef904a/00055.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/2ac9ef904a/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/2ac9ef904a/00060.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/2ac9ef904a/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/2ac9ef904a/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/2ac9ef904a/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/2ac9ef904a/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/2ac9ef904a/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/2ac9ef904a/00075.png
# ['00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png', '00070.png', '00075.png', '00080.png', '00085.png', '00090.png', '00095.png', '00100.png', '00105.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/2b659a49d7/00105.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/2b659a49d7/00110.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/2b659a49d7/00105.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/2b659a49d7/00115.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/2c11fedca8/00055.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/2c11fedca8/00060.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/2c11fedca8/00055.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/2c11fedca8/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/2c11fedca8/00055.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/2c11fedca8/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/2c11fedca8/00055.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/2c11fedca8/00075.png
# ['00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png', '00070.png', '00075.png', '00080.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/2d9a1a1d49/00080.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/2d9a1a1d49/00085.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/2d9a1a1d49/00080.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/2d9a1a1d49/00090.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/2d9a1a1d49/00080.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/2d9a1a1d49/00095.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/2d9a1a1d49/00080.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/2d9a1a1d49/00100.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/2d9a1a1d49/00080.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/2d9a1a1d49/00105.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/2d9a1a1d49/00080.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/2d9a1a1d49/00110.png
# ['00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png', '00070.png', '00075.png', '00080.png', '00085.png', '00090.png', '00095.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/2e00393d96/00095.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/2e00393d96/00100.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/2e00393d96/00095.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/2e00393d96/00105.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/2e00393d96/00095.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/2e00393d96/00110.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/30176e3615/00055.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/30176e3615/00060.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/30176e3615/00055.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/30176e3615/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/30176e3615/00055.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/30176e3615/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/30176e3615/00055.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/30176e3615/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/3245e049fb/00065.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/3245e049fb/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/3245e049fb/00065.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/3245e049fb/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/37c19d1087/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/37c19d1087/00050.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/37c19d1087/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/37c19d1087/00055.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/37c19d1087/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/37c19d1087/00060.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/37c19d1087/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/37c19d1087/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/37c19d1087/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/37c19d1087/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/37c19d1087/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/37c19d1087/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/3e2845307e/00060.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/3e2845307e/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/3e2845307e/00060.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/3e2845307e/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/3e2845307e/00060.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/3e2845307e/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/3e91f10205/00025.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/3e91f10205/00030.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/3e91f10205/00025.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/3e91f10205/00035.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/3e91f10205/00025.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/3e91f10205/00040.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/3e91f10205/00025.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/3e91f10205/00045.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/3e91f10205/00025.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/3e91f10205/00050.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/3e91f10205/00025.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/3e91f10205/00055.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/3e91f10205/00025.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/3e91f10205/00060.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/3e91f10205/00025.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/3e91f10205/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/3e91f10205/00025.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/3e91f10205/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/3e91f10205/00025.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/3e91f10205/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/3f45a470ad/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/3f45a470ad/00050.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/3f45a470ad/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/3f45a470ad/00055.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/3f45a470ad/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/3f45a470ad/00060.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/3f45a470ad/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/3f45a470ad/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/3f45a470ad/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/3f45a470ad/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/3f45a470ad/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/3f45a470ad/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/420caf0859/00055.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/420caf0859/00060.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/420caf0859/00055.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/420caf0859/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/420caf0859/00055.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/420caf0859/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/420caf0859/00055.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/420caf0859/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/46630b55ae/00055.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/46630b55ae/00060.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/46630b55ae/00055.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/46630b55ae/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/46630b55ae/00055.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/46630b55ae/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/46630b55ae/00055.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/46630b55ae/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/49058178b8/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/49058178b8/00050.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/49058178b8/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/49058178b8/00055.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/49058178b8/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/49058178b8/00060.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/49058178b8/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/49058178b8/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/49058178b8/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/49058178b8/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/49058178b8/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/49058178b8/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/4a8af115de/00020.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/4a8af115de/00025.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/4a8af115de/00020.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/4a8af115de/00030.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/4a8af115de/00020.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/4a8af115de/00035.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/4a8af115de/00020.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/4a8af115de/00040.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/4a8af115de/00020.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/4a8af115de/00045.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/4a8af115de/00020.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/4a8af115de/00050.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/4a8af115de/00020.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/4a8af115de/00055.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/4a8af115de/00020.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/4a8af115de/00060.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/4a8af115de/00020.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/4a8af115de/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/4a8af115de/00020.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/4a8af115de/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/4a8af115de/00020.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/4a8af115de/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/4e49c2a9c7/00055.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/4e49c2a9c7/00060.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/4e49c2a9c7/00055.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/4e49c2a9c7/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/4e49c2a9c7/00055.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/4e49c2a9c7/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/4e49c2a9c7/00055.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/4e49c2a9c7/00075.png
# ['00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png', '00070.png', '00075.png', '00080.png', '00085.png', '00090.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/4e7a28907f/00090.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/4e7a28907f/00095.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/4e7a28907f/00090.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/4e7a28907f/00100.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/51a597ee04/00050.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/51a597ee04/00055.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/51a597ee04/00050.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/51a597ee04/00060.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/51a597ee04/00050.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/51a597ee04/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/51a597ee04/00050.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/51a597ee04/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/51a597ee04/00050.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/51a597ee04/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/57d5289a01/00060.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/57d5289a01/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/57d5289a01/00060.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/57d5289a01/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/57d5289a01/00060.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/57d5289a01/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/585dd0f208/00065.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/585dd0f208/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/585dd0f208/00065.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/585dd0f208/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/598935ef05/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/598935ef05/00050.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/598935ef05/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/598935ef05/00055.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/598935ef05/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/598935ef05/00060.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/598935ef05/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/598935ef05/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/598935ef05/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/598935ef05/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/598935ef05/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/598935ef05/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/5b07b4229d/00050.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/5b07b4229d/00055.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/5b07b4229d/00050.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/5b07b4229d/00060.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/5b07b4229d/00050.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/5b07b4229d/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/5b07b4229d/00050.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/5b07b4229d/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/5b07b4229d/00050.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/5b07b4229d/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/5de9b90f24/00060.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/5de9b90f24/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/5de9b90f24/00060.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/5de9b90f24/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/5de9b90f24/00060.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/5de9b90f24/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/61d08ef5a1/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/61d08ef5a1/00050.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/61d08ef5a1/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/61d08ef5a1/00055.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/61d08ef5a1/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/61d08ef5a1/00060.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/61d08ef5a1/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/61d08ef5a1/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/61d08ef5a1/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/61d08ef5a1/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/61d08ef5a1/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/61d08ef5a1/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/61ed178ecb/00060.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/61ed178ecb/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/61ed178ecb/00060.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/61ed178ecb/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/61ed178ecb/00060.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/61ed178ecb/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/6406c72e4d/00060.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/6406c72e4d/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/6406c72e4d/00060.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/6406c72e4d/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/6406c72e4d/00060.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/6406c72e4d/00075.png
# ['00060.png', '00065.png', '00070.png', '00075.png', '00080.png', '00085.png', '00090.png', '00095.png', '00100.png', '00105.png', '00110.png', '00115.png', '00120.png', '00125.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/678a2357eb/00125.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/678a2357eb/00130.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/678a2357eb/00125.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/678a2357eb/00135.png
# ['00165.png', '00170.png', '00175.png', '00180.png', '00185.png', '00190.png', '00195.png', '00200.png', '00205.png', '00210.png', '00215.png', '00220.png', '00225.png', '00230.png', '00235.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/6a37a91708/00235.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/6a37a91708/00240.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/6c23d89189/00060.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/6c23d89189/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/6c23d89189/00060.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/6c23d89189/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/6c23d89189/00060.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/6c23d89189/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/6c623fac5f/00035.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/6c623fac5f/00040.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/6c623fac5f/00035.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/6c623fac5f/00045.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/6c623fac5f/00035.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/6c623fac5f/00050.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/6c623fac5f/00035.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/6c623fac5f/00055.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/6c623fac5f/00035.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/6c623fac5f/00060.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/6c623fac5f/00035.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/6c623fac5f/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/6c623fac5f/00035.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/6c623fac5f/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/6c623fac5f/00035.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/6c623fac5f/00075.png
# ['00065.png', '00070.png', '00075.png', '00080.png', '00085.png', '00090.png', '00095.png', '00100.png', '00105.png', '00110.png', '00115.png', '00120.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/6e618d26b6/00120.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/6e618d26b6/00125.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/6e618d26b6/00120.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/6e618d26b6/00130.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/6e618d26b6/00120.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/6e618d26b6/00135.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/6e618d26b6/00120.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/6e618d26b6/00140.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/72690ef572/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/72690ef572/00050.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/72690ef572/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/72690ef572/00055.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/72690ef572/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/72690ef572/00060.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/72690ef572/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/72690ef572/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/72690ef572/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/72690ef572/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/72690ef572/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/72690ef572/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/7435690c8c/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/7435690c8c/00050.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/7435690c8c/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/7435690c8c/00055.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/7435690c8c/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/7435690c8c/00060.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/7435690c8c/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/7435690c8c/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/7435690c8c/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/7435690c8c/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/7435690c8c/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/7435690c8c/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/7660005554/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/7660005554/00050.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/7660005554/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/7660005554/00055.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/7660005554/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/7660005554/00060.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/7660005554/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/7660005554/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/7660005554/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/7660005554/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/7660005554/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/7660005554/00075.png
# ['00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/76693db153/00060.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/76693db153/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/76693db153/00060.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/76693db153/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/76693db153/00060.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/76693db153/00075.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/76693db153/00060.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/76693db153/00080.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/76693db153/00060.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/76693db153/00085.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png', '00070.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/76962c7ed2/00070.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/76962c7ed2/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/77610860e0/00055.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/77610860e0/00060.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/77610860e0/00055.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/77610860e0/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/77610860e0/00055.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/77610860e0/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/77610860e0/00055.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/77610860e0/00075.png
# ['00055.png', '00060.png', '00065.png', '00070.png', '00075.png', '00080.png', '00085.png', '00090.png', '00095.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/77c834dc43/00095.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/77c834dc43/00100.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/77c834dc43/00095.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/77c834dc43/00105.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/77c834dc43/00095.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/77c834dc43/00110.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/77c834dc43/00095.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/77c834dc43/00115.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/77c834dc43/00095.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/77c834dc43/00120.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/77c834dc43/00095.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/77c834dc43/00125.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/77c834dc43/00095.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/77c834dc43/00130.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png', '00070.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/784398620a/00070.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/784398620a/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png', '00070.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/7c37d7991a/00070.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/7c37d7991a/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/7cec7296ae/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/7cec7296ae/00050.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/7cec7296ae/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/7cec7296ae/00055.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/7cec7296ae/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/7cec7296ae/00060.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/7cec7296ae/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/7cec7296ae/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/7cec7296ae/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/7cec7296ae/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/7cec7296ae/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/7cec7296ae/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/7e9b6bef69/00065.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/7e9b6bef69/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/7e9b6bef69/00065.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/7e9b6bef69/00075.png
# ['00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png', '00070.png', '00075.png', '00080.png', '00085.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8088bda461/00085.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8088bda461/00090.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8088bda461/00085.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8088bda461/00095.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8088bda461/00085.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8088bda461/00100.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8088bda461/00085.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8088bda461/00105.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8088bda461/00085.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8088bda461/00110.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8088bda461/00085.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8088bda461/00115.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8200245704/00040.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8200245704/00045.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8200245704/00040.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8200245704/00050.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8200245704/00040.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8200245704/00055.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8200245704/00040.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8200245704/00060.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8200245704/00040.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8200245704/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8200245704/00040.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8200245704/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8200245704/00040.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8200245704/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/823e7a86e8/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/823e7a86e8/00050.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/823e7a86e8/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/823e7a86e8/00055.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/823e7a86e8/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/823e7a86e8/00060.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/823e7a86e8/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/823e7a86e8/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/823e7a86e8/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/823e7a86e8/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/823e7a86e8/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/823e7a86e8/00075.png
# ['00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png', '00070.png', '00075.png', '00080.png', '00085.png', '00090.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8345358fb8/00090.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8345358fb8/00095.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/83d3130ba0/00035.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/83d3130ba0/00040.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/83d3130ba0/00035.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/83d3130ba0/00045.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/83d3130ba0/00035.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/83d3130ba0/00050.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/83d3130ba0/00035.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/83d3130ba0/00055.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/83d3130ba0/00035.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/83d3130ba0/00060.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/83d3130ba0/00035.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/83d3130ba0/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/83d3130ba0/00035.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/83d3130ba0/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/83d3130ba0/00035.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/83d3130ba0/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/84a4bf147d/00065.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/84a4bf147d/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/84a4bf147d/00065.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/84a4bf147d/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8647d06439/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8647d06439/00050.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8647d06439/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8647d06439/00055.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8647d06439/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8647d06439/00060.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8647d06439/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8647d06439/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8647d06439/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8647d06439/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8647d06439/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8647d06439/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8b0cfbab97/00020.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8b0cfbab97/00025.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8b0cfbab97/00020.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8b0cfbab97/00030.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8b0cfbab97/00020.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8b0cfbab97/00035.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8b0cfbab97/00020.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8b0cfbab97/00040.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8b0cfbab97/00020.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8b0cfbab97/00045.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8b0cfbab97/00020.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8b0cfbab97/00050.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8b0cfbab97/00020.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8b0cfbab97/00055.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8b0cfbab97/00020.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8b0cfbab97/00060.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8b0cfbab97/00020.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8b0cfbab97/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8b0cfbab97/00020.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8b0cfbab97/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8b0cfbab97/00020.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8b0cfbab97/00075.png
# ['00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png', '00070.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8b4fb018b7/00070.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8b4fb018b7/00075.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8b4fb018b7/00070.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8b4fb018b7/00080.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8bffc4374b/00065.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8bffc4374b/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8bffc4374b/00065.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/8bffc4374b/00075.png
# ['00190.png', '00195.png', '00200.png', '00205.png', '00210.png', '00215.png', '00220.png', '00225.png', '00230.png', '00235.png', '00240.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/9047bf3222/00240.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/9047bf3222/00245.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/9047bf3222/00240.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/9047bf3222/00250.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/9047bf3222/00240.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/9047bf3222/00255.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/9047bf3222/00240.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/9047bf3222/00260.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/9047bf3222/00240.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/9047bf3222/00265.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/923137bb7f/00060.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/923137bb7f/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/923137bb7f/00060.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/923137bb7f/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/923137bb7f/00060.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/923137bb7f/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png', '00070.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/92a28cd233/00070.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/92a28cd233/00075.png
# ['00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png', '00070.png', '00075.png', '00080.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/93ff35e801/00080.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/93ff35e801/00085.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/93ff35e801/00080.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/93ff35e801/00090.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/93ff35e801/00080.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/93ff35e801/00095.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/93ff35e801/00080.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/93ff35e801/00100.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/93ff35e801/00080.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/93ff35e801/00105.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/93ff35e801/00080.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/93ff35e801/00110.png
# ['00055.png', '00060.png', '00065.png', '00070.png', '00075.png', '00080.png', '00085.png', '00090.png', '00095.png', '00100.png', '00105.png', '00110.png', '00115.png', '00120.png', '00125.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/9582e0eb33/00125.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/9582e0eb33/00130.png
# ['00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png', '00070.png', '00075.png', '00080.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/9966f3adac/00080.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/9966f3adac/00085.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/9966f3adac/00080.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/9966f3adac/00090.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/9966f3adac/00080.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/9966f3adac/00095.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/9966f3adac/00080.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/9966f3adac/00100.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/9966f3adac/00080.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/9966f3adac/00105.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/9966f3adac/00080.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/9966f3adac/00110.png
# ['00055.png', '00060.png', '00065.png', '00070.png', '00075.png', '00080.png', '00085.png', '00090.png', '00095.png', '00100.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/9ecec5f8ea/00100.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/9ecec5f8ea/00105.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/9ecec5f8ea/00100.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/9ecec5f8ea/00110.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/9ecec5f8ea/00100.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/9ecec5f8ea/00115.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/9ecec5f8ea/00100.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/9ecec5f8ea/00120.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/9ecec5f8ea/00100.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/9ecec5f8ea/00125.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/9ecec5f8ea/00100.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/9ecec5f8ea/00130.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png', '00070.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/9f30bfe61e/00070.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/9f30bfe61e/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/a023141022/00055.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/a023141022/00060.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/a023141022/00055.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/a023141022/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/a023141022/00055.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/a023141022/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/a023141022/00055.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/a023141022/00075.png
# ['00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png', '00070.png', '00075.png', '00080.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/a2554c9f6d/00080.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/a2554c9f6d/00085.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/a2554c9f6d/00080.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/a2554c9f6d/00090.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/a2554c9f6d/00080.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/a2554c9f6d/00095.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/a2554c9f6d/00080.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/a2554c9f6d/00100.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/a2554c9f6d/00080.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/a2554c9f6d/00105.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/a2554c9f6d/00080.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/a2554c9f6d/00110.png
# ['00140.png', '00145.png', '00150.png', '00155.png', '00160.png', '00165.png', '00170.png', '00175.png', '00180.png', '00185.png', '00190.png', '00195.png', '00200.png', '00205.png', '00210.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/a36e8c79d8/00210.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/a36e8c79d8/00215.png
# ['00070.png', '00075.png', '00080.png', '00085.png', '00090.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/a402dc0dfe/00090.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/a402dc0dfe/00095.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/a402dc0dfe/00090.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/a402dc0dfe/00100.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/a402dc0dfe/00090.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/a402dc0dfe/00105.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/a402dc0dfe/00090.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/a402dc0dfe/00110.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/a402dc0dfe/00090.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/a402dc0dfe/00115.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/a402dc0dfe/00090.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/a402dc0dfe/00120.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/a402dc0dfe/00090.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/a402dc0dfe/00125.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/a402dc0dfe/00090.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/a402dc0dfe/00130.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/a402dc0dfe/00090.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/a402dc0dfe/00135.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/a402dc0dfe/00090.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/a402dc0dfe/00140.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/a402dc0dfe/00090.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/a402dc0dfe/00145.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/a800d85e88/00050.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/a800d85e88/00055.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/a800d85e88/00050.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/a800d85e88/00060.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/a800d85e88/00050.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/a800d85e88/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/a800d85e88/00050.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/a800d85e88/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/a800d85e88/00050.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/a800d85e88/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/a9c9c1517e/00055.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/a9c9c1517e/00060.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/a9c9c1517e/00055.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/a9c9c1517e/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/a9c9c1517e/00055.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/a9c9c1517e/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/a9c9c1517e/00055.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/a9c9c1517e/00075.png
# ['00175.png', '00180.png', '00185.png', '00190.png', '00195.png', '00200.png', '00205.png', '00210.png', '00215.png', '00220.png', '00225.png', '00230.png', '00235.png', '00240.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/ad54468654/00240.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/ad54468654/00245.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/ad54468654/00240.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/ad54468654/00250.png
# ['00150.png', '00155.png', '00160.png', '00165.png', '00170.png', '00175.png', '00180.png', '00185.png', '00190.png', '00195.png', '00200.png', '00205.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/ae2cecf5f6/00205.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/ae2cecf5f6/00210.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/ae2cecf5f6/00205.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/ae2cecf5f6/00215.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/ae2cecf5f6/00205.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/ae2cecf5f6/00220.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/ae2cecf5f6/00205.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/ae2cecf5f6/00225.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/ae9cd16dbf/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/ae9cd16dbf/00050.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/ae9cd16dbf/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/ae9cd16dbf/00055.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/ae9cd16dbf/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/ae9cd16dbf/00060.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/ae9cd16dbf/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/ae9cd16dbf/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/ae9cd16dbf/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/ae9cd16dbf/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/ae9cd16dbf/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/ae9cd16dbf/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png', '00070.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b27b28d581/00070.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b27b28d581/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b379ab4ff5/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b379ab4ff5/00050.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b379ab4ff5/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b379ab4ff5/00055.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b379ab4ff5/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b379ab4ff5/00060.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b379ab4ff5/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b379ab4ff5/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b379ab4ff5/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b379ab4ff5/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b379ab4ff5/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b379ab4ff5/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b4805ae9cd/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b4805ae9cd/00050.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b4805ae9cd/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b4805ae9cd/00055.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b4805ae9cd/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b4805ae9cd/00060.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b4805ae9cd/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b4805ae9cd/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b4805ae9cd/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b4805ae9cd/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b4805ae9cd/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b4805ae9cd/00075.png
# ['00065.png', '00070.png', '00075.png', '00080.png', '00085.png', '00090.png', '00095.png', '00105.png', '00110.png', '00115.png', '00120.png', '00125.png', '00130.png', '00135.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b5a09a83f3/00135.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b5a09a83f3/00140.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b5a09a83f3/00135.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b5a09a83f3/00145.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b70a2c0ab1/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b70a2c0ab1/00050.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b70a2c0ab1/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b70a2c0ab1/00055.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b70a2c0ab1/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b70a2c0ab1/00060.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b70a2c0ab1/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b70a2c0ab1/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b70a2c0ab1/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b70a2c0ab1/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b70a2c0ab1/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b70a2c0ab1/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b7f31b7c36/00060.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b7f31b7c36/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b7f31b7c36/00060.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b7f31b7c36/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b7f31b7c36/00060.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b7f31b7c36/00075.png
# ['00105.png', '00110.png', '00115.png', '00120.png', '00125.png', '00130.png', '00135.png', '00140.png', '00145.png', '00150.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b7f675fb98/00150.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b7f675fb98/00155.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b7f675fb98/00150.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b7f675fb98/00160.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b7f675fb98/00150.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b7f675fb98/00165.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b7f675fb98/00150.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b7f675fb98/00170.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b7f675fb98/00150.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b7f675fb98/00175.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b7f675fb98/00150.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b7f675fb98/00180.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b7fb871660/00050.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b7fb871660/00055.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b7fb871660/00050.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b7fb871660/00060.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b7fb871660/00050.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b7fb871660/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b7fb871660/00050.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b7fb871660/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b7fb871660/00050.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b7fb871660/00075.png
# ['00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png', '00070.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b871db031a/00070.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b871db031a/00075.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b871db031a/00070.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b871db031a/00080.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b8c3210036/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b8c3210036/00050.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b8c3210036/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b8c3210036/00055.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b8c3210036/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b8c3210036/00060.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b8c3210036/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b8c3210036/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b8c3210036/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b8c3210036/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b8c3210036/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b8c3210036/00075.png
# ['00220.png', '00225.png', '00230.png', '00235.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b938d79dff/00235.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b938d79dff/00240.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b938d79dff/00235.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b938d79dff/00245.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b938d79dff/00235.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b938d79dff/00250.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b938d79dff/00235.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b938d79dff/00255.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b938d79dff/00235.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b938d79dff/00260.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b938d79dff/00235.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b938d79dff/00265.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b938d79dff/00235.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b938d79dff/00270.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b938d79dff/00235.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b938d79dff/00275.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b938d79dff/00235.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b938d79dff/00280.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b938d79dff/00235.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b938d79dff/00285.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b938d79dff/00235.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b938d79dff/00290.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b938d79dff/00235.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b938d79dff/00295.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png', '00070.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b941aef1a0/00070.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/b941aef1a0/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/bd321d2be6/00060.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/bd321d2be6/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/bd321d2be6/00060.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/bd321d2be6/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/bd321d2be6/00060.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/bd321d2be6/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/bd5b2e2848/00040.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/bd5b2e2848/00045.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/bd5b2e2848/00040.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/bd5b2e2848/00050.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/bd5b2e2848/00040.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/bd5b2e2848/00055.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/bd5b2e2848/00040.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/bd5b2e2848/00060.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/bd5b2e2848/00040.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/bd5b2e2848/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/bd5b2e2848/00040.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/bd5b2e2848/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/bd5b2e2848/00040.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/bd5b2e2848/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/be3e3cffbd/00050.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/be3e3cffbd/00055.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/be3e3cffbd/00050.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/be3e3cffbd/00060.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/be3e3cffbd/00050.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/be3e3cffbd/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/be3e3cffbd/00050.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/be3e3cffbd/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/be3e3cffbd/00050.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/be3e3cffbd/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/c52bce43db/00065.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/c52bce43db/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/c52bce43db/00065.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/c52bce43db/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/c6a12c131f/00050.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/c6a12c131f/00055.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/c6a12c131f/00050.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/c6a12c131f/00060.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/c6a12c131f/00050.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/c6a12c131f/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/c6a12c131f/00050.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/c6a12c131f/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/c6a12c131f/00050.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/c6a12c131f/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png', '00070.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/ca91c69e3b/00070.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/ca91c69e3b/00075.png
# ['00050.png', '00055.png', '00060.png', '00065.png', '00070.png', '00075.png', '00080.png', '00085.png', '00090.png', '00095.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/ca91e99105/00095.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/ca91e99105/00100.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/ca91e99105/00095.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/ca91e99105/00105.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/ca91e99105/00095.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/ca91e99105/00110.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/ca91e99105/00095.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/ca91e99105/00115.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/ca91e99105/00095.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/ca91e99105/00120.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/ca91e99105/00095.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/ca91e99105/00125.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/cff8191891/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/cff8191891/00050.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/cff8191891/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/cff8191891/00055.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/cff8191891/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/cff8191891/00060.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/cff8191891/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/cff8191891/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/cff8191891/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/cff8191891/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/cff8191891/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/cff8191891/00075.png
# ['00065.png', '00070.png', '00075.png', '00080.png', '00085.png', '00090.png', '00095.png', '00100.png', '00105.png', '00110.png', '00115.png', '00120.png', '00125.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/d107a1457c/00125.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/d107a1457c/00130.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/d107a1457c/00125.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/d107a1457c/00135.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/d107a1457c/00125.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/d107a1457c/00140.png
# ['00210.png', '00215.png', '00220.png', '00225.png', '00230.png', '00235.png', '00240.png', '00245.png', '00250.png', '00255.png', '00260.png', '00265.png', '00270.png', '00275.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/d123d674c1/00275.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/d123d674c1/00280.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/d123d674c1/00275.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/d123d674c1/00285.png
# ['00000.png', '00005.png', '00010.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/d2484bff33/00065.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/d2484bff33/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/d2484bff33/00065.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/d2484bff33/00075.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/d2484bff33/00065.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/d2484bff33/00080.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/d292a50c7f/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/d292a50c7f/00050.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/d292a50c7f/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/d292a50c7f/00055.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/d292a50c7f/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/d292a50c7f/00060.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/d292a50c7f/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/d292a50c7f/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/d292a50c7f/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/d292a50c7f/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/d292a50c7f/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/d292a50c7f/00075.png
# ['00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/d3f5c309cc/00065.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/d3f5c309cc/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/d3f5c309cc/00065.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/d3f5c309cc/00075.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/d3f5c309cc/00065.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/d3f5c309cc/00080.png
# ['00030.png', '00035.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png', '00070.png', '00075.png', '00080.png', '00085.png', '00090.png', '00095.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/d44e6acd1d/00095.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/d44e6acd1d/00100.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/d44e6acd1d/00095.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/d44e6acd1d/00105.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/d44e6acd1d/00095.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/d44e6acd1d/00110.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/d7157a9f44/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/d7157a9f44/00050.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/d7157a9f44/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/d7157a9f44/00055.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/d7157a9f44/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/d7157a9f44/00060.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/d7157a9f44/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/d7157a9f44/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/d7157a9f44/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/d7157a9f44/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/d7157a9f44/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/d7157a9f44/00075.png
# ['00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png', '00070.png', '00075.png', '00080.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/d9010348a1/00080.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/d9010348a1/00085.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/d9010348a1/00080.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/d9010348a1/00090.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/df0638b0a0/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/df0638b0a0/00050.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/df0638b0a0/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/df0638b0a0/00055.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/df0638b0a0/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/df0638b0a0/00060.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/df0638b0a0/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/df0638b0a0/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/df0638b0a0/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/df0638b0a0/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/df0638b0a0/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/df0638b0a0/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/df5e2152b3/00065.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/df5e2152b3/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/df5e2152b3/00065.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/df5e2152b3/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e0bdb5dfae/00035.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e0bdb5dfae/00040.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e0bdb5dfae/00035.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e0bdb5dfae/00045.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e0bdb5dfae/00035.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e0bdb5dfae/00050.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e0bdb5dfae/00035.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e0bdb5dfae/00055.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e0bdb5dfae/00035.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e0bdb5dfae/00060.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e0bdb5dfae/00035.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e0bdb5dfae/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e0bdb5dfae/00035.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e0bdb5dfae/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e0bdb5dfae/00035.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e0bdb5dfae/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png', '00070.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e1194c2e9d/00070.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e1194c2e9d/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e16945b951/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e16945b951/00050.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e16945b951/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e16945b951/00055.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e16945b951/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e16945b951/00060.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e16945b951/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e16945b951/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e16945b951/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e16945b951/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e16945b951/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e16945b951/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png', '00070.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e33c18412a/00070.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e33c18412a/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e3bf38265f/00050.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e3bf38265f/00055.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e3bf38265f/00050.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e3bf38265f/00060.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e3bf38265f/00050.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e3bf38265f/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e3bf38265f/00050.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e3bf38265f/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e3bf38265f/00050.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e3bf38265f/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e3d60e82d5/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e3d60e82d5/00050.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e3d60e82d5/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e3d60e82d5/00055.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e3d60e82d5/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e3d60e82d5/00060.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e3d60e82d5/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e3d60e82d5/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e3d60e82d5/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e3d60e82d5/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e3d60e82d5/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e3d60e82d5/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png', '00070.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e415093d27/00070.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e415093d27/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e495f32c60/00040.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e495f32c60/00045.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e495f32c60/00040.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e495f32c60/00050.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e495f32c60/00040.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e495f32c60/00055.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e495f32c60/00040.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e495f32c60/00060.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e495f32c60/00040.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e495f32c60/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e495f32c60/00040.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e495f32c60/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e495f32c60/00040.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e495f32c60/00075.png
# ['00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e4e2983570/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e4e2983570/00050.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e4e2983570/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e4e2983570/00055.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e4e2983570/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e4e2983570/00060.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e4e2983570/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e4e2983570/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e4e2983570/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e4e2983570/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e4e2983570/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e4e2983570/00075.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e4e2983570/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e4e2983570/00080.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png', '00070.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e4ffb6d0dd/00070.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e4ffb6d0dd/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e5ce96a55d/00060.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e5ce96a55d/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e5ce96a55d/00060.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e5ce96a55d/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e5ce96a55d/00060.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e5ce96a55d/00075.png
# ['00150.png', '00155.png', '00160.png', '00165.png', '00170.png', '00175.png', '00180.png', '00185.png', '00190.png', '00195.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e6be243065/00195.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e6be243065/00200.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e6be243065/00195.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e6be243065/00205.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e6be243065/00195.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e6be243065/00210.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e6be243065/00195.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e6be243065/00215.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e6be243065/00195.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e6be243065/00220.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e6be243065/00195.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e6be243065/00225.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png', '00070.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e75a466eea/00070.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e75a466eea/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e78922e5e6/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e78922e5e6/00050.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e78922e5e6/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e78922e5e6/00055.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e78922e5e6/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e78922e5e6/00060.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e78922e5e6/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e78922e5e6/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e78922e5e6/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e78922e5e6/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e78922e5e6/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e78922e5e6/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png', '00070.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e8f7904326/00070.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e8f7904326/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e92b6bfea4/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e92b6bfea4/00050.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e92b6bfea4/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e92b6bfea4/00055.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e92b6bfea4/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e92b6bfea4/00060.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e92b6bfea4/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e92b6bfea4/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e92b6bfea4/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e92b6bfea4/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e92b6bfea4/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e92b6bfea4/00075.png
# ['00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png', '00070.png', '00075.png', '00080.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e9422ad240/00080.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e9422ad240/00085.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e9422ad240/00080.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e9422ad240/00090.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e9422ad240/00080.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e9422ad240/00095.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e9422ad240/00080.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e9422ad240/00100.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e9422ad240/00080.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e9422ad240/00105.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e9422ad240/00080.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e9422ad240/00110.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e99706b555/00040.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e99706b555/00045.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e99706b555/00040.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e99706b555/00050.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e99706b555/00040.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e99706b555/00055.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e99706b555/00040.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e99706b555/00060.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e99706b555/00040.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e99706b555/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e99706b555/00040.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e99706b555/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e99706b555/00040.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/e99706b555/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png', '00070.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/ea444a37eb/00070.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/ea444a37eb/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/ef0a8e8f35/00055.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/ef0a8e8f35/00060.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/ef0a8e8f35/00055.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/ef0a8e8f35/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/ef0a8e8f35/00055.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/ef0a8e8f35/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/ef0a8e8f35/00055.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/ef0a8e8f35/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/f04cf99ee6/00060.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/f04cf99ee6/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/f04cf99ee6/00060.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/f04cf99ee6/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/f04cf99ee6/00060.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/f04cf99ee6/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png', '00070.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/f0ad38da27/00070.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/f0ad38da27/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/f1d99239eb/00065.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/f1d99239eb/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/f1d99239eb/00065.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/f1d99239eb/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/f305a56d9f/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/f305a56d9f/00050.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/f305a56d9f/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/f305a56d9f/00055.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/f305a56d9f/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/f305a56d9f/00060.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/f305a56d9f/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/f305a56d9f/00065.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/f305a56d9f/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/f305a56d9f/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/f305a56d9f/00045.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/f305a56d9f/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png', '00070.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/fb4cbc514b/00070.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/fb4cbc514b/00075.png
# ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png', '00065.png']
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/fe6c244f63/00065.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/fe6c244f63/00070.png
# file copy /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/fe6c244f63/00065.png /data1/guoxi/YouTube-VOS/pretreatment_data/train/Annotations/fe6c244f63/00075.png
#
# Process finished with exit code 0