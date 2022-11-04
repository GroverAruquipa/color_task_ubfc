# -*- coding: utf-8 -*-
"""
Test on green color
@author: Sameh
"""
import cv2
import numpy as np
import pandas as pd


opnv=10
clsnv = 15


#Read the CSV files containing the calibration data for each colors
dfgr= pd.read_csv('files_calibrated/green.csv')
dflimits=pd.read_csv('files_calibrated/limits.csv')

##This first part is all abour color recognition
def colorvalues(color):
    
    mingr= np.array([dfgr['hMin'][0],dfgr['sMin'][0],dfgr['vMin'][0]],np.uint8)
    maxgr= np.array([dfgr['hMax'][0],dfgr['sMax'][0],dfgr['vMax'][0]],np.uint8)
    
    
    #Assign the calibration data to the corresponding color
    if color == 'green':
        return mingr, maxgr

    # else return error
    else:
        return ('error')
def area_limit(border):
    if border=='1':
        return dflimits['limit1'][0]  
    elif border=='2':
        return dflimits['limit2'][0] 
    elif border=='3':
        return dflimits['limit3'][0] 
    elif border=='4':
        return dflimits['limit4'][0] 

#This part is about shape recognition 
class color_functions: 
    def findContourseOfTheMask(img,mask):
    # Find contours
        contours, hierarchy = cv2.findContours (mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        return contours
    # PLot contours
    def plotContours(img,contours):
        # Draw contours
        img = cv2.drawContours (img, contours, -1, (0, 255, 0), 3)
        return img

    def findCenter ( img, contours ):
        # Find the center of the contour
        centers=[]
        for cnt in contours:
            M = cv2.moments (cnt)
            cx = int (M ['m10'] / M ['m00'])
            cy = int (M ['m01'] / M ['m00'])
            #save centers in vector 
            centers.append([cx,cy])
            cv2.circle (img, (cx, cy), 5, (255, 0, 0), -1)
        return centers,img
    """what's the use why not juste one """
    #Plot the center of the contour
    def plotCenter(img,contours):
        # Find the center of the contour
        for cnt in contours:
            M = cv2.moments (cnt)
            cx = int (M ['m10'] / M ['m00'])
            cy = int (M ['m01'] / M ['m00'])
            cv2.circle (img, (cx, cy), 5, (255, 0, 0), -1)
        return img
    def drawBoxAroundObjectWithMask(img,mask):
        # Find contours
        contours, hierarchy = cv2.findContours (mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        #Draw a rectangle around the contour
        for cnt in contours:
            x, y, w, h = cv2.boundingRect (cnt)
            cv2.rectangle (img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        return img
    #The different filters used next aim to improve the contour/shape recognition
    def eroding_image(img,ker):
        kernel = np.ones (( ker, ker ), np.uint8 )
        erosion = cv2.erode (img, kernel, iterations = 1)
        return erosion
    def dilate_image(img,ker):
        kernel = np.ones (( ker, ker ), np.uint8 )
        dilate = cv2.dilate(img, kernel, iterations=1)
        return dilate
    def opening_image(img,ker):
        kernel = np.ones (( ker, ker ), np.uint8 )
        opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
        return opening
    def closing_image(img,ker):
        kernel = np.ones (( ker, ker ), np.uint8 )
        closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
        return closing
    def writeTextInTheCenterOfTheContour(img,contours,text,offset):
        # Find the center of the contour
        for cnt in contours:
            M = cv2.moments(cnt)
            cx = int (M ['m10'] / M ['m00'])
            cy = int (M ['m01'] / M ['m00'])
            cv2.putText (img, text, (cx, cy+offset), cv2.FONT_ITALIC, 0.6, (0, 0, 0), 2, cv2.LINE_AA)  
        return img

    #function to find the height and width of the image
    def findsector(img,contours):
        #obtain height and width of the image
        height, width = img.shape[:2]
        sectorv=[]
        #if centre of the contour is in the middle of the image then the object is in the middle of the image
        for cnt in contours:
            M = cv2.moments (cnt)
            cx = int (M ['m10'] / M ['m00'])
            cy = int (M ['m01'] / M ['m00'])
            if cy<=area_limit('4')*height/4 and cy>=area_limit('3')*height/4:
                sector=1
            if cy<=area_limit('3')*height/4 and cy>=area_limit('2')*height/4:
                sector=2
            if cy<=area_limit('2')*height/4 and cy>=area_limit('1')*height/4:
                sector=3
            if cy<=area_limit('1')*height/4 and cy>=0*height/4:
                sector=4
            #put,text in image
            print(cy)
            cv2.putText (img, str(sector), (cx, cy+20), cv2.FONT_ITALIC, 0.6, (0, 0, 0), 2, cv2.LINE_AA)
            ## appen sector in sectorv 
            sectorv.append(sector)          
        return sectorv,img

class detection_color:
    def __init__(self, image, minv, maxv, dil, ero,opn,clsn):
        self.image = image
        self.minv = minv
        self.maxv = maxv
        self.dil = dil
        self.ero = ero
        self.opn = opn
        self.clsn = clsn
    def colori(hsvimage, minv, maxv, dil, ero, opn, clsn):
        full_mask = cv2.inRange(hsvimage, minv, maxv)
        
        # call eroding from class color_functions
        full_mask=color_functions.eroding_image(full_mask,ero)

        # call dilate from class color_functions
        full_mask=color_functions.dilate_image(full_mask,dil)
        
        full_mask=color_functions.opening_image(full_mask,opn)
        
        full_mask=color_functions.closing_image(full_mask,clsn)

        # call findContourseOfTheMask from class color_functions
        contours=color_functions.findContourseOfTheMask(hsvimage,full_mask)
        return full_mask , contours

def processImage(img1):
    ##create image 
    image = img1
    #Convert image from BGR to HSV
    hsvimage = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    ###############Orange########################
    countourscounter=[]
    colorcounter=[]
    sectorcounter=[]
    ############To find the region of the center################
    ## Size of the image
    
    ###############################################
    ####################Green###################
    minvgr,maxvgr =colorvalues('green')

    dilgr=20
    erogr=6
    
    full_maskgr,contoursgr=detection_color.colori(hsvimage, minvgr, maxvgr, dilgr, erogr, opnv, clsnv)
    kernel=np.ones((100,100),np.uint8)
    full_maskgr = cv2.morphologyEx(full_maskgr, cv2.MORPH_OPEN, kernel)

    ## call findcenter from class color_functions
    centersgr,imggr=color_functions.findCenter(image,contoursgr)

    text="Green"

    ## call writeTextInTheCenterOfTheContour from class color_functions
    imggr=color_functions.writeTextInTheCenterOfTheContour(imggr,contoursgr,text,0)

    #call findsector from class color_functions
    sectorvgr, image=color_functions.findsector(image,contoursgr)

    #call drawBoxAroundObjectWithMask from class color_functions
    imaux=color_functions.drawBoxAroundObjectWithMask(image,full_maskgr)
    print("sectorvgreen",sectorvgr)
    ## appen centersor in countourscounter
    countourscounter.append(centersgr)
    colorcounter.append("Green")
    sectorcounter.append(sectorvgr)
    
    #####################
    # size of the list countourscounter
    #convert countourscounter to numpy array
    countourscounter1=np.array(countourscounter)
    #append countourcounter lists to a list
    listcentersx=[]
    listcentersy=[]
    listcolor=[]
    listsector=[]
    #for to countourscounter
    counter=0
    for i in range(len(countourscounter)):
        for j in range(len(countourscounter[i])):
            counter=counter+1
            listcentersx.append(countourscounter[i][j][0])
            listcentersy.append(countourscounter[i][j][1])
            listcolor.append(colorcounter[i])
            listsector.append(sectorcounter[i][j])

            print('The centers are')
            print(countourscounter[i][j])
            text=str(counter)
            center=countourscounter[i][j]
            cv2.putText (imaux, text, (center[0]+20, center[1]+20), cv2.FONT_ITALIC, 0.6, (255, 255, 255), 2, cv2.LINE_AA)

    maskx=full_maskgr
    return maskx, imaux, listcentersx, listcentersy, listcolor, listsector
