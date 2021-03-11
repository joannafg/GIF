#  ===============================
#  AUTHOR     :Ziming Fang 
#  CREATE DATE     :3/11/21 
#  PURPOSE     :save the keypoints and descriptors of a gif video 
#  SPECIAL NOTES: file edit based on 
#                   https://www.youtube.com/watch?v=nO3csmVyoOQ
#                   https://www.youtube.com/watch?v=oXlwWbU8l2o 
#                   sift_demo.py 
#                   https://pythonexamples.org/python-opencv-cv2-create-video-from-images/ 
#  ===============================
#  Change History:

# ==================================
import cv2 as cv
import numpy as np
import glob

print("OpenCV version:")
print(cv.__version__)

sift = cv.SIFT_create()

video_kp_array = []
video_des_array = []
frameSize = (320, 320)

out = cv.VideoWriter('media/sift_running.mp4',cv.VideoWriter_fourcc(*'DIVX'), 1, frameSize)


# read video 
capture = cv.VideoCapture('media/running.mp4')
while True: 
    isTrue, frame = capture.read()

    # feature extraction 
    gray= cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    kp, des = sift.detectAndCompute(gray,None)

    # save the processed video for demonstration 
    img=cv.drawKeypoints(gray,kp,img,flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    out.write(img)

    # save keypoints and descriptors 
    video_kp_array.append(kp)
    video_des_array.append(des)

    # if 'd' key is pressed, break out of the loop 
    if cv.waitKey(20) & 0xFF==ord('d'): 
        break 
 

out.release()
capture.release()
sys.exit()