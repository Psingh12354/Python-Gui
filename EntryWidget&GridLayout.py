from tkinter import *
root = Tk()
def getvals():
    print(f"The value of username is {a_value.get()}")
    print(f"The value of password is {b_value.get()}")
# use f as fstring to print the variable inside the curly brackcket
root.geometry("655x333")
a=Label(root,text="Username")
b=Label(root,text="Password")
a.grid()
b.grid(row=1) # is pack method such as pack
# Variable classes in tkinter
# BooleanVar, DoubleVar, IntVar, StringVar
a_value=StringVar()
b_value=StringVar()
userentry=Entry(root,textvariable=a_value)
passentry=Entry(root,textvariable=b_value)
userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)
Button(text="Submit",command=getvals).grid()
mainloop()