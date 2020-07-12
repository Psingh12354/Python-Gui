"""CheckButton: To select any number of options by displaying a number of options to a user as toggle buttons. The general syntax is:
w = CheckButton(master, option=value)
There are number of options which are used to change the format of this widget. Number of options can be passed as parameters separated by commas. Some of them are listed below.

Title: To set the title of the widget.
activebackground: to set the background color when widget is under the cursor.
activeforeground: to set the foreground color when widget is under the cursor.
bg: to set he normal backgrouSteganography
Break

Secret Code:

Attach a File:nd color.

command: to call a function.
font: to set the font on the button label.
image: to set the image on the widget."""
from tkinter import *
root=Tk()
var1=IntVar
Checkbutton(root,text='male', variable=var1).grid(row=0, sticky=W)
var2=IntVar
Checkbutton(root,text='female', variable=var2).grid(row=1, sticky=W)
mainloop()