import cv2
import numpy as np
src = cv2.imread("1.jpg", cv2.IMREAD_GRAYSCALE)

h , w = src.shape
#仿射变换，图片缩小两倍
A1 = np.array([[0.5,0,0],
              [0,0.5,0]],np.float32)
d1 = cv2.warpAffine(src,A1,(w,h),borderValue=125)#图片，仿射矩阵，大小，填充模式


#限缩小后平移
A2 = np.array([[0.5,0,w/4],
              [0,0.5,h/4]],np.float32)
d2 = cv2.warpAffine(src,A2,(w,h),borderValue=125)#图片，仿射矩阵，大小，填充模式

#在d2的基础上，绕图像的中心旋转
A3 = cv2.getRotationMatrix2D((w/2,h/2),30,1)#绕中心旋转30度
d3 = cv2.warpAffine(src,A3,(w,h),borderValue=125)

#简单的3个角度旋转
xz90 = cv2.rotate(src,cv2.ROTATE_90_COUNTERCLOCKWISE)#逆时针旋转90
xz_90 = cv2.rotate(src,cv2.ROTATE_90_CLOCKWISE)#顺时针旋转90
xz_180 = cv2.rotate(src,cv2.ROTATE_180)#旋转180

cv2.imshow("YT",src)
cv2.imshow("SXPY",d2)
cv2.imshow("SX",d1)
cv2.imshow("XZ",d3)
cv2.imshow("xz90",xz90)
cv2.imshow("xz_90",xz_90)
cv2.imshow("xz_180",xz_180)


cv2.waitKey(0)#暂停能看到图片
cv2.destroyAllWindows()#释放资源