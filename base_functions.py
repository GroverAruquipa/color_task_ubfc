import cv2
import numpy as np
import pandas as pd
#dfbl = pd.read_csv('blue.csv')
dfbl=pd.read_csv('files_calibrated/blue.csv')
dfor= pd.read_csv('files_calibrated/orange.csv')
dfgr= pd.read_csv('files_calibrated/green.csv')
dfy= pd.read_csv('files_calibrated/yellow.csv')
dfp= pd.read_csv('files_calibrated/pink.csv')
dfpu= pd.read_csv('files_calibrated/purple.csv')
dfwh= pd.read_csv('files_calibrated/white.csv')
dflimits=pd.read_csv('files_calibrated/limits.csv')
#function without input with the values of hsv orange

def colorvalues(color):
    '''
    naranjamenor = np.array([144,123,105],np.uint8)  ## orange
    naranjamayor = np.array([179,176,255],np.uint8)   ## orange
    minvgr = np.array([25, 75, 86],np.uint8) 
    maxvgr = np.array([91, 250, 255],np.uint8) 
    minvy = np.array([11, 86, 132],np.uint8) 
    maxvy = np.array([21, 255, 255],np.uint8)
    minvp = np.array([150,180,120],np.uint8) 
    maxvp = np.array([180,255,255],np.uint8)   
    minvpu = np.array([129,120,100],np.uint8) 
    maxvpu = np.array([140,150,255],np.uint8)
    '''
    #minvbl = np.array([90,50,70],np.uint8) 
    #maxvbl = np.array([120,255,255],np.uint8)  
    minwh = np.array([90,35,160],np.uint8) 
    maxwh = np.array([133,115,255],np.uint8)
    ## Read blue.csv file with pandas
    #dfbl = pd.read_csv('blue.csv')
    minor= np.array([dfor['hMin'][0],dfor['sMin'][0],dfor['vMin'][0]],np.uint8)
    mayor= np.array([dfor['hMax'][0],dfor['sMax'][0],dfor['vMax'][0]],np.uint8)

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
    if color == 'orange':
        return minor, mayor
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
        # Draw contours
        #img = cv2.drawContours (img, contours, -1, (0, 255, 0), 3)
        #Draw a rectangle around the contour
        for cnt in contours:
            x, y, w, h = cv2.boundingRect (cnt)
            cv2.rectangle (img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        return img
    def eroding_image(img,ker):
        kernel = np.ones (( ker, ker ), np.uint8 )
        erosion = cv2.erode (img, kernel, iterations = 1)
        return erosion
    def dilate_image(img,ker):
        kernel = np.ones (( ker, ker ), np.uint8 )
        dilate = cv2.dilate(img, kernel, iterations=1)
        return dilate

    def writeTextInTheCenterOfTheContour(img,contours,text,offset):
        # Find the center of the contour
        for cnt in contours:
            M = cv2.moments(cnt)
            cx = int (M ['m10'] / M ['m00'])
            cy = int (M ['m01'] / M ['m00'])
            cv2.putText (img, text, (cx, cy+offset), cv2.FONT_ITALIC, 0.6, (0, 0, 0), 2, cv2.LINE_AA)  
        return img

    #function tu find the height and width of the image
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
            #puttext in image
            print(cy)
            cv2.putText (img, str(sector), (cx, cy+20), cv2.FONT_ITALIC, 0.6, (0, 0, 0), 2, cv2.LINE_AA)
            ## appen sector in sectorv 
            sectorv.append(sector)          
        return sectorv,img

class detection_color:
    def __init__(self, image, minv, maxv, dil, ero):
        self.image = image
        self.minv = minv
        self.maxv = maxv
        self.dil = dil
        self.ero = ero
    def colori(hsvimage, minv, maxv, dil, ero):
        full_mask = cv2.inRange(hsvimage, minv, maxv)
        #full_mask=eroding_image(full_mask,ero)
        # call eroding from class color_functions
        full_mask=color_functions.eroding_image(full_mask,ero)
        #full_mask=dilate_image(full_mask,dil)
        # call dilate from class color_functions
        full_mask=color_functions.dilate_image(full_mask,dil)
        #result = cv2.bitwise_and(result, result, mask=full_mask)
        #contours=findContourseOfTheMask(hsvimage,full_mask)
        # call findContourseOfTheMask from class color_functions
        contours=color_functions.findContourseOfTheMask(hsvimage,full_mask)
        return full_mask , contours
    def colori2(hsvimage, minv, maxv, dil, ero): ## orange
        full_mask = cv2.inRange(hsvimage, minv, maxv)
        #full_mask=dilate_image(full_mask,dil)
        full_mask=color_functions.dilate_image(full_mask,dil)
        #full_mask=eroding_image(full_mask,ero)
        #result = cv2.bitwise_and(result, result, mask=full_mask)
        #contours=findContourseOfTheMask(hsvimage,full_mask)
        contours=color_functions.findContourseOfTheMask(hsvimage,full_mask)
        return full_mask , contours

def processImage(img1):
    ##create image 
    #image = cv2.imread('paperEval.png')
    image = img1
    #cv2.imshow("Original", image)
    hsvimage = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    #result = image.copy()
    ###############Orange########################
    countourscounter=[]
    colorcounter=[]
    sectorcounter=[]
    ############To find the region of the center################
    ## Size of the image

    ############################

    #minvor = np.array([144,123,105],np.uint8)  ## orange
    #maxvor = np.array([179,176,255],np.uint8)   ## orange
    minvor,maxvor =colorvalues('orange')
    dilor=20
    eroor=10
    #full_maskor,contoursor=colori(hsvimage, minvor, maxvor, dilor, eroor)
    full_maskor,contoursor=detection_color.colori(hsvimage, minvor, maxvor, dilor, eroor)

    ## findcenters
    #centersor,imgor=findCenter(image,contoursor) ### centersor is the position of the center of the contours
    ## call findcenter from class color_functions
    centersor,imgor=color_functions.findCenter(image,contoursor)
    text="Orange"
    #imgor=writeTextInTheCenterOfTheContour(imgor,contoursor,text,0)
    ## call writeTextInTheCenterOfTheContour from class color_functions
    imgor=color_functions.writeTextInTheCenterOfTheContour(imgor,contoursor,text,0)
    ##plot centers
    #sectorvor,image=findsector(image,contoursor)
    #call findsector from class color_functions
    sectorvor,image=color_functions.findsector(image,contoursor)
    print("sectorvorange",sectorvor)
    #put sector in the center of the contour
    ## appen centersor in countourscounter
    countourscounter.append(centersor)
    colorcounter.append("Orange")
    sectorcounter.append(sectorvor)
    #imaux=drawBoxAroundObjectWithMask(image,full_maskor)
    #call drawBoxAroundObjectWithMask from class color_functions
    imaux=color_functions.drawBoxAroundObjectWithMask(image,full_maskor)
    #
    ###############################################
    ####################Green###################
    #minvgr = np.array([25, 75, 86],np.uint8) 
    #maxvgr = np.array([91, 250, 255],np.uint8)  
    minvgr,maxvgr =colorvalues('green')

    dilgr=40
    erogr=6
    #full_maskgr,contoursgr=colori(hsvimage, minvgr, maxvgr, dilgr, erogr)
    full_maskgr,contoursgr=detection_color.colori(hsvimage, minvgr, maxvgr, dilgr, erogr)
    ## apply opening
    
    #opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
    # apply oppening to the mask
    kernel=np.ones((100,100),np.uint8)
    full_maskgr = cv2.morphologyEx(full_maskgr, cv2.MORPH_OPEN, kernel)
    

    #centersgr,imggr=findCenter(image,contoursgr)
    ## call findcenter from class color_functions
    centersgr,imggr=color_functions.findCenter(image,contoursgr)

    text="Green"
    #imggr=writeTextInTheCenterOfTheContour(imggr,contoursgr,text,0)
    ## call writeTextInTheCenterOfTheContour from class color_functions
    imggr=color_functions.writeTextInTheCenterOfTheContour(imggr,contoursgr,text,0)

    #sectorvgr, image=findsector(image,contoursgr)
    #call findsector from class color_functions
    sectorvgr, image=color_functions.findsector(image,contoursgr)
    #imaux=drawBoxAroundObjectWithMask(imaux,full_maskgr)
    #call drawBoxAroundObjectWithMask from class color_functions
    imaux=color_functions.drawBoxAroundObjectWithMask(imaux,full_maskgr)
    print("sectorvgreen",sectorvgr)
    ## appen centersor in countourscounter
    countourscounter.append(centersgr)
    colorcounter.append("Green")
    sectorcounter.append(sectorvgr)
    #####################
    ###############yellow###################
    #minvy = np.array([11, 86, 132],np.uint8) 
    #maxvy = np.array([21, 255, 255],np.uint8)
    minvy,maxvy =colorvalues('yellow')
    dily=50
    eroy=6
    #full_maskoy,contoursy=colori(hsvimage, minvy, maxvy, dily, eroy)
    full_maskoy,contoursy=detection_color.colori(hsvimage, minvy, maxvy, dily, eroy)
    #centersy,imgy=findCenter(image,contoursy)
    ## call findcenter from class color_functions
    centersy,imgy=color_functions.findCenter(image,contoursy)
    text="Yellow"
    #imgy=writeTextInTheCenterOfTheContour(imgy,contoursy,text,0)
    ## call writeTextInTheCenterOfTheContour from class color_functions
    imgy=color_functions.writeTextInTheCenterOfTheContour(imgy,contoursy,text,0)
    #sectorvy, image=findsector(image,contoursy)
    #call findsector from class color_functions
    sectorvy, image=color_functions.findsector(image,contoursy)
    ## appen centersor in countourscounter
    countourscounter.append(centersy)
    colorcounter.append("Yellow")
    sectorcounter.append(sectorvy)
    #imaux=drawBoxAroundObjectWithMask(imaux,full_maskoy)
    #call drawBoxAroundObjectWithMask from class color_functions
    imaux=color_functions.drawBoxAroundObjectWithMask(imaux,full_maskoy)
    ###############Pink###################
    #minvp = np.array([150,180,120],np.uint8) 
    #maxvp = np.array([180,255,255],np.uint8)
    minvp,maxvp =colorvalues('pink')  
    dilp=20
    erop=2
    #full_maskpk,contourspk=colori(hsvimage, minvy, maxvy, dily, eroy)
    full_maskpk,contourspk=detection_color.colori(hsvimage, minvp, maxvp, dilp, erop)
    #centerspk,imgpk=findCenter(image,contourspk)
    ## call findcenter from class color_functions
    centerspk,imgpk=color_functions.findCenter(image,contourspk)
    text="Pink"
    #imgpk=writeTextInTheCenterOfTheContour(imgpk,contourspk,text,0)
    ## call writeTextInTheCenterOfTheContour from class color_functions
    imgpk=color_functions.writeTextInTheCenterOfTheContour(imgpk,contourspk,text,0)
    #sectorvpk, image=findsector(image,contourspk)
    #call findsector from class color_functions
    sectorvpk, image=color_functions.findsector(image,contourspk)
    countourscounter.append(centerspk)
    colorcounter.append("Pink")
    sectorcounter.append(sectorvpk)

    #imaux=drawBoxAroundObjectWithMask(imaux,full_maskpk)
    #call drawBoxAroundObjectWithMask from class color_functions
    imaux=color_functions.drawBoxAroundObjectWithMask(imaux,full_maskpk)

    ##############Purple####################
    #minvpu = np.array([129,120,100],np.uint8) 
    #maxvpu = np.array([140,150,255],np.uint8)
    minvpu,maxvpu =colorvalues('purple')
    dilpu=40
    eropu=10
    #full_maskpu,contourspu=colori(hsvimage, minvy, maxvy, dily, eroy)
    full_maskpu,contourspu=detection_color.colori(hsvimage, minvpu, maxvpu, dilpu, eropu)
    #centerspu,imgpu=findCenter(image,contourspu)
    ## call findcenter from class color_functions
    centerspu,imgpu=color_functions.findCenter(image,contourspu)
    text="Purple"
    #imgpu=writeTextInTheCenterOfTheContour(imgpu,contourspu,text,0)
    ## call writeTextInTheCenterOfTheContour from class color_functions
    imgpu=color_functions.writeTextInTheCenterOfTheContour(imgpu,contourspu,text,0)
    #sectorvpu, image=findsector(image,contourspu)
    #call findsector from class color_functions
    sectorvpu, image=color_functions.findsector(image,contourspu)
    countourscounter.append(centerspu)
    colorcounter.append("Purple")
    sectorcounter.append(sectorvpu)
    #imaux=drawBoxAroundObjectWithMask(imaux,full_maskpu)
    #call drawBoxAroundObjectWithMask from class color_functions
    imaux=color_functions.drawBoxAroundObjectWithMask(imaux,full_maskpu)

    ##################Blue######################
    #minvbl = np.array([90,50,70],np.uint8) 
    #maxvbl = np.array([120,255,255],np.uint8)
    minvbl,maxvbl =colorvalues('blue')  
    dily=20
    eroy=10
    #full_maskbl,contoursbl=colori(hsvimage, minvy, maxvy, dily, eroy)
    full_maskbl,contoursbl=detection_color.colori(hsvimage, minvbl, maxvbl, dily, eroy)
    #centersbl,imgbl=findCenter(image,contoursbl)
    ## call findcenter from class color_functions
    centersbl,imgbl=color_functions.findCenter(image,contoursbl)
    text="Blue"
    #imgbl=writeTextInTheCenterOfTheContour(imgbl,contoursbl,text,0)
    ## call writeTextInTheCenterOfTheContour from class color_functions
    imgbl=color_functions.writeTextInTheCenterOfTheContour(imgbl,contoursbl,text,0)
    #sectorvbl, image=findsector(image,contoursbl)
    #call findsector from class color_functions
    sectorvbl, image=color_functions.findsector(image,contoursbl)
    countourscounter.append(centersbl)
    colorcounter.append("Blue")
    sectorcounter.append(sectorvbl)
    #imaux=drawBoxAroundObjectWithMask(imaux,full_maskbl)
    #call drawBoxAroundObjectWithMask from class color_functions
    imaux=color_functions.drawBoxAroundObjectWithMask(imaux,full_maskbl)
    ####################White###################
    #minwh = np.array([90,35,160],np.uint8) 
    #maxwh = np.array([133,115,255],np.uint8)
    minwh,maxwh =colorvalues('white')
    dilwh=20
    erowh=5
    #full_maskwh,contourswh=colori(hsvimage, minvy, maxvy, dily, eroy)
    full_maskwh,contourswh=detection_color.colori(hsvimage, minwh, maxwh, dilwh, erowh)
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
