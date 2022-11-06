"""Final GUI """
from tkinter import *
from PIL import Image, ImageTk
import cv2
import os 
import tkinter.filedialog as tkFileDialog

def nothing(x):
    pass

"""Creat a funtion to select an input image to use as a calibration source
    Calirate the colors and save the calibration data as an output in csv files
    to be used in the main code"""

def select_image():
    # grab a reference to the image panels
    global panelA, panelB

    # open a file chooser dialog and allow the user to select an input image
    path = tkFileDialog.askopenfilename() #save the path of the chosen image
    # ensure a file path was selected
    if len(path) > 0:  #if a file has been selected proceed
        # load the image from disk corresponding to the saved path
        image = cv2.imread(path)
        #save image
        cv2.imwrite('paperEval.png',image)
        #tool script will convert the image to grayscale 
        #detect edges in it, set and save the calibration data
        os.system('python tool.py')  # Open python scrpt command line

        
#creat function to call limits 
#code that will allow us to devide the frame into different sections
def limits(): 
    os.system('python limits.py')   # Open python scrpt command line
    
#creat function to the main program to display all the detection and filtering   
def main(): 
    os.system('python main2.py')    # Open python scrpt command line
    
#creat function to call the comparison code to display data dispersion    
def comparision():
    os.system('python comparehuh2.py')  # Open python scrpt command line
    
    
    
# initialize the window toolkit along with the two image panels
root = Tk()
panelA = None
panelB = None


# button to call the video with final results with all the filters applied
btn3 = Button(root, text="show results", command=main)
btn3.pack(side="right", fill="both", expand="yes", padx="10", pady="10")

#Creat button to display graphs to compare RGB and HSV representation
btn4 = Button(root, text="comparaison", command=comparision)
btn4.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")

# create a button, then when pressed, will trigger a file chooser
# dialog and allow the user to select an input image; then add the
btn = Button(root, text="Calibrate color", command=select_image)
btn.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")
#Button to calibrate the limits  
btn2 = Button(root, text="Calibrate 4 Sectors", command=limits)
btn2.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")
# kick off the GUI

root.mainloop()