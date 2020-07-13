"""Scale: It is used to provide a graphical slider that allows to select any value from that scale. The general syntax is:
w = Scale(master, option=value)
master is the parameter used to represent the parent window.
There are number of options which are used to change the format of the widget. Number of options can be passed as parameters separated by commas. Some of them are listed below.

cursor: To change the cursor pattern when the mouse is over the widget.
activebackground: To set the background of the widget when mouse is over the widget.
bg: to set he normal background color.
orient: Set it to HORIZONTAL or VERTICAL according to the requirement.
from_: To set the value of one end of the scale range.
to: To set the value of the other end of the scale range.
image: to set the image on the widget.
width: to set the width of the widget."""
from tkinter import *
root=Tk()
w=Scale(root,from_=0,to=43)
w.pack()
w=Scale(root,from_=0,to=200,orient=HORIZONTAL)
w.pack()
mainloop()