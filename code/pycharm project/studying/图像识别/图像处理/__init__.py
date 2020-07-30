import cv2
import numpy as np

s = np.array([[0.5,0,0],[0,0.5,0],[0,0,1]])
t = np.array([[1,0,100],[0,1,200],[0,0,1]])

A = np.dot(t,s)#这里不能理解为点乘，而应该理解为矩阵的乘法
print(A)