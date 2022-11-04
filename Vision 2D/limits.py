import tkinter as tk
import pandas as pd
root= tk.Tk()

canvas1 = tk.Canvas(root, width=400, height=300, relief='raised')
canvas1.pack()

label1 = tk.Label(root, text='Insert the limits in percentage:', font=('helvetica', 10))
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='Type numbers linke 1, 2, 3, 4:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry(root) 
canvas1.create_window(200, 140, window=entry1)
entry2= tk.Entry(root)
canvas1.create_window(200, 160, window=entry2)
entry3= tk.Entry(root)
canvas1.create_window(200, 180, window=entry3)
entry4= tk.Entry(root)
canvas1.create_window(200, 200, window=entry4)
def get_square_root():
    x1 = entry1.get()
    x2= entry2.get()
    x3= entry3.get()
    x4= entry4.get()
    #save x1, x2, x3, x4 in csv file
    dfw=pd.DataFrame(columns=['limit1', 'limit2', 'limit3', 'limit4'])
    dfw.loc[len(dfw)] = [x1, x2, x3, x4]
    dfw.to_csv('limits.csv',index=False)

    #label4 = tk.Label(root, text=float(x1)**0.5, font=('helvetica', 10, 'bold'))
    #canvas1.create_window(200, 230, window=label4)
    
button1 = tk.Button(text='Save the values', command=get_square_root, bg='green', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 240, window=button1)
# Exit button   
button2 = tk.Button(text='Exit Application', command=root.destroy, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 280, window=button2)
root.mainloop()