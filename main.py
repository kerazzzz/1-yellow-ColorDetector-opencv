import cv2

#for drawing boundry box: pillow is image processing library
from PIL import Image

#import module which gets color range
from util import get_limits

yellow = [0, 255, 255] #yellow in BGR



cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()    #ret->bool; frame-> img of each frame of the captured video
    # cv2.imshow('frame', frame)



    #we will work on hsv so change color to hsv
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)



    lowerLimit, upperLimit = get_limits(color=yellow)

    #check range
    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit )

    mask_ =Image.fromarray(mask)    #pillow
    bbox = mask_.getbbox()           #
    print(bbox)

    if bbox is not None:
        x1,y1, x2, y2 = bbox;
        cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0),3)

    cv2.imshow('mask', mask)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

