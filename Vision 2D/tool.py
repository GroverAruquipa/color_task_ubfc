"""The tool function to be called from the interface
    is meant to process the image and extract data to be stored
    thus called later on for the main program"""
import cv2
import numpy as np
import pandas as pd


"""Declare Tables to be used to store calibration data extracted from picures,
 i,e, the max and min values of HSV for each color """ 
df=pd.DataFrame(columns=['hMin', 'hMax', 'sMin', 'sMax', 'vMin', 'vMax', 'color'])

dfw=pd.DataFrame(columns=['hMin', 'hMax', 'sMin', 'sMax', 'vMin', 'vMax', 'color'])
dfy=pd.DataFrame(columns=['hMin', 'hMax', 'sMin', 'sMax', 'vMin', 'vMax', 'color'])
dfo=pd.DataFrame(columns=['hMin', 'hMax', 'sMin', 'sMax', 'vMin', 'vMax', 'color'])
dfgreen=pd.DataFrame(columns=['hMin', 'hMax', 'sMin', 'sMax', 'vMin', 'vMax', 'color'])
dfblue=pd.DataFrame(columns=['hMin', 'hMax', 'sMin', 'sMax', 'vMin', 'vMax', 'color'])
dfpink=pd.DataFrame(columns=['hMin', 'hMax', 'sMin', 'sMax', 'vMin', 'vMax', 'color'])
dfpurple=pd.DataFrame(columns=['hMin', 'hMax', 'sMin', 'sMax', 'vMin', 'vMax', 'color'])

"""Fuctions to extract data and save them in a CSV file
    For each color, the HSV max and min are collected and stored in the tables above and an CSV file"""
def nothing(*arg):
    pass
def white(*args):
    print('white')
    global hMin, hMax, sMin, sMax, vMin, vMax
    #Locate and save the calibration values
    dfw.loc[len(dfw)] = [hMin, hMax, sMin, sMax, vMin, vMax, 0]
    #Save date into the CSV file without index (no row indices)    
    dfw.to_csv('white.csv',index=False)
    pass
def yellow(*args):
    print('yellow')
    global hMin, hMax, sMin, sMax, vMin, vMax
    #Locate and save the calibration values
    dfy.loc[len(dfy)] = [hMin, hMax, sMin, sMax, vMin, vMax, 1]
    #Save date into the CSV file without index (no row indices)  
    dfy.to_csv('yellow.csv',index=False)
    pass
def orange(*args):
    print('orange')
    global hMin, hMax, sMin, sMax, vMin, vMax
    dfo.loc[len(dfo)] = [hMin, hMax, sMin, sMax, vMin, vMax, 2]
    #Save date into the CSV file without index (no row indices)  
    dfo.to_csv('orange.csv',index=False)
    pass
def green(*args):
    print('green')
    global hMin, hMax, sMin, sMax, vMin, vMax
    dfgreen.loc[len(dfgreen)] = [hMin, hMax, sMin, sMax, vMin, vMax, 3]
    #Save date into the CSV file without index (no row indices)  
    dfgreen.to_csv('green.csv',index=False)
    pass
def blue(*args):
    print('blue')
    global hMin, hMax, sMin, sMax, vMin, vMax
    dfblue.loc[len(dfblue)] = [hMin, hMax, sMin, sMax, vMin, vMax, 4]
    #Save date into the CSV file without index (no row indices)  
    dfblue.to_csv('blue.csv',index=False)
    pass
def pink(*args):
    print('pink')
    global hMin, hMax, sMin, sMax, vMin, vMax
    dfpink.loc[len(dfpink)] = [hMin, hMax, sMin, sMax, vMin, vMax, 5]
    #Save date into the CSV file without index (no row indices)  
    dfpink.to_csv('pink.csv',index=False)
    pass
def purple(*args):
    print('purple')
    global hMin, hMax, sMin, sMax, vMin, vMax
    dfpurple.loc[len(dfpurple)] = [hMin, hMax, sMin, sMax, vMin, vMax, 6]
    #Save date into the CSV file without index (no row indices)  
    dfpurple.to_csv('purple.csv',index=False)
    pass

# function with button to save the color
    
# Load image
image = cv2.imread('paperEval.png')

# Create a window for the image
cv2.namedWindow('image')

# Create trackbars for color change ibterval
# Hue is from 0-179 for Opencv
cv2.createTrackbar('HMin', 'image', 0, 179, nothing)
cv2.createTrackbar('SMin', 'image', 0, 255, nothing)
cv2.createTrackbar('VMin', 'image', 0, 255, nothing)
cv2.createTrackbar('HMax', 'image', 0, 179, nothing)
cv2.createTrackbar('SMax', 'image', 0, 255, nothing)
cv2.createTrackbar('VMax', 'image', 0, 255, nothing)

##Create buttons to save and exit
cv2.createButton('white', white, None, cv2.QT_PUSH_BUTTON, 1)
cv2.createButton('yellow', yellow, None, cv2.QT_PUSH_BUTTON, 1)
cv2.createButton('orange', orange, None, cv2.QT_PUSH_BUTTON, 1)
cv2.createButton('green', green, None, cv2.QT_PUSH_BUTTON, 1)
cv2.createButton('blue', blue, None, cv2.QT_PUSH_BUTTON, 1)
cv2.createButton('pink', pink, None, cv2.QT_PUSH_BUTTON, 1)
cv2.createButton('purple', purple, None, cv2.QT_PUSH_BUTTON, 1)



# Set default value for Max HSV trackbars
cv2.setTrackbarPos('HMax', 'image', 179)
cv2.setTrackbarPos('SMax', 'image', 255)
cv2.setTrackbarPos('VMax', 'image', 255)

# Initialize HSV min/max values
hMin = sMin = vMin = hMax = sMax = vMax = 0
phMin = psMin = pvMin = phMax = psMax = pvMax = 0

while(1):
    # Get current positions of all trackbars
    hMin = cv2.getTrackbarPos('HMin', 'image')
    sMin = cv2.getTrackbarPos('SMin', 'image')
    vMin = cv2.getTrackbarPos('VMin', 'image')
    hMax = cv2.getTrackbarPos('HMax', 'image')
    sMax = cv2.getTrackbarPos('SMax', 'image')
    vMax = cv2.getTrackbarPos('VMax', 'image')
    
    # Set minimum and maximum HSV values to display
    lower = np.array([hMin, sMin, vMin])
    upper = np.array([hMax, sMax, vMax])

    # Convert to HSV format and color threshold
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(image, image, mask=mask)

    # Print if there is a change in HSV value
    if((phMin != hMin) | (psMin != sMin) | (pvMin != vMin) | (phMax != hMax) | (psMax != sMax) | (pvMax != vMax) ):
        print("(hMin = %d , sMin = %d, vMin = %d), (hMax = %d , sMax = %d, vMax = %d)" % (hMin , sMin , vMin, hMax, sMax , vMax))
        phMin = hMin
        psMin = sMin
        pvMin = vMin
        phMax = hMax
        psMax = sMax
        pvMax = vMax      
    ## if button event is triggered, save the HSV values to csv file
    if cv2.waitKey(1) & 0xFF == ord('w'):
        print('white')
        df = df.append({'wh': [hMin,sMin,vMin,hMax,sMax,vMax]}, ignore_index=True)
        df.to_csv('data.csv',index=False)
    # Display result image
    cv2.imshow('image', result)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
# ctrl p 