import numpy as np
import cv2
# load the image 
image = cv2.imread("images.jpg")
main = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (47,47), 0)
(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
image = main.copy()
cv2.circle(image, maxLoc,47, (255,0, 0), 10)
im=cv2.resize(image, (960,800))
cv2.imshow("Output",im)
cv2.waitKey(0)