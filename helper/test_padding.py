# import os
# from PIL import Image
# import numpy as np

# mask = Image.open('/disk2/guoxi/YouTube-VOS/train/Annotations/ff5a1ec4f3/00130.png')
# obj_id = list(np.unique(mask))
# print(mask)
# print(obj_id)
# for ind in obj_id[1:]:
#     print(ind)

#
# import os
# from PIL import Image
# import numpy as np
# import shutil
#
# img_fol_rp = '/disk2/guoxi/YouTube-VOS/train/JPEGImages/'
# mask_fol_rp = '/disk2/guoxi/YouTube-VOS/train/Annotations/'
# fol_set = os.listdir(mask_fol_rp)  # os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表。这个列表以字母顺序。
# fol_set.sort()
# i=15
# for fol_name in fol_set:
#     #print(fol_name)
#     mask_rp = mask_fol_rp + fol_name + '/'   # 生成每个文件夹
#     mask_set = os.listdir(mask_rp)           # 生成每个集
#     mask_set.sort()
#     print(mask_set)
#
#     if len(mask_set) < 16:
#         img_rp = img_fol_rp + fol_name + '/'
#         if len(mask_set) < i:
#             i =len(mask_set)
#         # print(len(mask_set), mask_rp)
#         # i+=1
#         print(i)
#         # last_name = mask_set[-1]
#         # last_order = int(last_name[:-4])
#         # for _ in range(len(mask_set), 16):
#         #     last_order += 5
#         #     name = str(last_order).zfill(5)
#         #     shutil.copyfile(mask_rp+last_name, mask_rp+name+'.png')
#         #     print('file copy', mask_rp+last_name, mask_rp+name+'.png')
#         #     shutil.copyfile(img_rp+last_name[:-4]+'.jpg', img_rp+name+'.jpg')
# for len in range(16):
#     padding_num_first = (16 - len) // 2
#     padding_num_last = 16 - len - padding_num_first
#     print(len)
#     # print(padding_num_first)
#     # print(padding_num_last)
