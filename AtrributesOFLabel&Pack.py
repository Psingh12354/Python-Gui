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