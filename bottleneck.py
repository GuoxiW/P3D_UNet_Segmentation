from __future__ import print_function
import torch.nn as nn

import utils


class Bottleneck(nn.Module):
    expansion = 4

    def __init__(self, inplanes, planes, stride=1, downsample=None, n_s=0, depth_3d=47, ST_struc=('A', 'B', 'C'), dilation=1):
        super(Bottleneck, self).__init__()
        self.downsample = downsample
        self.depth_3d = depth_3d
        self.ST_struc = ST_struc
        self.len_ST = len(self.ST_struc)

        stride_p = stride
        if self.downsample is not None:
            stride_p = (1, 2, 2)
        # if n_s < self.depth_3d:
        # for layer1
        if n_s == 0:
            stride_p = 1
        # modified, we make sure layer3 can enter
        elif n_s >= 11:
            stride_p = 1
        self.conv1 = nn.Conv3d(inplanes, planes, kernel_size=1, bias=False, stride=stride_p, dilation=(1, dilation, dilation))
        self.bn1 = nn.BatchNorm3d(planes)

        self.id = n_s
        self.ST = list(self.ST_struc)[self.id % self.len_ST]
        # if self.id < self.depth_3d:
        self.conv2 = utils.conv_S(planes, planes, stride=1, padding=(0, 1, 1), dilation=dilation)
        self.bn2 = nn.BatchNorm3d(planes)
        #
        self.conv3 = utils.conv_T(planes, planes, stride=1, padding=(1, 0, 0))
        self.bn3 = nn.BatchNorm3d(planes)

        if n_s < self.depth_3d:
            self.conv4 = nn.Conv3d(planes, planes * 4, kernel_size=1, bias=False, dilation=(1, dilation, dilation))
            self.bn4 = nn.BatchNorm3d(planes * 4)
        else:
            self.conv4 = nn.Conv2d(planes, planes * 4, kernel_size=1, bias=False, dilation=dilation)
            self.bn4 = nn.BatchNorm2d(planes * 4)
        self.relu = nn.ReLU(inplace=True)

        self.stride = stride

    def ST_A(self, x):
        x = self.conv2(x)
        x = self.bn2(x)
        x = self.relu(x)

        x = self.conv3(x)
        x = self.bn3(x)
        x = self.relu(x)

        return x

    def ST_B(self, x):
        tmp_x = self.conv2(x)
        tmp_x = self.bn2(tmp_x)
        tmp_x = self.relu(tmp_x)

        x = self.conv3(x)
        x = self.bn3(x)
        x = self.relu(x)

        return x + tmp_x

    def ST_C(self, x):
        x = self.conv2(x)
        x = self.bn2(x)
        x = self.relu(x)

        tmp_x = self.conv3(x)
        tmp_x = self.bn3(tmp_x)
        tmp_x = self.relu(tmp_x)

        return x + tmp_x

    def forward(self, x):
        residual = x

        out = self.conv1(x)
        out = self.bn1(out)
        out = self.relu(out)

        if self.ST == 'A':
            out = self.ST_A(out)
        elif self.ST == 'B':
            out = self.ST_B(out)
        elif self.ST == 'C':
            out = self.ST_C(out)

        out = self.conv4(out)
        out = self.bn4(out)

        if self.downsample is not None:
            residual = self.downsample(x)

        out += residual
        out = self.relu(out)

        return out

