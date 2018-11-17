import cv2
import numpy as np
import argparse
import os
import sys


kernel = np.ones((5,5),np.uint8)

def auto_canny(image, sigma=0.33):
    # compute the median of the single channel pixel intensities
    v = np.median(image)
    # apply automatic Canny edge detection using the computed median
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    print("lower = {}, upper = {}".format(lower, upper))
    edged = cv2.Canny(image, lower, upper)
    return edged


def detect_edge(image_file_path):
    orig_img = cv2.imread(image_file_path)
    cv2.imshow('orig_img', orig_img)
    
    gray_img =  cv2.cvtColor(orig_img,cv2.COLOR_BGR2GRAY).astype(float)
    cv2.imshow('gray_img', gray_img)
    
    edge_x = cv2.Sobel(gray_img,cv2.CV_64F,1,0,ksize=3)
    cv2.imshow('sobel_x', edge_x)
    
    edge_y = cv2.Sobel(gray_img,cv2.CV_64F,0,1,ksize=3)
    cv2.imshow('sobel_y', edge_y)

    sobel = cv2.Sobel(gray_img,cv2.CV_64F,1,1,ksize=3)
    cv2.imshow('sobel', sobel)


    laplacian = cv2.Laplacian(gray_img, cv2.CV_64F)
    cv2.imshow('laplacian', laplacian)
    
    canny_edges = auto_canny(orig_img)
    cv2.imshow('canny_edges', canny_edges)

    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    

def main():
    parser_description = 'Performs edge detection on an image using the sobel feldman algorithm'
    parser = argparse.ArgumentParser(description=parser_description)
    parser.add_argument('--image', type=str, required=True, help='path of the image to be processed')
    args = parser.parse_args()
    
    if not args.image.strip() or not os.path.isfile(args.image):
        print('Please provide a valid path to an image file')
        sys.exit(-1)
        
    detect_edge(args.image)
    
        
    
    
    
if __name__ == '__main__':
    main()
