from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("733x566")
root.title("Pycharm")
def myFunc():
    print("Hi all")

def help():
    print("I will help you")
    a=tmsg.showinfo("Help ", "You got help") # first is above name and inner name is second

def rate():
    print("Rate us")
    value=tmsg.askquestion("How was your experience?","You use this Gui is this good?")
    print(value)
    # this condition is use when user give write input for better rating
    if value == "yes":
        msg="Great. Rate us on appstore please"
    else:
        msg="Tell us what is wrong we will contact you"
    tmsg.showinfo("Experience",msg)
def pk():
    ans=tmsg.askretrycancel("Priyanshu Hello","Hi Priyanshu")
    if ans:
        print("Retry")
    else:
        print("Cancel")
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

m3=Menu(filemenu,tearoff=0)
m3.add_command(label="Help",command=help)
m3.add_command(label="Rate us",command=rate)
m3.add_command(label="Priyanshu",command=pk)
filemenu.add_cascade(label="Help",menu=m3)
root.config(menu=filemenu)
mainloop()