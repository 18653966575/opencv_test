"""
获取图片信息
"""
import cv2
import numpy as np

img=cv2.imread('E:/a.jpg')

#形状（行，列，深度？）
print(img.shape)
#像素数目
print(img.size)
#数据类型
print(img.dtype)
