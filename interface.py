
# import the necessary packages
from tkinter import *
from PIL import Image
from PIL import ImageTk
import tkinter.filedialog as tkFileDialog
import cv2
import os 
def nothing(x):
    pass


def select_image():
    # grab a reference to the image panels
    global panelA, panelB

    # open a file chooser dialog and allow the user to select an input
    # image
    path = tkFileDialog.askopenfilename()
    #os.system('/home/grover/my_env/scripts/color_detection/tool.py')
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

# initialize the window toolkit along with the two image panels
root = Tk()
panelA = None
panelB = None

# create a button, then when pressed, will trigger a file chooser
# dialog and allow the user to select an input image; then add the
# button the GUI
btn = Button(root, text="Select an image and calibrate color", command=select_image)
btn.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")
#Button to calibrate the limits  
btn2 = Button(root, text="Calibrate 4 Sectors", command=limits)
btn2.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")
# kick off the GUI
root.mainloop()