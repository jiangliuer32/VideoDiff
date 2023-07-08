from VideoInfo import *
from airtest.aircv.cal_confidence import *
import numpy
import math
import cv2
import sys
class VideoDiff():
    def __init__(self,inFileA,inFileB,diffNumber):
        """
        :param inFileA:A视频路径
        :param inFileB:B视频路径
        :param diffNumber: 抽帧次数
        """
        self.inFileA = inFileA
        self.inFileB = inFileB
        #self.outFile = outFile
        self.diffNumber = diffNumber

    def videoDiff(self):
        """
        视频抽帧比较
        :return: 字典形式返回对比数据
        """
        diffResult={}
        #获取A视频信息
        videoA = VideoInfo(self.inFileA)
        infoA  = videoA.getVideoInfo()
        videoLengthA=round(float(infoA['duration']),2)

        #获取B视频信息
        videoB = VideoInfo(self.inFileB)
        infoB  = videoB.getVideoInfo()
        videoLengthB=round(float(infoB['duration']),2)

        #1.优先判断视频时常是否相等 2.抽帧对比结果
        if  videoLengthA != videoLengthB:
            print("视频时长不相等,A视频：%s秒,B视频：%s秒" %(videoLengthA,videoLengthB))
            sys.exit()
        else:
            timeInterval = round(math.floor(videoLengthA)/self.diffNumber,1) #根据输入抽帧频率,判断截取时间间隔
            time = timeInterval

            for i in range(1,self.diffNumber+1):
                outA = videoA.getframeByTime(time)
                image_array = numpy.asarray(bytearray(outA), dtype="uint8")
                imageA = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

                outB = videoB.getframeByTime(time)
                image_array = numpy.asarray(bytearray(outB), dtype="uint8")
                imageB = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

                #使用算法对比
                confidence = cal_ccoeff_confidence(imageA, imageB)
                diffResult[time] = confidence
                time += timeInterval

        return diffResult
