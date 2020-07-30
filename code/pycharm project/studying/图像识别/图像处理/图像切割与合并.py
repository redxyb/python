import cv2
import numpy as np

#图像切割与合并
def cut_img(image):
    #切割
    src_cut = image[100:200,150:250]#两个切片差值保持一致
    cv2.imshow("cut_img",src_cut)

    #合并
    image[50:150,50:150] = src_cut#两个切片差值保持一致
    cv2.imshow("unicon",image)

src = cv2.imread("1.jpg")
#print(src.shape)

cv2.imshow("yt", src)
cut_img(src)

cv2.waitKey(0)
cv2.destroyWindow()