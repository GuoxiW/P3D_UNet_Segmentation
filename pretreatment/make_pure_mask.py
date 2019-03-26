# 生成一个224x224纯黑的背景，当图片中没有mask时由此代替
import numpy as np
from PIL import Image
mask_rp = '/data1/guoxi/YouTube-VOS/train_nomutation/Annotations/0248626d9a/00000.png'
pure_mask_rp = '/data1/guoxi/p3d/dataset/'
pure_mask_name = 'pure_mask_224.png'
mask = Image.open(mask_rp)
mask = mask.resize((224, 224), Image.NEAREST)
mask_np = np.asarray(mask, dtype=np.uint8)
templet = np.zeros(mask_np.shape, dtype=np.uint8)
pure_mask = Image.fromarray(templet, mode='L')
pure_mask.save(pure_mask_rp + pure_mask_name)
