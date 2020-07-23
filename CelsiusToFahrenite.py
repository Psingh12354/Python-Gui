from tkinter import *
import tkinter.font as font
root=Tk()
root.geometry("500x250")
def convert():
    celsius=celsius_val.get()
    if(celsius.replace(".","",1).isdigit()):
        error_msg.grid_forget()
        fahrenite=(float(celsius)*9/5)+32
        output.config(text="Temperature in Fahrenheit : "+str(fahrenite))
    else:
        error_msg.grid(row=1,column=1)
root.title("Celsius to Fahrenheit Converter")
description=Label(text="Celsius to Fahrenheit",font=font.Font(size=25),fg="grey").pack()
frame=Frame(root)
frame.pack(pady=25)
message=Label(frame,text="Enter the temperatur in Celsius : ",font=font.Font(size=10))
message.grid(row=0,column=0)
celsius_val=Entry(frame)
celsius_val.grid(row=0,column=1)
error_msg=Label(frame,text="Please enter a valid input...",font=font.Font(size=10),fg='red')
output=Label(frame,font=font.Font(size=12))
output.grid(row=2,column=0,columnspan=2,pady=10)
btn=Button(frame,text="Convert",width=30,fg="black",bg="sandy brown",bd=0,padx=20,pady=10,command=convert,font=font.Font(weight="bold"))
btn.grid(row=3,column=0,columnspan = 2, pady = 10)
mainloop()