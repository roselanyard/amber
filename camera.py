import cv2
import numpy as np
from matplotlib import pyplot as plt


# Note camera IDs may differ based upon hardware
camL = cv2.VideoCapture(1)
if not camL.isOpened():
 print("Cannot open left camera")
 exit()
camR = cv2.VideoCapture(0)
if not camR.isOpened():
 print("Cannot open right camera")
 exit()
# Read frames from each camera
retL, frameL = camL.read()
if not retL:
    print("Can't receive frame from left camera")
retR, frameR = camR.read()
if not retR:
    print("Can't recieve frame from right camera")
camL.release
camR.release

# Convert frames to grayscale images
stereoL = cv2.cvtColor(frameL, cv2.COLOR_BGR2GRAY) 
stereoR = cv2.cvtColor(frameR, cv2.COLOR_BGR2GRAY) 


stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
disparity = stereo.compute(stereoL, stereoR)
plt.imshow(disparity,'gray')
plt.show()
