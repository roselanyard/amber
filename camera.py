# This module handles camera input and outputs
# a numpy array containing RGB values for each pixel.
# This module should contain a function which gets camera input using OpenCV
import cv2
import numpy as np


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

gaussian_kernel_size = (5, 5)
gaussian_std_dev = 4


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
    disparity_smoothed = cv2.GaussianBlur(disparity, gaussian_kernel_size, gaussian_std_dev)

    cv2.imwrite('data/frame.png', disparity)
    cv2.imwrite('data/frameblurred.png', disparity_smoothed)
    #scaledDisparity = cv2.resize(disparity, (960, 1080))
    #out.write(scaledDisparity)
    newRes = (8, 8)
    resized = cv2.resize(disparity, newRes)
    resizedBlur = cv2.resize(disparity_smoothed, newRes)
    print(resized)
    print(framesRead)
    cv2.imwrite('data/resizedFrame.png',resized)
    cv2.imwrite('data/resizedBlurredFrame.png',resizedBlur)

    ret, rawFrame = vid.read()

vid.release
#out.release