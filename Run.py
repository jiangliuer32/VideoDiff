from VideoDiff import *

if __name__ == '__main__':
    videoPathA = '视频A路径'
    videoPathB = '视频B路径'
    diffNumber = 12 #视频抽取图片数。抽取规则：根据视频时常，平均取时间点抽取图片，例如：时常12秒，抽取12次数，固每秒抽取一次
    diff = VideoDiff(videoPathA,videoPathB,diffNumber)
    result = diff.videoDiff()
    print(result)
    for key, value in result.items():
        if value <= 0.96:
            print("对比出现diff:两视频第%.1f秒抽帧,对比度为：%s" %(key,value))
        else:
            print("对比相同:两视频第%.1f秒抽帧,对比度为：%s" %(key,value))