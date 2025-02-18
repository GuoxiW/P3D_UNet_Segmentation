import torch
import torch.utils.data as data
from PIL import Image
import os
import functools
import random


#  读取不同的mask信息，需要更改maskloader函数
#  mask_loader中选取最大的数
#  成为共有多少个mask 0到数字range


def pil_loader(path):
    img = Image.open(path)
    return img
    # # open path as file to avoid ResourceWarning (https://github.com/python-pillow/Pillow/issues/835)
    # with open(path, 'rb') as f:
    #     with Image.open(f) as img:
    #         return img
    #         # return img.convert('RGB')


def mask_pil_loader(path):
    if not os.path.exists(path):
        path = '/disk2/guoxi/p3d/dataset/pure_mask.png'
    img = Image.open(path)
    return img
# path = '/disk2/guoxi/p3d/dataset/pure_mask.png'
# img = Image.open(path)
# print(img)
# def make_pure_mask():

#
# path = '/disk2/guoxi/p3d/dataset/trainannot/e0f217dd59/00080_1.png'
# img = mask_pil_loader(path)
# print(img)

# need modify


def get_default_image_loader():
    return pil_loader


def get_default_mask_image_loader():
    return mask_pil_loader
# def video_loader(video_dir_path, frame_names, is_mask, image_loader):
#     # print('frame_indices:', frame_indices)
#     video = []
#     #post_fix = '.png'
#     if is_mask:
#         post_fix = '.png'
#     else:
#         post_fix = '.jpg'
#
#     for name in frame_names:
#         image_path = video_dir_path + '/' + name + post_fix
#         video.append(image_loader(image_path))
#     return video


def video_loader(video_dir_path, frame_names, image_loader):
    video = []

    for name in frame_names:
        image_path = video_dir_path + '/' + name + '.jpg'
        video.append(image_loader(image_path))
    return video


def mask_video_loader(video_dir_path, frame_names, image_loader):
    video = []
    mask_tol_num = get_total_mask_num(video_dir_path)
    mask_num = str(random.randint(1, mask_tol_num))
    # print(mask_num)
    for name in frame_names:
        image_path = video_dir_path + '/' + name + '_' + mask_num + '.png'
        video.append(image_loader(image_path))
    return video


def get_total_mask_num(video_dir_path):
    mask_num = 0
    image_set = os.listdir(video_dir_path)
    image_set.sort()

    for image in image_set:
        if len(image) == 9:
            continue
        tem = int(image[-5])

        # print(tem)
        if tem > mask_num:
            mask_num = tem

    return mask_num

    #     # obtain the begin order for image set
    # img_set = os.listdir(video_dir_path)
    # img_set.sort()
    # first_img_name = img_set[0]
    # base_order = int(first_img_name[:-4])
    # for i in frame_indices:
    #     temp_order = (i-1)*5 + base_order
    #     image_path = video_dir_path + '/' + '{:05d}'.format(temp_order) + post_fix
    #     print('image_path:', image_path)
    #     if os.path.exists(image_path):
    #         video.append(image_loader(image_path))
    #     else:
    #         return video
    #
    # return video


def get_default_mask_video_loader():
    image_loader = get_default_mask_image_loader()
    return functools.partial(mask_video_loader, image_loader=image_loader)


def get_default_video_loader():
    image_loader = get_default_image_loader()
    return functools.partial(video_loader, image_loader=image_loader)


def get_video_names(vid_rp):
    video_set = os.listdir(vid_rp)
    video_set.sort()

    return video_set


def make_dataset(root_path):

    video_names = get_video_names(root_path)

    dataset = []
    for i in range(len(video_names)):
        if i % 1000 == 0:
            print('dataset loading [{}/{}]'.format(i, len(video_names)))

        video_path = os.path.join(root_path, video_names[i])

        # obtain n_frames
        frame_set = os.listdir(video_path)
        frame_set.sort()
        frame_set = [i[:-4] for i in frame_set]
        n_frames = len(frame_set)
        sample = {
            'video': video_path,
            'n_frames': n_frames,
            'video_id': video_names[i],
            'frame_set': frame_set
        }

        dataset.append(sample)

    return dataset


