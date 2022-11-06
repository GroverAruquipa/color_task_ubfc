from tkinter import * #Library to create the GUI
import pandas as pd #Library for data manipulation
class Return_Value_In_Entry(): #Class to return the value of the entry
    def __init__(self): #Constructor of the class
        self.Master=Tk() #Create the window
        self.Entry1=Entry(self.Master) #Create the entry 1
        self.Entry1.pack() #Show the entry 1 in the window
        self.Entry2=Entry(self.Master)
        self.Entry2.pack()
        self.Entry3=Entry(self.Master) #Create the entry 1 
        self.Entry3.pack()  #Show the entry 1 in the window
        self.Entry4=Entry(self.Master)
        self.Entry4.pack()
        self.label = Label(self.Master, text='Insert the limits in percentage:', font=('helvetica', 10)) #Create the label 
        self.label.pack()#Show the label in the window 
        self.Button=Button(self.Master,text="Save",command=self.Return) #Create the button to save the limits 
        self.exitButton = Button(self.Master, text="Exit", command=self.Exit) #Create the button to exit the window
        self.defaultButton = Button(self.Master, text="Default", command=self.Return) #Create the button to save the limits
        self.defaultButton.pack()#Show the button in the window
        self.Button.pack()#Show the button in the window 
        self.exitButton.pack() #Show the button in the window           
        self.Master.mainloop()#Show the window 
    def Return(self):#Function to return the value of the entry
        self.var1=self.Entry1.get()#Get the value of the entry 1 
        self.var2=self.Entry2.get()#Get the value of the entry 2
        self.var3=self.Entry3.get()#Get the value of the entry 3
        self.var4=self.Entry4.get()#Get the value of the entry 4
        if self.Button['state'] == 'active':#Check if the button is active
            df=pd.DataFrame(columns=['limit1', 'limit2', 'limit3', 'limit4'])#Create a data frame with the limits
            df.loc[0] = [self.var1, self.var2, self.var3, self.var4]#Add the limits to the data frame
            df.to_csv('limits.csv',index=False)#Save the data frame as a csv file
        if self.defaultButton['state'] == 'active':#Check if the button is active
            print('default')
            df=pd.DataFrame(columns=['limit1', 'limit2', 'limit3', 'limit4'])#Create a data frame with the limits
            df.loc[0] = [1, 2, 3, 4]#Add the limits to the data frame 
            df.to_csv('limits.csv',index=False)#Save the data frame as a csv file
            self.Entry1.delete(0, END)#Delete the value of the entry 1 
            self.Entry2.delete(0, END)#Delete the value of the entry 2
            self.Entry3.delete(0, END)#Delete the value of the entry 3
            self.Entry4.delete(0, END)#Delete the value of the entry 4
            self.Entry1.insert(0, 1) #Insert the value of the entry 1
            self.Entry2.insert(0, 2) #Insert the value of the entry 2
            self.Entry3.insert(0, 3) #Insert the value of the entry 3
            self.Entry4.insert(0, 4) #Insert the value of the entry 4
        print(self.var1)
        print(self.var2)
        print(self.var3)
        print(self.var4)
    def Exit(self):
        self.Master.destroy() #Destroy the window
Return_Value_In_Entry() #Call the class