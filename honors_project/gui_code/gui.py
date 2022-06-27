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
#Code for tab1 items
ttk.Label(tab1, text="Commander Page").grid(column = 0, row = 0, padx = 30, pady = 30)
'''
text = Text(tab1)
text.pack(fill="both", expand=True)
'''
'''
input_text = StringVar()
entry1 = ttk.Entry(tab1, textvariable = input_text, justify = CENTER)
entry1.focus_force()
entry1.pack(side = TOP, ipadx = 30, ipady = 6)
'''

#ttk.combobox(tab1, text = "Enter commands here")
##################################################

#################################################
#Code for tab2 items
ttk.Label(tab2, text = "Drone Page").grid(column = 0, row = 0, padx = 30, pady = 30)
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

