### MOuse Clicker
import cv2 
import numpy as np

x_co=0
y_co=0
def click_event(event, x, y, flags, param):
    global x_co
    global y_co
    if event == cv2.EVENT_LBUTTONDOWN:
        x_co=x
        y_co=y
        print(x_co, ' ', y_co)
        font = cv2.FONT_HERSHEY_SIMPLEX #font style
        strXY = str(x_co) + ', ' + str(y_co)
        cv2.putText(img, strXY, (x_co,y_co), font, .5, (255,255,0), 2)
        cv2.imshow('image', img)
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y_co, x_co, 0]
        green = img[y_co, x_co, 1]
        red = img[y_co, x_co, 2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR = str(blue) + ', ' + str(green) + ', ' + str(red)
        cv2.putText(img, strBGR, (x_co,y_co), font, .5, (0,255,255), 2)
        cv2.imshow('image', img)
capture=cv2.VideoCapture(0)
while True:
    ret, img=capture.read()
    cv2.imshow('image', img)
    cv2.setMouseCallback('image', click_event)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()



