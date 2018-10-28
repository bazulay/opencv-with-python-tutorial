import numpy as np
import cv2

im1 = cv2.imread('../images/samurai.jpeg')
im2 = cv2.imread('../images/china.jpeg')
im3 = im1 + im2
cv2.imshow('im1',im1)
cv2.imshow('im2',im2)
cv2.imshow('im3',im3)
cv2.waitKey(0)
cv2.destroyAllWindows()
print("im3.max() = {}".format(im3.max()))
