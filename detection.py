import cv2
import numpy as np

# Load the screenshot
img = cv2.imread("chess_screenshot.png")

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,15,600,apertureSize = 3)
# Use adaptive thresholding to create a binary image
thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

lines = cv2.HoughLinesP(edges,3,np.pi/180,100,thresh,minLineLength=5,maxLineGap=15)
for line in lines:
    x1,y1,x2,y2 = line[0]
    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

# Display the image with the circles
cv2.imshow("Detected Chess Pieces", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
