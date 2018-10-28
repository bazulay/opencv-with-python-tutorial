import numpy as np
import cv2

im1 = cv2.imread('../images/samurai.jpeg')
im2 = cv2.imread('../images/china.jpeg')
dst = cv2.addWeighted(im1,0.7,im2,0.3,0)
cv2.imshow('im1',im1)
cv2.imshow('im2',im2)
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
