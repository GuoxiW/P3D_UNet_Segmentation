from __future__ import division
import math
import random
from PIL import Image, ImageOps
import numpy as np
import numbers


class JointResize(object):
    """Resize the input PIL.Image to the given 'size'.
    size can be a tuple (target_height, target_width)
    or an integer, in which case the target will be of a square shape (size, size)
    interpolation: Default: PIL.Image.BILINEAR
    """

    def __init__(self, size, interpolation=Image.BILINEAR):
        self.size = size
        self.interpolation = interpolation

    def __call__(self, imgs):
        return [img.resize((self.size, self.size), self.interpolation) for img in imgs]


class MaskResize(object):
    """Resize the input PIL.Image to the given 'size'.
    size should be an integer, in which case the target will be of a square shape (size, size)
    interpolation: Default: interpolation=Image.NEAREST
    """

    def __init__(self, size, interpolation=Image.NEAREST):
        self.size = size
        self.interpolation = interpolation

    def __call__(self, imgs):
        return [img.resize((self.size, self.size), self.interpolation) for img in imgs]


class JointRandomCrop(object):
    """Crops the given list of PIL.Image at a random location to have a region of
    the given size. size can be a tuple (target_height, target_width)
    or an integer, in which case the target will be of a square shape (size, size)
    """

    def __init__(self, size, padding=0):
        if isinstance(size, numbers.Number):  # 来判断一个对象是否是一个已知的类型
            self.size = (int(size), int(size))
        else:
            self.size = size
        self.padding = padding

    def __call__(self, imgs):
        if self.padding > 0:
            imgs = [ImageOps.expand(img, border=self.padding, fill=0) for img in imgs]  # #扩展图像边界，宽度为border，填充用fill

        w, h = imgs[0].size
        th, tw = self.size
        if w == tw and h == th:
            return imgs

        x1 = random.randint(0, w - tw)
        y1 = random.randint(0, h - th)
        return [img.crop((x1, y1, x1 + tw, y1 + th)) for img in imgs]  # (left, upper, right, lower)


class JointRandomHorizontalFlip(object):  # 水平翻转
    """Randomly horizontally flips the given list of PIL.Image with a probability of 0.5
    """

    def __call__(self, imgs):
        if random.random() < 0.5:
            return [img.transpose(Image.FLIP_LEFT_RIGHT) for img in imgs]

        # res = list()
        # for img in imgs:
        #     temp = img.transpose(Image.FLIP_LEFT_RIGHT)
        #     res.append(temp)

        return imgs


class RandomErase(object):
    '''
    Class that performs Random Erasing in Random Erasing Data Augmentation by Zhong et al.
    -------------------------------------------------------------------------------------
    probability: The probability that the operation will be performed.
    sl: min erasing area  # 最小擦除区域
    sh: max erasing area  # 最大擦除区域
    r1: min aspect ratio  # 最小纵横比
    mean: erasing value
    -------------------------------------------------------------------------------------
    '''

    def __init__(self, probability=0.5, sl=0.02, sh=0.4, r1=0.3, mean=[125, 123, 113]):
        self.probability = probability
        self.mean = mean
        self.sl = sl
        self.sh = sh
        self.r1 = r1

    def __call__(self, img):

        if random.uniform(0, 1) > self.probability:
            return img

        for attempt in range(100):

            img_np = np.asarray(img, dtype=np.uint8)
            area = img_np.shape[0] * img_np.shape[1]  # 数值 表示多少个像素

            target_area = random.uniform(self.sl, self.sh) * area
            aspect_ratio = random.uniform(self.r1, 1 / self.r1)  # 纵横比

            h = int(round(math.sqrt(target_area * aspect_ratio)))  #round() 方法返回浮点数x的四舍五入值。
            w = int(round(math.sqrt(target_area / aspect_ratio)))

            if w < img_np.shape[1] and h < img_np.shape[0]:
                x1 = random.randint(0, img_np.shape[0] - h)
                y1 = random.randint(0, img_np.shape[1] - w)
                if img_np.shape[2] == 3:
                    img_np.flags.writeable = True ##
                    img_np[x1:x1 + h, y1:y1 + w, :] = 255 * np.random.rand(h,w,3)
                else:
                    img_np[x1:x1 + h, y1:y1 + w, 0] = 255 * np.random.rand(h,w,1)
                img = Image.fromarray(img_np, mode='RGB') ##rgb???
                return img
        return img
