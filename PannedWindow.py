"""PannedWindowIt is a container widget which is used to handle number of panes arranged in it. The general syntax is:
w = PannedWindow(master, option=value)
master is the parameter used to represent the parent window.
There are number of options which are used to change the format of the widget. Number of options can be passed as parameters separated by commas. Some of them are listed below.

bg: to set he normal background color.
bd: to set the size of border around the indicator.
cursor: To appear the cursor when the mouse over the menubutton.
width: to set the width of the widget.
height: to set the height of the widget."""
from tkinter import *
m1=PanedWindow()
m1.pack(fill=BOTH,expand=1)
left = Entry(m1, bd = 5)
m1.add(left)
m2 = PanedWindow(m1, orient = VERTICAL)
m1.add(m2)
top = Scale( m2, orient = HORIZONTAL)
m2.add(top)
mainloop()