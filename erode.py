#coding:gbk
'''
��̬ѧת��--���͡������㡢������
'''
import cv2
import numpy as np

img = cv2.imread('E:\j.png',0)
kernel = np.ones((5,5),np.uint8)
#����
erosion = cv2.erode(img,kernel,iterations = 1)

#�����㣺�ȸ�ʴ������
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

#�����㣺�������ٸ�ʴ
closingImg = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

#��̬ѧ�ݶ�
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)


cv2.imshow("����", erosion)
cv2.imshow("������",opening)
cv2.imshow("������",closingImg)
cv2.imshow("�ݶ�",gradient)
cv2.waitKey()
cv2.destroyAllWindows()
