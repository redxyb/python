import cv2
import numpy as np
from scipy import signal

#定义roberts函数
def Roberts(I,_boundary="full",_fillvalue = 0):
    #获取图片的尺寸
    H1,W1 = I.shape[0:2]
    #定义算子的尺寸
    H2,W2 = 2,2

    #进行45度方向的卷积
    #1.定义卷积和
    R1 = np.array([[1,0],[0,-1]],np.float32)
    #2.定义锚点位置
    kr1,kc1 = 0,0

    #进行135度卷积
    R2 = np.array([[1, 0], [0, 1]], np.float32)
    kr2, kc2 = 0, 0

    #卷积的计算
    IConR1 = signal.convolve2d(I,R1,mode="full",boundary=_boundary,fillvalue=_fillvalue)
    IConR2 = signal.convolve2d(I,R2,mode="full",boundary=_boundary,fillvalue=_fillvalue)

    #截取得到same卷积
    IConR1 = IConR1[H2-kr1-1:H1+H2-kr1-1,W2-kc1-1:W1+W2-kc1-1]
    IConR2 = IConR2[H2-kr2-1:H1+H2-kr2-1,W2-kc2-1:W1+W2-kc2-1]
    return (IconR1,IConR1)

if __name__ == '__main__':
    # 读取照片
    image = cv2.imread("1.jpg",flags=0)
    cv2.imshow("yt",image)

    IconR1 = Roberts(image,"symm")

    #取图片数组的各个值的绝对值
    IconR1 = np.abs(IconR1)

    #RGB图像的位深为8位
    edge45 = IconR1.astype(np.uint8)
    cv2.namedWindow("edge45",cv2.WINDOW_NORMAL)
    cv2.imshow("edge45",edge45)

    

    cv2.waitKey(0)
    cv2.destroyWindow()

