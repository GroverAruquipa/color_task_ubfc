"""Code to compare data dispertion between RGB and HSV representations.
    First we compare 3D dispertion than a histogram to better see the noise"""
import cv2
import tkinter as tk
import matplotlib as mtp
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.figure import Figure


##Creating an interface since this code is to be called from the main GUI
root= tk.Tk()
root.title("Comparaison")

mtp.use("TkAgg")  ##Agg rendering to a Tk canvas

canvas = tk.Canvas(root)


#read image
img = cv2.imread('paperEval.png')

"""" Split the input image into RGB colors :
    the outputs b,g,r are vectors containing the
    blue, green and red values for each pixel of the input image"""
b,g,r = cv2.split(img)
#convert input image from RGB to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
"""    the outputs h,s,v are vectors containing the
    hue, saturation and value values for each pixel of the input image"""
h,s,v = cv2.split(hsv)

            #################################################
            #illustrate 3D representation of data dispersion#
            #################################################
figure1 = plt.figure(figsize=(10, 5), dpi=100)  #creat figure with given size

ax1 = figure1.add_subplot(121, projection='3d') #devide figure into subplot of x,y,z axes

ax1.scatter(b, g, r, cmap=cm.jet, marker='.' ) #scatter plot of the RGB data into 3D space
####set graph infos####
ax1.set_xlabel('Blue')     #axis x for blue values
ax1.set_ylabel('Green')    #axis y for green values
ax1.set_zlabel('Red')      #axis z for red values
ax1.set_title('RGB 3D projection')   #set title for the subplot



ax2 = figure1.add_subplot(122, projection='3d') #devide figure into subplot of x,y,z axes
ax2.scatter(h, s, v,c=(h+s+v), cmap=cm.jet, marker='.') #scatter plot of HSV data into 3D space
####set graph infos####
ax2.set_xlabel('H')       #axis x for Hue values
ax2.set_ylabel('S')       #axis y for saturation values
ax2.set_zlabel('V')       #axis z for Value values
ax2.set_title('HSV 3D projection') #set title for the subplot
 
figure1.suptitle('3D projection comparison', fontsize='xx-large') #set title for the figure

###Dsiplay results in a Tkinter canvas as a figure hence the use of mtp.use("TkAgg")
chart1= FigureCanvasTkAgg(figure1, root) #display figure1 containing 3D projections in the main window
chart1.draw()
chart1.get_tk_widget().pack(side="top", fill="both",expand="no")  #pack canva and place figure at the top

        ################################################
           #illustrate histograms of data dispersion#
        ################################################
figure2 = plt.figure(figsize=(10, 5), dpi=100) #creat a second figure with the same size as the first

his1 = figure2.add_subplot(121) #devide the second figure into two subplots
#calculate Histograme for Blue Red and Green data and then store them in seperate arrays 
hist_b = cv2.calcHist([b],[0],None,[256],[0,256])   #Histogram for blue values
hist_g = cv2.calcHist([g],[0],None,[256],[0,256])   #Histogram for green values
hist_r = cv2.calcHist([r],[0],None,[256],[0,256])   #Histogram for red values
plt.plot(hist_r, color='r', label="r")              #Plot Histogram for blue values and hold
plt.plot(hist_g, color='g', label="g")              #Plot Histogram for green values and hold
plt.plot(hist_b, color='b', label="b")              #Plot Histogram for red values
plt.legend()                                        #display legends for each graph
plt.title('RGB histogram')                          #Set title for subfigure 1
plt.show()                                          #Plot the 3 histograms in the same figure

    
his2 = figure2.add_subplot(122)#devide the second figure into two subplots
#calculate Histograme for HSV data and then store them in seperate arrays 
hist_h = cv2.calcHist([h],[0],None,[256],[0,256])   #Histogram for Hue values
hist_s = cv2.calcHist([s],[0],None,[256],[0,256])   #Histogram for Saturation values
hist_v = cv2.calcHist([v],[0],None,[256],[0,256])   #Histogram for Value values
plt.plot(hist_h, color='r', label="h")              #Plot Histogram for Hue values and hold
plt.plot(hist_s, color='g', label="s")              #Plot Histogram for Saturation values and hold
plt.plot(hist_v, color='b', label="v")              #Plot Histogram for Values values and hold
plt.legend()                                        #display legends for each graph
plt.title('HSV histogram')                          #Set title for subfigure 2
plt.show()                                          #Plot the 3 histograms in the same figure

figure2.suptitle('Histogram comparison', fontsize='xx-large')  #set title for the figure

###Dsiplay results in a Tkinter canvas as a figure hence the use of mtp.use("TkAgg")
chart2= FigureCanvasTkAgg(figure2, root) #display figure1 containing 3D projections in the main window
chart2.draw()
chart2.get_tk_widget().pack(side="bottom", fill="both",expand="no") #pack canva and place figure at the top


root.mainloop()