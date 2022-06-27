'''
from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("600x600")

def newTab(*args):
    newFrame = Frame(root, width=500, height=500)
    tabsArea.add(newFrame, text="Untitled.txt")
    text = Text(newFrame)
    text.pack(fill="both", expand=True)

button = Button(root, text="New Tab", command=newTab)
tabsArea = ttk.Notebook(root)

button.pack(side="top")
tabsArea.pack(pady=15, fill="both", expand=True)

# Add the first tab
newTab()

root.mainloop()
'''
from tkinter import *
from tkinter import ttk




class App(Tk):
    def __init__(self):
        super(App, self).__init__()

        self.title("Tkinter Tab Widgets")
        self.minsize(600,400)
        self.wm_iconbitmap("icon.ico")


        tabControl = ttk.Notebook(self)
        self.tab1 = ttk.Frame(tabControl)
        tabControl.add(self.tab1, text = "Tab 1")

        self.tab2 = ttk.Frame(tabControl)
        tabControl.add(self.tab2, text = "Tab 2")
        tabControl.pack(expand = 1, fill = "both")

        self.widgets()


    def widgets(self):

        labelFrame = LabelFrame(self.tab1, text = "First Tab")
        labelFrame.grid(column = 0, row = 0, padx = 8, pady = 4)

        label = Label(labelFrame, text = "Enter Your Name:")
        label.grid(column = 0, row = 0, sticky = 'W')

        textEdit = Entry(labelFrame, width = 20)
        textEdit.grid(column = 1, row = 0)
        label2 = Label(labelFrame, text = "Enter Your Password:")
        label2.grid(column = 0, row = 1)
        textEdit = Entry(labelFrame, width = 20)
        textEdit.grid(column= 1, row = 1)
        labelFrame2 = LabelFrame(self.tab2, text = "Second Tab")
        labelFrame2.grid(column = 0, row = 0, padx = 8, pady = 4)
        label = Label(labelFrame2, text="Enter Your Name:")
        label.grid(column=0, row=0, sticky='W')
        textEdit = Entry(labelFrame2, width=20)
        textEdit.grid(column=1, row=0)
        label2 = Label(labelFrame2, text="Enter Your Password:")
        label2.grid(column=0, row=1)
        textEdit = Entry(labelFrame2, width=20)
        textEdit.grid(column=1, row=1)









app = App()
app.mainloop()
