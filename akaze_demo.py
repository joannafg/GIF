#  ===============================
#  AUTHOR     :Ziming Fang 
#  CREATE DATE     :3/11/21 
#  PURPOSE     :process a single picture with AKAZE algorithm 
#  SPECIAL NOTES: file edit based on https://docs.opencv.org/3.4/db/d70/tutorial_akaze_matching.html 
#                 and https://stackoverflow.com/questions/36796025/how-do-you-use-akaze-in-open-cv-on-python 
#  ===============================
#  Change History:

# ==================================
from __future__ import print_function
import cv2 as cv
import numpy as np
import argparse
from math import sqrt

img1 = cv.imread(cv.samples.findFile('./media/pumpkin.jpg'), cv.IMREAD_GRAYSCALE)
if img1 is None: # or img2 is None:
    print('Could not open or find the images!')
    exit(0)

akaze = cv.AKAZE_create()
kpts1, desc1 = akaze.detectAndCompute(img1, None)

print("keypoints: {}, descriptors: {}".format(len(kpts1), desc1.shape))


exit(0)