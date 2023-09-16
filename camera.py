# This module handles camera input and outputs
# a numpy array containing RGB values for each pixel.
# This module should contain a function which gets camera input using OpenCV
import cv2
import numpy as np
from matplotlib import pyplot as plt
from split_image import split_image


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

index = 0
stereo = cv2.StereoBM_create(numDisparities=272, blockSize=31)
stereo.setPreFilterType(1)
stereo.setPreFilterSize(7)
stereo.setPreFilterCap(1)
stereo.setTextureThreshold(10)
stereo.setUniquenessRatio(5)
stereo.setSpeckleRange(0)
stereo.setSpeckleWindowSize(0)
stereo.setDisp12MaxDiff(10)
stereo.setMinDisparity(0)
while retL == True & retR == True:
    # Convert frames to grayscale images
    stereoL = cv2.cvtColor(frameL, cv2.COLOR_BGR2GRAY) 
    stereoR = cv2.cvtColor(frameR, cv2.COLOR_BGR2GRAY) 
    res720 = (1280, 720)
    stereoL = cv2.resize(stereoL, res720)
    stereoR = cv2.resize(stereoR, res720)


    disparity = stereo.compute(stereoL, stereoR)
    cv2.imwrite('data/frame.png', disparity)
    newRes = (6, 6)
    resized = cv2.resize(disparity, newRes)
    print(resized)
    cv2.imwrite('data/resizedFrame.png',resized)
    retL, frameL = camL.read()
    retR, frameR = camR.read()
    if not retL:
        print("Can't receive frame from left camera")
        break
    if not retR:
        print("Can't recieve frame from right camera")
        break
