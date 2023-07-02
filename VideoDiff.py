import VideoInfo

class VideoDiff(VideoInfo):
    def int__(self,inFile,outFile,duration):
        super().__init__(inFile, outFile)
        self.duration = duration

    def videoDiff(self,videoA,videoB):