# def make_dataset(root_path, n_samples_for_each_video, sample_duration):
#
#     video_names = get_video_names(root_path)
#
#     dataset = []
#     for i in range(len(video_names)):
#         if i % 1000 == 0:
#             print('dataset loading [{}/{}]'.format(i, len(video_names)))
#
#         video_path = os.path.join(root_path, video_names[i])
#         if not os.path.exists(video_path):
#             print('not exist', video_path)
#             continue
#
#         begin_t = 1
#         # obtain n_frames
#         frame_set = os.listdir(video_path)
#         # frame_set.sort()
#         n_frames = len(frame_set)
#         end_t = n_frames
#         sample = {
#             'video': video_path,
#             'segment': [begin_t, end_t],
#             'n_frames': n_frames,
#             'video_id': video_names[i]
#         }
#
#         if n_samples_for_each_video == 1:
#             sample['frame_indices'] = list(range(1, n_frames + 1))
#             dataset.append(sample)
#         else:
#             if n_samples_for_each_video > 1:
#                 step = max(1, math.ceil((n_frames - 1 - sample_duration)/(n_samples_for_each_video - 1)))
#             else:
#                 step = sample_duration
#             for j in range(1, n_frames, step):
#                 sample_j = copy.deepcopy(sample)
#                 sample_j['frame_indices'] = list(
#                     range(j, min(n_frames + 1, j + sample_duration)))
#                 dataset.append(sample_j)
#
#     return dataset


class UCF101(data.Dataset):
    """
    Args:
        root (string): Root directory path.
        spatial_transform (callable, optional): A function/transform that  takes in an PIL image  # 空间变换
            and returns a transformed version. E.g, ``transforms.RandomCrop``
        temporal_transform (callable, optional): A function/transform that  takes in a list of frame indices  # 时间维度变换
            and returns a transformed version
        target_transform (callable, optional): A function/transform that takes in the
            target and transforms it.
        loader (callable, optional): A function to load an video given its path and frame indices.
     Attributes:
        classes (list): List of the class names.
        class_to_idx (dict): Dict with items (class_name, class_index).
        imgs (list): List of (image path, class_index) tuples
    """

    def __init__(self,
                 root_path,
                 split,
                 spatial_transform=None,
                 target_transform=None,
                 joint_transform=None,
                 clip_transform=None,
                 sample_duration=16):
        root_path = root_path + split + '/'
        # print('root_path', root_path)
        self.data = make_dataset(root_path)
        self.split = split
        self.sample_duration = sample_duration

        self.spatial_transform = spatial_transform
        self.target_transform = target_transform
        self.joint_transform = joint_transform
        self.clip_transform = clip_transform
        self.loader = get_default_video_loader()
        self.loader_mask = get_default_mask_video_loader()

    def __getitem__(self, index):
        """
        Args:
            index (int): Index
        Returns:
            tuple: (image, target) where target is class_index of the target class.
        """
        path = self.data[index]['video']

        vid_len = self.data[index]['n_frames']
        sample_duration = self.sample_duration
        start_point = random.randint(0, vid_len - sample_duration)

        reference_point = random.randint(0, start_point)

        frame_indices = list(range(start_point, start_point + sample_duration))
        # print('index', frame_indices)
        frame_set = self.data[index]['frame_set']
        sel_names = [frame_set[i] for i in frame_indices]

        reference_sel_names = [frame_set[reference_point]]

        clip = self.loader(path, sel_names)

        reference_clip = self.loader(path, reference_sel_names)

        path_mask = path.replace(self.split, self.split+'annot')

        groundtruth = self.loader_mask(path_mask, sel_names)

        reference_mask = self.loader_mask(path_mask, reference_sel_names)

        if self.spatial_transform is not None:
            self.spatial_transform.randomize_parameters()
            clip = [self.spatial_transform(img) for img in clip]
            reference_clip = [self.spatial_transform(img) for img in reference_clip]

        if self.target_transform is not None:
            groundtruth = [self.target_transform(img) for img in groundtruth]
            reference_mask = [self.target_transform(img) for img in reference_mask]

        if self.joint_transform is not None:
            clip = [self.joint_transform(img) for img in clip]
            reference_clip = [self.joint_transform(img) for img in reference_clip]
            groundtruth = [self.joint_transform(img) for img in groundtruth]
            reference_mask = [self.joint_transform(img) for img in reference_mask]

        if self.clip_transform is not None:
            clip = [self.clip_transform(img) for img in clip]

        clip = torch.stack(clip, 0).permute(1, 0, 2, 3)
        reference_clip = torch.stack(reference_clip, 0).permute(1, 0, 2, 3)
        reference_clip = reference_clip.expand([-1, 16, -1, -1])

        reference_mask = torch.stack(reference_mask, 0).permute(1, 0, 2, 3)
        reference_mask = reference_mask.expand([-1, 16, -1, -1])
        groundtruth = torch.stack(groundtruth, 0).permute(1, 0, 2, 3)


        clip_new = torch.cat((reference_clip, reference_mask, clip), 0)

        return clip_new, groundtruth


    def __len__(self):
        return len(self.data)


