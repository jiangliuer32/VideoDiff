from VideoDiff import *

if __name__ == '__main__':
    vadeoPathA = 'C:/Users/xiaoli/Desktop/1.mp4'
    vadeoPathB = 'C:/Users/xiaoli/Desktop/test2.mp4'
    diffNumber = 12 #视频抽取图片数。抽取规则：根据视频时常，平均取时间点抽取图片，例如：时常12秒，抽取12次数，固每秒抽取一次
    t = VideoDiff(vadeoPathA,vadeoPathB,diffNumber)
    a=t.videoDiff()
    print(a)
    for key, value in a.items():
        if value <= 0.96:
            print("对比出现diff:两视频第%.1f秒抽帧,对比度为：%s" %(key,value))
        else:
            print("对比相同:两视频第%.1f秒抽帧,对比度为：%s" %(key,value))