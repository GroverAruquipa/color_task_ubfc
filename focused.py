### FOcused
import cv2
"""
Reading a video stream
"""
# Configure video stream source: 0 is the defaut one
cam = cv2.VideoCapture(0)
if (not cam.isOpened):
    print('Impossible to read the camera !')
# Display stream until clic on SPACE when mouse pointer in video display
while (True):
    ret, frame = cam.read()
    cv2.imshow('video', frame)
    if cv2.waitKey(2)>=27:
        break
# Deallocate memory
cam.release()
cv2.destroyAllWindows()