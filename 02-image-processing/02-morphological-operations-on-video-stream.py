import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #lower_limit = np.array([165, 129, 151])
    #upper_limit = np.array([180, 198, 213])
    #lower_limit = np.array([77, 82, 102])
    #upper_limit = np.array([86, 170, 201])
    lower_limit = np.array([44, 78, 111])
    upper_limit = np.array([52, 136, 240])

    mask = cv2.inRange(hsv, lower_limit, upper_limit)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    kernel = np.ones((5,5), np.uint8)
    erosion = cv2.erode(mask, kernel, iterations = 1)
    dilation = cv2.dilate(mask, kernel, iterations = 1)
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing  = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    gradient = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel)
    


    cv2.imshow('orig', frame)
    #cv2.imshow('hsv', hsv)
    cv2.imshow('res', res)
    cv2.imshow('mask', mask)
    cv2.imshow('erosion', erosion)
    cv2.imshow('dilation', dilation)
    cv2.imshow('opening', opening)
    cv2.imshow('closing', closing )
    cv2.imshow('gradient', gradient )

    if cv2.waitKey(5) & 0xFF == 27:
        break

cv2.destroyAllWindows()
cap.release()
