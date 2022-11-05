import cv2
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from PIL import Image, ImageTk
class Appcompare():
    def __init__(self, master) :
        #add 2 canvas
        self.canvas1 = tk.Canvas(master)
        self.canvas1.pack()
        self.canvas2 = tk.Canvas(master)
        self.canvas2.pack()
        #plot the domains of the image
        #read image
        img = cv2.imread('paperEval.png')
        # read in image with PIL 
        self.original = Image.open('paperEval.png')
        # convert to hsv with opencv
        self.hsv = cv2.cvtColor(np.array(self.original), cv2.COLOR_RGB2HSV)
        #convert to rgb with opencv
        self.rgb = cv2.cvtColor(np.array(self.original), cv2.COLOR_RGB2BGR)
        #separete the image in 3 channels
        #plot scatter plot img
        #separete the image in 3 channels
        b,g,r = cv2.split(self.rgb )
        #read image
        #hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        #separete the image in 3 channels
        h,s,v = cv2.split(self.hsv)
        #plot the scatter plot
        figure1 = plt.figure()
        ax1 = figure1.add_subplot(111, projection='3d')
        ax1.scatter(b, g, r, c='r', marker='o')
        ax1.set_xlabel('Blue')
        ax1.set_ylabel('Green')
        ax1.set_zlabel('Red')
        ax1.set_title('RGB 3D projection')
        chart1 = FigureCanvasTkAgg(figure1, master)
        chart1.get_tk_widget().pack(side="right",fill="both", expand="yes", padx="10", pady="10")
        #plot the domains of the image
        #plot the scatter plot
        figure2 = plt.figure()
        ax2 = figure2.add_subplot(111, projection='3d')
        ax2.scatter(h, s, v, c='r', marker='o')
        ax2.set_xlabel('H')
        ax2.set_ylabel('S')
        ax2.set_zlabel('V')
        ax2.set_title('HSV 3D projection')
        chart2= FigureCanvasTkAgg(figure2, master)
        chart2.get_tk_widget().pack(side="left", fill="both",expand="yes", padx="10", pady="10")


root= tk.Tk()
app=Appcompare(root)
app.mainloop()