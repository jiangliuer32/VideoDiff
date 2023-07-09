from VideoDiff import *

if __name__ == '__main__':
    #输入运行参数
    videoPathA = '视频路径A'
    videoPathB = '视频路径B'
    diffNumber = 12 #视频抽取图片数。抽取规则：根据视频时常，平均取时间点抽取图片，例如：时常12秒，抽取12次数，固每秒抽取一次
    threshold = 0.96 #diff相似度阈值，根据需要自行调整，1为最大值

    diff = VideoDiff(videoPathA,videoPathB,diffNumber)
    result = diff.videoDiff()
    print(result) #字典：key：瞅着时间点 value：对比图
    for key, value in result.items():
        if value <= threshold:
            print("对比出现diff:两视频第%.1f秒抽帧,对比度为：%s" %(key,value))
        else:
            print("对比相同:两视频第%.1f秒抽帧,对比度为：%s" %(key,value))



