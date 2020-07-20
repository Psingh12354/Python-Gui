from tkinter import *
import tkinter.messagebox as tsmg
root=Tk()
root.geometry("455x234")
root.title("Radio Button")
# var= IntVar()
var=StringVar()
var.set("Radio")
def order():
    tsmg.showinfo("Order recived!",f"We have recived your order for {var.get()}.\nThanks for ordering")
Label(root,text="What would you like to have?",font="lucida 19 bold",justify=LEFT,padx=14).pack()
radio=Radiobutton(root,text="DOSA",padx=14,variable=var,value="Dosa").pack(anchor="w")
radio=Radiobutton(root,text="Idly",padx=14,variable=var,value="Idly").pack(anchor="w")
radio=Radiobutton(root,text="Paratha",padx=14,variable=var,value="Parath").pack(anchor="w")

radio=Radiobutton(root,text="Samosha",padx=14,variable=var,value="Samosha").pack(anchor="w")
Button(text="Order Now",command=order).pack()
mainloop()
