import cv2
import numpy as np
img = cv2.imread('../images/smiley.jpg')
img[200:350, 150:300] = img[0,0]
cv2.imshow('smiley', img)
cv2.imwrite('../images/smiley_minus_roi.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
