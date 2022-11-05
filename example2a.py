import cv2
import numpy as np
import pandas as pd
from tkinter import *
from PIL import Image, ImageTk

dfwhite=pd.DataFrame(columns=['hMin', 'hMax', 'sMin', 'sMax', 'vMin', 'vMax', 'color'])
dfyellow=pd.DataFrame(columns=['hMin', 'hMax', 'sMin', 'sMax', 'vMin', 'vMax', 'color'])
dforange=pd.DataFrame(columns=['hMin', 'hMax', 'sMin', 'sMax', 'vMin', 'vMax', 'color'])
dfgreen=pd.DataFrame(columns=['hMin', 'hMax', 'sMin', 'sMax', 'vMin', 'vMax', 'color'])
dfblue=pd.DataFrame(columns=['hMin', 'hMax', 'sMin', 'sMax', 'vMin', 'vMax', 'color'])
dfpink=pd.DataFrame(columns=['hMin', 'hMax', 'sMin', 'sMax', 'vMin', 'vMax', 'color'])
dfpurple=pd.DataFrame(columns=['hMin', 'hMax', 'sMin', 'sMax', 'vMin', 'vMax', 'color'])

class App(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.frame1 = Frame(self)
        self.frame2 = Frame(self)
        self.original = Image.open('paperEval.png')
        # convert to hsv with opencv
        self.hsv = cv2.cvtColor(np.array(self.original), cv2.COLOR_RGB2HSV)

        #show self.hsv in tkinter
        self.image = ImageTk.PhotoImage(Image.fromarray(self.hsv))
        #self.original= cv2.imread('paperEval.png')
        
        #self.image = ImageTk.PhotoImage(self.original) 
   

        self.display = Canvas(self.frame1)
        #self.xscale = Scale(self.frame2, from_=1, to=1000, orient=HORIZONTAL, command=self.resize)
        #self.yscale = Scale(self.frame2, from_=1, to=1000, orient=HORIZONTAL, command=self.resize)
        self.SliderHmin = Scale(self.frame2, from_=0, to=255, orient=HORIZONTAL, command=self.hsvthreshold)
        self.SliderHmax = Scale(self.frame2, from_=0, to=255, orient=HORIZONTAL, command=self.hsvthreshold)
        self.SliderSmin = Scale(self.frame2, from_=0, to=255, orient=HORIZONTAL, command=self.hsvthreshold)
        self.SliderSmax = Scale(self.frame2, from_=0, to=255, orient=HORIZONTAL, command=self.hsvthreshold)
        self.SliderVmin = Scale(self.frame2, from_=0, to=255, orient=HORIZONTAL, command=self.hsvthreshold)
        self.SliderVmax = Scale(self.frame2, from_=0, to=255, orient=HORIZONTAL, command=self.hsvthreshold)
        #Create buttons for green, blue, red, yellow, orange, purple, pink, white, black
        self.green = Button(self.frame2, text="Green", command=self.hsvthreshold)
        self.blue = Button(self.frame2, text="Blue", command=self.hsvthreshold)
        self.white = Button(self.frame2, text="White", command=self.hsvthreshold)
        self.yellow = Button(self.frame2, text="Yellow", command=self.hsvthreshold)
        self.orange = Button(self.frame2, text="Orange", command=self.hsvthreshold)
        self.purple = Button(self.frame2, text="Purple", command=self.hsvthreshold)
        self.pink = Button(self.frame2, text="Pink", command=self.hsvthreshold)
        
        self.green.pack()
        self.blue.pack()
        self.white.pack()
        self.yellow.pack()
        self.orange.pack()
        self.purple.pack()
        self.pink.pack()

        self.display.pack(fill=BOTH, expand=1)
        self.SliderHmin.pack()
        self.SliderHmax.pack()
        self.SliderSmin.pack()
        self.SliderSmax.pack()
        self.SliderVmin.pack()
        self.SliderVmax.pack()
        self.pack(fill=BOTH, expand=1)
        self.frame1.pack(fill=BOTH, expand=1)
        self.frame2.pack()
        self.bind("<Configure>", self.hsvthreshold)
        #self.bind("<Configure>", self.resize)
    def hsvthreshold(self, *args):
       
        #resize image
        #self.resize()
        #get values from sliders
        global hMin, hMax, sMin, sMax, vMin, vMax
        Hmin = self.SliderHmin.get()
        Hmax = self.SliderHmax.get()
        Smin = self.SliderSmin.get()
        Smax = self.SliderSmax.get()
        Vmin = self.SliderVmin.get()
        Vmax = self.SliderVmax.get()
        #threshold hsv
        lower = np.array([Hmin,Smin,Vmin])
        upper = np.array([Hmax,Smax,Vmax])
        mask = cv2.inRange(self.hsv, lower, upper)
        #bitwise and mask original image
        res = cv2.bitwise_and(self.hsv,self.hsv, mask= mask)
        #show thresholded image
        self.image = ImageTk.PhotoImage(Image.fromarray(res))
        #self.image = ImageTk.PhotoImage(Image.fromarray(self.hsv))
        self.display.delete("IMG")
        #display image 
        self.display.create_image(self.display.winfo_width()/4, self.display.winfo_height()/4, anchor=CENTER, image=self.image, tags="IMG")
        #get value button for green and save Hmin, Hmax, Smin, Smax, Vmin, Vmax in csv
        #greenvar=self.green.ge
        #obtaing the status of green button
       
        if self.green['state'] == 'active':
            print('green')
            #Print the values of the sliders
            dfgreen.loc[0] = [Hmin, Hmax, Smin, Smax, Vmin, Vmax, 3]
            dfgreen.to_csv('green.csv', index=False)
        if self.blue['state'] == 'active':
            print('blue')
            #Print the values of the sliders
            dfblue.loc[0] = [Hmin, Hmax, Smin, Smax, Vmin, Vmax, 2]
            dfblue.to_csv('blue.csv', index=False)
        if self.white['state'] == 'active':
            print('white')
            #Print the values of the sliders
            dfwhite.loc[0] = [Hmin, Hmax, Smin, Smax, Vmin, Vmax, 1]
            dfwhite.to_csv('white.csv', index=False)
        if self.yellow['state'] == 'active':
            print('yellow')
            #Print the values of the sliders
            dfyellow.loc[0] = [Hmin, Hmax, Smin, Smax, Vmin, Vmax, 4]
            dfyellow.to_csv('yellow.csv', index=False)
        if self.orange['state'] == 'active':
            print('orange')
            #Print the values of the sliders
            dforange.loc[0] = [Hmin, Hmax, Smin, Smax, Vmin, Vmax, 5]
            dforange.to_csv('orange.csv', index=False)
        if self.purple['state'] == 'active':
            print('purple')
            #Print the values of the sliders
            dfpurple.loc[0] = [Hmin, Hmax, Smin, Smax, Vmin, Vmax, 6]
            dfpurple.to_csv('purple.csv', index=False)
        if self.pink['state'] == 'active':
            print('pink')
            #Print the values of the sliders
            dfpink.loc[0] = [Hmin, Hmax, Smin, Smax, Vmin, Vmax, 7]
            dfpink.to_csv('pink.csv', index=False)
        

        pass





root = Tk()
app = App(root)
app.mainloop()