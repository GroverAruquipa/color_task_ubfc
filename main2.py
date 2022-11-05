import cv2
import numpy as np
import pandas as pd
from base_functions import *
import os
#call the video to process
cap = cv2.VideoCapture('paperEval.mp4')
#show results on the processed video with shapes and color recognition
out=cv2.VideoWriter('result_output.avi',cv2.VideoWriter_fourcc(*'DIVX'), 15, (640,480))
counterframe=1
#destroy centers.csv file
if os.path.exists('centers.csv'):
    os.remove('centers.csv')
#destroy centers.txt file
if os.path.exists('centers.txt'):
    os.remove('centers.txt')
while(cap.isOpened()):
    ret, frame = cap.read()
    # Eliminate shadows and noise
    frame = cv2.medianBlur(frame, 5)

    if ret==True:
        maskx, imaux, listcentersx, listcentersy, listcolor, listsector = processImage(frame)
        #same the number of frame, listcentersx, listcentersy, listcolor, listsector in a csv file
        df = pd.DataFrame({'frame_number': counterframe, 'x': listcentersx, 'y': listcentersy, 'color': listcolor, 'sector': listsector})
        df.to_csv('centers.csv', mode='a', header=False, index=False, encoding='utf-8')
        # save df in txt file
        df.to_csv('centers.txt', mode='a', header=False, index=False, encoding='utf-8')
        #cv2.imshow('frame',maskx)
        cv2.imshow('frame2',imaux)
        out.write(imaux) 
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyWindow('frame2')
            break
    else:
        break
    counterframe=counterframe+1
out.release()