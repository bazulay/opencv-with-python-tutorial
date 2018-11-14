import numpy as np
import cv2

logo = cv2.imread('../images/opencv-logo.png')
#cv2.imshow('1 - logo', logo)
rows, cols, channels = logo.shape
logo_gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
#cv2.imshow('2 - logo_gray', logo_gray)
ret, logo_mask = cv2.threshold(logo_gray, 10, 255, cv2.THRESH_BINARY)
#cv2.imshow('3 - logo_mask', logo_mask)
logo_mask_inv = cv2.bitwise_not(logo_mask)
#cv2.imshow('4 - logo_mask_inv', logo_mask_inv)

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    cv2.imshow('orig frame', frame)
    roi = frame[0:rows, 0:cols]
    roi_bg = cv2.bitwise_and(roi, roi, mask=logo_mask_inv)
    roi_fg = cv2.bitwise_and(logo, logo, mask=logo_mask)
    dst = cv2.add(roi_bg, roi_fg)
    frame[0:rows, 0:cols] = dst
    cv2.imshow('final frame', frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
cap.release()
