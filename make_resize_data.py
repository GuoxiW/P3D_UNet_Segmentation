from PIL import Image
import os
import shutil


def make_resize_data(fol_rp, size, out_rp):
    fol_set = os.listdir(fol_rp)
    fol_set.sort()

    for fol_name in fol_set:
        img_rp = fol_rp + fol_name + '/'
        img_set = os.listdir(img_rp)
        img_set.sort()
        os.mkdir(out_rp + fol_name + '/')

        for img_name in img_set:
            img = Image.open(img_rp + img_name)
            img = img.resize((size, size), Image.BILINEAR)
            img_save_rp = out_rp + fol_name + '/' + img_name
            img.save(img_save_rp)


def make_resize_data_mask(fol_rp, size, out_rp):
    fol_set = os.listdir(fol_rp)
    fol_set.sort()

    for fol_name in fol_set:
        img_rp = fol_rp + fol_name + '/'
        img_set = os.listdir(img_rp)
        img_set.sort()
        os.mkdir(out_rp + fol_name + '/')

        for img_name in img_set:
            if len(img_name) == 13:  # copy reference
                shutil.copy(img_rp + 'reference.txt', out_rp + fol_name + '/reference.txt')
            else:  # resize image
                img = Image.open(img_rp + img_name)
                img = img.resize((size, size), Image.NEAREST)
                img_save_rp = out_rp + fol_name + '/' + img_name
                img.save(img_save_rp)

# # test
# make_resize_data('/data1/guoxi/p3d_floder/dataset/test/train/', 256, '/data1/guoxi/p3d_floder/dataset/test/train_256/')
# make_resize_data_mask('/data1/guoxi/p3d_floder/dataset/test/mask/', 256, '/data1/guoxi/p3d_floder/dataset/test/mask_256/')

# make dataset
# 256的train,trainannot
make_resize_data('/data1/guoxi/p3d_floder/dataset/resize_data/train/', 256, '/data1/guoxi/p3d_floder/resized_dataset/train_dataset/train/')
make_resize_data_mask('/data1/guoxi/p3d_floder/dataset/resize_data/trainannot/', 256, '/data1/guoxi/p3d_floder/resized_dataset/train_dataset/trainannot/')

## 224的train,trainannot,val,valannot
make_resize_data('/data1/guoxi/p3d_floder/dataset/resize_data/train/', 224, '/data1/guoxi/p3d_floder/resized_dataset/reference_dataset/train/')
make_resize_data('/data1/guoxi/p3d_floder/dataset/resize_data/val/', 224, '/data1/guoxi/p3d_floder/resized_dataset/val_dataset/val/')
make_resize_data_mask('/data1/guoxi/p3d_floder/dataset/resize_data/trainannot/', 224, '/data1/guoxi/p3d_floder/resized_dataset/reference_dataset/trainannot/')
make_resize_data_mask('/data1/guoxi/p3d_floder/dataset/resize_data/valannot/', 224, '/data1/guoxi/p3d_floder/resized_dataset/val_dataset/valannot/')
