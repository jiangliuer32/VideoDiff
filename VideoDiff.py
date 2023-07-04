from VideoInfo import VideoInfo
import numpy
import math
import cv2


class VideoDiff():
    def __init__(self,inFileA,inFileB,outFile,duration):
        self.inFileA = inFileA
        self.inFileB = inFileB
        self.outFile = outFile
        self.duration = duration

    def videoDiff(self):
        videoA = VideoInfo(self.inFileA)
        infoA  = videoA.getVideoInfo()

        videoB = VideoInfo(self.inFileB)
        infoB  = videoB.getVideoInfo()

        if math.floor(infoB['duration']) != math.floor(infoA['duration']):
            print("视频时长不相等")
        else:
            vDuration = math.floor(infoA['duration'])%self.duration

            for i in (1,vDuration+1):
                time = time + vDuration
                out = videoA.getframeByTime(time)

                image_array = numpy.asarray(bytearray(out), dtype="uint8")
                image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
                outFile = outFile + "\\" + str(i) + ".img"
                cv2.inweite(self.outFile, image)

                img1 = cv2.resize(cv2.imread(image), (370, 800))  # 图片尺寸根据实际图片写入
                img2 = cv2.resize(cv2.imread(image), (370, 800))



