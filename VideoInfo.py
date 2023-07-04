import ffmpeg
import numpy
import cv2
import sys
import random
from airtest.aircv.cal_confidence import *

class VideoInfo:
    def __init__(self,inFile):
        self.inFile = inFile

    def getframeByTime(self,time):
        """
        指定时间节点读取任意帧
        """
        out, err = (
            ffmpeg.input(self.inFile, ss=time)
                  .output('pipe:', vframes=1, format='image2', vcodec='mjpeg')
                  .run(capture_stdout=True)
        )
        return out


    def getVideoInfo(self):
        """
        获取视频基本信息
        """
        probe = ffmpeg.probe(self.inFile)
        video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
        if video_stream is None:
            print('没有找到视频信息', file=sys.stderr)
            sys.exit(1)
        return video_stream


if __name__ == '__main__':
    t = VideoInfo()








    file_path = 'C:/Users/xiaoli/Desktop/VID20230702033914.mp4'
    video_info = get_video_info(file_path)
    width = int(video_stream['width'])
    height = int(video_stream['height'])
    total_duration = video_info['duration']
    print('总时间：' + total_duration + 's')
    random_time = random.randint(1, int(float(total_duration)) - 1) + random.random()
    print('随机时间：' + str(random_time) + 's')
    out = read_frame_by_time(file_path, random_time)
    print(type(out))
    image_array = numpy.asarray(bytearray(out), dtype="uint8")
    print(type(image_array))
    image_array = numpy.asarray(bytearray(out), dtype="uint8")
    image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
    cv2.inweite(self.outFile, image)
