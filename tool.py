import cv2 #Library for image processing
import numpy as np #Library for numerical operations
import pandas as pd #Library for data manipulation
from tkinter import * #Library for GUI
from PIL import Image, ImageTk #Library for image processing
############## Creating the df files #######
dfwhite=pd.DataFrame(columns=['hMin', 'hMax', 'sMin', 'sMax', 'vMin', 'vMax', 'color']) #create a dataframe for white color
dfyellow=pd.DataFrame(columns=['hMin', 'hMax', 'sMin', 'sMax', 'vMin', 'vMax', 'color']) #create a dataframe for yellow color
dforange=pd.DataFrame(columns=['hMin', 'hMax', 'sMin', 'sMax', 'vMin', 'vMax', 'color']) #create a dataframe for orange color
dfgreen=pd.DataFrame(columns=['hMin', 'hMax', 'sMin', 'sMax', 'vMin', 'vMax', 'color']) #create a dataframe for green color
dfblue=pd.DataFrame(columns=['hMin', 'hMax', 'sMin', 'sMax', 'vMin', 'vMax', 'color']) #create a dataframe for blue color
dfpink=pd.DataFrame(columns=['hMin', 'hMax', 'sMin', 'sMax', 'vMin', 'vMax', 'color']) #create a dataframe for pink color
dfpurple=pd.DataFrame(columns=['hMin', 'hMax', 'sMin', 'sMax', 'vMin', 'vMax', 'color'])#create a dataframe for purple color
class App(Frame):#Class for the GUI 
    def __init__(self, master):###The function init hepls to create the window and the sliders
        Frame.__init__(self, master) #create the window
        self.frame1 = Frame(self)
        self.frame2 = Frame(self)
        self.original = Image.open('paperEval.png')
        self.hsv = cv2.cvtColor(np.array(self.original), cv2.COLOR_RGB2HSV) # convert to hsv with opencv
        self.image = ImageTk.PhotoImage(Image.fromarray(self.hsv)) #show self.hsv in tkinter
        self.display = Canvas(self.frame1) #create a canvas
        self.SliderHmin = Scale(self.frame2, from_=0, to=255, orient=HORIZONTAL, command=self.hsvthreshold)#create a slider for Hmin
        self.SliderHmax = Scale(self.frame2, from_=0, to=255, orient=HORIZONTAL, command=self.hsvthreshold) #create a slider for Hmax
        self.SliderSmin = Scale(self.frame2, from_=0, to=255, orient=HORIZONTAL, command=self.hsvthreshold)#create a slider for Smin
        self.SliderSmax = Scale(self.frame2, from_=0, to=255, orient=HORIZONTAL, command=self.hsvthreshold)#create a slider for Smax
        self.SliderVmin = Scale(self.frame2, from_=0, to=255, orient=HORIZONTAL, command=self.hsvthreshold)#create a slider for Vmin
        self.SliderVmax = Scale(self.frame2, from_=0, to=255, orient=HORIZONTAL, command=self.hsvthreshold)#create a slider for Vmax
        #Create label for each slider
        self.labelHmin = Label(self.frame2, text="Hmin")#create a label for Hmin
        self.labelHmax = Label(self.frame2, text="Hmax")#create a label for Hmax
        self.labelSmin = Label(self.frame2, text="Smin")#create a label for Smin
        self.labelSmax = Label(self.frame2, text="Smax")#create a label for Smax
        self.labelVmin = Label(self.frame2, text="Vmin")#create a label for Vmin
        self.labelVmax = Label(self.frame2, text="Vmax")#create a label for Vmax
        #Create buttons for green, blue, red, yellow, orange, purple, pink, white, black
        self.green = Button(self.frame2, text="Green", command=self.hsvthreshold)#create a button for green
        self.blue = Button(self.frame2, text="Blue", command=self.hsvthreshold)#create a button for blue
        self.white = Button(self.frame2, text="White", command=self.hsvthreshold)#create a button for white
        self.yellow = Button(self.frame2, text="Yellow", command=self.hsvthreshold)#create a button for yellow
        self.orange = Button(self.frame2, text="Orange", command=self.hsvthreshold)#create a button for orange
        self.purple = Button(self.frame2, text="Purple", command=self.hsvthreshold)#create a button for purple
        self.pink = Button(self.frame2, text="Pink", command=self.hsvthreshold)#create a button for pink
        self.defv = Button(text='Default values', command=self.hsvthreshold, bg='green', fg='white', font=('helvetica', 9, 'bold'))#create a button for default values
        self.close = Button(text='Close', command=self.close_window, bg='brown', fg='white', font=('helvetica', 9, 'bold'))#create a button for closing the window
        ########INitial condditions slider#############
        self.SliderHmin.set(0)
        self.SliderHmax.set(255)
        self.SliderSmin.set(0)
        self.SliderSmax.set(255)
        self.SliderVmin.set(0)
        self.SliderVmax.set(255)
        #########################################33
        self.pack(fill=BOTH, expand=1)#pack the window
        self.frame1.pack(side=LEFT, fill=BOTH, expand=1)#pack the frame1
        self.frame2.pack(side=BOTTOM, fill=BOTH, expand=1)#pack the frame2
        self.display.pack(fill=BOTH, expand=1)#pack the canvas
        self.SliderHmin.pack()
        self.SliderHmax.pack()
        self.SliderSmin.pack()#pack the slider for Smin
        self.SliderSmax.pack()
        self.SliderVmin.pack()
        self.SliderVmax.pack()#pack the sliders Vmax
        '''
        self.labelHmin.pack()
        self.labelHmax.pack()
        self.labelSmin.pack()
        self.labelSmax.pack()
        self.labelVmin.pack()
        self.labelVmax.pack()
        '''
        self.blue.pack()#pack the button blue
        self.white.pack()
        self.yellow.pack()
        self.orange.pack()
        self.purple.pack()#pack the button purple
        self.pink.pack()
        self.defv.pack()
        self.close.pack()#pack the button close
        self.bind("<Configure>", self.hsvthreshold)#bind the function hsvthreshold to the window
    def hsvthreshold(self, *args):#function to create the mask(Not input) is working similar to a callback function!!!!!!!!!
        global hMin, hMax, sMin, sMax, vMin, vMax #global variables
        Hmin = self.SliderHmin.get()#get the value of the slider Hmin
        Hmax = self.SliderHmax.get()
        Smin = self.SliderSmin.get()
        Smax = self.SliderSmax.get()#get the value of the slider Smax
        Vmin = self.SliderVmin.get()
        Vmax = self.SliderVmax.get()#get the value of the slider Vmax
        lower = np.array([Hmin,Smin,Vmin])#create a lower array
        upper = np.array([Hmax,Smax,Vmax])#create a upper array
        mask = cv2.inRange(self.hsv, lower, upper)#create a mask
        self.bgr2 = cv2.cvtColor(self.hsv, cv2.COLOR_HSV2BGR)#convert the hsv image to bgr
        res= cv2.bitwise_and(self.bgr2,self.bgr2, mask= mask)#create a res image
        self.image = ImageTk.PhotoImage(Image.fromarray(res))#convert the res image to a photoimage
        self.display.delete("IMG")#delete the previous image
        self.display.create_image(self.display.winfo_width()/1.2, self.display.winfo_height()/1.2, anchor=CENTER, image=self.image, tags="IMG")#create a new image
        self.resize()#resize the image
        self.display.pack(fill=BOTH, expand=1)#pack the canvas
        self.frame1.pack(fill=BOTH, expand=1)#pack the frame1
        if self.green['state'] == 'active':#if the button green is active
            print('green')
            dfgreen.loc[0] = [Hmin, Hmax, Smin, Smax, Vmin, Vmax, 3]#add the values to the dataframe
            dfgreen.to_csv('green.csv', index=False)#save the dataframe to a csv file
        if self.blue['state'] == 'active':#if the button blue is active
            print('blue')
            dfblue.loc[0] = [Hmin, Hmax, Smin, Smax, Vmin, Vmax, 2]
            dfblue.to_csv('blue.csv', index=False)
        if self.white['state'] == 'active':
            print('white')
            dfwhite.loc[0] = [Hmin, Hmax, Smin, Smax, Vmin, Vmax, 1]#add the values to the dataframe
            dfwhite.to_csv('white.csv', index=False)#save the dataframe to a csv file
        if self.yellow['state'] == 'active':
            print('yellow')
            dfyellow.loc[0] = [Hmin, Hmax, Smin, Smax, Vmin, Vmax, 4]#add the values to the dataframe yellow
            dfyellow.to_csv('yellow.csv', index=False)#save the dataframe to a csv file yellow
        if self.orange['state'] == 'active':
            print('orange')
            dforange.loc[0] = [Hmin, Hmax, Smin, Smax, Vmin, Vmax, 5]
            dforange.to_csv('orange.csv', index=False)
        if self.purple['state'] == 'active':
            print('purple')
            dfpurple.loc[0] = [Hmin, Hmax, Smin, Smax, Vmin, Vmax, 6]
            dfpurple.to_csv('purple.csv', index=False)
        if self.pink['state'] == 'active':
            print('pink')
            dfpink.loc[0] = [Hmin, Hmax, Smin, Smax, Vmin, Vmax, 7]#add the values to the dataframe 
            dfpink.to_csv('pink.csv', index=False) #save the dataframe to a csv file
        if self.defv['state'] == 'active':#if the button default is active save the default values
            print('default')
            #Print the values of the sliders
            dfgreen.loc[0] = [25, 91, 75, 250, 86, 255, 3]
            dfgreen.to_csv('green.csv', index=False)
            dfblue.loc[0] = [90, 120, 50, 255, 70, 255, 0]
            dfblue.to_csv('blue.csv', index=False)
            dfwhite.loc[0] = [90, 133, 35, 115, 160, 255, 0]#add the values to the dataframe dfwhite
            dfwhite.to_csv('white.csv', index=False)#save the dataframe to a csv file dfwhite
            dfyellow.loc[0] = [11, 21, 86, 255, 132, 255, 1]#add the values to the dataframe dfyellow
            dfyellow.to_csv('yellow.csv', index=False)#save the dataframe to a csv file dfyellow
            dforange.loc[0] = [144, 179, 123, 176, 105, 255, 2]
            dforange.to_csv('orange.csv', index=False)
            dfpurple.loc[0] = [129, 140, 120, 150, 100, 255, 0]
            dfpurple.to_csv('purple.csv', index=False)
            dfpink.loc[0] = [150, 180, 180, 255, 120, 255, 5]#pink
            dfpink.to_csv('pink.csv', index=False)  # Print the values of the sliders
    def close_window(self):#function to close the window and destroy the object(NO input)
        self.master.destroy()#destroy the object
        pass
root = Tk()#create the root
root.geometry("800x600")#set the size of the window
app = App(root)#create the object
app.mainloop()#start the mainloop