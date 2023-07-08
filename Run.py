from VideoDiff import *

if __name__ == '__main__':
    file_path1 = 'C:/Users/xiaoli/Desktop/test1.mp4'
    file_path2 = 'C:/Users/xiaoli/Desktop/test3.mp4'
    t = VideoDiff(file_path1,file_path2,12)
    a=t.videoDiff()
    print(a)
    for key, value in a.items():
        if key <= 0.99:
            print( "两视频第%.1f秒抽帧,对比度为：%s,对比出现diff" %(key,value))
        else:
            print( "两视频第%.1f秒抽帧,对比度为：%s,对比相同" %(key,value))