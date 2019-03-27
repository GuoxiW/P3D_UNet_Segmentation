YouTube VOS 数据清洗顺序

1.使用remove_wrong_pixel进行出错mask的删除
判定标准：
使用remove_for_find_pixel进行所有mask的筛选，筛选出像素个数小于255的mask。
人工筛选，对于噪声引起的mask出错，直接删除。

```
72个小于阈值删除的
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
32个手动删除的
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
共104个

```

2.图片padding
判定标准
使用pre_padding函数，对于图片数少于16张的视频进行单边padding操作。

```
 ['00000.png', '00005.png', '00010.png', '00015.png', '00020.png', '00025.png', '00030.png', '00035.png', '00040.png', '00045.png', '00050.png', '00055.png', '00060.png']
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
```

3.mask padding
使用pre_mask_padding函数，将图片按mask分开，格式为00000_0。

4.处理突变帧
具体方法：
假设编号较大的mask总是后出现的，所以对于出现突变帧的视频，仅需改变的是dataset中参考帧的选择，避免出现参考帧中不包含mask的情况

通过mask_change函数，将每一帧之前距离最近的突变帧的顺序找出来，写入mask文件夹下的reference.txt中，在dataset中使用read_mask_set函数读取这个第一帧

当选取的所有帧中出现某一帧mask不存在的情况，则通过dataset函数中的mask_pil_loader函数读取'/data1/guoxi/p3d/dataset/pure_mask.png'目录下的纯黑帧代替。


5.制作数据集
使用seperate_train_val函数，分割出训练集和数据集

