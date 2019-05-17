import os
from collections import defaultdict
import subprocess
import cv2


class Extractor():
    def __init__(self, fps, ext, split, video_dir, frame_dir, use_ambiguous=False, num_class=20):
        self.fps = fps
        self.ext = ext
        self.split = split
        self.video_dir = video_dir
        self.frame_dir = frame_dir
        self.use_ambiguous = use_ambiguous
        self.num_class = num_class
        self.meta_dir = os.path.join(self.frame_dir, 'annotation_')

    def id_and_name(self):
        '''
        parse detclasslist.txt, obtain class name and index
        '''
        # learn
        class_id = defaultdict(int)
        class_file = os.path.join(self.meta_dir+self.split, 'detclasslist.txt')
        with open(class_file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                # learn
                cid = int(line.strip().split()[0])
                cname = line.strip().split()[1]
                class_id[cname] = cid
        if self.use_ambiguous:
            class_id['Ambiguous'] = self.num_class + 1
        return class_id

    def record_annotation(self, segment):
        '''
        record annotation in txt file
        '''
        keys = list(segment.keys())
        keys.sort()
        with open('segment_annotation.txt', 'w') as f:
            for k in keys:
                f.write('{}\n{}\n\n'.format(k, segment[k]))

    def annotation_parser(self, show=False):
        class_id = self.id_and_name()
        segment = dict()

        for cname in class_id.keys():
            file = '{}_{}.txt'.format(cname, self.split)
            with open(os.path.join(self.meta_dir+self.split, file), 'r') as f:
                lines = f.readlines()
                for line in lines:
                    vid_name = line.strip().split()[0]
                    start_t = float(line.strip().split()[1])
                    end_t = float(line.strip().split()[2])

                    if vid_name in segment.keys():
                        segment[vid_name].append([start_t, end_t, class_id[cname]])
                    else:
                        # create initial list
                        segment[vid_name] = [[start_t, end_t, class_id[cname]]]
        # sort the segment according to start time
        for vid in segment.keys():
            segment[vid].sort(key=lambda x: x[0])

        # record segment annotation
        if show:
            self.record_annotation(segment)

        return segment

    def ffmpeg(self, filename, outfile, fps):
        command = ['ffmpeg', '-i', filename, '-q:v', '1', '-r', str(fps), outfile]
        pipe = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        pipe.communicate()

    def image_resize(self, filename, size=(171, 128)):
        # learn
        img = cv2.imread(filename, 100)
        # check
        img = cv2.resize(img, size, cv2.INTER_CUBIC)
        cv2.imwrite(filename, img, [100])

    def extract_frame(self, show=False):
        '''
        extract frames from video
        '''
        segment = self.annotation_parser(show)
        vid_list = segment.keys()

        for vid in vid_list:
            filename = os.path.join(self.video_dir, self.split, vid+self.ext)
            out_dir = os.path.join(self.frame_dir, self.split, vid)
            if not os.path.exists(out_dir):
                os.makedirs(out_dir)
            outfile = os.path.join(out_dir, 'image_%5d.jpg')
            self.ffmpeg(filename, outfile, self.fps)
            # resize to (171, 128)
            for name in os.listdir(out_dir):
                self.image_resize(os.path.join(out_dir, name))

            # show information
            num_frame = len(os.listdir(out_dir))
            print(filename, self.fps, num_frame)


if __name__ == '__main__':
    fps = 25
    ext = '.mp4'
    split = 'val'
    video_dir = '/data/guoxi/BasicDataset/THUMOS2014/val'
    frame_dir = '/data1/guoxii/FRTAL/dataset/test'

    extractor = Extractor(fps, ext, split, video_dir, frame_dir, use_ambiguous=False)
    extractor.extract_frame(show=True)
