"""SpinBox: It is an entry of ‘Entry’ widget. Here, value can be input by selecting a fixed value of numbers.The general syntax is:
w = SpinBox(master, option=value)
There are number of options which are used to change the format of the widget. Number of options can be passed as parameters separated by commas. Some of them are listed below.

bg: to set he normal background color.
bd: to set the size of border around the indicator.
cursor: To appear the cursor when the mouse over the menubutton.
command: To call a function.
width: to set the width of the widget.
activebackground: To set the background when mouse is over the widget.
disabledbackground: To disable the background when mouse is over the widget.
from_: To set the value of one end of the range.
to: To set the value of the other end of the range."""
from tkinter import *
root=Tk()
w=Spinbox(root,from_=0,to=10)
w.pack()
mainloop()