from airtest.aircv.cal_confidence import *
import cv2


img_1_path='C:/Users/xiaoli/Desktop/ima/test.jpg'
img_2_path='C:/Users/xiaoli/Desktop/ima/test3.jpg'

# image_array1 = numpy.asarray(bytearray(img_1_path), dtype="uint8")
# image_array2 = numpy.asarray(bytearray(img_2_path), dtype="uint8")


# img1 = cv2.imdecode(img_1_path, cv2.IMREAD_COLOR)
# img2 = cv2.imdecode(img_2_path, cv2.IMREAD_COLOR)


img1 = cv2.resize(cv2.imread(img_1_path), (370, 800))  # 图片尺寸根据实际图片写入
img2 = cv2.resize(cv2.imread(img_2_path), (370, 800))
print(type(img1))
confidence = cal_ccoeff_confidence(img1, img2)

print(confidence)