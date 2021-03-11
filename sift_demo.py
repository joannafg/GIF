#  ===============================
#  AUTHOR     :Ziming Fang 
#  CREATE DATE     :3/11/21 
#  PURPOSE     :process a single picture with SIFT algorithm 
#  SPECIAL NOTES: adapted from https://docs.opencv.org/master/da/df5/tutorial_py_sift_intro.html 
#  ===============================
#  Change History:

# ==================================
import numpy as np
import cv2 as cv

img = cv.imread('./media/pumpkin.jpg')
gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
sift = cv.SIFT_create()
kp = sift.detect(gray,None)
# img=cv.drawKeypoints(gray,kp,img)
# cv.imwrite('sift_keypoints.jpg',img)
img=cv.drawKeypoints(gray,kp,img,flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv.imwrite('./media/sift_keypoints.jpg',img)

exit(0) 