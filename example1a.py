import cv2
import numpy as np
import pandas as pd
from tkinter import *
from PIL import Image, ImageTk


from tkinter import *
from PIL import Image, ImageTk

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
        self.xscale = Scale(self.frame2, from_=1, to=1000, orient=HORIZONTAL, command=self.resize)
        self.yscale = Scale(self.frame2, from_=1, to=1000, orient=HORIZONTAL, command=self.resize)
        self.display.pack(fill=BOTH, expand=1)
        self.xscale.pack()
        self.yscale.pack()
        self.pack(fill=BOTH, expand=1)
        self.frame1.pack(fill=BOTH, expand=1)
        self.frame2.pack()
        self.bind("<Configure>", self.resize)
    def hsvthreshold(self, *args):
        pass

    def resize(self, *args):
        size = (self.xscale.get(), self.yscale.get())
        resized = self.original.resize(size,Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(resized)
        self.display.delete("IMG")
        self.display.create_image(self.display.winfo_width()/2, self.display.winfo_height()/2, anchor=CENTER, image=self.image, tags="IMG")

root = Tk()
app = App(root)
app.mainloop()