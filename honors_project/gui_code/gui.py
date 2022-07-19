import tkinter as tk
from tkinter import *
from tkinter import ttk #notebook module import
#from tkinter.messagebox import askyesno

#creating the root
root = tk.Tk() #creating parent window
#root.geometry("600x600")
root.title("Experimentation GUI")

#code for items in main GUI
title = tk.Label(root, text="Communication GUI")
title.pack()



##################################################
#code to create multiple tabs within the gui
notebook = ttk.Notebook(root)
tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)

#creating and adding tabs to the GUI
tabControl.add(tab1, text='REDIS Communication')
tabControl.add(tab2, text='REDIS output')
tabControl.add(tab3, text='Plotting')
tabControl.pack(expand=1, fill = 'both')
##################################################

##################################################


#Code for tab1 widgets -> Commander Page
label_1 = ttk.Label(tab1, text="Commander Page", font=('tnr', 20))
label_1.grid(row=0, column=0, sticky='nw')
#label_1.pack(side='left')

label_exp_1 = ttk.Label(tab1, text="brief explanation of commander page")
label_exp_1.grid(row=1, column=0, sticky='nw', pady=20)

label_box = ttk.Label(tab1, text="List of commands:")
label_box.grid(row=4, column=0, sticky='sw')

command_text = tk.Text(tab1, height=10)
command_text.insert(INSERT, "00:'hello commander!'")
command_text.grid(row=5, column=0, sticky='ew')
command_text.config(state='disabled')

btn_connect = ttk.Button(tab1, text="Press to connect!")
btn_connect.grid(row=5, column=2, sticky='w')

label_msg = ttk.Label(tab1, text='Enter commands here:')
label_msg.grid(row=8, column=0, sticky='w',pady=10)

command_msg = tk.StringVar()
msg_box = ttk.Entry(tab1, textvariable=command_msg)
msg_box.grid(row=9, column = 0, sticky='w')

def send():
    command_sent = command_msg.get()
    print("the command was: " + command_sent)


btn_send = Button(tab1,text="Send",command=send)
btn_send.grid(row=10, column=0,sticky='w')
#################################################


#################################################
#Code for tab2 items
label_2 = ttk.Label(tab2, text = "Drone Page", font=('tnr',20))
label_2.grid(column = 0, row = 0, sticky='nw')

output_box = tk.Text(tab2, height=10)
output_box.grid(row=5, column=0, sticky='ew')
output_box.config(state='normal')
output_box.insert(INSERT, "testing")
output_box.config(state='disable')
output_box.config(state='normal')
output_box.insert(INSERT,"\ntesting 2")
#################################################





################################################
#Code for tab3 items
ttk.Label(tab3, text = "Data organization").grid(column=0, row=0, padx=30, pady=30)
#################################################
root.mainloop()

'''
window = Tk()
window.title("hello header")
window.mainloop()
'''
