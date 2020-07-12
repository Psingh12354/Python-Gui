"""Frame: It acts as a container to hold the widgets. It is used for grouping and organizing the widgets. The general syntax is:
w = Frame(master, option=value)
master is the parameter used to represent the parent window.
There are number of options which are used to change the format of the widget. Number of options can be passed as parameters separated by commas. Some of them are listed below.

highlightcolor: To set the color of the focus highlight when widget has to be focused.
bd: to set the border width in pixels.
bg: to set the normal background color.
cursor: to set the cursor used.
width: to set the width of the widget.
height: to set the height of the widget."""
from tkinter import *

root = Tk()
frame = Frame(root)
frame.pack()
bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)
redbutton = Button(frame, text='Red', fg='red')
redbutton.pack(side=LEFT)
greenbutton = Button(frame, text='Brown', fg='brown')
greenbutton.pack(side=LEFT)
bluebutton = Button(frame, text='Blue', fg='blue')
bluebutton.pack(side=LEFT)
blackbutton = Button(bottomframe, text='Black', fg='black')
blackbutton.pack(side=BOTTOM)
root.mainloop() 