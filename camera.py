# This module handles camera input and outputs
# a numpy array containing RGB values for each pixel.
# This module should contain a function which gets camera input using OpenCV
import cv2
import numpy as np
from matplotlib import pyplot as plt
import sharedvars

def normalize_video(x):
    return (x + 16)/1200

vid = cv2.VideoCapture('data/vr-vid.mp4')
if (vid.isOpened()== False): 
  print("Error opening video stream or file")


#depthOutSmooth = cv2.VideoWriter('data/depthSmooth.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 30, (960,1080),False)
#depthOutPlain = cv2.VideoWriter('data/depthNormal.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 30, (960,1080),False)
#scaledOut = cv2.VideoWriter('data/scaled.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 30, (8,8), False)


index = 0
stereo = cv2.StereoBM_create(numDisparities=32, blockSize=21)
stereo.setPreFilterType(0)
stereo.setPreFilterSize(5)
stereo.setPreFilterCap(5)
stereo.setTextureThreshold(25)
stereo.setUniquenessRatio(1)
stereo.setSpeckleRange(1)
stereo.setSpeckleWindowSize(2)
stereo.setDisp12MaxDiff(2)
stereo.setMinDisparity(1)

gaussian_kernel_size = (5, 5)
gaussian_std_dev = 4


ret, rawFrame = vid.read()

#cv2.imwrite('data/rawFrame.png', rawFrame)

#split_image('data/rawFrame.png', 1, 2, False, False)
framesRead = 0

def update_depth_map():
    global ret
    global rawFrame
    global framesRead
    while ret == True and sharedvars.exiting is not True:
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
        with sharedvars.depthmap_lock:
            sharedvars.kbyk_depthmap = normalize_video(resized)
        # print(resized)
        # print(sharedvars.kbyk_depthmap)
        # print(framesRead)
        cv2.imwrite('data/resizedFrame.png',resized)
        ret, rawFrame = vid.read()

    vid.release()
#out.release
