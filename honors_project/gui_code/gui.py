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
tabControl.add(tab1, text='Connecting to REDIS')
tabControl.add(tab2, text='REDIS output')
tabControl.add(tab3, text='Plotting')
tabControl.pack(expand=1, fill = 'both')
##################################################

##################################################


#Code for tab1 widgets -> Commander Page
label_1 = ttk.Label(tab1, text="Commander Page")
label_1.grid(row=0, column=0, sticky='nw')
#label_1.pack(side='left')

label_exp_1 = ttk.Label(tab1, text="brief explanation of commander page")
label_exp_1.grid(row=1, column=0, sticky='nw')

label_box = ttk.Label(tab1, text="List of commands:")
label_box.grid(row=4, column=0, sticky='sw')



command_text = tk.Text(tab1, height=10)
command_text.grid(row=5, column=0, sticky=tk.EW)
command_text.config(state='disabled')

btn_connect = ttk.Button(tab1, text="Press to connect!")
btn_connect.grid(row=5, column=2)

label_msg = ttk.Label(tab1, text='Enter commands here:')
label_msg.grid(row=8, column=0)

command_msg = tk.StringVar()
msg_box = ttk.Entry(tab1, textvariable=command_msg)
msg_box.grid(row=9, column = 0, padx = 15, pady=15)

def send():
    command_sent = command_msg.get()
    print("the command was: " + command_sent)


btn_send = Button(tab1,text="Send",command=send)
btn_send.grid(row=9, column=1)

#creating text widget that holds commands

#creating scroll bar widget and  set its command to text widget
#scrollbar = ttk.Scrollbar(tab1, orient='vertical', command=text.yview).grid(row=4, column=1, sticky=tk.NS)
#text['yscrollcommand'] = scrollbar.set
#scrollbar.config(command=text.yview)

#just fills the text box with text


'''
for i in range(1,50):
    position = f'{1}.0'
    command_text.insert(position,f'command {i}\n');
'''


'''
past_msg = tk.Label(tab1, height = 10).grid(row=3,column = 0, sticky=tk.EW)
scrollbar = ttk.Scrollbar(tab1, orient='vertical', command=text.yview).grid(row=3,column=1, sticky=tk.NS)
text['yscrollcommand'] = scrollbar.set

for i in range(1,50):
    position = f'{i}.0'
    text.insert(position,f'line {i}\n');
'''
##################################################


#################################################
#Code for tab2 items
label_2 = ttk.Label(tab2, text = "Drone Page").grid(column = 0, row = 0, padx = 30, pady = 30)
output_box = ttk.Label()
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
