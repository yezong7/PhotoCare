import cv2
import  numpy as np

img = cv2.imread("img/bingbing_is_mine.jpg")
kernel = np.ones((5,5),np.uint8)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(5,5),0)
imgCanny = cv2.Canny(imgBlur,50,100)

imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
imgEroded = cv2.erode(imgDialation,kernel,iterations=1)

cv2.imshow("imgBefore",imgCanny)
cv2.imshow("imgAfter1",imgDialation)
cv2.imshow("imgAfter2",imgEroded)
cv2.waitKey(0)
cv2.destroyAllWindows()
