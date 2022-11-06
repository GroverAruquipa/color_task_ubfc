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
maskx, imaux, listcentersx, listcentersy, listcolor, listsector, color_mask = processImage(img)


full_filtering=maskx

filtering_pink = color_mask[0]
filtering_purple = color_mask[1]
filtering_blue = color_mask[2]
filtering_white = color_mask[3]
filtering_yellow = color_mask[4]
filtering_orange = color_mask[5]
filtering_green = color_mask[6]



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
plt.plot(hist_full, color='k')

plt.title('full mask histogram')
plt.show()


figure2 = plt.figure(figsize=(10, 5), dpi=100)  #creat figure with given size

his2 = figure2.add_subplot(331)
hist_yellow = cv2.calcHist(filtering_yellow ,[0],None,[256],[0,256])
plt.plot(hist_yellow , color='y')

plt.title('yellow filtering histogram')
plt.show()

his3 = figure2.add_subplot(335)
hist_pink = cv2.calcHist(filtering_pink ,[0],None,[256],[0,256])
plt.plot(hist_pink, color='m')

plt.title('Pink filtering histogram')
plt.show()

his4 = figure2.add_subplot(332)
hist_purple = cv2.calcHist(filtering_purple ,[0],None,[256],[0,256])
plt.plot(hist_purple, color='tab:purple')

plt.title('purple filtering histogram')
plt.show()

his5 = figure2.add_subplot(333)
hist_blue = cv2.calcHist(filtering_blue ,[0],None,[256],[0,256])
plt.plot(hist_blue, color='b')

plt.title('blue filtering histogram')
plt.show()

his6 = figure2.add_subplot(334)
hist_white = cv2.calcHist(filtering_white ,[0],None,[256],[0,256])
plt.plot(hist_white , color='k')

plt.title('white filtering histogram')
plt.show()

his7 = figure2.add_subplot(336)
hist_orange = cv2.calcHist(filtering_orange ,[0],None,[256],[0,256])
plt.plot(hist_orange , color='tab:orange')

plt.title('orange filtering histogram')
plt.show()

his8 = figure2.add_subplot(337)
hist_green = cv2.calcHist(filtering_green ,[0],None,[256],[0,256])
plt.plot(hist_green, color='g')

plt.title('green filtering histogram')
plt.show()



figure3 = plt.figure(figsize=(10, 5), dpi=100)  #creat figure with given size

his9 = figure3.add_subplot(111)

plt.plot(hist_green, color='g')
plt.plot(hist_white , color='k')
plt.plot(hist_orange , color='tab:orange')
plt.plot(hist_blue, color='b')
plt.plot(hist_purple, color='m')
plt.plot(hist_pink, color='tab:purple')
plt.plot(hist_yellow, color='y')
plt.title('all filters histogram')
plt.show()

figure1.suptitle('Histogram final result comparison', fontsize='xx-large')
figure2.suptitle('Histogram filters comparison', fontsize='xx-large')

chart1= FigureCanvasTkAgg(figure1, root)
chart1.draw()
chart1.get_tk_widget().pack(side="top", fill="both",expand="no")

chart2= FigureCanvasTkAgg(figure2, root)
chart2.draw()
chart2.get_tk_widget().pack(side="right", fill="both",expand="no")

chart3= FigureCanvasTkAgg(figure3, root)
chart3.draw()
chart3.get_tk_widget().pack(side="top", fill="both",expand="no")


root.mainloop()