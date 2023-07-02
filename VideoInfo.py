import ffmpeg
import numpy
import cv2
import sys
import random
import math



def read_frame_by_time(in_file, time):
    """
    指定时间节点读取任意帧
    """
    out, err = (
        ffmpeg.input(in_file, ss=time)
              .output('pipe:', vframes=1, format='image2', vcodec='mjpeg')
              .run(capture_stdout=True)
    )
    # image_array = numpy.asarray(bytearray(out), dtype="uint8")
    # image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
    # cv2.imshow('frame', image)
    # cv2.inweite('C:/Users/xiaoli/Desktop/VID20230702033914.mp4','test')
    # cv2.waitKey()
    return out


def get_video_info(in_file):
    """
    获取视频基本信息
    """
    try:
        probe = ffmpeg.probe(in_file)
        video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
        if video_stream is None:
            print('No video stream found', file=sys.stderr)
            sys.exit(1)
        return video_stream
    except ffmpeg.Error as err:
        print(str(err.stderr, encoding='utf8'))
        sys.exit(1)

if __name__ == '__main__':
    file_path = 'C:/Users/xiaoli/Desktop/VID20230702033914.mp4'
    video_info = get_video_info(file_path)
    total_duration = video_info['duration']
    print('总时间：' + total_duration + 's')
    random_time = random.randint(1, int(float(total_duration)) - 1) + random.random()
    print('随机时间：' + str(random_time) + 's')
    out = read_frame_by_time(file_path, random_time)
    print(type(out))
    image_array = numpy.asarray(bytearray(out), dtype="uint8")
    print(type(image_array))
    image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
    cv2.imshow('frame', image)
    cv2.imwrite('C:/Users/xiaoli/Desktop/test2.jpg',image)
    cv2.waitKey()