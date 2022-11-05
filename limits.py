from tkinter import *
import pandas as pd
class Return_Value_In_Entry():
    def __init__(self):
        
        self.Master=Tk()
        self.Entry1=Entry(self.Master)
        self.Entry1.pack()
        self.Entry2=Entry(self.Master)
        self.Entry2.pack()
        self.Entry3=Entry(self.Master)
        self.Entry3.pack()
        self.Entry4=Entry(self.Master)
        self.Entry4.pack()
        
        # add label title
        self.label = Label(self.Master, text='Insert the limits in percentage:', font=('helvetica', 10))
        self.label.pack()

        self.Button=Button(self.Master,text="Save",command=self.Return)
        # exit button
        self.exitButton = Button(self.Master, text="Exit", command=self.Exit)
        #button save deffault
        self.defaultButton = Button(self.Master, text="Default", command=self.Return)
        self.defaultButton.pack()
        self.Button.pack()
        self.exitButton.pack()            

        self.Master.mainloop()

    def Return(self):
        self.var1=self.Entry1.get()
        self.var2=self.Entry2.get()
        self.var3=self.Entry3.get()
        self.var4=self.Entry4.get()
        #Status of the button save
        if self.Button['state'] == 'active':
            #Save values in a csv file
            df=pd.DataFrame(columns=['limit1', 'limit2', 'limit3', 'limit4'])
            df.loc[0] = [self.var1, self.var2, self.var3, self.var4]
            df.to_csv('limits.csv',index=False)

            #self.Master.destroy()
        if self.defaultButton['state'] == 'active':
            print('default')
            df=pd.DataFrame(columns=['limit1', 'limit2', 'limit3', 'limit4'])
            df.loc[0] = [1, 2, 3, 4]
            df.to_csv('limits.csv',index=False)
            # write default values in the entry
            #clear the entry
            self.Entry1.delete(0, END)
            self.Entry2.delete(0, END)
            self.Entry3.delete(0, END)
            self.Entry4.delete(0, END)
            self.Entry1.insert(0, 1)
            self.Entry2.insert(0, 2)
            self.Entry3.insert(0, 3)
            self.Entry4.insert(0, 4)
            #self.Master.destroy()
        
        print(self.var1)
        print(self.var2)
        print(self.var3)
        print(self.var4)
    def Exit(self):
        self.Master.destroy()

Return_Value_In_Entry() 