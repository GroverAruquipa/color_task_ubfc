""""This code contains all the functions for the video processing :
    Color recognition using calibration data
    shape detection
    calculating the surface area of each shape
    """
import cv2
import numpy as np
import pandas as pd
########### Global values to open and close operations#########
opnv=30
clsnv = 25
##########################
#Read the CSV files containing the calibration data for each colors
dfbl=pd.read_csv('blue.csv')
dfor= pd.read_csv('orange.csv')
dfgr= pd.read_csv('green.csv')
dfy= pd.read_csv('yellow.csv')
dfp= pd.read_csv('pink.csv')
dfpu= pd.read_csv('purple.csv')
dfwh= pd.read_csv('white.csv')
# File for the limits of the area
dflimits=pd.read_csv('files_calibrated/limits.csv')
#Input: String(color), Output: Min/Max Intervals, 
#Behabioral: This function reads the min and max intervals for the HSV process 
def colorvalues(color):
    #Extract the calibration data from the csv files for color in orange 
    minor= np.array([dfor['hMin'][0],dfor['sMin'][0],dfor['vMin'][0]],np.uint8)
    maxor= np.array([dfor['hMax'][0],dfor['sMax'][0],dfor['vMax'][0]],np.uint8)
    #Extract the calibration data from the csv files for the color Green 
    mingr= np.array([dfgr['hMin'][0],dfgr['sMin'][0],dfgr['vMin'][0]],np.uint8)
    maxgr= np.array([dfgr['hMax'][0],dfgr['sMax'][0],dfgr['vMax'][0]],np.uint8)
    #Lo mismo para yellow
    minvy= np.array([dfy['hMin'][0],dfy['sMin'][0],dfy['vMin'][0]],np.uint8)
    maxvy= np.array([dfy['hMax'][0],dfy['sMax'][0],dfy['vMax'][0]],np.uint8)
    #Lo mismo para pink 
    minvp= np.array([dfp['hMin'][0],dfp['sMin'][0],dfp['vMin'][0]],np.uint8)
    maxvp= np.array([dfp['hMax'][0],dfp['sMax'][0],dfp['vMax'][0]],np.uint8)
    #Lo mismo para purple
    minvpu= np.array([dfpu['hMin'][0],dfpu['sMin'][0],dfpu['vMin'][0]],np.uint8)
    maxvpu= np.array([dfpu['hMax'][0],dfpu['sMax'][0],dfpu['vMax'][0]],np.uint8)
    #Lo mismo white 
    minwh= np.array([dfwh['hMin'][0],dfwh['sMin'][0],dfwh['vMin'][0]],np.uint8)
    maxwh= np.array([dfwh['hMax'][0],dfwh['sMax'][0],dfwh['vMax'][0]],np.uint8)
    #Lo mismo para blue
    minvbl = np.array([dfbl['hMin'][0],dfbl['sMin'][0],dfbl['vMin'][0]],np.uint8)
    maxvbl= np.array([dfbl['hMax'][0],dfbl['sMax'][0],dfbl['vMax'][0]],np.uint8)
    #Assign the calibration data to the corresponding color
    #Orange 
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
    else:
        return ('error')
