import cv2
import numpy as np

img = cv2.imread('images/opencv-logo.png', -1)
print ("type(img) = {}".format(type(img)))
print ("len(img) = {}".format(len(img)))
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
