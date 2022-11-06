import cv2
import numpy as np
import pandas as pd
from base_functions import *
import os
cap = cv2.VideoCapture('paperEval.mp4')#call the video to process
out=cv2.VideoWriter('result_output.avi',cv2.VideoWriter_fourcc(*'DIVX'), 15, (640,480))#show results on the processed video with shapes and color recognition
counterframe=1
if os.path.exists('centers.csv'):#destroy centers.csv file
    os.remove('centers.csv')
if os.path.exists('centers.txt'):#destroy centers.txt file
    os.remove('centers.txt')
while(cap.isOpened()):
    ret, frame = cap.read()
    frame = cv2.medianBlur(frame, 5)# Eliminate shadows and noise
    if ret==True: #if the video is not over
        maskx, imaux, listcentersx, listcentersy, listcolor, listsector = processImage(frame)
        df = pd.DataFrame({'frame_number': counterframe, 'x': listcentersx, 'y': listcentersy, 'color': listcolor, 'sector': listsector})
        df.to_csv('centers.csv', mode='a', header=False, index=False, encoding='utf-8')#save the centers for the frame in a csv file
        df.to_csv('centers.txt', mode='a', header=False, index=False, encoding='utf-8')#save the centers for the frame in a txt file
        cv2.imshow('frame2',imaux) #show the processed video
        out.write(imaux) #save the processed video
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyWindow('frame2')
            break
    else:
        break
    counterframe=counterframe+1
out.release()#release the video