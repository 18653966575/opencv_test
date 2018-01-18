import cv2

print("--------- Test OpenCV ---------")

src = cv2.imread("D:/a.jpg", cv2.IMREAD_GRAYSCALE)
cv2.namedWindow("input image", cv2.WINDOW_AUTOSIZE)
cv2.imshow("input image", src)
cv2.waitKey()
cv2.destroyAllWindows()
print("--------- End Test ---------")
