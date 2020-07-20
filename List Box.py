from tkinter import *
root=Tk()
Label(root,text="Number Increment",bg="yellow").pack()
def add():
    global i
    lbx.insert(ACTIVE, f"{i}")
    i+=1
i = 0
root.geometry("455x233")
root.title("Listbox tutorial")
lbx = Listbox(root)
lbx.pack()
lbx.insert(END, "First item of our listbox")
Button(root, text="Add Item", command=add).pack()
mainloop()