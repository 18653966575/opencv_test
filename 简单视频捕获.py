import cv2
import numpy as np
cap=cv2.VideoCapture(0)

while(1):
    ret,frame=cap.read() #注意，前面必须两个声明，用逗号隔开！！！

    # 显示图像
    cv2.imshow('frame',frame)

    k=cv2.waitKey(5)&0xFF
    if k==27: #ESC键盘退出
        break

# 关闭窗口
cv2.destroyAllWindows()
