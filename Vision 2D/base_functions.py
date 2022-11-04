""""This code contains all the functions for the video processing :
    Color recognition using calibration data
    shape detection
    calculating the surface area of each shape
    """
import cv2
import numpy as np
import pandas as pd


opnv=10
clsnv = 15


#Read the CSV files containing the calibration data for each colors
dfbl=pd.read_csv('files_calibrated/blue.csv')
dfor= pd.read_csv('files_calibrated/orange.csv')
dfgr= pd.read_csv('files_calibrated/green.csv')
dfy= pd.read_csv('files_calibrated/yellow.csv')
dfp= pd.read_csv('files_calibrated/pink.csv')
dfpu= pd.read_csv('files_calibrated/purple.csv')
dfwh= pd.read_csv('files_calibrated/white.csv')
dflimits=pd.read_csv('files_calibrated/limits.csv')

##This first part is all abour color recognition
def colorvalues(color):
    #Extract the calibration data from the csv files for each color
    minor= np.array([dfor['hMin'][0],dfor['sMin'][0],dfor['vMin'][0]],np.uint8)
    maxor= np.array([dfor['hMax'][0],dfor['sMax'][0],dfor['vMax'][0]],np.uint8)

    mingr= np.array([dfgr['hMin'][0],dfgr['sMin'][0],dfgr['vMin'][0]],np.uint8)
    maxgr= np.array([dfgr['hMax'][0],dfgr['sMax'][0],dfgr['vMax'][0]],np.uint8)
    
    minvy= np.array([dfy['hMin'][0],dfy['sMin'][0],dfy['vMin'][0]],np.uint8)
    maxvy= np.array([dfy['hMax'][0],dfy['sMax'][0],dfy['vMax'][0]],np.uint8)
    
    minvp= np.array([dfp['hMin'][0],dfp['sMin'][0],dfp['vMin'][0]],np.uint8)
    maxvp= np.array([dfp['hMax'][0],dfp['sMax'][0],dfp['vMax'][0]],np.uint8)
    
    minvpu= np.array([dfpu['hMin'][0],dfpu['sMin'][0],dfpu['vMin'][0]],np.uint8)
    maxvpu= np.array([dfpu['hMax'][0],dfpu['sMax'][0],dfpu['vMax'][0]],np.uint8)

    minwh= np.array([dfwh['hMin'][0],dfwh['sMin'][0],dfwh['vMin'][0]],np.uint8)
    maxwh= np.array([dfwh['hMax'][0],dfwh['sMax'][0],dfwh['vMax'][0]],np.uint8)

    minvbl = np.array([dfbl['hMin'][0],dfbl['sMin'][0],dfbl['vMin'][0]],np.uint8)
    maxvbl= np.array([dfbl['hMax'][0],dfbl['sMax'][0],dfbl['vMax'][0]],np.uint8)
    
    #Assign the calibration data to the corresponding color
    if color == 'orange':
        return minor, maxor
    elif color == 'green':
        return mingr, maxgr
    elif color == 'yellow':
        return minvy, maxvy
    elif color == 'purple':
        return minvpu, maxvpu
    elif color == 'pink':
        return minvp, maxvp
    elif color == 'blue':
        return minvbl, maxvbl
    elif color == 'white':
        return minwh, maxwh
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

    ############################

    minvor,maxvor =colorvalues('orange')
    dilor=20
    eroor=10

    full_maskor,contoursor=detection_color.colori(hsvimage, minvor, maxvor, dilor, eroor, opnv, clsnv)

    ## find centers
    ### centersor is the position of the center of the contours
    ## call findcenter from class color_functions
    centersor,imgor=color_functions.findCenter(image,contoursor)
    text="Orange"

    ## call writeTextInTheCenterOfTheContour from class color_functions
    imgor=color_functions.writeTextInTheCenterOfTheContour(imgor,contoursor,text,0)
    ##plot centers

    #call findsector from class color_functions
    sectorvor,image=color_functions.findsector(image,contoursor)
    print("sectorvorange",sectorvor)
    #put sector in the center of the contour
    ## save centersor in countourscounter
    countourscounter.append(centersor)
    colorcounter.append("Orange")
    sectorcounter.append(sectorvor)

    #call drawBoxAroundObjectWithMask from class color_functions
    imaux=color_functions.drawBoxAroundObjectWithMask(image,full_maskor)
    
    ###############################################
    ####################Green###################
    minvgr,maxvgr =colorvalues('green')

    dilgr=25
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
    imaux=color_functions.drawBoxAroundObjectWithMask(imaux,full_maskgr)
    print("sectorvgreen",sectorvgr)
    ## appen centersor in countourscounter
    countourscounter.append(centersgr)
    colorcounter.append("Green")
    sectorcounter.append(sectorvgr)
    
    #####################
    ###############yellow###################
    minvy,maxvy =colorvalues('yellow')
    dily=25
    eroy=6

    full_maskoy,contoursy=detection_color.colori(hsvimage, minvy, maxvy, dily, eroy, opnv, clsnv)

    ## call findcenter from class color_functions
    centersy,imgy=color_functions.findCenter(image,contoursy)
    text="Yellow"

    ## call writeTextInTheCenterOfTheContour from class color_functions
    imgy=color_functions.writeTextInTheCenterOfTheContour(imgy,contoursy,text,0)

    #call findsector from class color_functions
    sectorvy, image=color_functions.findsector(image,contoursy)
    ## save centersor in countourscounter
    countourscounter.append(centersy)
    colorcounter.append("Yellow")
    sectorcounter.append(sectorvy)

    #call drawBoxAroundObjectWithMask from class color_functions
    imaux=color_functions.drawBoxAroundObjectWithMask(imaux,full_maskoy)
    
    ###############Pink###################
    minvp,maxvp =colorvalues('pink')  
    dilp=10
    erop=2

    full_maskpk,contourspk=detection_color.colori(hsvimage, minvp, maxvp, dilp, erop, opnv, clsnv)

    ## call findcenter from class color_functions
    centerspk,imgpk=color_functions.findCenter(image,contourspk)
    text="Pink"
    
    ## call writeTextInTheCenterOfTheContour from class color_functions
    imgpk=color_functions.writeTextInTheCenterOfTheContour(imgpk,contourspk,text,0)

    #call findsector from class color_functions
    sectorvpk, image=color_functions.findsector(image,contourspk)
    countourscounter.append(centerspk)
    colorcounter.append("Pink")
    sectorcounter.append(sectorvpk)

    #call drawBoxAroundObjectWithMask from class color_functions
    imaux=color_functions.drawBoxAroundObjectWithMask(imaux,full_maskpk)

    ##############Purple####################
    minvpu,maxvpu =colorvalues('purple')
    dilpu=20
    eropu=10

    full_maskpu,contourspu=detection_color.colori(hsvimage, minvpu, maxvpu, dilpu, eropu, opnv, clsnv)
    ## call findcenter from class color_functions
    centerspu,imgpu=color_functions.findCenter(image,contourspu)
    text="Purple"
    
    ## call writeTextInTheCenterOfTheContour from class color_functions
    imgpu=color_functions.writeTextInTheCenterOfTheContour(imgpu,contourspu,text,0)

    #call findsector from class color_functions
    sectorvpu, image=color_functions.findsector(image,contourspu)
    countourscounter.append(centerspu)
    colorcounter.append("Purple")
    sectorcounter.append(sectorvpu)

    #call drawBoxAroundObjectWithMask from class color_functions
    imaux=color_functions.drawBoxAroundObjectWithMask(imaux,full_maskpu)

    ##################Blue######################
    minvbl,maxvbl =colorvalues('blue')  
    dily=15
    eroy=10

    full_maskbl,contoursbl=detection_color.colori(hsvimage, minvbl, maxvbl, dily, eroy, opnv, clsnv)

    ## call findcenter from class color_functions
    centersbl,imgbl=color_functions.findCenter(image,contoursbl)
    text="Blue"

    ## call writeTextInTheCenterOfTheContour from class color_functions
    imgbl=color_functions.writeTextInTheCenterOfTheContour(imgbl,contoursbl,text,0)

    #call findsector from class color_functions
    sectorvbl, image=color_functions.findsector(image,contoursbl)
    countourscounter.append(centersbl)
    colorcounter.append("Blue")
    sectorcounter.append(sectorvbl)

    #call drawBoxAroundObjectWithMask from class color_functions
    imaux=color_functions.drawBoxAroundObjectWithMask(imaux,full_maskbl)
    
    ####################White###################
    minwh,maxwh =colorvalues('white')
    dilwh=20
    erowh=5

    full_maskwh,contourswh=detection_color.colori(hsvimage, minwh, maxwh, dilwh, erowh, opnv, clsnv)
    ## call findcenter from class color_functions
    centerswh,imgwh=color_functions.findCenter(image,contourswh)
    text="White"
    imgwh=color_functions.writeTextInTheCenterOfTheContour(imgwh,contourswh,text,0)
    sectorvwh, image=color_functions.findsector(image,contourswh)
    countourscounter.append(centerswh)
    colorcounter.append("White")
    sectorcounter.append(sectorvwh)
    imaux=color_functions.drawBoxAroundObjectWithMask(imaux,full_maskwh)

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

    maskx=full_maskpu
    return maskx, imaux, listcentersx, listcentersy, listcolor, listsector
