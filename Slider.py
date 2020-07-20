from tkinter import *
import tkinter.messagebox as tsmg
root=Tk()
root.geometry("455x234")
root.title("Slider")
def getdollar():
    print(f"We have credited {myslider2.get()}  dollars to your bank account")
    tsmg.showinfo("Amount Credited!",f"We have credited {myslider2.get()}  dollars to your bank account")
# myslider=Scale(root,from_=0,to=455)
# myslider.pack()
# for horizontal
Label(root,text="How many dollar do you have").pack()
myslider2=Scale(root,from_=0,to=100,orient=HORIZONTAL,tickinterval=50) # tickinterval is use to make a particular gap
myslider2.set(10) # 10 is default value
Button(root,text="Get dollars",pady=10,command=getdollar).pack()
myslider2.pack()
mainloop()
