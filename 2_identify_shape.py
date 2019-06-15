import numpy as np
import cv2

image = cv2.imread('someshapes.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('Images', image)
cv2.waitKey(0)

# apply threshold
ret, thresh = cv2.threshold(gray, 127, 255, 1)

# contours : bagus untuk detect shape
# extract contours
# cv2.findContours (return 3 parameter in Python 2, return 2 parameter in Python 3)
# find Contours untuk detect boundary
_, contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

for contour in contours:
        # approxPolyDP mengembalikan nilai sudut dari shape yang ada
        approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)

        if(len(approx) == 3):
                shapeName = 'Triangle'
        elif (len(approx) == 4):
                x,y,w,h = cv2.boundingRect(contour)                

                if(abs(w-h) <= 3):
                        shapeName = 'Square'                        
                else:
                        shapeName = 'Rectangle'
        else:
                if (len(approx) == 10):
                        shapeName = 'Star'                        
                elif (len(approx) >= 15):
                        shapeName = 'Circle'

        # drawContours : menggambar contour dengan warnanya
        cv2.drawContours(image, [contour], 0, (0, 255, 255) , -1)
        M = cv2.moments(contour)

        # mendapatkan center point dari shape
        x = int(M['m10'] / M['m00'])
        y = int(M['m01'] / M['m00'])
        cv2.putText(image, shapeName, (x-50, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 1)                

        cv2.imshow('Identifying Shapes', image)
        cv2.waitKey(0)