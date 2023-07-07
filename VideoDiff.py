from VideoInfo import VideoInfo
from airtest.aircv.cal_confidence import *
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
        diffResult=[] #存储diff结果
        videoA = VideoInfo(self.inFileA)
        infoA  = videoA.getVideoInfo()

        videoB = VideoInfo(self.inFileB)
        infoB  = videoB.getVideoInfo()

        if math.floor(infoB['duration']) != math.floor(infoA['duration']):
            print("视频时长不相等")
        else:
            vDuration = math.floor(infoA['duration'])%self.duration #根据输入 选择截取图片次数

            for i in (1,vDuration+1):
                time = time + vDuration

                outA = videoA.getframeByTime(time)
                image_array = numpy.asarray(bytearray(outA), dtype="uint8")
                imageA = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
                heightA, widthA, channels = imageA.shape
                #wideA =

                outB = videoB.getframeByTime(time)
                image_array = numpy.asarray(bytearray(outB), dtype="uint8")
                imageB = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
                heightB, widthB, channels = imageB.shape

                # outFile = outFile + "\\" + str(i) + ".img"
                # cv2.inweite(self.outFile, image)

                img1 = cv2.resize(cv2.imread(imageA), (heightA, widthA))  # 图片尺寸根据实际图片写入
                img2 = cv2.resize(cv2.imread(imageB), (heightB, widthB))
                confidence = cal_ccoeff_confidence(img1, img2)

                if confidence < 95:
                    print("视频校验失败")
                    diffResult.append(confidence)
                else:
                    diffResult.append(confidence)

