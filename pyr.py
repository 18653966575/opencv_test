'''
图像金字塔
'''

import cv2
import matplotlib.pyplot as plt

img = cv2.imread('a.jpg',0) #直接读为灰度图像
img1 = cv2.pyrDown(img)
img2 = cv2.pyrDown(img1)
img3 = cv2.pyrDown(img2)

img4 = cv2.pyrUp(img3)
# cv2.imshow('org',img)
# cv2.imshow('res',img1)
# cv2.waitKey()
# cv2.destroyAllWindows()
# exit()
plt.subplot(131),plt.imshow(img,'gray')
plt.subplot(132),plt.imshow(img3,'gray')
plt.subplot(133),plt.imshow(img4,'gray')
plt.show()
