# This module handles camera input and outputs
# a numpy array containing RGB values for each pixel.
# This module should contain a function which gets camera input using OpenCV
import cv2
import numpy as np
from matplotlib import pyplot as plt

def normalize_video(x):
    return (x + 16)/1200

vid = cv2.VideoCapture('data/vr-vid.mp4')
if (vid.isOpened()== False): 
  print("Error opening video stream or file")


#out = cv2.VideoWriter('data/outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 30, (960,1080))


index = 0
stereo = cv2.StereoBM_create(numDisparities=80, blockSize=15)
stereo.setPreFilterType(0)
stereo.setPreFilterSize(7)
stereo.setPreFilterCap(11)
stereo.setTextureThreshold(10)
stereo.setUniquenessRatio(1)
stereo.setSpeckleRange(15)
stereo.setSpeckleWindowSize(30)
stereo.setDisp12MaxDiff(0)
stereo.setMinDisparity(0)

ret, rawFrame = vid.read()

#cv2.imwrite('data/rawFrame.png', rawFrame)

#split_image('data/rawFrame.png', 1, 2, False, False)
framesRead = 0
while ret == True:
    lArray, rArray = np.hsplit(rawFrame, 2)
    framesRead += 1
    # Convert frames to grayscale images


    stereoL = cv2.cvtColor(lArray, cv2.COLOR_BGR2GRAY) 
    stereoR = cv2.cvtColor(rArray, cv2.COLOR_BGR2GRAY) 



    disparity = stereo.compute(stereoL, stereoR)
    cv2.imwrite('data/frame.png', disparity)
    #scaledDisparity = cv2.resize(disparity, (960, 1080))
    #out.write(scaledDisparity)
    newRes = (8, 8)
    resized = cv2.resize(disparity, newRes)
    normalized_kxk_array = normalize_video(resized)
    print(resized)
    print(normalized_kxk_array)
    print(framesRead)
    cv2.imwrite('data/resizedFrame.png',resized)
    ret, rawFrame = vid.read()

vid.release
#out.release