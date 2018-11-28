import cv2
import numpy as np
import argparse
import os
import sys

methods = {'cv2.TM_CCOEFF':cv2.TM_CCOEFF, 
        'cv2.TM_CCOEFF_NORMED':cv2.TM_CCOEFF_NORMED, 
        'cv2.TM_CCORR':cv2.TM_CCORR, 
        'cv2.TM_CCORR_NORMED':cv2.TM_CCORR_NORMED, 
        'cv2.TM_SQDIFF':cv2.TM_SQDIFF, 
        'cv2.TM_SQDIFF_NORMED':cv2.TM_SQDIFF_NORMED}

method_options = list(methods.keys())

def match_template(image, template, scan_methods, multiple, threshold):
    img_bgr = cv2.imread(image)
    img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    template_bgr = cv2.imread(template)
    template_gray = cv2.cvtColor(template_bgr, cv2.COLOR_BGR2GRAY)
    w, h = template_gray.shape[::-1]
    cv2.imshow('image-to-scan', img_bgr)
    cv2.imshow('template', template_bgr)
    for scan_method in scan_methods:
        img_disp = img_bgr.copy()
        res = cv2.matchTemplate(img_gray, template_gray, methods[scan_method])
        if not multiple:
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            if methods[scan_method] in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
                loc = (np.array([min_loc[1],]), np.array([min_loc[0],]))
            else:
                loc = (np.array([max_loc[1],]), np.array([max_loc[0],]))
        else:
            loc = np.where(res >= threshold)
        print("number of cordinates found is: {}".format(len(loc[0])))
        for pt in zip(*loc[::-1]):
            cv2.rectangle(img_disp, pt, (pt[0]+w, pt[1]+h), (0,255,0), 2)
        cv2.imshow("res_{}".format(scan_method), res)
        cv2.imshow(scan_method, img_disp)
        cv2.cv2.waitKey(0)
    cv2.destroyAllWindows()


    

def main():
    parser_description = 'Performs template matching'
    parser = argparse.ArgumentParser(description=parser_description)
    parser.add_argument('--image', type=str, required=True, 
            help='path of the image to scan for matches')
    parser.add_argument('--template', type=str, required=True, 
            help='path of the template image to scan for')
    parser.add_argument('--scan-method', choices=method_options.copy().append('all'), 
            default='cv2.TM_CCOEFF_NORMED', nargs='?', metavar='', 
            help="what cv method to use for template matching one of: all {}".format(", ".join(method_options)))
    parser.add_argument('--multiple', action='store_true',
            help="whether to look for multiple instances of the template in the picture default is to look for the single best fit")
    parser.add_argument('--threshold', type=float, nargs='?', default=0.90, 
            help="When scanning for multiple instances, every pixel above that is a match, default is 0.9")


    
    args = parser.parse_args()
    
    if not os.path.isfile(args.image):
        print('Please provide a valid path to an image file')
        sys.exit(-1)
    if not os.path.isfile(args.template):
        print('Please provide a valid path to a template file')
        sys.exit(-1)
    if args.scan_method == 'all':
        method_list = list(methods.keys())
    else:
        method_list = [args.scan_method]

    match_template(args.image, args.template, method_list, args.multiple, args.threshold)
    
        
    
    
    
if __name__ == '__main__':
    main()
