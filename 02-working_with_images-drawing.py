import numpy as np
import cv2

# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
img = cv2.line(img,(0,0),(511,511),(255,0,0),5)
#Draw rectangle
img = cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
#Draw a circle
img = cv2.circle(img,(447,63), 63, (0,0,255), -1)
#Draw an ellipse
img = cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)
#Draw a polygon
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
img = cv2.polylines(img,[pts],True,(0,255,255))


pts1 = np.array([[100,10],[200,20],[180,100],[80,50]], np.int32)
pts1 = pts1.reshape((-1,1,2))
img = cv2.polylines(img,[pts1],False,(0,255,255))

#Add Text
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
