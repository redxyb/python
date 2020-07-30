import cv2
import numpy as np

def creat_img():
    img = np.ones([400,400,3],np.float32)
    img[:, :, 0] = img[:, :, 0] * 0
    img[:, :, 1] = img[:, :, 1] * 0
    img[:, :, 2] = img[:, :, 2] * 1

    cv2.imshow("creating",img)

creat_img()
cv2.waitKey(0)
cv2.destroyWindow()