#base of python/redis communication gui

#BUILDING THE GUI

#from tkinter import *
#from tkinter import ttk
import tkinter as tk
'''
root = Tk()
frame1 = ttk.Frame(root, padding = 10)
frame1.grid()
ttk.Label(frame1, text = "Hello world!").grid(column = 0, row = 0)
ttk.Button(frame1, text = "Quit", command = root.destroy).grid(column = 1, row = 0)
root.mainloop()
'''
'''
class App(tk.Frame):

	def __init__(self, master):
		super().__init__(master)
		self.pack()

		self.entrythingy = tk.Entry()
		self.entrythingy.pack()

		#create the application varaible
		self.contents = tk.StringVar()

		#set it to some value ??
		self.contents.set("this is a varaible")

		#tell the 'entry widget??' to WATCH this veraible
		self.entrythingy["textvaraible"] = self.contents

		#Define a callback for when the user hits return
		#it prints the current value of the variable
		self.entrythingy.bind('<Key-Return>', self.print_contents)

	def print_contents(self, event):
		print("Hi!! the current entry conent is:",
			self.contents.get())

root = tk.Tk()
myapp = App(root)
myapp.mainloop()
'''


class App(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.pack()

#create the application
myapp = App()

#hehehe methods hehehe windows manager class.... which i don't have?? damn
myapp.master.title("heriugheirug")
myapp.master.maxsize(1000, 400)

#start program!
myapp.mainloop()
