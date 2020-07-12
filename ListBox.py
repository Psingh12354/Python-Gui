"""Listbox: It offers a list to the user from which the user can accept any number of options.
The general syntax is:
w = Listbox(master, option=value)
master is the parameter used to represent the parent window.
There are number of options which are used to change the format of the widget. Number of options can be passed as parameters separated by commas. Some of them are listed below.

highlightcolor: To set the color of the focus highlight when widget has to be focused.
bg: to set he normal background color.
bd: to set the border width in pixels.
font: to set the font on the button label.
image: to set the image on the widget.
width: to set the width of the widget.
height: to set the height of the widget."""
from tkinter import *
root=Tk()
lb=Listbox(root)
lb.insert(1, 'Python')
lb.insert(2, 'Java')
lb.insert(3, 'C++')
lb.insert(4, 'Any other')
lb.pack()
root.mainloop()