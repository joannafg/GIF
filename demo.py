import cv2 as cv

print("OpenCV version:")
print(cv.__version__)

# read image 
img = cv.imread('./media/pumpkin.jpg')
# the name of the video, the image 
cv.imshow('pumpkin', img)

# read video 
capture = cv.VideoCapture('media/running.mp4')
while True: 
    isTrue, frame = capture.read()
    # frame is the frame 
    cv.imshow('Video', frame)

    # if 'd' key is pressed, break out of the loop 
    if cv.waitKey(20) & 0xFF==ord('d'): 
        break 


# cv.waitKey(0) # wait from keyboard action? 
capture.release()
cv.destroyAllWindows()
sys.exit()