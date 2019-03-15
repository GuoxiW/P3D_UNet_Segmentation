import os
from PIL import Image
import numpy as np
import shutil

mask_fol_rp = '/disk2/guoxi/YouTube-VOS/train/Annotations/'
image_fol_rp = '/disk2/guoxi/YouTube-VOS/train/JPEGImages/'
fol_set = os.listdir(mask_fol_rp)  # 读取所有的mask,即所有的文件夹名称 mask文件夹 0000001521243214
fol_set.sort()

for fol_name in fol_set:   # 每个文件夹下
    mask_rp = mask_fol_rp + fol_name + '/'  # 获得文件夹路径
    image_rp = image_fol_rp + fol_name + '/'
    mask_set = os.listdir(mask_rp)   #
    mask_set.sort()   # 每个文件夹下所有mask
    mask_num = []

    for mask_name in mask_set:  # 所有mask
        if mask_name[-4:] != '.png':
            continue
        mask = Image.open(mask_rp + mask_name)
        mask_np = np.asarray(mask, dtype=np.uint8)
        obj_ind = list(np.unique(mask_np))  # mask为彩色数据，读取出每个物体的id 0为背景，1 2 3 分别为要分割的物体
        obj_ind = max(obj_ind)
        if not len(mask_num):
            mask_num.append(obj_ind)
        if obj_ind > max(mask_num):
            mask_num.append(obj_ind)
            # if mask_name != '00000.png':
            print(mask_rp + mask_name + ' ' + str(obj_ind))
        # print(mask_num)
    # if len(mask_num) > 1:
    #     print(mask_rp)
    #     shutil.rmtree(mask_rp)
    #     shutil.rmtree(image_rp)

# 没有背景
#         if min(obj_ind) > 0:
#             print(mask_rp + mask_name)
# /disk2/guoxi/YouTube-VOS/train/Annotations/0248626d9a/00000.png
# /disk2/guoxi/YouTube-VOS/train/Annotations/4db117e6c5/00000.png
# /disk2/guoxi/YouTube-VOS/train/Annotations/534a560609/00000.png
# /disk2/guoxi/YouTube-VOS/train/Annotations/534a560609/00005.png
# /disk2/guoxi/YouTube-VOS/train/Annotations/534a560609/00010.png
# /disk2/guoxi/YouTube-VOS/train/Annotations/534a560609/00015.png
# /disk2/guoxi/YouTube-VOS/train/Annotations/534a560609/00070.png
# /disk2/guoxi/YouTube-VOS/train/Annotations/534a560609/00075.png
# /disk2/guoxi/YouTube-VOS/train/Annotations/97e59f09fa/00050.png

