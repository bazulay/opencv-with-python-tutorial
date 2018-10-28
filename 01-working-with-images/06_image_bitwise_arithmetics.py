import cv2
import numpy as np

#loading 2 images
img1 = cv2.imread('../images/samurai.jpeg')
cv2.imshow('1 orig image', img1)

img2 = cv2.imread('../images/opencv-logo.png')
cv2.imshow('2 orig logo', img2)

#find the logo image dimentions
rows, cols, channels = img2.shape

#defining region of interest at the size of the logo 
#on the upper left side of img1 
roi = img1[0:rows, 0:cols ]

#converting the logo to grayscale
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
cv2.imshow('3 logo converted to grayscale', img2gray)

#creating a mask with the threshold function
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
cv2.imshow('4 mask', mask)

#now creating the inverted mask
mask_inv = cv2.bitwise_not(mask)
cv2.imshow('5 mask inverted', mask_inv)


#now black-out the area of logo in ROI
roi_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
cv2.imshow('6 roi bckground', roi_bg)


#take only region of logo from logo image.
roi_fg = cv2.bitwise_and(img2, img2, mask=mask)
cv2.imshow('7 roi foregroung ', roi_fg)

#summing up roi background with roi forgroung
dst = cv2.add(roi_bg, roi_fg)
cv2.imshow('8 adding the roi gg to fg', dst)

#replacing the corresponding area in the original image 
img1[0:rows, 0:cols ] = dst
cv2.imshow('9 result', img1)

cv2.waitKey(0)
cv2.destroyAllWindows()