class UCF101_test(data.Dataset):
    """
    Args:
        root (string): Root directory path.
        spatial_transform (callable, optional): A function/transform that  takes in an PIL image
            and returns a transformed version. E.g, ``transforms.RandomCrop``
        temporal_transform (callable, optional): A function/transform that  takes in a list of frame indices
            and returns a transformed version
        target_transform (callable, optional): A function/transform that takes in the
            target and transforms it.
        loader (callable, optional): A function to load an video given its path and frame indices.
     Attributes:
        classes (list): List of the class names.
        class_to_idx (dict): Dict with items (class_name, class_index).
        imgs (list): List of (image path, class_index) tuples
    """

    def __init__(self,
                 root_path,
                 split,
                 spatial_transform=None,
                 target_transform=None,
                 sample_duration=16):
        root_path = root_path + split + '/'
        # print('root_path', root_path)
        self.data = make_dataset(root_path)
        self.split = split
        self.sample_duration = sample_duration

        self.spatial_transform = spatial_transform
        self.target_transform = target_transform
        self.loader = get_default_video_loader()
        # self.loader_mask = get_default_video_loader(is_mask=True)

    def gen_indexes(self, vid_length, sample_duration):
        ind_sets = list()
        begin_ind = 0
        end_ind = sample_duration
        while end_ind < vid_length:
            ind_sets.append(list(range(begin_ind, end_ind)))
            begin_ind = end_ind
            end_ind += sample_duration
        ind_sets.append(list(range(vid_length - sample_duration, vid_length)))
        return ind_sets

    def __getitem__(self, index):
        """
        Args:
            index (int): Index
        Returns:
            tuple: (image, target) where target is class_index of the target class.
        """
        path = self.data[index]['video']
        name_video = self.data[index]['video_id']
        names_frames = self.data[index]['frame_set']

        vid_len = self.data[index]['n_frames']
        sample_duration = self.sample_duration

        ind_sets = self.gen_indexes(vid_len, sample_duration)
        clips_set = list()
        for frame_indices in ind_sets:
            # print('index', frame_indices)
            frame_set = self.data[index]['frame_set']
            sel_names = [frame_set[i] for i in frame_indices]

            clip = self.loader(path, sel_names)

            if self.spatial_transform is not None:
                self.spatial_transform.randomize_parameters()
                clip = [self.spatial_transform(img) for img in clip]
            clip = torch.stack(clip, 0).permute(1, 0, 2, 3)
            # print('type(clip):', type(clip))
            clips_set.append(clip)

        return clips_set, name_video, names_frames


    def __len__(self):
        return len(self.data)


def get_training_set(opt, spatial_transform, target_transform, joint_transform, clip_transform):
    video_path, sample_duration = opt
    training_data = UCF101(
        root_path=video_path,
        split='train',
        spatial_transform=spatial_transform,
        target_transform=target_transform,
        joint_transform=joint_transform,
        clip_transform=clip_transform,
        sample_duration=sample_duration)

    return training_data


def get_validation_set(opt, spatial_transform, target_transform, joint_transform=None, clip_transform=None):
    video_path, sample_duration = opt
    validation_data = UCF101(
        root_path=video_path,
        split='val',
        spatial_transform=spatial_transform,
        target_transform=target_transform,
        joint_transform=joint_transform,
        clip_transform=clip_transform,
        sample_duration=sample_duration)
    return validation_data


def get_test_set(opt, spatial_transform, target_transform, split):
    video_path, sample_duration = opt
    test_data = UCF101_test(
        root_path=video_path,
        split=split,
        spatial_transform=spatial_transform,
        target_transform=target_transform,
        sample_duration=sample_duration)
    return test_data
