import cv2
import numpy as np
#角点检测

def corner_image(image):
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray",gray)
    #cv2.cornerHarris()参数：src 图像，blockSize 领域大小，ksize窗口大小，k自由系数--0.04-0.06
    corners = cv2.cornerHarris(gray,7,5,0.04)
    