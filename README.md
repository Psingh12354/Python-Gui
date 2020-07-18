#                                                                              Python-Gui

**_Here i upload my Python GUI based Programm


##                                                                      Welcome all to my github Page


#                                                                             Tkinter Programming

_Tkinter is the standard GUI library for Python. Python when combined with Tkinter provides a fast and easy way to create GUI applications. Tkinter provides a powerful object-_oriented interface to the Tk GUI toolkit.

Creating a GUI application using Tkinter is an easy task. All you need to do is perform the following steps −

Import the Tkinter module.

Create the GUI application main window.

Add one or more of the above-mentioned widgets to the GUI application.

Enter the main event loop to take action against each event triggered by the user.
##                                                      The order of program is not random

  **Adding two number 
  
```
from tkinter import *
def addNumber():
    res=int(e1.get())+int(e2.get())
    myText.set(res)
root=Tk()
myText=StringVar()
Label(root,text="First Number : ").grid(row=0,sticky=W)
Label(root,text="Second Number : ").grid(row=1,sticky=W)
Label(root,text="Result : ").grid(row=3,sticky=W)
result=Label(root,text="",textvariable=myText).grid(row=3,column=1,sticky=W)
e1=Entry(root)
e2=Entry(root)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
b=Button(root,text="Add",command=addNumber)
b.grid(row=0, column=2,columnspan=2, rowspan=2,sticky=W+E+N+S, padx=5, pady=5)
mainloop()
```

  **Atrributes OF Label & Pack
  
  ```
  from tkinter import *
root=Tk()
root.geometry("444x233")
root.title("My name is Priyanshu Singh")
# Important Label Optionn
# text - add_the_text
# bd - backgroung
# fg - foreground
# font - sets the font
# padx - x padding
# pady - y padding
#font=("comicsansms",19,"bold") or font="comicsansms 19 bold"
# relief - border styling - SUNKEN,RAISED,GROOVE,RIDGE
# use triple quotes for taking multiple input as string
title_label=Label(text="Linux is the best-known and most-used open source operating system.\n As an operating system, Linux is software that sits underneath \nall of the other software on a computer, receiving requests from those\n programs and relaying these requests to the computer's hardware.",bg="red",fg="White",padx=110,pady=90,font=("comicsansms",19,"bold"),borderwidth=3,relief=SUNKEN)

# Important Pack options
# anchor = nw
# side = top, bottom, left, right  #if you want to go to south then use bottom
# fill  fill=x command show to move window according to khicne # ne northeast ond so on
# padx
# pady
title_label.pack(side=BOTTOM,anchor="se",fill="x")
mainloop()
```

 
