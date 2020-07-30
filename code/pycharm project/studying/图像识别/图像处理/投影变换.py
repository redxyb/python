#假如（0，0） （200，0） （0，200） （200，200） 原坐标
#（100，20） （200，20） （50，70） （250，70） 投影变换的矩阵
import cv2
import numpy as np

img = cv2.imread("图像处理/1.jpg", cv2.IMREAD_COLOR)
#得到三个颜色通道的值
b = img[:,:,0]
g = img[:,:,1]
r = img[:,:,2]

cv2.imshow("yt",img)
cv2.imshow("blue",b)
cv2.imshow("green",g)
cv2.imshow("red",r)

cv2.waitKey(0)#暂停能看到图片
cv2.destroyAllWindows()#释放资源

# src = np.array([[0,0],[200,0],[0,200],[200,200]],np.float32)#只支持32维数据
# dst = np.array([[100,20],[200,20],[50,70],[250,70]],np.float32)
#
# p = cv2.getPerspectiveTransform(src,dst)#投影矩阵
# print(p)
# print(type(p))
# print(p.dtype)
#
# cv2.warpPerspective()