import cv2 as cv


#Reading Photos

#img = cv.imread('C:/Users/phowe/Documents/OpenCVPhotos/Photos/Cat.jpg')
#cv.imshow('Cat', img)
#cv.waitKey(0)
#Reading Videos

capture = cv.VideoCapture('C:/Users/phowe/OneDrive/Videos/Xbox Game DVR/11-18-2016_6-57-00_PM.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()





