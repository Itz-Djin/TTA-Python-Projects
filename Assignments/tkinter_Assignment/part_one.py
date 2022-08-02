#imports tkinter module
from tkinter import *

#creates a window and assigns it to the variable "win"
win = Tk()

#creates buttons for the window
#the class "Button" takes the parent window as the first argument
#Just doing the following commands won't allow the buttons to appear in the window
#They must first be placed with a geometry manager
#the two most common are "pack" and "grid"

b1 = Button(win, text="One")
b2 = Button(win, text="Two")

b3 = Button(win, text="Three")
'''
b4 = Button(win, text="Four")

#"pack" you tell you widget to pack itself into its parent.
#a side may be specified (TOP, LEFT, RIGHT, BOTTOM), TOP is default
b1.pack(side=LEFT, padx = 10)
b2.pack(side=LEFT, padx = 10)
b3.pack(side=LEFT, padx = 10)
b4.pack(side=LEFT, padx = 10)
grid"
'''

b1.grid(row=0, column=0)
b2.grid(row=1, column=1)
b3.grid(row=2, column=2)

