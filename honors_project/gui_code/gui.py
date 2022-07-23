#necessary imports for gui
from gui_commander import *
#import gui_commander
#from gui_commander import enter_ip, connect
import tkinter as tk
from tkinter import *
from tkinter import ttk #notebook module import
import redis
import os

#creating the root
root = tk.Tk() #creating parent window
#root.geometry("600x600")
root.title("Experimentation GUI")

#code for items in main GUI
title = tk.Label(root, text="Communication GUI")
title.pack()

label_box = ttk.Label(root, text="List of commands:")
label_box.pack()

command_text = tk.Text(root, height=10)
command_text.insert(INSERT, "00:'hello commander!'")
#command_text.grid(sticky='ew')
command_text.pack()
command_text.config(state='disabled')


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

#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################

#################################################
#Code for tab1 items#############################
#################################################

label_1 = ttk.Label(tab1, text="Commander Page", font=('tnr', 20))
label_1.grid(row=0, column=0, sticky='nw')
#label_1.pack(side='left')

label_exp_1 = ttk.Label(tab1, text="brief explanation of commander page")
label_exp_1.grid(row=1, column=0, sticky='nw', pady=20)



#def connect():
 #   print("connection achieved!")

def dis_connect():
    print("connection severed!")

#ip_address_entered=0

def enter_ip():
    ip_address_entered = ip_address.get()
    print(ip_address_entered)
    print('enter ip pressed')

def get_ip():

    print('get ip!')
    return ip_address.get()


label_ip = ttk.Label(tab1, text='Enter ip address:')
label_ip.grid(row=8,column=0, sticky='w')
ip_address = tk.StringVar()
ip_text = ttk.Entry(tab1, textvariable=ip_address)
ip_text.grid(row=9, column=0, sticky='w')
btn_ip = ttk.Button(tab1, text='enter ip', command=enter_ip)
btn_ip.grid(row=10,column =0,sticky='w')


def connect_press():
    ip_address_con = get_ip()
    connect(ip_address_con)



btn_connect = ttk.Button(tab1, text="Press to connect!", command=connect_press)
btn_connect.grid(row=13,column=0, sticky='w')



label_msg = ttk.Label(tab1, text='Enter commands here:')
label_msg.grid(row=15, column=0, sticky='w',pady=10)

command_msg = tk.StringVar()
msg_box = ttk.Entry(tab1, textvariable=command_msg)
msg_box.grid(row=16, column = 0, sticky='w')

def send():
    command_sent = command_msg.get()
    print("the command was: " + command_sent)


btn_send = Button(tab1,text="Send",command=send)
btn_send.grid(row=17, column=0,sticky='w')
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################

#################################################
#Code for tab2 items#############################
#################################################

label_2 = ttk.Label(tab2, text = "Drone Page", font=('tnr',20))
label_2.grid(column = 0, row = 0, sticky='nw')


def enter_ip_2():
    ip_address_entered = ip_address_2.get()
    print(ip_address_entered)
    print('enter ip 2 pressed')

def get_ip_2():

    print('get ip 2!')
    return ip_address_2.get()

label_ip_2 = ttk.Label(tab2, text='Enter ip address for Drone:')
label_ip_2.grid(row=8,column=0, sticky='w')
ip_address_2 = tk.StringVar()
ip_text_2 = ttk.Entry(tab2, textvariable=ip_address_2)
ip_text_2.grid(row=9, column=0, sticky='w')
btn_ip_2 = ttk.Button(tab2, text='enter ip', command=enter_ip_2)
btn_ip_2.grid(row=10,column =0,sticky='w')


def connect_press_2():
    ip_address_con = get_ip_2()
    print(ip_address_con)
    #connect(ip_address_con)


btn_connect_2 = ttk.Button(tab2, text="Press to connect 2!", command=connect_press_2)
btn_connect_2.grid(row=13,column=0, sticky='w')

output_box = tk.Text(tab2, height=10)
output_box.grid(row=20, column=0, sticky='s')
output_box.config(state='normal')
output_box.insert(INSERT, "testing")
output_box.config(state='disable')
output_box.config(state='normal')
output_box.insert(INSERT,"\ntesting 2")
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################

#################################################
#Code for tab3 items#############################
#################################################

ttk.Label(tab3, text = "Data organization").grid(column=0, row=0, padx=30, pady=30)
#################################################
root.mainloop()

'''
window = Tk()
window.title("hello header")
window.mainloop()
'''
