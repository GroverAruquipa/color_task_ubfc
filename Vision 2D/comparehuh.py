import cv2
import tkinter as tk
import matplotlib as mtp
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.figure import Figure



root= tk.Tk()
root.title("Comparaison")

mtp.use("TkAgg")

canvas = tk.Canvas(root)

#plot the domains of the image
#read image
img = cv2.imread('paperEval.png')
b,g,r = cv2.split(img)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(hsv)

#plot the scatter plot
figure1 = plt.figure(figsize=(10, 5), dpi=100)

ax1 = figure1.add_subplot(121, projection='3d')

ax1.scatter(b, g, r ,cmap=cm.jet)
ax1.set_xlabel('Blue')
ax1.set_ylabel('Green')
ax1.set_zlabel('Red')
ax1.set_title('RGB 3D projection')


ax2 = figure1.add_subplot(122, projection='3d')
ax2.plot_surface(h, s, v, cmap=cm.jet)
ax2.set_xlabel('H')
ax2.set_ylabel('S')
ax2.set_zlabel('V')
ax2.set_title('HSV 3D projection')

chart2= FigureCanvasTkAgg(figure1, root)
chart2.get_tk_widget().pack(side="top", fill="both",expand="no")

root.mainloop()