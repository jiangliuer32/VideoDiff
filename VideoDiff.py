from VideoInfo import VideoInfo
import math
class VideoDiff():
    def __init__(self,inFileA,inFileB,duration):
        self.inFileA = inFileA
        self.inFileB = inFileB
        self.duration = duration

    def videoDiff(self):
        videoA = VideoInfo(self.inFileA)
        videoB = VideoInfo(self.inFileB)
        infoA  = videoA.getVideoInfo()
        infoB  = videoB.getVideoInfo()

        if infoB['duration'] ==

