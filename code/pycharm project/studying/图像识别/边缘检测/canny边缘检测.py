import cv2
'''边缘检测'''
src = cv2.imread("1.jpg")

canny = cv2.Canny(src,100,250)

cv2.imshow("yt",src)
cv2.imshow("canny",canny)

cv2.waitKey(0)
cv2.destroyWindow()