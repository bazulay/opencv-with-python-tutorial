import cv2
import numpy as np
import argparse
import os
import sys



def auto_canny(image, sigma=0.33):
    # compute the median of the single channel pixel intensities
    v = np.median(image)
    # apply automatic Canny edge detection using the computed median
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edged = cv2.Canny(image, lower, upper)
    return edged


def main():
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        ret, frame = cap.read()
        sobel = cv2.Sobel(frame, cv2.CV_64F,1,1,ksize=3)
        laplacian = cv2.Laplacian(frame, cv2.CV_64F)
        canny = auto_canny(frame)

        cv2.imshow('orig', frame)
        cv2.imshow('sobel', sobel)
        cv2.imshow('laplacian', laplacian)
        cv2.imshow('canny', canny)
        if cv2.waitKey(3) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
        
    
    
    
if __name__ == '__main__':
    main()
