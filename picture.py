"""
Created on Sun Jan 5 14:59:58 2014
@author: duan
"""

import numpy as np
import cv2

# 创建黑色的画布
img = np.zeros((512, 512, 3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
#画一条对角线
cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)

#画一个矩形
cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)

#画一个圆
cv2.circle(img,(447,63), 63, (0,0,255), -1)

#画一个椭圆
cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

#写字
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2)

cv2.imshow("input image", img)
cv2.waitKey()
cv2.destroyAllWindows()



