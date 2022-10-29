import cv2
import numpy as np
import pandas as pd
#Create csv file
dfw=pd.DataFrame(columns=['hMin', 'hMax', 'sMin', 'sMax', 'vMin', 'vMax', 'color'])
dfy=pd.DataFrame(columns=['hMin', 'hMax', 'sMin', 'sMax', 'vMin', 'vMax', 'color'])
dfo=pd.DataFrame(columns=['hMin', 'hMax', 'sMin', 'sMax', 'vMin', 'vMax', 'color'])
dfgreen=pd.DataFrame(columns=['hMin', 'hMax', 'sMin', 'sMax', 'vMin', 'vMax', 'color'])
dfblue=pd.DataFrame(columns=['hMin', 'hMax', 'sMin', 'sMax', 'vMin', 'vMax', 'color'])
dfpink=pd.DataFrame(columns=['hMin', 'hMax', 'sMin', 'sMax', 'vMin', 'vMax', 'color'])
dfpurple=pd.DataFrame(columns=['hMin', 'hMax', 'sMin', 'sMax', 'vMin', 'vMax', 'color'])

#df.to_csv('data.csv',index=False)
def nothing(*arg):
    pass
def white(*args):
    print('white')
    global hMin, hMax, sMin, sMax, vMin, vMax
    # create dfw
    #save values in csv file
    dfw.loc[len(dfw)] = [hMin, hMax, sMin, sMax, vMin, vMax, 0]
    #delete white.csv file    
    dfw.to_csv('white.csv',index=False)
    pass
def yellow(*args):
    print('yellow')
    global hMin, hMax, sMin, sMax, vMin, vMax
    # create dfw
    #save values in csv file
    dfy.loc[len(dfy)] = [hMin, hMax, sMin, sMax, vMin, vMax, 1]
    #delete white.csv file
    
    dfy.to_csv('yellow.csv',index=False)
    pass
def orange(*args):
    print('orange')
    global hMin, hMax, sMin, sMax, vMin, vMax
    dfo.loc[len(dfo)] = [hMin, hMax, sMin, sMax, vMin, vMax, 2]
    dfo.to_csv('orange.csv',index=False)
    pass
def green(*args):
    print('green')
    global hMin, hMax, sMin, sMax, vMin, vMax
    dfgreen.loc[len(dfgreen)] = [hMin, hMax, sMin, sMax, vMin, vMax, 3]
    
    dfgreen.to_csv('green.csv',index=False)
    pass
def blue(*args):
    print('blue')
    global hMin, hMax, sMin, sMax, vMin, vMax
    dfblue.loc[len(dfblue)] = [hMin, hMax, sMin, sMax, vMin, vMax, 4]
    
    dfblue.to_csv('blue.csv',index=False)
    pass
def pink(*args):
    print('pink')
    global hMin, hMax, sMin, sMax, vMin, vMax
    dfpink.loc[len(dfpink)] = [hMin, hMax, sMin, sMax, vMin, vMax, 5]
    dfpink.to_csv('pink.csv',index=False)
    pass
def purple(*args):
    print('purple')
    global hMin, hMax, sMin, sMax, vMin, vMax
    dfpurple.loc[len(dfpurple)] = [hMin, hMax, sMin, sMax, vMin, vMax, 6]
    dfpurple.to_csv('purple.csv',index=False)
    pass

# function with button to save the color
    
# Load image
image = cv2.imread('paperEval.png')

# Create a window
cv2.namedWindow('image')

# Create trackbars for color change
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