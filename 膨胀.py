#coding:gbk
'''
形态学转换--膨胀、开运算、闭运算
'''
import cv2
import numpy as np

img = cv2.imread('E:\j.png',0)
kernel = np.ones((5,5),np.uint8)
#膨胀
erosion = cv2.erode(img,kernel,iterations = 1)

#开运算：先腐蚀再膨胀
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

#闭运算：先膨胀再腐蚀
closingImg = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

#形态学梯度
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)


cv2.imshow("膨胀", erosion)
cv2.imshow("开运算",opening)
cv2.imshow("闭运算",closingImg)
cv2.imshow("梯度",gradient)
cv2.waitKey()
cv2.destroyAllWindows()
