import cv2 as cv

print("OpenCV version:")
print(cv.__version__)

img = cv.imread('pumpkin.jpg')

# the name of the video, the image 
cv.imshow('pumpkin', img)

# wait from keyboard action? 
cv.waitKey(0)
cv.destroyAllWindows()
exit()
