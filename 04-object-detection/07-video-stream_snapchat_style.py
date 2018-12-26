import numpy as np
import cv2

#Globals
ear_img_base = None
ear_img_right = None
ear_img_left = None
rows = None
cols = None
channels = None
ear_img_right_gray = None
ear_img_left_gray = None
ear_img_right_mask = None
ear_img_left_mask = None
ear_img_right_mask_inv = None
ear_img_left_mask_inv = None

ears = ['','../images/ear1.png', '../images/ear2.png', '../images/ear3.png' ]
h_adjustments = [0, 1/6, 1/1.3, 1/6]
w_adjustments = [0, 0,50, 10]
resize_adjustments = [0, 0.5, 0.7, 0.3]
height_adjustment = None
width_adjustment = None
resize_adjustment = None
ear_index = 0



def populate_globals(idx):
    global ear_img_base, ear_img_right, ear_img_left, rows, cols, channels,\
            ear_img_right_gray, ear_img_left_gray, ear_img_right_mask, \
            ear_img_left_mask, ear_img_right_mask_inv, ear_img_left_mask_inv, \
            height_adjustment, width_adjustment, resize_adjustment, ear_index
    
    height_adjustment = h_adjustments[idx]
    width_adjustment  = w_adjustments[idx]
    resize_adjustment = resize_adjustments[idx]
    ear_index = idx
    if idx == 0:
        return
    ear_img_base = cv2.imread(ears[idx])
    ear_img_right = cv2.resize(ear_img_base, (0,0), fx=resize_adjustment, fy=resize_adjustment)
    ear_img_left = cv2.flip(ear_img_right,1)

    rows, cols, channels = ear_img_right.shape
    ear_img_right_gray = cv2.cvtColor(ear_img_right, cv2.COLOR_BGR2GRAY)
    ear_img_left_gray  = cv2.flip(ear_img_right_gray, 1)

    ret, ear_img_right_mask = cv2.threshold(ear_img_right_gray, 10, 255, cv2.THRESH_BINARY)
    ear_img_left_mask = cv2.flip(ear_img_right_mask, 1)

    ear_img_right_mask_inv = cv2.bitwise_not(ear_img_right_mask)
    ear_img_left_mask_inv = cv2.flip(ear_img_right_mask_inv, 1)


face_cascade = cv2.CascadeClassifier('../resources/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
populate_globals(0)


def detect_face_rects(img):
    face_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    face_rects = face_cascade.detectMultiScale(face_img, 
            scaleFactor=1.1,
            minNeighbors=25,
            minSize=(40, 40),
            flags=cv2.CASCADE_SCALE_IMAGE)
    return face_rects


while True:
    _, frame = cap.read(0)
    if ear_index >= 0 and ear_index < len(ears):
        rects = detect_face_rects(frame)
        # when ear_index is zero than simplt draw a rectangle around the detected face
        if ear_index == 0:
            for (x,y,w,h) in rects:
                cv2.rectangle(frame, (x,y), (x+w,y+h), (255,255,255), 2)
        # otherwise handle the ears
        else: 
            for (x, y, w, h) in rects:
                l_cord = (x - width_adjustment, y + int(h * height_adjustment) - rows)
                r_cord = (x + w - cols + width_adjustment, y + int(h * height_adjustment) - rows)
                if l_cord[1] < 0 or (r_cord[0] + cols) > frame.shape[1]: 
                    print ("Skipping l_cord = {}, y_cord = {}".format(l_cord, r_cord))
                    continue
                #constructing the left ear
                left_roi = frame[l_cord[1]:l_cord[1] + rows, l_cord[0]:l_cord[0] + cols]
                left_roi_bg = cv2.bitwise_and(left_roi, left_roi, mask=ear_img_left_mask_inv)
                left_roi_fg = cv2.bitwise_and(ear_img_left, ear_img_left, mask=ear_img_left_mask)
                left_dst = cv2.add(left_roi_bg, left_roi_fg)
                frame[l_cord[1]:l_cord[1] + rows, l_cord[0]:l_cord[0] + cols] = left_dst
                #constructing the right ear
                right_roi = frame[r_cord[1]:r_cord[1] + rows, r_cord[0]:r_cord[0] + cols]
                right_roi_bg = cv2.bitwise_and(right_roi, right_roi, mask=ear_img_right_mask_inv)
                right_roi_fg = cv2.bitwise_and(ear_img_right, ear_img_right, mask=ear_img_right_mask)
                right_dst = cv2.add(right_roi_bg, right_roi_fg)
                frame[r_cord[1]:r_cord[1] + rows, r_cord[0]:r_cord[0] + cols] = right_dst
    cv2.imshow('frame', frame)

    k = cv2.waitKey(1)
    if k == 27:
        break
    elif k > 0 and chr(k).isdigit() and int(chr(k)) <  len(ears):
        print ("Populating {}".format(ears[int(chr(k))]))
        populate_globals(int(chr(k)))


cv2.destroyAllWindows()
cap.release()
