import cv2
import tkinter as tk
import matplotlib as mtp
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from base_functions import *


root= tk.Tk()
root.title("Filters Histograms")
mtp.use("TkAgg")
canvas = tk.Canvas(root)

#insert the different filtering results
img = cv2.imread('paperEval.png')
b,g,r = cv2.split(img)
full_filtering=cv2.split("insert final image after filtering here")
Treshold_img = ("insert treshhol result here")
Erosion_img = ("insert erosion result here")
Dilatation_img = ("insert dilatation here")
opening_img=("insert openin result here")
closing_img=("inser closing result here")


figure1 = plt.figure(figsize=(10, 5), dpi=100)  #creat figure with given size

his1 = figure1.add_subplot(121) #devide the second figure into two subplots
#calculate Histograme for Blue Red and Green data and then store them in seperate arrays 
hist_b = cv2.calcHist([b],[0],None,[256],[0,256])   #Histogram for blue values
hist_g = cv2.calcHist([g],[0],None,[256],[0,256])   #Histogram for green values
hist_r = cv2.calcHist([r],[0],None,[256],[0,256])   #Histogram for red values
plt.plot(hist_r, color='r', label="r")              #Plot Histogram for blue values and hold
plt.plot(hist_g, color='g', label="g")              #Plot Histogram for green values and hold
plt.plot(hist_b, color='b', label="b")              #Plot Histogram for red values
plt.legend()                                        #display legends for each graph
plt.title('RGB histogram')                          #Set title for subfigure 1       
plt.show() 
    
his2 = figure1.add_subplot(122)
hist_full = cv2.calcHist(full_filtering,[0],None,[256],[0,256])
plt.plot(hist_full, color='b', label="v")
plt.legend()
plt.title('full mask histogram')
plt.show()


figure2 = plt.figure(figsize=(10, 5), dpi=100)  #creat figure with given size
his2 = figure2.add_subplot(312)
hist_Tresh = cv2.calcHist(Treshold_img,[0],None,[256],[0,256])
plt.plot(hist_Tres, color='b', label="v")
plt.legend()
plt.title('full mask histogram')
plt.show()

his3 = figure2.add_subplot(321)
hist_Erosion = cv2.calcHist(erosion_img,[0],None,[256],[0,256])
plt.plot(hist_Dilution, color='r', label="h")
plt.legend()
plt.title('erosion histogram')
plt.show()

his4 = figure2.add_subplot(322)
hist_Dilution = cv2.calcHist(dilusion_img,[0],None,[256],[0,256])
plt.plot(hist_Dilution, color='r', label="h")
plt.legend()
plt.title('Dilusion histogram')
plt.show()

his5 = figure2.add_subplot(323)
hist_Opening = cv2.calcHist(opeing_img,[0],None,[256],[0,256])
plt.plot(hist_Opening, color='b', label="v")
plt.legend()
plt.title('Opening histogram')
plt.show()

his6 = figure2.add_subplot(324)
hist_Closing = cv2.calcHist(closing_img,[0],None,[256],[0,256])
plt.plot(hist_Closing, color='r', label="h")
plt.legend()
plt.title('Closing histogram')
plt.show()

figure1.suptitle('Histogram final result comparison', fontsize='xx-large')

figure2.suptitle('Histogram filters comparison', fontsize='xx-large')

chart1= FigureCanvasTkAgg(figure1, root)
chart1.draw()
chart1.get_tk_widget().pack(side="bottom", fill="both",expand="no")

root.mainloop()