# 帧突变
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/0043f083b5/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/00917dcfc4/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/011ac0a06f/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/01baa5a4e1/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/01c4cb5ffe/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/01e64dd36a/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/02d28375aa/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/031ccc99b1/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/0358b938c1/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/0368107cf1/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/0379ddf557/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/038b2cc71d/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/04fe256562/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/05a0a513df/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/05a569d8aa/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/05ffcfed85/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/0630391881/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/07129e14a4/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/07177017e9/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/07353b2a89/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/075926c651/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/076f206928/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/07c62c3d11/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/082900c5d4/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/0860df21e2/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/08d50b926c/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/08e1e4de15/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/093c335ccc/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/09ff54fef4/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/0c3a04798c/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/0c44a9d545/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/0ce06e0121/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/0d97fba242/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/0d9cc80d7e/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/0dab85b6d3/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/0e05f0e232/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/0ea68d418b/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/106242403f/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/10eced835e/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/1122c1d16a/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/114e7676ec/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/1178932d2f/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/11a0c3b724/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/11c722a456/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/11ce6f452e/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/120cb9514d/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/122896672d/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/12bddb2bcb/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/1336440745/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/14f9bd22b5/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/15097d5d4e/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/1514e3563f/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/15617297cc/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/15abbe0c52/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/15f67b0fab/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/165c3c8cd4/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/165c42b41b/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/165ec9e22b/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/185bf64702/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/1903f9ea15/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/1917b209f2/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/19367bb94e/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/193ffaa217/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/198afe39ae/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/19a6e62b9b/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/19c00c11f9/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/19ee80dac6/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/1a6c0fbd1e/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/1a8afbad92/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/1aa3da3ee3/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/1af8d2395d/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/1c9f9eb792/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/1cd10e62be/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/1d746352a6/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/1da4e956b1/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/1de4a9e537/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/1e1a18c45a/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/1f1beb8daa/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/1f64955634/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/1f7d31b5b2/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/1f8014b7fd/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/1f9c7d10f1/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/203594a418/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2039c3aecb/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/211bc5d102/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/217bae91e5/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/222597030f/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/223a0e0657/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/223bd973ab/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/22472f7395/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/224e7c833e/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2263a8782b/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/22a1141970/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2376440551/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/238b84e67f/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/238d4b86f6/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/23b0c8a9ab/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/23f404a9fc/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2431dec2fd/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2457274dbc/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/246b142c4d/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/24866b4e6a/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/24ab0b83e8/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/250116161c/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/256dcc8ab8/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2680861931/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/26de3d18ca/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/270ed80c12/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/27303333e1/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/27659fa7d6/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/281629cb41/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/288c117201/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/28a8eb9623/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/28f4a45190/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/29d779f9e3/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/29dde5f12b/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2a6a30a4ea/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2a6d9099d1/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2b6c30bbbd/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2c3ea7ee7d/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2c41fa0648/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2c5537eddf/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2c6e63b7de/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2cb10c6a7e/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2cc5d9c5f6/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2d8f5e5025/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2dcc417f82/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2df005b843/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2df356de14/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2e03b8127a/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2e0f886168/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2ea78f46e4/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2f53822e88/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2f5b0c89b1/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/2f96f5fc6f/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/3064ad91e8/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/30c35c64a4/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/328d918c7d/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/33098cedb4/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/334cb835ac/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/34fbee00a6/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/3543d8334c/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/357a710863/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/35c6235b8d/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/35d01a438a/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/362c5bc56e/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/369dde050a/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/374b479880/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/37c19d1087/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/37ddce7f8b/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/37fa0001e8/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/38eb2bf67f/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/390352cced/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/390c51b987/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/3a079fb484/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/3aa3f1c9e8/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/3aa7fce8b6/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/3aa876887d/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/3ab9b1a85a/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/3b3b0af2ee/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/3b6c7988f6/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/3b6e983b5b/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/3bd9a9b515/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/3beef45388/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/3c019c0a24/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/3c47ab95f8/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/3c5ff93faf/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/3d8997aeb6/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/3e04a6be11/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/3e108fb65a/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/3e38336da5/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/3f0b0dfddd/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/3f4f3bc803/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/3fea675fab/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/401888b36c/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/4083cfbe15/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/40f4026bf5/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/4100b57a3a/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/4122aba5f9/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/418bb97e10/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/43326d9940/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/43a6c21f37/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/4416bdd6ac/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/44b1da0d87/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/44b4dad8c9/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/4536c882e5/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/457e717a14/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/45bf0e947d/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/45f8128b97/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/4607f6c03c/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/466ba4ae0c/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/4680236c9d/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/4743bb84a7/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/479f5d7ef6/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/4804ee2767/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/4810c3fbca/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/49c879f82d/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/49e7326789/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/4a341402d0/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/4a6e3faaa1/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/4b3154c159/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/4b54d2587f/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/4b556740ff/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/4baa1ed4aa/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/4bf5763d24/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/4cef87b649/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/4cf208e9b3/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/4daa179861/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/4db117e6c5/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/4de4ce4dea/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/4e4e06a749/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/4e70279712/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/4e72856cc7/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/4e82b1df57/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/4ec9da329e/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/4f601d255a/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/4f827b0751/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/4facd8f0e8/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/500c835a86/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/50c6f4fe3e/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/5110dc72c0/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/5158d6e985/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/51eef778af/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/51f384721c/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/521cfadcb4/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/52c7a3d653/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/52d225ed52/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/53253f2362/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/5352c4a70e/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/5380eaabff/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/53af427bb2/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/540850e1c7/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/556c79bbf2/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/559824b6f6/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/571ca79c71/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/578f211b86/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/5790ac295d/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/57bfb7fa4c/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/57c010175e/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/57d5289a01/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/58045fde85/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/585dd0f208/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/589f65f5d5/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/59323787d5/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/59bf0a149f/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/5a50640995/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/5ab49d9de0/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/5b27d19f0b/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/5b48ae16c5/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/5baaebdf00/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/5bc77844da/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/5bddc3ba25/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/5c6ea7dac3/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/5d1e24b6e3/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/5e08de0ed7/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/5e1ce354fd/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/5e418b25f9/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/5e4ee19663/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/5e8d59dc31/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/5ee23ca60e/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/5f32cf521e/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/5fb8aded6a/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/5fba90767d/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/600be7f53e/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/6057307f6e/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/606c86c455/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/60e51ff1ae/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/61b481a78b/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/61da008958/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/625892cf0b/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/62d6ece152/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/62ede7b2da/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/6363c87314/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/63d90c2bae/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/6454f548fd/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/64a43876b7/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/65ab7e1d98/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/65dcf115ab/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/668364b372/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/6693a52081/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/669b572898/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/675ed3e1ca/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/6846ac20df/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/68a2fad4ab/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/68ea4a8c3d/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/68fa8300b4/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/692eb57b63/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/69c67f109f/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/69ea9c09d1/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/6ade215eb0/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/6afd692f1a/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/6b1e04d00d/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/6b685eb75b/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/6b928b7ba6/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/6bdab62bcd/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/6bf2e853b1/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/6c23d89189/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/6c54265f16/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/6d4bf200ad/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/6dd36705b9/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/6df3637557/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/6e618d26b6/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/6eb30b3b5a/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/6ecad29e52/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/6f4789045c/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/6f67d7c4c4/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/6f96e91d81/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/6fce7f3226/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/7136a4453f/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/7143fb084f/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/714d902095/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/71d67b9e19/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/720e3fa04c/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/72cadebbce/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/72e8d1c1ff/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/731b825695/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/732626383b/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/733824d431/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/73c6ae7711/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/747f1b1f2f/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/75504539c3/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/75595b453d/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/7584129dc3/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/75cee6caf0/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/75eaf5669d/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/764503c499/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/76693db153/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/767856368b/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/76a75f4eee/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/76b90809f7/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/77e7f38f4d/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/78254660ea/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/784398620a/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/78d3676361/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/78f1a1a54f/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/792218456c/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/79e9db913e/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/7a13a5dfaa/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/7a5f46198d/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/7a8b5456ca/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/7b0fd09c28/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/7b39fe7371/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/7c078f211b/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/7c78a2266d/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/7cc9258dee/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/7d1333fcbe/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/7e24023274/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/7eb2605d96/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/7f02b3cfe2/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/7f21063c3a/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/7f5faedf8b/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/7f838baf2b/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/7fa5f527e3/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/804382b1ad/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/80f16b016d/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/823e7a86e8/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/827171a845/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/832b5ef379/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/83a8151377/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/83daba503a/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/84752191a3/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/847eeeb2e0/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/854c48b02a/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8604bb2b75/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/86a40b655d/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/86d3755680/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8749369ba0/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8799ab0118/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/885673ea17/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8891aa6dfa/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/89363acf76/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8953138465/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/895cbf96f9/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/89d6336c2b/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8a5d6c619c/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8b99a77ac5/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8ba04b1e7b/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8bbeaad78b/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8bdb091ccf/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8d87897d66/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8dd3ab71b9/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8def5bd3bf/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8e3a83cf2d/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8e98ae3c84/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8ec3065ec2/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8ecf51a971/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8f1600f7f6/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/8f918598b6/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/90118a42ee/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/9076f4b6db/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/909dbd1b76/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/90d300f09b/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/9151cad9b5/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/91bb8df281/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/9268e1f88a/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/92a28cd233/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/92dabbe3a0/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/934bdc2893/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/939bdf742e/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/94209c86f0/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/950be91db1/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/9533fc037c/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/957f7bc48b/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/958073d2b0/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/96825c4714/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/96dfc49961/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/96e1a5b4f8/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/96fbe5fc23/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/9715cc83dc/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/97659ed431/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/97ba838008/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/97d9d008c7/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/98595f2bb4/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/98911292da/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/9893a3cf77/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/98a8b06e7f/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/98ba3c9417/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/999d53d841/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/99fcba71e5/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/9a2f2c0f86/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/9a3254a76e/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/9c29c047b0/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/9c3ce23bd1/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/9ce6f765c3/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/9d407c3aeb/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/9e249b4982/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/9eadcea74f/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/a023141022/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/a06722ba82/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/a09c39472e/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/a0b61c959e/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/a1aaf63216/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/a1bd8e5349/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/a1dfdd0cac/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/a20fd34693/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/a263ce8a87/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/a2a800ab63/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/a2c996e429/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/a2f2a55f01/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/a34f440f33/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/a3c502bec3/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/a402dc0dfe/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/a416b56b53/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/a5cd17bb11/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/a5ea2b93b6/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/a5ec5b0265/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/a5f472caf4/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/a68259572b/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/a6d8a4228d/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/a73d3c3902/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/a8999af004/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/a919392446/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/a965504e88/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/a973f239cd/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/a9804f2a08/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/a99738f24c/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/a9c9c1517e/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/aa1a338630/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/aa6d999971/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ab56201494/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/abb50c8697/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ac2cb1b9eb/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ac31fcd6d0/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ac783ef388/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/acbf581760/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/acf44293a2/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/acff336758/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ad3d1cfbcb/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ad573f7d31/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/adfdd52eac/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ae01cdab63/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ae1bcbd423/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ae93214fe6/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ae9cd16dbf/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/af0b54cee3/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/af8ad72057/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/afe1a35c1e/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b05ad0d345/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b0cca8b830/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b1f540a4bd/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b24fe36b2a/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b27b28d581/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b2b0baf470/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b2b2756fe7/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b2ce7699e3/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b2edc76bd2/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b30bf47bcd/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b379ab4ff5/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b4807569a5/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b4b715a15b/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b4e5ad97aa/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b5aae1fe25/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b678b7db00/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b69926d9fa/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b6b8d502d4/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b6bb00e366/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b6d79a0845/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b6ec609f7b/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b70a5a0d50/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b72ac6e10b/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b77e5eddef/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b7a2c2c83c/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b7f31b7c36/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b86e50d82d/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/b8c3210036/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/bac9db04f5/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/bb04e28695/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/bb1c770fe7/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/bb2d220506/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/bb334e5cdb/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/bb337f9830/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/bbb4302dda/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/bbd31510cf/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/bc3b9ee033/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/bc4240b43c/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/bc6b8d6371/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/bcaad44ad7/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/be376082d0/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/be3e3cffbd/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/be8b72fe37/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/beb921a4c9/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/bf461df850/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/c10d07c90d/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/c1268d998c/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/c130c3fc0c/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/c1c830a735/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/c219d6f8dc/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/c27adaeac5/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/c307f33da2/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/c31fa6c598/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/c34d120a88/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/c3509e728d/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/c3e4274614/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/c3edc48cbd/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/c41e6587f5/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/c438858117/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/c4ff9b4885/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/c55784c766/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/c62188c536/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/c69689f177/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/c6d9526e0d/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/c7c2860db3/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/c7cef4aee2/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/c8b869a04a/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/c8d79e3163/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/c8edab0415/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/c8f6cba9fd/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/c922365dd4/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/c96379c03c/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/c96465ee65/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/c965afa713/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/c98b6fe013/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/c99e92aaf0/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/c9bf64e965/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ca1828fa54/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ca3787d3d3/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/caecf0a5db/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/cb35a87504/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/cb3f22b0cf/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/cc892997b8/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/cd603bb9d1/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ce1bc5743a/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ce7d1c8117/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ce7dbeaa88/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/cea7697b25/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/cef824a1e1/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/cf13f5c95a/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/cfda2dcce5/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d01608c2a5/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d04258ca14/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d0483573dc/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d0c65e9e95/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d123d674c1/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d1802f69f8/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d182c4483a/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d280fcd1cb/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d2857f0faa/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d2a58b4fa6/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d301ca58cc/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d3987b2930/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d454e8444f/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d53b955f78/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d5b6c6d94a/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d5cae12834/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d6476cad55/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d6917db4be/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d69f757a3f/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d6c02bfda5/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d6e12ef6cc/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d7135cf104/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d724134cfd/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d7b34e5d73/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d847e24abd/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d8596701b7/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d87069ba86/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d874654b52/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d8eb07c381/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/d9db6f1983/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/da7a816676/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/dac361e828/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/dc704dd647/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/dde8e67fb4/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/df01f277f1/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/df11931ffe/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/df2bc56d7c/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/df365282c6/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/df39a0d9df/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/df59cfd91d/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/df741313c9/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/df7626172f/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/dfc0d3d27a/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/dfdbf91a99/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e0b2ceee6f/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e0f7208874/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e19edcd34b/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e1f14510fa/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e22de45950/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e27bbedbfe/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e29e9868a8/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e33c18412a/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e39e3e0a06/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e3e4134877/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e3f4635e03/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e4428801bc/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e588433c1e/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e5d6b70a9f/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e6f065f2b9/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e76c55933f/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e78922e5e6/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e78d450a9c/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e88b6736e4/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e8962324e3/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e8cee8bf0b/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e8ed1a3ccf/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e90c10fc4c/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e92e1b7623/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e93f83e512/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e9422ad240/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e98eda8978/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e9d3c78bf3/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/e9ec1b7ea8/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ea065cc205/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ea16d3fd48/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ea3b94a591/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/eaab4d746c/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/eb383cb82e/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ebbb90e9f9/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ec28252938/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ecae59b782/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ed844e879f/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ed8f814b2b/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ed9ff4f649/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/edb8878849/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/edd663afa3/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ee316eaed6/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ee3f509537/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ee40a1e491/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ee4bf100f1/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ee947ed771/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ef232a2aed/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ef45ce3035/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ef6359cea3/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/efce0c1868/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/f0268aa627/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/f04cf99ee6/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/f08928c6d3/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/f0ad38da27/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/f3085d6570/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/f3325c3338/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/f36483c824/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/f3fc0ea80b/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/f46184f393/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/f46c364dca/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/f470b9aeb0/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/f48b535719/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/f4aa882cfd/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/f4daa3dbd5/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/f5966cadd2/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/f5bddf5598/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/f6474735be/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/f659251be2/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/f6f59d986f/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/f74c3888d7/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/f7961ac1f0/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/f7a71e7574/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/f7afbf4947/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/f7cf4b4a39/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/f7e0c9bb83/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/f8af30d4b6/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/f8c3fb2b01/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/f9750192a4/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/f9823a32c2/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/f99d535567/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/f9ae3d98b7/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/f9bd1fabf5/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/f9ea6b7f31/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/fad633fbe1/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/fb4cbc514b/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/fb4e6062f7/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/fbaca0c9df/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/fbc645f602/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/fbe8488798/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/fc6186f0bb/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/fc96cda9d8/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/fdb3d1fb1e/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/fe24b0677d/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/fe3c02699d/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/fed208bfca/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ff15a5eff6/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ff5a1ec4f3/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/ff773b1a1e/
# /disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/fffe5f8df6/

