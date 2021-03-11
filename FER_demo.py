#  ===============================
#  AUTHOR     :Ziming Fang 
#  CREATE DATE     :3/11/21 
#  PURPOSE     :read a face emotion for a image  
#  SPECIAL NOTES: file edit based on 
#                   https://analyticsindiamag.com/face-emotion-recognizer-in-6-lines-of-code/ 
#  ===============================
#  Change History:

# ==================================

from fer import FER
import matplotlib.pyplot as plt 
import cv2 as cv
import numpy as np
import glob

img = plt.imread("media/happy.jpeg")
detector = FER(mtcnn=True)
print(detector.detect_emotions(img))
plt.imshow(img)
emotion, score = detector.top_emotion(img)
print(emotion,score)