"""Final GUI """
from tkinter import *
import PyQt5   ####why not working huh 
from PIL import Image, ImageTk
import cv2
import os 
import tkinter.filedialog as tkFileDialog

def nothing(x):
    pass


def select_image():
    # grab a reference to the image panels
    global panelA, panelB

    # open a file chooser dialog and allow the user to select an input
    # image
    path = tkFileDialog.askopenfilename()
    # ensure a file path was selected
    if len(path) > 0:
        # load the image from disk, convert it to grayscale, and detect
        # edges in it
        image = cv2.imread(path)
        #save image
        cv2.imwrite('paperEval.png',image)
        os.system('python tool.py')

        # Open python scrpt command line

def limits(): 
    os.system('python limits.py')
def main(): 
    os.system('python main2.py')
    
def comparision():
    os.system('python comparehuh.py')
    
    
    
# initialize the window toolkit along with the two image panels
root = Tk()
panelA = None
panelB = None

# create a button, then when pressed, will trigger a file chooser
# dialog and allow the user to select an input image; then add the
# button the GUI
btn3 = Button(root, text="show results", command=main)
btn3.pack(side="right", fill="both", expand="yes", padx="10", pady="10")
btn4 = Button(root, text="comparaison", command=comparision)
btn4.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")
btn = Button(root, text="Calibrate color", command=select_image)
btn.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")
#Button to calibrate the limits  
btn2 = Button(root, text="Calibrate 4 Sectors", command=limits)
btn2.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")
# kick off the GUI

root.mainloop()