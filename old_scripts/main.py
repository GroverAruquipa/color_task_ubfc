import cv2
import numpy as np
import pandas as pd
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

def colori(hsvimage, minv, maxv, dil, ero): ## orange
    full_mask = cv2.inRange(hsvimage, minv, maxv)
    full_mask=eroding_image(full_mask,ero)
    full_mask=dilate_image(full_mask,dil)
    #result = cv2.bitwise_and(result, result, mask=full_mask)
    contours=findContourseOfTheMask(hsvimage,full_mask)
    return full_mask , contours
def colori2(hsvimage, minv, maxv, dil, ero): ## orange
    full_mask = cv2.inRange(hsvimage, minv, maxv)
    full_mask=dilate_image(full_mask,dil)
    full_mask=eroding_image(full_mask,ero)
    #result = cv2.bitwise_and(result, result, mask=full_mask)
    contours=findContourseOfTheMask(hsvimage,full_mask)
    return full_mask , contours
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
        if cy<=4*height/4 and cy>=3*height/4:
            sector=1
        if cy<=3*height/4 and cy>=2*height/4:
            sector=2
        if cy<=2*height/4 and cy>=1*height/4:
            sector=3
        if cy<=1*height/4 and cy>=0*height/4:
            sector=4
        #puttext in image
        print(cy)
        cv2.putText (img, str(sector), (cx, cy+20), cv2.FONT_ITALIC, 0.6, (0, 0, 0), 2, cv2.LINE_AA)
        ## appen sector in sectorv 
        sectorv.append(sector)          
    return sectorv,img
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

    minvor = np.array([144,123,105],np.uint8)  ## orange
    maxvor = np.array([179,176,255],np.uint8)   ## orange
    dilor=20
    eroor=10
    full_maskor,contoursor=colori(hsvimage, minvor, maxvor, dilor, eroor)
    ## findcenters
    centersor,imgor=findCenter(image,contoursor) ### centersor is the position of the center of the contours
    text="Orange"
    imgor=writeTextInTheCenterOfTheContour(imgor,contoursor,text,0)
    ##plot centers
    sectorvor,image=findsector(image,contoursor)
    print("sectorvorange",sectorvor)
    #put sector in the center of the contour
    ## appen centersor in countourscounter
    countourscounter.append(centersor)
    colorcounter.append("Orange")
    sectorcounter.append(sectorvor)
    imaux=drawBoxAroundObjectWithMask(image,full_maskor);
    #
    ###############################################
    ####################Green###################
    minvgr = np.array([25, 75, 86],np.uint8) 
    maxvgr = np.array([91, 250, 255],np.uint8)  
    dilgr=40
    erogr=6
    full_maskgr,contoursgr=colori(hsvimage, minvgr, maxvgr, dilgr, erogr)
    ## apply opening
    
    #opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
    # apply oppening to the mask
    kernel=np.ones((100,100),np.uint8)
    full_maskgr = cv2.morphologyEx(full_maskgr, cv2.MORPH_OPEN, kernel)
    

    centersgr,imggr=findCenter(image,contoursgr)
    text="Green"
    imggr=writeTextInTheCenterOfTheContour(imggr,contoursgr,text,0)

    sectorvgr, image=findsector(image,contoursgr)
    imaux=drawBoxAroundObjectWithMask(imaux,full_maskgr);
    print("sectorvgreen",sectorvgr)
    ## appen centersor in countourscounter
    countourscounter.append(centersgr)
    colorcounter.append("Green")
    sectorcounter.append(sectorvgr)
    #####################
    ###############yellow###################
    minvy = np.array([11, 86, 132],np.uint8) 
    maxvy = np.array([21, 255, 255],np.uint8)  
    dily=50
    eroy=6
    full_maskoy,contoursy=colori(hsvimage, minvy, maxvy, dily, eroy)
    centersy,imgy=findCenter(image,contoursy)
    text="Yellow"
    imgy=writeTextInTheCenterOfTheContour(imgy,contoursy,text,0)
    sectorvy, image=findsector(image,contoursy)

    ## appen centersor in countourscounter
    countourscounter.append(centersy)
    colorcounter.append("Yellow")
    sectorcounter.append(sectorvy)
    imaux=drawBoxAroundObjectWithMask(imaux,full_maskoy);
    ###############Pink###################
    minvy = np.array([150,180,120],np.uint8) 
    maxvy = np.array([180,255,255],np.uint8)  
    dily=20
    eroy=2
    full_maskpk,contourspk=colori(hsvimage, minvy, maxvy, dily, eroy)
    centerspk,imgpk=findCenter(image,contourspk)
    text="Pink"
    imgpk=writeTextInTheCenterOfTheContour(imgpk,contourspk,text,0)
    sectorvpk, image=findsector(image,contourspk)
    countourscounter.append(centerspk)
    colorcounter.append("Pink")
    sectorcounter.append(sectorvpk)

    imaux=drawBoxAroundObjectWithMask(imaux,full_maskpk);

    ##############Purple####################
    minvy = np.array([129,120,100],np.uint8) 
    maxvy = np.array([140,150,255],np.uint8)  
    dily=40
    eroy=10
    full_maskpu,contourspu=colori(hsvimage, minvy, maxvy, dily, eroy)
    centerspu,imgpu=findCenter(image,contourspu)
    text="Purple"
    imgpu=writeTextInTheCenterOfTheContour(imgpu,contourspu,text,0)
    sectorvpu, image=findsector(image,contourspu)
    countourscounter.append(centerspu)
    colorcounter.append("Purple")
    sectorcounter.append(sectorvpu)
    imaux=drawBoxAroundObjectWithMask(imaux,full_maskpu)

    ##################Blue######################
    minvy = np.array([90,50,70],np.uint8) 
    maxvy = np.array([120,255,255],np.uint8)  
    dily=20
    eroy=10
    full_maskbl,contoursbl=colori(hsvimage, minvy, maxvy, dily, eroy)
    centersbl,imgbl=findCenter(image,contoursbl)
    text="Blue"
    imgbl=writeTextInTheCenterOfTheContour(imgbl,contoursbl,text,0)
    sectorvbl, image=findsector(image,contoursbl)
    countourscounter.append(centersbl)
    colorcounter.append("Blue")
    sectorcounter.append(sectorvbl)
    imaux=drawBoxAroundObjectWithMask(imaux,full_maskbl)
    ####################White###################
    minvy = np.array([90,35,160],np.uint8) 
    maxvy = np.array([133,115,255],np.uint8)  
    dily=20
    eroy=5
    full_maskwh,contourswh=colori(hsvimage, minvy, maxvy, dily, eroy)
    centerswh,imgwh=findCenter(image,contourswh)
    text="White"
    imgwh=writeTextInTheCenterOfTheContour(imgwh,contourswh,text,0)
    sectorvwh, image=findsector(image,contourswh)
    countourscounter.append(centerswh)
    colorcounter.append("White")
    sectorcounter.append(sectorvwh)
    imaux=drawBoxAroundObjectWithMask(imaux,full_maskwh)
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

cap = cv2.VideoCapture('paperEval.mp4')
out=cv2.VideoWriter('result_output.avi',cv2.VideoWriter_fourcc(*'DIVX'), 15, (640,480))
counterframe=1
while(cap.isOpened()):
    ret, frame = cap.read()
    # Eliminate shadows and noise
    #frame = cv2.GaussianBlur(frame, (5, 5), 0)
    frame = cv2.medianBlur(frame, 5)
    #frame = cv2.bilateralFilter(frame, 9, 75, 75)
    #frame = cv2.fastNlMeansDenoisingColored(frame,None,10,10,7,21)
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
            break
    else:
        break
    counterframe=counterframe+1
out.release()



