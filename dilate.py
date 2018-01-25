'''
形态学转换--腐蚀
前景物体的边界腐蚀掉
'''

import cv2
import numpy as np

img = cv2.imread('E:\j.png',0)
kernel = np.ones((5,5),np.uint8)
#腐蚀
dilation = cv2.dilate(img,kernel,iterations = 1)

cv2.imshow("res", dilation)
cv2.waitKey()
cv2.destroyAllWindows()
