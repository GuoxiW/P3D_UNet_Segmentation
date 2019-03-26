# P3D-transform设置

- [ ] resize

- 直接使用make_resize_data执行resize_transform,将数据分为dataset和reference_dataset。

- [ ] 随机裁剪(val中为None)

- 16帧视频clip和对应的groungtruth由256x256裁剪成224x224。

- 采用list相加的办法实现裁剪同一位置。


- [ ] 随机水平翻转(val中为None)
- 对reference_clip,reference_mask,clip,groundtruth进行概率0.5的随机水平翻转。
- 采用list相加的办法实现同时水平翻转。

- [ ] 随机擦除(val中为None)

- 对clip进行随机擦除。


- [ ] 原图变换

- clip,reference_clip进行ToTensor和norm。

- [ ] mask变换
- groundtruth,reference_clip进行ToTensor。

