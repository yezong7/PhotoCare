import cv2

img = cv2.imread("img/bingbing_is_mine.jpg")

imgCropped = img[0:200, 200:400]

cv2.imshow("imgBefore",img)
cv2.imshow("imgAfter",imgCropped)

cv2.waitKey(0)
cv2.destroyAllWindows()
