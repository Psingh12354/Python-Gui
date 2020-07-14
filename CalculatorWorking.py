from tkinter import *
def btnClick(numbers):
    global operator
    operator=operator+str(numbers)
    text_Input.set(operator)
def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")
def btnEqualsInput():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=""

root=Tk()
root.title("Calculator")
operator=""
text_Input = StringVar()
txtDislay=Entry(root,font=('arial',20,'bold'), textvariable=text_Input,bd=30,insertwidth=4,
                bg="burlywood1",justify='right').grid(columnspan=4)
btn7=Button(root,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="7",command=lambda : btnClick(7),bg="gray").grid(row=1,column=0)
btn8=Button(root,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="8",command=lambda : btnClick(8),bg="gray").grid(row=1,column=1)
btn9=Button(root,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="9",command=lambda : btnClick(9),bg="gray").grid(row=1,column=2)
Addition=Button(root,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="+",command=lambda : btnClick("+"),bg="gray").grid(row=1,column=3)

btn4=Button(root,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="6",command=lambda : btnClick(4),bg="gray").grid(row=2,column=0)
btn5=Button(root,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="6",command=lambda : btnClick(5),bg="gray").grid(row=2,column=1)
btn6=Button(root,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="6",command=lambda : btnClick(6),bg="gray").grid(row=2,column=2)
Subtraction=Button(root,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="-",command=lambda : btnClick("-"),bg="gray").grid(row=2,column=3)


btn3=Button(root,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="3",bg="gray",command=lambda : btnClick(3)).grid(row=3,column=0)
btn2=Button(root,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="2",command=lambda : btnClick(2),bg="gray").grid(row=3,column=1)
btn1=Button(root,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="1",command=lambda : btnClick(1),bg="gray").grid(row=3,column=2)
Multiplication=Button(root,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="x",command=lambda : btnClick("*"),bg="gray").grid(row=3,column=3)

btn0=Button(root,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="0",bg="gray",command=lambda : btnClick(0)).grid(row=4,column=0)
btnClear=Button(root,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="C",bg="gray",command=btnClearDisplay).grid(row=4,column=1)
btnEquals=Button(root,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="=",bg="gray",command=btnEqualsInput).grid(row=4,column=2)
Division=Button(root,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="/",command=lambda : btnClick("/"),bg="gray").grid(row=4,column=3)
root.mainloop()
