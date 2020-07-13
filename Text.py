"""Text: To edit a multi-line text and format the way it has to be displayed.
The general syntax is:
w  =Text(master, option=value)
There are number of options which are used to change the format of the text. Number of options can be passed as parameters separated by commas. Some of them are listed below.

highlightcolor: To set the color of the focus highlight when widget has to be focused.
insertbackground: To set the background of the widget.
bg: to set he normal background color.
font: to set the font on the button label.
image: to set the image on the widget.
width: to set the width of the widget.
height: to set the height of the widget."""
from tkinter import *
root=Tk()
T=Text(root,height=2,width=30)
T.pack()
T.insert(END,'Priyanshu \nSingh\n')
mainloop()