import cv2
import numpy as np

def load_img():
    blank_img =np.zeros((300,400))
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(blank_img,text='BARAK',org=(25,150), fontFace=font,fontScale= 3 ,color=(255,255,255),thickness=16,lineType=cv2.LINE_AA)
    return blank_img


def run():
    orig = load_img()
    cv2.imshow('1-orig', orig)

    kernel = np.ones((5,5), np.uint8)
    
    #Erosion
    erosion1 = cv2.erode(orig, kernel, iterations = 1)
    cv2.imshow('2-erosion1', erosion1)

    erosion3 = cv2.erode(orig, kernel, iterations = 3)
    cv2.imshow('3-erosion3', erosion3)
   
    #dilation
    dilation = cv2.dilate(orig, kernel, iterations = 1)
    cv2.imshow('4-dilation', dilation)

    #opening
    white_noise = np.random.randint(low=0,high=2,size=(300,400))
    white_noise = white_noise*255
    noise_img = white_noise + orig
    cv2.imshow('5-noise_img', noise_img)
    opening = cv2.morphologyEx(noise_img, cv2.MORPH_OPEN, kernel)
    cv2.imshow('6-opening', opening)

    #closing
    black_noise = np.random.randint(low=0,high=2,size=(300,400))
    black_noise= black_noise * -255
    black_noise_img = orig + black_noise
    black_noise_img[black_noise_img==-255] = 0
    cv2.imshow('7-black_noise_img', black_noise_img)
    closing = cv2.morphologyEx(black_noise_img, cv2.MORPH_CLOSE, kernel)
    cv2.imshow('8-closing', closing)

    #Morphological gradient
    gradient = cv2.morphologyEx(orig, cv2.MORPH_GRADIENT,kernel)
    cv2.imshow('9-gradient', gradient)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run()
