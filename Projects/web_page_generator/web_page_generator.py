import string
import tkinter as tk
from tkinter import *
#A python library that allows you to create web documents and display them in the browser
import webbrowser

from numpy import pad
from setuptools import Command

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self,master)
        #sets title of GUI window
        self.master.title("Web Page Generator")

        self.varCustomText = StringVar()

        #creates a button 
        self.btn_default = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        #positions the Button
        self.btn_default.grid(row=2, column=1, padx=(10,10) , pady=(10,10))

        #creates button for custom text option
        self.btn_submit = Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.customText)
        #positions the button
        self.btn_submit.grid(row=2, column=2, padx=(10, 10), pady=(10, 10))

        #creates the label for the text entry box
        self.lbl_customtxt = Label(self.master, text="Enter custom text or click the Default HTML page button")
        #positions the text label
        self.lbl_customtxt.grid(row=0, column=0, padx=(20,0))

        #creates the entry box to add custom text for the HTML page
        self.ent_customtxt = Entry(self.master, text=self.varCustomText)
        #positions the entry field
        self.ent_customtxt.grid(row=1, column=0, pady=(10, 0))

    #creates the defaultHTML function that creates a default html page
    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")
    #takes in user input from the entry field and creates the users custom html page
    def customText(self):
        htmlText = self.varCustomText.get()
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")





if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()