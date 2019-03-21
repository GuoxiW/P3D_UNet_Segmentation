import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.nn.init as init


def conv_S(in_planes, out_planes, stride=1, padding=1, dilation=1):
    # as is descriped, conv S is 1x3x3
    return nn.Conv3d(in_planes, out_planes, kernel_size=(1, 3, 3), stride=stride,
                     padding=(0, dilation, dilation), bias=False, dilation=(1, dilation, dilation))


def conv_T(in_planes,out_planes,stride=1,padding=1):
    # conv T is 3x1x1
    return nn.Conv3d(in_planes,out_planes,kernel_size=(3,1,1),stride=stride,
                     padding=padding,bias=False)


def downsample_basic_block(x, planes, stride):
    out = F.avg_pool3d(x, kernel_size=1, stride=stride)
    zero_pads = torch.Tensor(out.size(0), planes - out.size(1),
                             out.size(2), out.size(3),
                             out.size(4)).zero_()
    if isinstance(out.data, torch.cuda.FloatTensor):
        zero_pads = zero_pads.cuda()

    out = torch.cat([out.data, zero_pads], dim=1)

    return out


def weights_init(m):
	if isinstance(m, nn.Conv2d) or isinstance(m, nn.Conv3d):
		# kaiming is first name of author whose last name is 'He' lol
		init.kaiming_uniform_(m.weight)


def train(model, trn_loader, optimizer, criterion):
    model.train()
    trn_loss = 0
    for batch_idx, (inputs, targets) in enumerate(trn_loader):

        pred_mask = model(inputs.cuda())
        target = targets.cuda()

        optimizer.zero_grad()
        loss = criterion(pred_mask, target)
        loss.backward()
        optimizer.step()
        loss_value = loss.item()
        print(loss_value)
        trn_loss += loss_value
    trn_loss /= len(trn_loader)  # n_batches
    return trn_loss


def test(model, test_loader, criterion):
    model.eval()
    test_loss = 0
    for inputs, targets in test_loader:
        with torch.no_grad():
            pred_mask = model(inputs.cuda())

        target = targets.cuda()
        loss = criterion(pred_mask, target)
        loss_value = loss.item()
        print('reach here', loss_value)
        test_loss += loss_value

    test_loss /= len(test_loader)  # n_batches
    return test_loss