#Input: Border(string), Output: limits of the area(int)
#Behavioral: This funtions returns the limits of the image
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
#Behavioral: This class contains the functions to processo the image 
class color_functions: 
    #Input: Image(matrix) and mask(binary matrix), Output: Image with the contours(BINARY)
    #Behavioral: This function returns the contours of the image
    def findContourseOfTheMask(img,mask):
        contours, hierarchy = cv2.findContours (mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # Find contours
        return contours
    #Input: Image(matrix) and mask(binary matrix), Output: Image with the contours(BINARY) PLOTED
    #Behavioral: This function returns the main image with the contours of the image
    def plotContours(img,contours):
        img = cv2.drawContours (img, contours, -1, (0, 255, 0), 3)
        return img
    #Input: Image(matrix) and countours(binary), Output: Center of the contour and image with the center(int)
    #Behavioral: This function returns the center of the contour and the image with the center
    def findCenter ( img, contours ):
        centers=[]
        for cnt in contours:
            M = cv2.moments (cnt) # Calculate moments for each contour
            cx = int (M ['m10'] / M ['m00']) # Calculate center of contour
            cy = int (M ['m01'] / M ['m00']) # Calculate center of contour
            centers.append([cx,cy]) # save the center of the contour
            cv2.circle (img, (cx, cy), 5, (255, 0, 0), -1) # Draw center of contour
        return centers,img
    #Input: Image(matrix) and countours(binary), Output: Center of the contour and image with the center plotted(matrix)
    #Behavioral: This function returns the center of the contour and the image with the center plotted
    def plotCenter(img,contours):
        for cnt in contours:
            M = cv2.moments (cnt)
            cx = int (M ['m10'] / M ['m00'])
            cy = int (M ['m01'] / M ['m00'])
            cv2.circle (img, (cx, cy), 5, (255, 0, 0), -1)
        return img
    #Input: Image(matrix) and countours(binary), Output: Image with rectangle around the contour(matrix)
    #Behavioral: This function returns the image with the rectangle around the contour
    def drawBoxAroundObjectWithMask(img,mask):
        contours, hierarchy = cv2.findContours (mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # Find contours
        for cnt in contours:
            x, y, w, h = cv2.boundingRect (cnt) # Find bounding rectangle
            cv2.rectangle (img, (x, y), (x + w, y + h), (0, 255, 0), 2) # Draw bounding rectangle
        return img
   #Input: Image(matrix) and kernel, Output: Image after the erosion(matrix)
    #Behavioral: This function returns the image after the erosion
    def eroding_image(img,ker):
        kernel = np.ones (( ker, ker ), np.uint8 )# Create kernel
        erosion = cv2.erode (img, kernel, iterations = 1)#Erode the image
        return erosion
    #Input: Image(matrix) and kernel, Output: Image after the dilation(matrix)
    #Behavioral: This function returns the image after the dilation
    def dilate_image(img,ker):
        kernel = np.ones (( ker, ker ), np.uint8 )
        dilate = cv2.dilate(img, kernel, iterations=1)#Dilate the image
        return dilate
    #Input: Image(matrix) and kernel, Output: Image after the opening(matrix)
    #Behavioral: This function returns the image after the opening
    def opening_image(img,ker):
        kernel = np.ones (( ker, ker ), np.uint8 )
        opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)#Opening the image
        return opening
    #Input: Image(matrix) and kernel, Output: Image after the closing(matrix)
    #Behavioral: This function returns the image after the closing
    def closing_image(img,ker):
        kernel = np.ones (( ker, ker ), np.uint8 )
        closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)#Closing the image
        return closing
    #Input: Image(matrix) contours(minary matrix), text to plot(string) offset(int), Output: Image with a text(matrix)
    #Behavioral: This function returns the image with a text
    def writeTextInTheCenterOfTheContour(img,contours,text,offset):
        for cnt in contours:
            M = cv2.moments(cnt)
            cx = int (M ['m10'] / M ['m00'])
            cy = int (M ['m01'] / M ['m00'])
            cv2.putText (img, text, (cx, cy+offset), cv2.FONT_ITALIC, 0.6, (0, 0, 0), 2, cv2.LINE_AA)#Write the text in the center of the contour  
        return img
    #Input: Image(matrix) contours(minary matrix), Output: Image with a text of the area limit(matrix) and sector(int)
    #Behavioral: This function returns the image with a text of the area limit
    def findsector(img,contours):
        height, width = img.shape[:2] #Get the height and width of the image
        sectorv=[]
        for cnt in contours:
            M = cv2.moments (cnt)
            cx = int (M ['m10'] / M ['m00'])
            cy = int (M ['m01'] / M ['m00'])
            if cy<=area_limit('4')*height/4 and cy>=area_limit('3')*height/4: #If the center of the contour is in the area 
                sector=1
            if cy<=area_limit('3')*height/4 and cy>=area_limit('2')*height/4:
                sector=2
            if cy<=area_limit('2')*height/4 and cy>=area_limit('1')*height/4:
                sector=3
            if cy<=area_limit('1')*height/4 and cy>=0*height/4:
                sector=4
            print(cy)
            cv2.putText (img, str(sector), (cx, cy+20), cv2.FONT_ITALIC, 0.6, (0, 0, 0), 2, cv2.LINE_AA)  #put,text in image
            sectorv.append(sector)## appen sector in sectorv           
        return sectorv,img

class detection_color:
    #Contructor of the class
    def __init__(self, image, minv, maxv, dil, ero,opn,clsn):
        self.image = image
        self.minv = minv
        self.maxv = maxv
        self.dil = dil
        self.ero = ero
        self.opn = opn
        self.clsn = clsn