# /disk2/guoxi/YouTube-VOS/train/Annotations/0043f083b5/00010.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/0043f083b5/00040.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/00917dcfc4/00030.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/011ac0a06f/00130.png 5
# /disk2/guoxi/YouTube-VOS/train/Annotations/02d28375aa/00150.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/0358b938c1/00165.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/0358b938c1/00200.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/04fe256562/00065.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/05a0a513df/00020.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/05ffcfed85/00015.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/07129e14a4/00140.png 4
# /disk2/guoxi/YouTube-VOS/train/Annotations/07353b2a89/00015.png 4
# /disk2/guoxi/YouTube-VOS/train/Annotations/076f206928/00060.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/07c62c3d11/00045.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/0860df21e2/00045.png 1
# /disk2/guoxi/YouTube-VOS/train/Annotations/08d50b926c/00140.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/09ff54fef4/00010.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/0d9cc80d7e/00015.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/0e05f0e232/00095.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/106242403f/00015.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/1122c1d16a/00005.png 4
# /disk2/guoxi/YouTube-VOS/train/Annotations/1122c1d16a/00015.png 5
# /disk2/guoxi/YouTube-VOS/train/Annotations/11a0c3b724/00050.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/120cb9514d/00045.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/120cb9514d/00055.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/122896672d/00120.png 4
# /disk2/guoxi/YouTube-VOS/train/Annotations/1336440745/00065.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/15617297cc/00030.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/165c3c8cd4/00010.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/165c42b41b/00010.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/185bf64702/00035.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/1903f9ea15/00010.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/1903f9ea15/00015.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/19367bb94e/00025.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/193ffaa217/00020.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/19a6e62b9b/00110.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/1a6c0fbd1e/00005.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/1a8afbad92/00015.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/1a8afbad92/00055.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/1aa3da3ee3/00010.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/1aa3da3ee3/00025.png 4
# /disk2/guoxi/YouTube-VOS/train/Annotations/1af8d2395d/00055.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/1d746352a6/00015.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/1da4e956b1/00005.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/1de4a9e537/00030.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/1e1a18c45a/00075.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/1e1a18c45a/00140.png 4
# /disk2/guoxi/YouTube-VOS/train/Annotations/1f1beb8daa/00130.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/1f9c7d10f1/00100.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/203594a418/00030.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/223bd973ab/00005.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/22472f7395/00025.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/22a1141970/00205.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/2376440551/00135.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/238b84e67f/00020.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/238d4b86f6/00035.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/238d4b86f6/00045.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/2431dec2fd/00075.png 4
# /disk2/guoxi/YouTube-VOS/train/Annotations/256dcc8ab8/00130.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/2680861931/00040.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/270ed80c12/00020.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/270ed80c12/00050.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/270ed80c12/00070.png 4
# /disk2/guoxi/YouTube-VOS/train/Annotations/27303333e1/00100.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/281629cb41/00035.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/29d779f9e3/00225.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/29dde5f12b/00150.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/2c3ea7ee7d/00005.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/2c41fa0648/00010.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/2c5537eddf/00015.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/2cb10c6a7e/00025.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/2cc5d9c5f6/00070.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/2df005b843/00005.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/2df356de14/00005.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/2e03b8127a/00060.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/2ea78f46e4/00160.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/2f96f5fc6f/00025.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/3064ad91e8/00140.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/30c35c64a4/00125.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/34fbee00a6/00055.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/362c5bc56e/00040.png 4
# /disk2/guoxi/YouTube-VOS/train/Annotations/369dde050a/00020.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/374b479880/00090.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/37c19d1087/00025.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/37c19d1087/00040.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/37ddce7f8b/00050.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/37ddce7f8b/00130.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/38eb2bf67f/00050.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/390c51b987/00015.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/3a079fb484/00035.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/3aa3f1c9e8/00090.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/3ab9b1a85a/00005.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/3b3b0af2ee/00005.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/3b3b0af2ee/00020.png 4
# /disk2/guoxi/YouTube-VOS/train/Annotations/3b3b0af2ee/00065.png 5
# /disk2/guoxi/YouTube-VOS/train/Annotations/3b6e983b5b/00090.png 1
# /disk2/guoxi/YouTube-VOS/train/Annotations/3bd9a9b515/00115.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/3e04a6be11/00035.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/3e108fb65a/00035.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/3f0b0dfddd/00010.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/3f4f3bc803/00085.png 4
# /disk2/guoxi/YouTube-VOS/train/Annotations/3fea675fab/00050.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/4083cfbe15/00050.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/40f4026bf5/00005.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/40f4026bf5/00015.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/40f4026bf5/00110.png 4
# /disk2/guoxi/YouTube-VOS/train/Annotations/4122aba5f9/00040.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/4122aba5f9/00055.png 4
# /disk2/guoxi/YouTube-VOS/train/Annotations/4122aba5f9/00090.png 5
# /disk2/guoxi/YouTube-VOS/train/Annotations/43326d9940/00005.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/43a6c21f37/00105.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/44b1da0d87/00015.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/44b1da0d87/00080.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/466ba4ae0c/00070.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/466ba4ae0c/00140.png 4
# /disk2/guoxi/YouTube-VOS/train/Annotations/4804ee2767/00010.png 4
# /disk2/guoxi/YouTube-VOS/train/Annotations/4810c3fbca/00005.png 1
# /disk2/guoxi/YouTube-VOS/train/Annotations/49c879f82d/00085.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/49e7326789/00125.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/4b3154c159/00095.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/4b54d2587f/00005.png 1
# /disk2/guoxi/YouTube-VOS/train/Annotations/4b556740ff/00090.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/4baa1ed4aa/00005.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/4cef87b649/00085.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/4db117e6c5/00035.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/4db117e6c5/00045.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/4e70279712/00030.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/4e72856cc7/00020.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/4e82b1df57/00030.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/4f601d255a/00025.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/4f601d255a/00040.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/4f827b0751/00025.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/5158d6e985/00080.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/5158d6e985/00145.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/51eef778af/00005.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/51f384721c/00020.png 1
# /disk2/guoxi/YouTube-VOS/train/Annotations/52d225ed52/00085.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/53253f2362/00040.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/53af427bb2/00040.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/559824b6f6/00010.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/559824b6f6/00075.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/5790ac295d/00050.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/57c010175e/00040.png 4
# /disk2/guoxi/YouTube-VOS/train/Annotations/57d5289a01/00010.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/58045fde85/00020.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/589f65f5d5/00070.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/59323787d5/00070.png 10
# /disk2/guoxi/YouTube-VOS/train/Annotations/59bf0a149f/00010.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/59bf0a149f/00110.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/5a50640995/00050.png 1
# /disk2/guoxi/YouTube-VOS/train/Annotations/5a50640995/00055.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/5a50640995/00065.png 4
# /disk2/guoxi/YouTube-VOS/train/Annotations/5a50640995/00150.png 5
# /disk2/guoxi/YouTube-VOS/train/Annotations/5b48ae16c5/00005.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/5b48ae16c5/00035.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/5baaebdf00/00110.png 4
# /disk2/guoxi/YouTube-VOS/train/Annotations/5c6ea7dac3/00040.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/5e1ce354fd/00060.png 6
# /disk2/guoxi/YouTube-VOS/train/Annotations/5e8d59dc31/00015.png 1
# /disk2/guoxi/YouTube-VOS/train/Annotations/5ee23ca60e/00020.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/5f32cf521e/00055.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/5fba90767d/00140.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/60e51ff1ae/00025.png 1
# /disk2/guoxi/YouTube-VOS/train/Annotations/62ede7b2da/00070.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/64a43876b7/00095.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/65ab7e1d98/00040.png 5
# /disk2/guoxi/YouTube-VOS/train/Annotations/669b572898/00125.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/68a2fad4ab/00005.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/692eb57b63/00045.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/6afd692f1a/00110.png 4
# /disk2/guoxi/YouTube-VOS/train/Annotations/6c54265f16/00015.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/6dd36705b9/00005.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/6df3637557/00025.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/6eb30b3b5a/00020.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/6eb30b3b5a/00035.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/6fce7f3226/00020.png 1
# /disk2/guoxi/YouTube-VOS/train/Annotations/6fce7f3226/00025.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/7143fb084f/00020.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/714d902095/00005.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/71d67b9e19/00105.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/71d67b9e19/00110.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/720e3fa04c/00040.png 1
# /disk2/guoxi/YouTube-VOS/train/Annotations/72cadebbce/00050.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/731b825695/00075.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/733824d431/00085.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/73c6ae7711/00015.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/75504539c3/00045.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/75504539c3/00050.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/7584129dc3/00015.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/7584129dc3/00085.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/7584129dc3/00135.png 4
# /disk2/guoxi/YouTube-VOS/train/Annotations/764503c499/00010.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/76693db153/00055.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/767856368b/00020.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/767856368b/00025.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/76b90809f7/00010.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/76b90809f7/00055.png 4
# /disk2/guoxi/YouTube-VOS/train/Annotations/77e7f38f4d/00085.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/78254660ea/00050.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/784398620a/00010.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/792218456c/00065.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/79e9db913e/00055.png 5
# /disk2/guoxi/YouTube-VOS/train/Annotations/7a13a5dfaa/00090.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/7b0fd09c28/00155.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/7c078f211b/00115.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/7cc9258dee/00050.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/7d1333fcbe/00030.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/7f21063c3a/00015.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/7f5faedf8b/00040.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/7f838baf2b/00035.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/7f838baf2b/00045.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/804382b1ad/00060.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/823e7a86e8/00015.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/8604bb2b75/00230.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/8749369ba0/00065.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/885673ea17/00065.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/885673ea17/00090.png 4
# /disk2/guoxi/YouTube-VOS/train/Annotations/885673ea17/00095.png 5
# /disk2/guoxi/YouTube-VOS/train/Annotations/8891aa6dfa/00065.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/8891aa6dfa/00070.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/89363acf76/00010.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/89363acf76/00025.png 4
# /disk2/guoxi/YouTube-VOS/train/Annotations/8953138465/00120.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/8b99a77ac5/00010.png 4
# /disk2/guoxi/YouTube-VOS/train/Annotations/8ba04b1e7b/00070.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/8dd3ab71b9/00020.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/8dd3ab71b9/00045.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/8e3a83cf2d/00030.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/8ec3065ec2/00155.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/8f1600f7f6/00005.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/9076f4b6db/00155.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/909dbd1b76/00050.png 12
# /disk2/guoxi/YouTube-VOS/train/Annotations/90d300f09b/00020.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/9151cad9b5/00050.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/91bb8df281/00095.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/9268e1f88a/00010.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/92a28cd233/00005.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/92dabbe3a0/00270.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/939bdf742e/00100.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/94209c86f0/00045.png 4
# /disk2/guoxi/YouTube-VOS/train/Annotations/957f7bc48b/00065.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/958073d2b0/00030.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/96e1a5b4f8/00015.png 1
# /disk2/guoxi/YouTube-VOS/train/Annotations/96fbe5fc23/00020.png 1
# /disk2/guoxi/YouTube-VOS/train/Annotations/96fbe5fc23/00025.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/98595f2bb4/00065.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/98911292da/00015.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/9893a3cf77/00025.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/9a3254a76e/00035.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/9d407c3aeb/00065.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/9eadcea74f/00095.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/a1aaf63216/00030.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/a263ce8a87/00035.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/a2a800ab63/00140.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/a2c996e429/00230.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/a2f2a55f01/00085.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/a5ea2b93b6/00005.png 1
# /disk2/guoxi/YouTube-VOS/train/Annotations/a5ea2b93b6/00020.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/a5ec5b0265/00080.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/a5f472caf4/00195.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/a6d8a4228d/00055.png 4
# /disk2/guoxi/YouTube-VOS/train/Annotations/a73d3c3902/00010.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/a73d3c3902/00035.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/a919392446/00085.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/a973f239cd/00055.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/a9804f2a08/00005.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/a9c9c1517e/00015.png 4
# /disk2/guoxi/YouTube-VOS/train/Annotations/a9c9c1517e/00025.png 5
# /disk2/guoxi/YouTube-VOS/train/Annotations/aa1a338630/00055.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/ab56201494/00120.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/acbf581760/00165.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/acf44293a2/00035.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/acf44293a2/00090.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/acff336758/00125.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/adfdd52eac/00045.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/ae01cdab63/00040.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/ae1bcbd423/00080.png 4
# /disk2/guoxi/YouTube-VOS/train/Annotations/ae9cd16dbf/00005.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/af8ad72057/00140.png 4
# /disk2/guoxi/YouTube-VOS/train/Annotations/afe1a35c1e/00065.png 11
# /disk2/guoxi/YouTube-VOS/train/Annotations/b0cca8b830/00015.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/b1f540a4bd/00020.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/b27b28d581/00040.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/b2edc76bd2/00035.png 5
# /disk2/guoxi/YouTube-VOS/train/Annotations/b2edc76bd2/00095.png 10
# /disk2/guoxi/YouTube-VOS/train/Annotations/b4e5ad97aa/00005.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/b5aae1fe25/00045.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/b678b7db00/00105.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/b678b7db00/00120.png 4
# /disk2/guoxi/YouTube-VOS/train/Annotations/b69926d9fa/00035.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/b6b8d502d4/00065.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/b6bb00e366/00145.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/b6d79a0845/00005.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/b6ec609f7b/00015.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/b77e5eddef/00030.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/b7f31b7c36/00040.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/b86e50d82d/00145.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/b8c3210036/00005.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/bb04e28695/00020.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/bb1c770fe7/00035.png 5
# /disk2/guoxi/YouTube-VOS/train/Annotations/bb1c770fe7/00145.png 9
# /disk2/guoxi/YouTube-VOS/train/Annotations/bb334e5cdb/00045.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/bb337f9830/00015.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/bc3b9ee033/00055.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/bc6b8d6371/00035.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/bcaad44ad7/00055.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/beb921a4c9/00095.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/bf461df850/00015.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/c130c3fc0c/00085.png 1
# /disk2/guoxi/YouTube-VOS/train/Annotations/c219d6f8dc/00020.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/c27adaeac5/00010.png 1
# /disk2/guoxi/YouTube-VOS/train/Annotations/c27adaeac5/00015.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/c307f33da2/00255.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/c3e4274614/00030.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/c438858117/00080.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/c4ff9b4885/00035.png 5
# /disk2/guoxi/YouTube-VOS/train/Annotations/c4ff9b4885/00055.png 6
# /disk2/guoxi/YouTube-VOS/train/Annotations/c55784c766/00040.png 5
# /disk2/guoxi/YouTube-VOS/train/Annotations/c55784c766/00045.png 6
# /disk2/guoxi/YouTube-VOS/train/Annotations/c6d9526e0d/00045.png 5
# /disk2/guoxi/YouTube-VOS/train/Annotations/c6d9526e0d/00065.png 6
# /disk2/guoxi/YouTube-VOS/train/Annotations/c7c2860db3/00035.png 4
# /disk2/guoxi/YouTube-VOS/train/Annotations/c8b869a04a/00015.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/c8d79e3163/00100.png 5
# /disk2/guoxi/YouTube-VOS/train/Annotations/c8edab0415/00020.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/c8edab0415/00065.png 5
# /disk2/guoxi/YouTube-VOS/train/Annotations/c922365dd4/00040.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/c96465ee65/00040.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/c965afa713/00040.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/ca1828fa54/00060.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/cb35a87504/00070.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/ce7d1c8117/00005.png 1
# /disk2/guoxi/YouTube-VOS/train/Annotations/cef824a1e1/00040.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/d0c65e9e95/00005.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/d123d674c1/00240.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/d1802f69f8/00105.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/d2a58b4fa6/00010.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/d301ca58cc/00025.png 4
# /disk2/guoxi/YouTube-VOS/train/Annotations/d454e8444f/00020.png 4
# /disk2/guoxi/YouTube-VOS/train/Annotations/d53b955f78/00025.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/d5b6c6d94a/00105.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/d5cae12834/00005.png 1
# /disk2/guoxi/YouTube-VOS/train/Annotations/d6476cad55/00020.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/d6917db4be/00005.png 1
# /disk2/guoxi/YouTube-VOS/train/Annotations/d6c02bfda5/00050.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/d7135cf104/00095.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/d7b34e5d73/00015.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/d7b34e5d73/00040.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/d847e24abd/00015.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/d8eb07c381/00060.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/da7a816676/00005.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/dac361e828/00105.png 4
# /disk2/guoxi/YouTube-VOS/train/Annotations/dde8e67fb4/00135.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/df2bc56d7c/00035.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/df365282c6/00115.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/df365282c6/00135.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/df39a0d9df/00015.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/df7626172f/00010.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/dfdbf91a99/00010.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/e0b2ceee6f/00005.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/e19edcd34b/00010.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/e1f14510fa/00005.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/e27bbedbfe/00020.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/e33c18412a/00045.png 4
# /disk2/guoxi/YouTube-VOS/train/Annotations/e39e3e0a06/00055.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/e39e3e0a06/00090.png 4
# /disk2/guoxi/YouTube-VOS/train/Annotations/e3e4134877/00125.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/e588433c1e/00015.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/e5d6b70a9f/00015.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/e5d6b70a9f/00040.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/e6f065f2b9/00005.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/e76c55933f/00050.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/e8cee8bf0b/00010.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/e8ed1a3ccf/00015.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/e90c10fc4c/00005.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/e9422ad240/00060.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/e98eda8978/00025.png 1
# /disk2/guoxi/YouTube-VOS/train/Annotations/e98eda8978/00060.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/e9d3c78bf3/00015.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/eb383cb82e/00055.png 4
# /disk2/guoxi/YouTube-VOS/train/Annotations/ebbb90e9f9/00055.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/ec28252938/00095.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/ecae59b782/00015.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/ecae59b782/00020.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/ecae59b782/00025.png 4
# /disk2/guoxi/YouTube-VOS/train/Annotations/ed8f814b2b/00040.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/ed9ff4f649/00040.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/ed9ff4f649/00060.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/ee316eaed6/00010.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/ee947ed771/00025.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/ef45ce3035/00050.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/f0268aa627/00050.png 4
# /disk2/guoxi/YouTube-VOS/train/Annotations/f04cf99ee6/00035.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/f3085d6570/00020.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/f3325c3338/00005.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/f36483c824/00095.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/f46c364dca/00170.png 5
# /disk2/guoxi/YouTube-VOS/train/Annotations/f48b535719/00035.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/f4aa882cfd/00150.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/f4daa3dbd5/00080.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/f5966cadd2/00035.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/f5966cadd2/00050.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/f5bddf5598/00050.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/f659251be2/00055.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/f7e0c9bb83/00010.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/f9ea6b7f31/00060.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/fb4cbc514b/00025.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/fb4e6062f7/00015.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/fbc645f602/00075.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/fc96cda9d8/00010.png 2
# /disk2/guoxi/YouTube-VOS/train/Annotations/fdb3d1fb1e/00020.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/fe24b0677d/00025.png 3
# /disk2/guoxi/YouTube-VOS/train/Annotations/ff5a1ec4f3/00165.png 5
# /disk2/guoxi/YouTube-VOS/train/Annotations/ff773b1a1e/00010.png 2