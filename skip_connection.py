import torch
import torch.nn as nn
import torch.nn.functional as F


class SkipConnection(nn.Module):

    def __init__(self, in_planes, out_planes, temporal_upsample=False, spatial_upsample=False):
        super(SkipConnection, self).__init__()
        self.temporal_upsample = temporal_upsample
        self.spatial_upsample = spatial_upsample

        self.relu = nn.ReLU(inplace=True)
        # cha_num_down = int(in_planes/8)
        cha_num_down = int(in_planes / 16)
        self.conv_cha_down = nn.Conv3d(in_channels=in_planes, out_channels=cha_num_down, kernel_size=1, bias=False)
        self.bn_cha_down = nn.BatchNorm3d(num_features=cha_num_down)
        self.conv_in = nn.Conv3d(in_channels=in_planes, out_channels=cha_num_down, kernel_size=1, bias=False)
        self.bn_in = nn.BatchNorm3d(num_features=cha_num_down)
        self.conv_skip = nn.Conv3d(in_channels=in_planes, out_channels=cha_num_down, kernel_size=1, bias=False)
        self.bn_skip = nn.BatchNorm3d(num_features=cha_num_down)


        cha_num_3d = 2 * cha_num_down
        # type A
        self.conv_a_s = nn.Conv3d(in_channels=cha_num_3d, out_channels=cha_num_3d, kernel_size=(1, 3, 3), padding=(0, 1, 1), bias=False)
        self.bn_a_s = nn.BatchNorm3d(num_features=cha_num_3d)
        self.conv_a_t = nn.Conv3d(in_channels=cha_num_3d, out_channels=cha_num_3d, kernel_size=(3, 1, 1), padding=(1, 0, 0), bias=False)
        self.bn_a_t = nn.BatchNorm3d(num_features=cha_num_3d)
        # type b
        self.conv_b_s = nn.Conv3d(in_channels=cha_num_3d, out_channels=cha_num_3d, kernel_size=(1, 3, 3), padding=(0, 1, 1), bias=False)
        self.bn_b_s = nn.BatchNorm3d(num_features=cha_num_3d)
        self.conv_b_t = nn.Conv3d(in_channels=cha_num_3d, out_channels=cha_num_3d, kernel_size=(3, 1, 1), padding=(1, 0, 0), bias=False)
        self.bn_b_t = nn.BatchNorm3d(num_features=cha_num_3d)
        # conv to reduce the channel
        self.conv_redu_cha = nn.Conv3d(in_channels=2*cha_num_3d, out_channels=cha_num_3d, kernel_size=1, bias=False)
        self.bn_redu_cha = nn.BatchNorm3d(num_features=cha_num_3d)

        self.conv_cha_up = nn.Conv3d(in_channels=2*cha_num_3d, out_channels=out_planes, kernel_size=1, bias=False)
        self.bn_cha_up = nn.BatchNorm3d(num_features=out_planes)

    def ST_A(self, x):
        x = self.relu(self.bn_a_s(self.conv_a_s(x)))
        x = self.relu(self.bn_a_t(self.conv_a_t(x)))
        return x

    def ST_B(self, x):
        out1 = self.relu(self.bn_b_s(self.conv_b_s(x)))
        out2 = self.relu(self.bn_b_t(self.conv_b_t(x)))
        out = torch.cat((out1, out2), dim=1)
        out = self.relu(self.bn_redu_cha(self.conv_redu_cha(out)))
        return out

    # def ST_C(self, x):
    #     out_s = self.relu(self.bn_st(self.conv_spatial(x)))
    #     out_t = self.relu(self.bn_st(self.conv_temporal(out_s)))
    #     out = torch.cat((out_s, out_t), dim=1)
    #     out = self.relu(self.bn_st(self.conv_redu_cha(out)))
    #     return out

    def forward(self, data):
        skip, x = data
        # temporal upsample
        if self.temporal_upsample:
            _, _, depth, hei, wid = x.size()
            x = F.interpolate(x, size=[depth*2, hei, wid], mode='trilinear', align_corners=True)

        fea_skip = self.relu(self.bn_skip(self.conv_skip(skip)))
        fea_x = self.relu(self.bn_in(self.conv_in(x)))
        fea = torch.cat((fea_skip, fea_x), dim=1)
        # spatial upsample
        if self.spatial_upsample:
            _, _, depth, hei, wid = fea.size()
            fea = F.interpolate(fea, size=[depth, hei*2, wid*2], mode='trilinear', align_corners=True)

        out_a = self.ST_A(fea)
        out_b = self.ST_B(fea)
        # out_c = self.ST_C(fea)
        out = torch.cat((out_a, out_b), dim=1)
        res = self.relu(self.bn_cha_up(self.conv_cha_up(out)))

        return res


# model = SkipConnection(in_planes=512, out_planes=256, temporal_upsample=True, spatial_upsample=True).cuda()
# skip = torch.randn((4, 512, 4, 28, 28)).float().cuda()
# fea = torch.randn((4, 512, 2, 28, 28)).float().cuda()
# res = model((skip, fea))
# print('res.size():', res.size())

