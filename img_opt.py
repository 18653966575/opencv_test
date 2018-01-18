"""
获取图片信息1234567
"""

import cv2
import numpy as np
img=cv2.imread('E:/a.jpg')

# px=img[100,100]
# print(px)EE
# blue=img[100,100,0]EE
# print(blue)

#形状（行，列，深度？）
print(img.shape)
#像素数目
print(img.size)
#数据类型
print(img.dtype)
