from tkinter import *
root=Tk()
root.geometry("733x566")
root.title("Pycharm")
def myFunc():
    print("Hi all")
# use this for non drop down
# mymenu=Menu(root)
# mymenu.add_command(label="File",command=myFunc)
# mymenu.add_command(label="Exit", command=quit)
# root.config(menu=mymenu)
# to remove tear off at above New Project use tearoff=0
filemenu=Menu(root)
m1=Menu(filemenu,tearoff=0)
m1.add_command(label="New Project",command=myFunc)
m1.add_command(label="Save",command=myFunc)
m1.add_command(label="Save As",command=myFunc)
m1.add_separator()
# to seprate use add_sepreate command is use
m1.add_command(label="Print",command=myFunc)
m1.add_command(label="Exit",command=quit)
filemenu.add_cascade(labe="File",menu=m1)
root.config(menu=filemenu)

m2=Menu(filemenu,tearoff=0)
m2.add_command(label="New Project",command=myFunc)
m2.add_command(label="Save",command=myFunc)
m2.add_command(label="Save As",command=myFunc)
m2.add_separator()
# to seprate use add_sepreate command is use
m2.add_command(label="Print",command=myFunc)
m2.add_command(label="Exit",command=quit)
filemenu.add_cascade(labe="Edit",menu=m2)
root.config(menu=filemenu)
mainloop()