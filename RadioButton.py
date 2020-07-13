"""RadioButton: It is used to offer multi-choice option to the user. It offers several options to the user and the user has to choose one option.
The general syntax is:
w = RadioButton(master, option=value)
There are number of options which are used to change the format of this widget. Number of options can be passed as parameters separated by commas. Some of them are listed below.

activebackground: to set the background color when widget is under the cursor.
activeforeground: to set the foreground color when widget is under the cursor.
bg: to set he normal background color.
command: to call a function.
font: to set the font on the button label.
image: to set the image on the widget.
width: to set the width of the label in characters.
height: to set the height of the label in characters."""
from tkinter import *
root=Tk()
v=IntVar()
Radiobutton(root,text='GfG',variable=v,value=1).pack(anchor=W)
Radiobutton(root,text='MIT',variable=v,value=2).pack(anchor=W)
mainloop()
