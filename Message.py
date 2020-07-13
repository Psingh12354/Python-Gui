"""Message: It refers to the multi-line and non-editable text. It works same as that of Label.
The general syntax is:

w = Message(master, option=value)
master is the parameter used to represent the parent window.
There are number of options which are used to change the format of the widget. Number of options can be passed as parameters separated by commas. Some of them are listed below.

bd: to set the border around the indicator.
bg: to set he normal background color.
font: to set the font on the button label.
image: to set the image on the widget.
width: to set the width of the widget.
height: to set the height of the widget."""
from tkinter import *
root=Tk()
ourMessage='Hi all'
messageVar=Message(root,text=ourMessage)
messageVar.config(bg='lightgreen')
messageVar.pack()
mainloop()