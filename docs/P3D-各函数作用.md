注：视频中的每一帧叫做图片，图片的真值groundtruth叫做真值，真值中的物体叫做mask

1.helper/cal_mask_sep:计算每一个图片中有多少个mask

2.helper/mask_inter:用于选择帧突变的视频，采用删除的方法，删除帧未突变的视频，留下帧突变的视频。

3.helper/pretreatment:以函数形式写的所有pretreatment操作。

4.helper/find_mask_pixel_num:设置阈值255,寻找像素数小于255的mask

5.helper/remove_for_find_pixel:设置阈值255，寻找像素数小于255的mask,删除正确的视频，然后在错误的视频中人工判断其是否为错误像素

6.pretreatment/remove_wrong_pixel:通过筛选出的错误像素，删除错误像素

7.pretreatment/make_pure_mask:生成一个224x224纯黑的背景，当图片中没有mask时由此代替

8.pretreatment/mask_change:用于处理突变帧，有突变帧时改变参考帧选取的第一帧，写入每一个视频中的'reference.txt'文件夹中，dataset中读取

9.pretreatment/pre_mask_padding：用于处理多个mask的情况，将名称命名为00000_0.png，00000_1.png

10.pretreatment/pre_padding:用于将不够16帧的视频padding到16帧，采取最后一帧的单边padding。

11.pretreatment/read_mask_change:用于读取mask_change函数得出的'reference.txt'

12.pretreatment/seperate_train_val:将train中的数据划分为train和val，即从train中删除一部分数据，复制到val中。

11.helper/test_padding:用于检测pretreatment/pre_padding视频padding的效果。

12.helper/test_wrong_mask:早期的用于检测错误mask的代码。

13.pretreatment/make_resize_data:将数据集resize成dataset和reference_dataset,从而在程序中减少resize_transform这一项。

14.pretreatment/mask_num:将每一个mask帧中有多少个mask记录在'refer_num.txt'中，从而dataloader中实现更快的读取，而若纯黑的mask，则写入1。

15.pretreatment/make_val_data:用于将val中所有的image和mask放在一个文件夹里，在evaluation中进行比对。

16.evaluation_for_matlab:生成用于DAVIS matlab计算的数据格式。

```
/fol_name/mask_name/00000.png
```

17.for_davis/change_davis_wrong:DAVIS数据集中的tennis项网球本应是背景0，但被标注成了255，用此函数来更改。

18.for_davis/get_fol_name:生成用于DAVIS matlab计算的train.txt,val.txt为空。

```
/data1/guoxi/p3d/p3d_evaluation/DAVIS/ImageSets/2017/train.txt
/data1/guoxi/p3d/p3d_evaluation/DAVIS/ImageSets/2017/val.txt
```

19.for_davis/remove_mask_folder:在使用DAVIS matlab将同一图片不同mask混合时，合成后的文件夹删除/1/，/2/文件夹。

20.remove_sep_mask_and_reference:删除ground truth中的reference.txt,refer_num.txt,00000_1.png等等影响evaluation的文件。
