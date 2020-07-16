#frames are the type of  border
from tkinter import *
root=Tk()
root.geometry("655x333")
f1=Frame(root,bg="grey",borderwidth=6,relief=SUNKEN)
f1.pack(side=LEFT,fill="y")
f2=Frame(root,borderwidth=8,bg="grey",relief=SUNKEN)
f2.pack(side=TOP,fill="x")
l=Label(f1,text="Project Tkinter - Pycharm",font="arial")
l.pack(pady=42)
l=Label(f2,text="Welcome to sublime text",font="arial")
l.pack(padx=42)
mainloop()