#Input: Image(3-matrix(HSV)) minium HSV limit(int), maxium HSV limit(int), dilatation parameter(int), erotion parameter(int), opening parameter(int), closing parameter(int), Output: Image with the contour(matrix) 
#  Output: full_mask: Image with the contour(matrix),contours: Contours of the image(binary matrix)
#Behavioral: This function returns the ithe mask and the contours of the image, for whaterver color is selected
    def colori(hsvimage, minv, maxv, dil, ero, opn, clsn):
        full_mask = cv2.inRange(hsvimage, minv, maxv)
        full_mask=color_functions.eroding_image(full_mask,ero)# call eroding from class color_functions
        full_mask=color_functions.dilate_image(full_mask,dil)# call dilate from class color_functions
        full_mask=color_functions.opening_image(full_mask,opn) # call opening from class color_functions
        full_mask=color_functions.closing_image(full_mask,clsn) # call closing from class color_functions
        contours=color_functions.findContourseOfTheMask(hsvimage,full_mask)# call findContourseOfTheMask from class color_functions
        return full_mask , contours
#iNPUT:IMAGE(3-MATRIX Rgb(FRAME)), OUTPUT:IMAGE(3-MATRIX HSV)
#output: maskx(Masks of the colors, matrixes(binary)), imaux(FInal image with all the information 3-Matrix), listcentersx(centers for the fram)(list), listcentersy(list), listcolor(list), listsector(list)
#Behavioral: This function returns the masks of the colors, the final image with all the information, the centers for the frame, the list of the colors and the list of the sectors
def processImage(img1):
    image = img1
    countourscounter=[]
    colorcounter=[]
    sectorcounter=[]
    hsvimage = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) #Convert image from BGR to HSV
    ###############Orange########################
    minvor,maxvor =colorvalues('orange')
    dilor=20 #dilate parameter 
    eroor=10 #erotion parameter
    full_maskor,contoursor=detection_color.colori(hsvimage, minvor, maxvor, dilor, eroor, opnv, clsnv)
    centersor,imgor=color_functions.findCenter(image,contoursor) ## call findcenter from class color_functions
    text="Orange"
    imgor=color_functions.writeTextInTheCenterOfTheContour(imgor,contoursor,text,0)# call writeTextInTheCenterOfTheContour from class color_functions
    sectorvor,image=color_functions.findsector(image,contoursor)# call findsector from class color_functions
    print("sectorvorange",sectorvor)
    countourscounter.append(centersor)## save centersor in countourscounter
    colorcounter.append("Orange")
    sectorcounter.append(sectorvor)
    imaux=color_functions.drawBoxAroundObjectWithMask(image,full_maskor)# drwa box around object with mask
    ####################Green###################
    minvgr,maxvgr =colorvalues('green')
    dilgr=25
    erogr=6
    full_maskgr,contoursgr=detection_color.colori(hsvimage, minvgr, maxvgr, dilgr, erogr, opnv, clsnv)
    kernel=np.ones((100,100),np.uint8)
    full_maskgr = cv2.morphologyEx(full_maskgr, cv2.MORPH_OPEN, kernel)
    centersgr,imggr=color_functions.findCenter(image,contoursgr) ## call findcenter from class color_functions
    text="Green"
    imggr=color_functions.writeTextInTheCenterOfTheContour(imggr,contoursgr,text,0)
    sectorvgr, image=color_functions.findsector(image,contoursgr)
    imaux=color_functions.drawBoxAroundObjectWithMask(imaux,full_maskgr)
    print("sectorvgreen",sectorvgr)
    countourscounter.append(centersgr)  ## appen centersor in countourscounter
    colorcounter.append("Green")
    sectorcounter.append(sectorvgr)
    ###############yellow###################
    minvy,maxvy =colorvalues('yellow')
    dily=25
    eroy=6
    full_maskoy,contoursy=detection_color.colori(hsvimage, minvy, maxvy, dily, eroy, opnv, clsnv)
    centersy,imgy=color_functions.findCenter(image,contoursy)## call findcenter from class color_functions
    text="Yellow"    
    imgy=color_functions.writeTextInTheCenterOfTheContour(imgy,contoursy,text,0)## call writeTextInTheCenterOfTheContour from class color_functions
    sectorvy, image=color_functions.findsector(image,contoursy)#call findsector from class color_functions
    countourscounter.append(centersy) ## save centersor in countourscounter
    colorcounter.append("Yellow")# Appen the color type in colorcounter
    sectorcounter.append(sectorvy) # Appen the sector type in sectorcounter
    imaux=color_functions.drawBoxAroundObjectWithMask(imaux,full_maskoy)#call drawBoxAroundObjectWithMask from class color_functions
    ###############Pink###################
    minvp,maxvp =colorvalues('pink')  
    dilp=10
    erop=2
    full_maskpk,contourspk=detection_color.colori(hsvimage, minvp, maxvp, dilp, erop, opnv, clsnv)    
    centerspk,imgpk=color_functions.findCenter(image,contourspk)## call findcenter from class color_functions
    text="Pink"
    imgpk=color_functions.writeTextInTheCenterOfTheContour(imgpk,contourspk,text,0)## call writeTextInTheCenterOfTheContour from class color_functions
    sectorvpk, image=color_functions.findsector(image,contourspk)#call findsector from class color_functions
    countourscounter.append(centerspk)
    colorcounter.append("Pink")
    sectorcounter.append(sectorvpk)
    imaux=color_functions.drawBoxAroundObjectWithMask(imaux,full_maskpk)#call drawBoxAroundObjectWithMask from class color_functions
    ##############Purple####################
    minvpu,maxvpu =colorvalues('purple')
    dilpu=20
    eropu=10
    full_maskpu,contourspu=detection_color.colori(hsvimage, minvpu, maxvpu, dilpu, eropu, opnv, clsnv)
    centerspu,imgpu=color_functions.findCenter(image,contourspu)## call findcenter from class color_functions
    text="Purple"
    imgpu=color_functions.writeTextInTheCenterOfTheContour(imgpu,contourspu,text,0)## call writeTextInTheCenterOfTheContour from class color_functions
    sectorvpu, image=color_functions.findsector(image,contourspu)#call findsector from class color_functions
    countourscounter.append(centerspu)
    colorcounter.append("Purple")
    sectorcounter.append(sectorvpu)    
    imaux=color_functions.drawBoxAroundObjectWithMask(imaux,full_maskpu)#call drawBoxAroundObjectWithMask from class color_functions
    ##################Blue######################
    minvbl,maxvbl =colorvalues('blue')  
    dily=15
    eroy=10
    full_maskbl,contoursbl=detection_color.colori(hsvimage, minvbl, maxvbl, dily, eroy, opnv, clsnv)
    centersbl,imgbl=color_functions.findCenter(image,contoursbl)## call findcenter from class color_functions
    text="Blue"
    imgbl=color_functions.writeTextInTheCenterOfTheContour(imgbl,contoursbl,text,0)## call writeTextInTheCenterOfTheContour from class color_functions    
    sectorvbl, image=color_functions.findsector(image,contoursbl)#call findsector from class color_functions
    countourscounter.append(centersbl)
    colorcounter.append("Blue")
    sectorcounter.append(sectorvbl)
    imaux=color_functions.drawBoxAroundObjectWithMask(imaux,full_maskbl)#call drawBoxAroundObjectWithMask from class color_functions
    ####################White###################
    minwh,maxwh =colorvalues('white')
    dilwh=20
    erowh=5
    full_maskwh,contourswh=detection_color.colori(hsvimage, minwh, maxwh, dilwh, erowh, opnv, clsnv)
    centerswh,imgwh=color_functions.findCenter(image,contourswh)## call findcenter from class color_functions
    text="White"
    imgwh=color_functions.writeTextInTheCenterOfTheContour(imgwh,contourswh,text,0)
    sectorvwh, image=color_functions.findsector(image,contourswh)
    countourscounter.append(centerswh)
    colorcounter.append("White")
    sectorcounter.append(sectorvwh)
    imaux=color_functions.drawBoxAroundObjectWithMask(imaux,full_maskwh)  
    countourscounter1=np.array(countourscounter)#convert countourscounter to numpy array
    listcentersx=[]#append countourcounter lists to a list
    listcentersy=[]
    listcolor=[]
    listsector=[]
    counter=0
    for i in range(len(countourscounter)): #for to countourscounter
        for j in range(len(countourscounter[i])):
            counter=counter+1
            listcentersx.append(countourscounter[i][j][0]) #append x coordinate to listcentersx
            listcentersy.append(countourscounter[i][j][1]) #append y coordinate to listcentersy
            listcolor.append(colorcounter[i]) #append color to listcolor
            listsector.append(sectorcounter[i][j]) #append sector to listsector
            print('The centers are')
            print(countourscounter[i][j])
            text=str(counter)
            center=countourscounter[i][j]#save countourscounter[i][j] in center
            cv2.putText (imaux, text, (center[0]+20, center[1]+20), cv2.FONT_ITALIC, 0.6, (255, 255, 255), 2, cv2.LINE_AA)#write the number of the center in the image
    maskx=full_maskpu#save full_maskpu in maskx
    return maskx, imaux, listcentersx, listcentersy, listcolor, listsector
