import argparse
import cv2
import numpy as np
import os
from matplotlib import cm
import sys



#GLOBAL VARIABLES
colors = []
current_color = 0
marks_updated = False
#IMAGES
main_img = None
main_img_copy = None
marker_img = None
segments_img = None



def create_bgr(i):
    x = np.array(cm.tab10(i))[:3]*255
    #color maps (cm) are RGB and needs to be converted to BGR
    return tuple([x[2], x[1], x[0]])


def initiate_color_list():
    global colors
    for i in range(10):
        colors.append(create_bgr(i))

def initiate_images(img_path):
    global main_img, marker_img, segments_img, main_img_copy
    main_img = cv2.imread(img_path)
    main_img_copy = np.copy(main_img)
    marker_img = np.zeros(main_img.shape[:2], dtype=np.int32)
    segments_img = np.zeros(main_img.shape, dtype=np.uint8)


def mouse_callback(event, x, y, flags, param):
    global marks_updated 
    if event == cv2.EVENT_LBUTTONDOWN:
        # TRACKING FOR MARKERS
        cv2.circle(marker_img, (x, y), 10, (current_color), -1)
        # DISPLAY ON USER IMAGE
        cv2.circle(main_img_copy, (x, y), 10, colors[current_color], -1)
        marks_updated = True    

def do_work(img_path):
    global segments_img, main_img_copy, current_color, marks_updated
    cv2.namedWindow('Orig Image')
    cv2.setMouseCallback('Orig Image', mouse_callback)
    while True:
        # SHow the 2 windows
        cv2.imshow('WaterShed Segments', segments_img)
        cv2.imshow('Orig Image', main_img_copy)
        # Close everything if Esc is pressed
        k = cv2.waitKey(1)
        if k == 27:
            break
        # Clear all colors and start over if 'c' is pressed
        elif k == ord('c'):
            initiate_images(img_path)
        # If a number 0-9 is chosen index the color
        elif k > 0 and chr(k).isdigit():
            # chr converts to printable digit
            current_color  = int(chr(k))
        # If we clicked somewhere, call the watershed algorithm on our chosen markers
        if marks_updated:
            marker_img_copy = marker_img.copy()
            cv2.watershed(main_img, marker_img_copy)
            segments_img = np.zeros(main_img.shape, dtype=np.uint8)
            for color_ind in range(len(colors)):
                segments_img[marker_img_copy == (color_ind)] = colors[color_ind]
            marks_updated = False
    cv2.destroyAllWindows()




def main():
    parser_description = 'Performs watershed algorithm based on custome selected seeds'
    parser = argparse.ArgumentParser(description=parser_description)
    parser.add_argument('--image', type=str, required=True,
            help='path of the image to process')
    args = parser.parse_args()
    if not os.path.isfile(args.image):
        print('Please provide a valid path to an image file')
        sys.exit(-1)
    initiate_color_list()
    initiate_images(args.image)
    do_work(args.image)
    






if __name__ == '__main__':
    main()

