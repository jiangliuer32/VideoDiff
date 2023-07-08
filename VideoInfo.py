import ffmpeg
class VideoInfo:
    """
    获取视频相关信息
    """
    def __init__(self,inFile):
        self.inFile = inFile

    def getframeByTime(self,time):
        """
        指定时间节点读取任意帧
        :param time: 指定时间点
        :return:
        """
        out, err = (
            ffmpeg.input(self.inFile, ss=time)
                  .output('pipe:', vframes=1, format='image2', vcodec='mjpeg')
                  .run(capture_stdout=True)
        )
        return out


    def getVideoInfo(self):
        """
        获取视频详细信息
        :return: 视频信息
        """
        #后期再写异常情况
        probe = ffmpeg.probe(self.inFile)
        video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
        return video_stream

