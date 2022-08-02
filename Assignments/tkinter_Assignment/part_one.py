#imports tkinter module
from tkinter import *

#creates a window and assigns it to the variable "win"
win = Tk()
#creates buttons for the window
#the class "Button" takes the parent window as the first argument
#Just doing the following commands won't allow the buttons to appear in the window
#They must first be placed with a geometry manager
#the two most common are "pack" and "grid"

sb = Scrollbar(win, orient=VERTICAL)
lb = Listbox(win, height=3)
v = StringVar()
e = Entry(win, textvariable = v)
f = Frame(win)
'''
b1 = Button(f, text="One")
b2 = Button(f, text="Two")
b3 = Button(f, text="Three")
l = Label(win, text="This label is over all buttons")
'''
def but1():
    print("Button one was pushed")

def but2():
    print("Button two was pushed")


#"pack" you tell you widget to pack itself into its parent.
#a side may be specified (TOP, LEFT, RIGHT, BOTTOM), TOP is default
'''
b1.pack(side=LEFT)
b1.configure(command=but1)
b2.pack(side=LEFT)
b2.configure(command=but2)
b3.pack(side=LEFT)
b3.configure(command=but1)
l.pack()
'''
lb.pack()
e.pack()
f.pack()

sb.pack(side=LEFT, fill=Y)
sb.configure(comman=lb.yview)
lb.configure(yscrollcommand=sb.set)

lb.insert(END, "first entry")
lb.insert(END, "second entry")
lb.insert(END, "third entry")
lb.insert(END, "fourth entry")
'''

b1.grid(row=0, column=0)
b2.grid(row=1, column=1)
b3.grid(row=2, column=2)
b4.grid(row=3, column=3)
l.grid(row=0, column=1)
'''
