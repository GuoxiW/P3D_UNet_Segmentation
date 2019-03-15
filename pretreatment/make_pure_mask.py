import numpy as np
from PIL import Image
mask_rp = '/disk2/guoxi/YouTube-VOS/train_nomutation/Annotations/0248626d9a/00000.png'
pure_mask_rp = '/disk2/guoxi/p3d/dataset/'
pure_mask_name = 'pure_mask.png'
mask = Image.open(mask_rp)
mask_np = np.asarray(mask, dtype=np.uint8)
templet = np.zeros(mask_np.shape, dtype=np.uint8)
pure_mask = Image.fromarray(templet, mode='L')
pure_mask.save(pure_mask_rp + pure_mask_name)
