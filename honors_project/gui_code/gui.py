import tkinter as tk
from tkinter import *
from tkinter import ttk #notebook module import
#from tkinter.messagebox import askyesno

#creating the root
root = tk.Tk() #creating parent window
#root.geometry("600x600")
root.title("Experimentation GUI")

#code for items in main GUI
title = tk.Label(root, text="GUI TITLE")
title.pack()



##################################################
#code to create multiple tabs within the gui
notebook = ttk.Notebook(root)
tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)

#creating and adding tabs to the GUI
tabControl.add(tab1, text='Connecting to REDIS')
tabControl.add(tab2, text='REDIS output')
tabControl.add(tab3, text='Plotting')
tabControl.pack(expand=1, fill = 'both')
##################################################

##################################################
#Code for tab1 widgets -> Commander Page
label_1 = ttk.Label(tab1, text="Commander Page").grid(column = 0, row = 0, padx = 30, pady = 30)

command_msg = tk.StringVar()
msg_box = ttk.Entry(tab1,textvariable=command_msg).grid(column = 0, row=1, padx = 15, pady=15)
msg_box.focus()
print(command_msg)

btn_msg = ttk.Button(tab1, text="Press to connect!").grid(column=0,row=2,padx=15,pady=15)
##################################################


#################################################
#Code for tab2 items
label_2 = ttk.Label(tab2, text = "Drone Page").grid(column = 0, row = 0, padx = 30, pady = 30)


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

