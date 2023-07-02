from airtest.aircv.cal_confidence import *

def makeFolderResult(imgPath, logName):
    logFloder = os.path.join(imgPath, f'图片对比结果')
    os.mkdir(logFloder)
    logPath = os.path.join(imgPath, f'图片对比结果/{logName}')
    return logPath

def wirteLog(msg, logPath):
    with open(logPath, "a+", encoding='utf-8') as f:
        f.write(msg)
        f.write("\n")

def imageCompare(imagePath, logPath,threshold:int):
    '''
    :param imagePath: 图片存放的路径
    :param logPath: 日志存放的路径
    :param threshold: 阈值,指定int类型
    :return:
    '''
    needCompareImgDict = {}
    for root, dirs, files in os.walk(imagePath):
        for file in files:
            if "_" in file:
                key = str(file).split("_")[0]
                if key not in needCompareImgDict.keys():
                    needCompareImgDict[key] = [os.path.join(root, file)]
                else:
                    tempList = needCompareImgDict[key]
                    tempList.append(os.path.join(root, file))
                    needCompareImgDict[key] = tempList
    #### 遍历字典,将同个ID下的图片进行对比
    for imgs in needCompareImgDict.values():
        for i in range(len(imgs) - 1):
            img_1_path = imgs[i]
            img_2_path = imgs[i + 1]
            img_1_Name = img_1_path.split("\\")[-1]
            img_2_Name = img_2_path.split("\\")[-1]
            img1 = cv2.resize(cv2.imread(img_1_path), (370, 800)) # 图片尺寸根据实际图片写入
            img2 = cv2.resize(cv2.imread(img_2_path), (370, 800))
            confidence = cal_ccoeff_confidence(img1, img2)
            if confidence > threshold:
                writeMsg = f"【对比失败】,疑似 {img_1_Name}  与  {img_2_Name} 两张图片一致,相似度为：{round(confidence * 100, 2)}%"
                wirteLog(writeMsg, logPath)
                print(writeMsg)
            else:
                pass

if __name__ == '__main__':
    imagePath = "填入你图片存放的路径"
    logName = str(imagePath.split("\\")[-1]) + ".txt"
    logPath = makeFolderResult(imagePath, logName)
    imageCompare(imagePath, logPath)
