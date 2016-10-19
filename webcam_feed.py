import cv2
from datetime import datetime

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

'''
w=int(vc.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH ))
h=int(vc.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT ))
# video recorder
fourcc = cv2.cv.CV_FOURCC(*'XVID')  # cv2.VideoWriter_fourcc() does not exist
video_writer = cv2.VideoWriter("output.mp4", fourcc, 25, (w, h))
'''
start = datetime.now()
while rval:
    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)    
    #if key == 97: # exit on ESC
    #    break
    end = datetime.now()
    if (end-start).seconds >= 10:
        break;

vc.release()
cv2.destroyAllWindows()
