from __future__ import print_function
import torch
import torch.nn as nn
import numpy as np
import math
from functools import partial

import bottleneck
import skip_connection
import utils


class P3D(nn.Module):

    def __init__(self, block, layers, skip_connection, modality='RGB', shortcut_type='B', ST_struc=('A','B','C')):
        self.inplanes = 64
        super(P3D, self).__init__()
        # self.conv1 = nn.Conv3d(3, 64, kernel_size=7, stride=(1, 2, 2),
        #                        padding=(3, 3, 3), bias=False)
        self.input_channel = 3 if modality=='RGB' else 2  # 2 is for flow
        self.ST_struc=ST_struc

        # self.conv1_custom = nn.Conv3d(self.input_channel, 64, kernel_size=(1,7,7), stride=(1,2,2), padding=(0,3,3), bias=False)
        # self.conv1_custom = nn.Conv3d(7, 64, kernel_size=(1, 7, 7), stride=(1, 2, 2), padding=(0, 3, 3), bias=False)
        self.conv1_my = nn.Conv3d(7, 64, kernel_size=(1, 7, 7), stride=(1, 2, 2), padding=(0, 3, 3), bias=False)

        self.depth_3d=sum(layers[:3])
        # C3D layers are only (res2,res3,res4),  res5 is C2D
        # In other worlds, layer1, layer2, layer3 use C3D, layer4 uses C2D

        self.bn1 = nn.BatchNorm3d(64) # bn1 is followed by conv1
        self.cnt = 0
        self.relu = nn.ReLU(inplace=True)
        self.maxpool = nn.MaxPool3d(kernel_size=(2, 3, 3), stride=2, padding=(0, 1, 1))       # pooling layer for conv1.
        # # only pool at temporal dimension
        self.maxpool_2 = nn.MaxPool3d(kernel_size=(2, 1, 1), padding=0, stride=(2, 1, 1))   # pooling layer for res2, 3, 4.
        # use 3D conv to replace nn.MaxPool3d
        # self.conv_pool_1 = nn.Conv3d(in_channels=256, out_channels=256, kernel_size=(3, 1, 1), stride=(2, 1, 1), padding=(1, 0, 0))
        # self.conv_pool_2 = nn.Conv3d(in_channels=512, out_channels=512, kernel_size=(3, 1, 1), stride=(2, 1, 1), padding=(1, 0, 0))
        # self.conv_pool_3 = nn.Conv3d(in_channels=1024, out_channels=1024, kernel_size=(3, 1, 1), stride=(2, 1, 1), padding=(1, 0, 0))

        self.layer1 = self._make_layer(block, 64, layers[0], shortcut_type)
        self.layer2 = self._make_layer(block, 128, layers[1], shortcut_type, stride=2)
        self.layer3 = self._make_layer(block, 256, layers[2], shortcut_type, stride=2, dilation=2)

        # for up-sample
        self.skip3 = self._make_connection(skip_connection, in_planes=1024, out_planes=512, temporal_upsample=True, spatial_upsample=False)
        self.skip2 = self._make_connection(skip_connection, in_planes=512, out_planes=256, temporal_upsample=True, spatial_upsample=True)
        self.skip1 = self._make_connection(skip_connection, in_planes=256, out_planes=64, temporal_upsample=True, spatial_upsample=False)
        self.skip0 = self._make_connection(skip_connection, in_planes=64, out_planes=64, temporal_upsample=False, spatial_upsample=True)
        self.skipf = self._make_connection(skip_connection, in_planes=64, out_planes=16, temporal_upsample=True, spatial_upsample=True)
        self.conv_mask = nn.Conv3d(in_channels=16, out_channels=1, kernel_size=1, bias=False)

        # sigmoid norm
        self.sigmoid = nn.Sigmoid()

        for m in self.modules():
            if isinstance(m, nn.Conv3d):
                n = m.kernel_size[0] * m.kernel_size[1] * m.out_channels
                m.weight.data.normal_(0, math.sqrt(2. / n))
            elif isinstance(m, nn.BatchNorm3d):
                m.weight.data.fill_(1)
                m.bias.data.zero_()

        # # some private attribute
        # self.input_size=(self.input_channel,16,160,160)       # input of the network
        # self.input_mean = [0.485, 0.456, 0.406] if modality == 'RGB' else [0.5]
        # self.input_std = [0.229, 0.224, 0.225] if modality == 'RGB' else [np.mean([0.229, 0.224, 0.225])]


    # @property
    # def scale_size(self):
    #     return self.input_size[2] * 256 // 160   # assume that raw images are resized (340,256).
    #
    # @property
    # def temporal_length(self):
    #     return self.input_size[1]
    #
    # @property
    # def crop_size(self):
    #     return self.input_size[2]

    def _make_connection(self, skip_connection, in_planes, out_planes, temporal_upsample=False, spatial_upsample=False):
        layers = []
        layers.append(skip_connection(in_planes, out_planes, temporal_upsample=temporal_upsample, spatial_upsample=spatial_upsample))
        return nn.Sequential(*layers)

    def _make_layer(self, block, planes, blocks, shortcut_type, stride=1, dilation=1):
        downsample = None
        stride_p = stride #especially for downsample branch.

        if self.cnt == 0:
            stride_p = 1
        # for layer2
        elif self.cnt < 11:
            stride_p = (1, 2, 2)
        # for layer3
        else:
            stride_p = 1
        if stride != 1 or self.inplanes != planes * block.expansion:
            if shortcut_type == 'A':
                downsample = partial(utils.downsample_basic_block,
                                     planes=planes * block.expansion,
                                     stride=stride)
            else:
                downsample = nn.Sequential(
                    nn.Conv3d(self.inplanes, planes * block.expansion,
                              kernel_size=1, stride=stride_p, bias=False, dilation=(1, dilation, dilation)),
                    nn.BatchNorm3d(planes * block.expansion)
                )

        layers = []
        layers.append(block(self.inplanes, planes, stride, downsample, n_s=self.cnt, depth_3d=self.depth_3d, ST_struc=self.ST_struc, dilation=dilation))
        self.cnt += 1

        self.inplanes = planes * block.expansion
        for i in range(1, blocks):
            layers.append(block(self.inplanes, planes, n_s=self.cnt, depth_3d=self.depth_3d, ST_struc=self.ST_struc, dilation=dilation))
            self.cnt += 1

        return nn.Sequential(*layers)

    def forward(self, x):
        skip_feas = list()
        # input:(N, 3, 16, 224, 224)
        x = self.conv1_my(x)
        x = self.bn1(x)
        x = self.relu(x)
        skip_feas.append(x)
        # before maxpool torch.Size([8, 64, 16, 112, 112])
        x = self.maxpool(x)
        skip_feas.append(x)
        # after maxpool torch.Size([8, 64, 8, 56, 56])

        # after layer1: torch.Size([8, 256, 8, 56, 56])
        out = self.layer1(x)
        skip_feas.append(out)
        x = self.maxpool_2(out)
        # after max pool torch.Size([8, 256, 4, 56, 56])

        out = self.layer2(x)
        skip_feas.append(out)
        x = self.maxpool_2(out)
        # [N, 512, 4, 28, 28]

        out = self.layer3(x)
        x = self.maxpool_2(out)
        # torch.Size([N, 1024, 1, 28, 14])

        # up-layer3
        fea_skip3 = out
        x = self.skip3((fea_skip3, x))
        # [N, 512, 2, 28, 28]

        # up-layer2
        fea_skip2 = skip_feas.pop()
        x = self.skip2((fea_skip2, x))
        # [N, 256, 4, 56, 56]

        # up-layer1
        fea_skip1 = skip_feas.pop()
        x = self.skip1((fea_skip1, x))
        # [N, 64, 8, 56, 56]

        # up-layer0
        fea_skip0 = skip_feas.pop()
        x = self.skip0((fea_skip0, x))
        # [N, 64, 8, 112, 112]

        # up-layerf
        fea_skipf = skip_feas.pop()
        x = self.skipf((fea_skipf, x))
        # [N, 16, 16, 224, 224]

        seg_map = self.sigmoid(self.conv_mask(x))
        # [N, 1, 16, 224, 224]

        return seg_map


def P3D199(modality='RGB',**kwargs):
    """construct a P3D199 model based on a ResNet-152-3D model.
    """
    model = P3D(bottleneck.Bottleneck, [3, 8, 36, 3], skip_connection.SkipConnection, modality=modality, **kwargs)
    # model = P3D(bottleneck.Bottleneck, [3, 4, 6, 3], modality=modality, **kwargs)

    return model


# data = torch.randn((4, 3, 16, 224, 224)).cuda()
# model = P3D199().cuda()
# output = model(data)
# print('output.size():', output.size())


