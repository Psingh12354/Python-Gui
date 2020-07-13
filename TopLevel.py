"""TopLevel: This widget is directly controlled by the window manager. It don’t need any parent window to work on.The general syntax is:
w = TopLevel(master, option=value)
There are number of options which are used to change the format of the widget. Number of options can be passed as parameters separated by commas. Some of them are listed below.

bg: to set he normal background color.
bd: to set the size of border around the indicator.
cursor: To appear the cursor when the mouse over the menubutton.
width: to set the width of the widget.
height: to set the height of the widget."""
from tkinter import *
root=Tk()
root.title('GfG')
top=Toplevel()
top.title('Python')
mainloop()