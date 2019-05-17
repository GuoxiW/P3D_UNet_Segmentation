import os
import numpy as np
import copy
import pickle
from preprocess.thumos14.extract_frames import Extractor


class RoIdb():

    def __init__(self, split, length, min_length, fps, overlap_th, frame_dir):
        self.split = split
        self.length = length
        self.min_length = min_length
        self.fps = fps
        self.overlap_th = overlap_th
        self.frame_dir = frame_dir
        self.meta_dir = os.path.join(frame_dir, 'annotation_')
        self.video_path = os.path.join(self.frame_dir, self.split)
        self.step = int(self.length / 4)
        self.window = self.length

    def get_segment(self):
        '''
        ## This should be improved ##
        '''
        ext = '.mp4'
        video_dir = '/data/guoxi/BasicDataset/THUMOS2014/val'
        extractor = Extractor(self.fps, ext, self.split, video_dir, self.frame_dir, use_ambiguous=False)
        segment = extractor.annotation_parser()
        return segment

    def rm_less_length(self, db):
        duration = db[:, 1] - db[:, 0]
        db = db[duration >= self.min_length]
        return db

    def rm_less_overlap(self, db, start, end):
        ## not *1.0
        time_in_wins = np.minimum(end, db[:, 1]) - np.maximum(start, db[:, 0])
        overlap = time_in_wins / (db[:, 1] - db[:, 0])
        assert min(overlap) >= 0
        assert max(overlap) <= 1
        db = db[overlap >= self.overlap_th]
        return db

    def roi_dict(self, video, start, end, stride, rois=None):
        data = {}
        data['flipped'] = False
        data['frames'] = np.array([[0, start, end, stride]])
        data['bg_name'] = os.path.join(self.frame_dir, self.split, video)
        data['fg_name'] = os.path.join(self.frame_dir, self.split, video)

        if self.split == 'val':
            data['wins'] = (rois[:, :2] - start) / stride # why '- start'?
            data['durations'] = data['wins'][:, 1] - data['wins'][:, 0]
            data['gt_classes'] = rois[:, 2]
            data['max_classes'] = rois[:, 2]
            data['max_overlaps'] = np.ones(len(rois))
        # check last image file
        last_image_file = os.path.join(self.frame_dir, self.split, video, 'image_' + str(end - 1).zfill(5) + '.jpg')
        assert os.path.isfile(last_image_file)
        return data

    def ana_rois(self, roidb, db, start, end, vid, flip):
        rois = db[np.logical_not(np.logical_or(db[:, 0] >= end, db[:, 1] <= start))]
        if len(rois) > 0:
            rois = self.rm_less_length(rois)
        if len(rois) > 0:
            rois = self.rm_less_overlap(rois, start, end)

        # append data
        if len(rois) > 0:
            rois[:, 0] = np.maximum(start, rois[:, 0])
            rois[:, 1] = np.minimum(end, rois[:, 1])

            stride = 1
            data = self.roi_dict(video=vid, start=start, end=end, stride=stride, rois=rois)
            roidb.append(data)

            if flip:
                data_flip = copy.deepcopy(data)
                data_flip['flipped'] = True
                roidb.append(data_flip)

    def gen_roidb(self, flip=False):
        roidb = list()

        if self.split == 'val':
            segment = self.get_segment()
        vid_list = os.listdir(self.video_path)
        for vid in vid_list:
            num_frame = len(os.listdir(os.path.join(self.video_path, vid)))
            if self.split == 'val':
                db = np.array(segment[vid])
                db[:, :2] = db[:, :2] * self.fps

            # forward
            for start in range(0, max(1, num_frame - self.length + 1), self.step):
                end = min(start + self.window, num_frame)
                if self.split == 'val':
                    self.ana_rois(roidb, db, start, end, vid, flip)
                else:
                    stride = 1
                    data = self.roi_dict(video=vid, start=start, end=end, stride=stride)
                    roidb.append(data)
                    if flip:
                        data_flip = copy.deepcopy(data)
                        data_flip['flipped'] = True
                        roidb.append(data_flip)

            # backward
            for end in range(num_frame, self.window - 1, -1 * self.step):
                start = end - self.window
                if self.split == 'val':
                    self.ana_rois(roidb, db, start, end, vid, flip)
                else:
                    ## Need improve
                    print('Test data do not need flip')

        return roidb


if __name__ == '__main__':
    split = 'val'
    length = 768
    min_length = 3
    fps = 25
    overlap_th = 0.7
    flip = True if split == 'val' else False
    filename = 'train_data_25fps_flipped.pkl' if split == 'val' else 'val_data_25fps.pkl'
    frame_dir = '/data1/guoxii/FRTAL/dataset/THUMOS14_frames'

    roidbor = RoIdb(split, length, min_length, fps, overlap_th, frame_dir)
    roidb = roidbor.gen_roidb(flip)
    pickle.dump(roidb, open(filename, 'wb'), pickle.HIGHEST_PROTOCOL)

    print('number of rois: {}'.format(len(roidb)))


