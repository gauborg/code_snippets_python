'''

Description: This code extracts images from a given video stream.
Author: Gaurav Borgaonkar
Date: 15 June 2020

'''

import cv2
 
# Opens the Video file
fname = "./sample_video.mp4"
video = cv2.VideoCapture(fname)

# image number sequence to start with
i=1000001

while(video.isOpened()):
    ret, frame = video.read()
    if ret == False:
        break
    frame = cv2.resize(frame, None, fx = 0.5, fy = 0.5, interpolation = cv2.INTER_CUBIC)

    # path to write images to ...
    cv2.imwrite('./images/image'+str(i)+'.jpg',frame)
    i+=1
 
cap.release()
cv2.destroyAllWindows()
