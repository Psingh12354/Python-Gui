"""Scrollbar: It refers to the slide controller which will be used to implement listed widgets.
The general syntax is:
w = Scrollbar(master, option=value)
master is the parameter used to represent the parent window.
There are number of options which are used to change the format of the widget. Number of options can be passed as parameters separated by commas. Some of them are listed below.

width: to set the width of the widget.
activebackground: To set the background when mouse is over the widget.
bg: to set he normal background color.
bd: to set the size of border around the indicator.
cursor: To appear the cursor when the mouse over the menubutton."""
from tkinter import *
root=Tk()
scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)
mylist=Listbox(root,yscrollcommand=scrollbar.set)
for line in range(100):
    mylist.insert(END,'This is a line number '+str(line))
mylist.pack(side=LEFT,fill=BOTH)
scrollbar.config(command=mylist.yview())
mainloop()