```
# move 96fbe5fc23
# move f5f051e9b4
# move 4a6e3faaa1
# move e8485a2615
# move fb47fcea1e
# move 0f9683715b
# move ea444a37eb
# move b0df7c5c5c
# move da080507b9
# move de6a9382ca
# move 4804ee2767
# move 1e1a18c45a
# move 4b556740ff
# move 72552a07c9
# move f7d49799ad
# move 16adde065e
# move d429c67630
# move c8ab107dd5
# move 9437c715eb
# move aa175e5ec7
# move b76df6e059
# move 2f680909e6
# move 4e824b9247
# move 64750b825f
# move 383bb93111
# move 4607f6c03c
# move dd415df125
# move 9684ef9d64
# move 8744b861ce
# move 57c010175e
# move 9077e69b08
# move 1232b2f1d4
# move 8f0a653ad7
# move 93ff35e801
# move 3f18728586
# move c64035b2e2
# move 09049f6fe3
# move c9c3cb3797
# move 692eb57b63
# move 9574b81269
# move 3988074b88
# move 6dd2827fbb
# move 1981e763cc
# move c32d4aa5d1
# move 08f561c65e
# move 484ab44de4
# move adc648f890
# move 63d37e9fd3
# move 6c5123e4bc
# move b6d79a0845
# move 07c62c3d11
# move a1dfdd0cac
# move ec3d4fac00
# move 9a08e7a6f8
# move 78e29dd4c3
# move e436d0ff1e
# move 3eede9782c
# move d38d1679e2
# move 86b2180703
# move 0f17fa6fcb
# move 3d5aeac5ba
# move a64a40f3eb
# move 5851739c15
# move 94a33abeab
# move c41e6587f5
# move b01080b5d3
# move 10eced835e
# move c9188f4980
# move b241e95235
# move 8f62a2c633
# move 6899d2dabe
# move a263ce8a87
# move 04667fabaa
# move 968492136a
# move d4193011f3
# move ed7455da68
# move 59d53d1649
# move 1ca5673803
# move d2b026739a
# move ba98512f97
# move 536b17bcea
# move 97756b264f
# move 6c81b014e9
# move df20a8650d
# move 3cc37fd487
# move 29d779f9e3
# move f2dd6e3add
# move 80f16b016d
# move d704766646
# move 8bfff50747
# move 625892cf0b
# move 260dd9ad33
# move 45c36a9eab
# move 6bf584200f
# move 9a02c70ba2
# move 25c750c6db
# move 720e7a5f1e
# move a36bdc4cab
# move b77e5eddef
# move 2d8f5e5025
# move 48bd66517d
# move c5ab1f09c8
# move e1f14510fa
# move f9750192a4
# move dd8636bd8b
# move 9445c3eca2
# move d39934abe3
# move b751e767f2
# move b8aaa59b75
# move ea5672ffa8
# move 75504539c3
# move 9e6ddbb52d
# move 27659fa7d6
# move 13ae097e20
# move a965504e88
# move 8e98ae3c84
# move 59fe33e560
# move 804c558adb
# move 6dd36705b9
# move 038b2cc71d
# move 5161e1fa57
# move 9a2f2c0f86
# move 80e41b608f
# move e4eaa63aab
# move 5cb49a19cf
# move 4e3f346aa5
# move 683de643d9
# move b15bf4453b
# move fe3c02699d
# move 1145b49a5f
# move 1180cbf814
# move 571ca79c71
# move 1336440745
# move 768671f652
# move 6b3a24395c
# move 0ea68d418b
# move 42da96b87c
# move c307f33da2
# move 5a91c5ab6d
# move 637681cd6b
# move 59a6459751
# move d7797196b4
# move 011ac0a06f
# move e3d5b2cd21
# move d14d1e9289
# move 38eb2bf67f
# move c2b974ec8c
# move 65ff12bcb5
# move c69689f177
# move f3325c3338
# move 1a6f3b5a4b
# move 3e04a6be11
# move 52ee406d9e
# move df5536cfb9
# move 57c7fc2183
# move 74d4cee0a4
# move 0974a213dc
# move 7584129dc3
# move 4eb6fc23a2
# move 8200245704
# move 49972c2d14
# move 720b398b9c
# move 536096501f
# move 7143fb084f
# move 6df3637557
# move 733824d431
# move 77d8aa8691
# move 77610860e0
# move d4dd1a7d00
# move 579393912d
# move e6387bd1e0
# move 4a86fcfc30
# move a73d3c3902
# move 377db65f60
# move 84696b5a5e
# move d3f5c309cc
# move 6419386729
# move efe828affa
# move 4918d10ff0
# move 081207976e
# move 29dde5f12b
# move 4ea77bfd15
# move 8f3b4a84ad
# move 747c44785c
# move 59623ec40b
# move 499bf07002
# move 1cada35274
# move 1257a1bc67
# move ce712ed3c9
# move d69967143e
# move 4c397b6fd4
# move 3b23792b84
# move ff5a1ec4f3
# move 238d4b86f6
# move 217bae91e5
# move 3e3e4be915
# move f0c34e1213
# move 5316d11eb7
# move e78d450a9c
# move 1022fe8417
# move a99bdd0079
# move 7d1333fcbe
# move ba1f03c811
# move 6057307f6e
# move b8c03d1091
# move 650b0165e4
# move 806b6223ab
# move add21ee467
# move 7550949b1d
# move 98ba3c9417
# move 11feabe596
# move b4b715a15b
# move 003234408d
# move e6be243065
# move 351cfd6bc5
# move 413bab0f0d
# move caeb6b6cbb
# move 082900c5d4
# move bbb4302dda
# move b841cfb932
# move f3704d5663
# move df8ad5deb9
# move cf13f5c95a
# move 2a821394e3
# move d6eed152c4
# move 2bdd82fb86
# move a1193d6490
# move e1ab7957f4
# move 0c3a04798c
# move 394454fa9c
# move 578f211b86
# move 9e29b1982c
# move 3dd48ed55f
# move 3f0b0dfddd
# move 714d902095
# move aaff16c2db
# move f1dc710cf4
# move b1d1cd2e6e
# move 90c7a87887
# move c4571bedc8
# move da0e944cc4
# move 4932911f80
# move 092e4ff450
# move fc9832eea4
# move 8f5d3622d8
# move 7163b8085f
# move aeba9ac967
# move 91634ee0c9
# move 07652ee4af
# move 12ec9b93ee
# move 8749369ba0
# move 3c700f073e
# move a2bcd10a33
# move 01e64dd36a
# move 4db117e6c5
# move 382caa3cb4
# move 56cc449917
# move 5c4c574894
# move 895e8b29a7
# move 3a2c1f66e5
# move a5122c6ec6
# move d44e6acd1d
# move 01b80e8e1a
# move b22099b419
# move 625817a927
# move 69023db81f
# move 282b0d51f5
# move e5abc0e96b
# move b37c01396e
# move 3beef45388
# move 4fdfef4dea
# move a18ad065fc
# move 66e98e78f5
# move 84e0922cf7
# move 3504df2fda
# move a046399a74
# move b9bcb3e0f2
# move 5c42aba280
# move 1157472b95
# move 17e33f4330
# move bd0d849da4
# move d3e6e05e16
# move 0450095513
# move 279214115d
# move f8c8de2764
# move 1705796b02
# move 7320b49b13
# move abbe2d15a0
# move 3b9ad0c5a9
# move 2039c3aecb
# move 8dda6bf10f
# move 4019231330
# move a5da03aef1
# move 6bf2e853b1
# move f1ec5c08fa
# move d44a764409
# move a973f239cd
# move 6e618d26b6
# move c6bb6d2d5c
# move e7ea10db28
# move d521aba02e
# move 6aa8e50445
# move f34497c932
# move ead5d3835a
# move 91c33b4290
# move f51c5ac84b
# move 1197e44b26
# move 077d32af19
# move 534a560609
# move 17c7bcd146
# move 01ff60d1fa
# move 2fc9520b53
# move 46f5093c59
# move 6454f548fd
# move 21386f5978
# move 310021b58b
# move 8939db6354
# move f2cfd94d64
# move c844f03dc7
# move 26de3d18ca
# move b6a1df3764
# move 764271f0f3
# move d708e1350c
# move 4cff5c9e42
# move fd33551c28
# move e128124b9d
# move d5ee40e5d0
# move 5e8d59dc31
# move 2ac9ef904a
# move 9893a3cf77
# move 0f6c2163de
# move 420caf0859
# move abeae8ce21
# move 0b5b5e8e5a
# move b70a5a0d50
# move 824ca5538f
# move 7bb0abc031
# move cdd57027c2
# move 9b22b54ee4
# move 72690ef572
# move 05774f3a2c
# move 4efb9a0720
# move eb6ac20a01
# move 39f6f6ffb1
# move a6a810a92c
# move aae78feda4
# move 9041a0f489
```

6.数据集resize:


使用/pretreatment/make_resize_data建立两个数据集，一个用于处理的dataset，一个是用于引用的reference。


dataset中存放的数据：256的train,trainannot,224的val,valannot。


reference_dataset中存放的数据：224的train,trainannot,val,valannot。



7.设置参考信息（txt）

7.1 使用/pretreatment/mask_change在mask文件夹建立reference.txt文件，标出每一帧之前最近的突变帧，用于选取参考帧。（参见4处理突变帧）

7.2 使用/pretreatment/mask_num在mask文件夹下建立refer_num.txt文件，用于标出每一帧各有都少个mask，从而randomint(1,mask)从中选择训练的mask。

注意，此时若原始数据时纯黑的，即其中没有物体，则为了让学到东西，refer_num.txt中置1，若中间的没有物体帧不影响mask的选取，仅需在dataloader中 mask_pil_loader 中指定一张纯黑mask的path。

8.将val的数据放在一起
使用/pretreatment/make_val_data，用于将val中所有的image和mask放在一个文件夹里，在evaluation中进行比对。
