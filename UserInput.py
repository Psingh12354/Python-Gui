from tkinter import *
root=Tk()
def getvals():
    print("Submitting form")
    print(f"{namevalue.get(), phoenvalue.get(), gendervalue.get(), emergencyvalue.get(), paymenetmodevalue.get(), foodservicevalue.get()} ")

    with open("records.txt","a") as f: # use a for append and if write use w only
        f.write(f"{namevalue.get(), phoenvalue.get(), gendervalue.get(), emergencyvalue.get(), paymenetmodevalue.get(), foodservicevalue.get()}\n ")
root.geometry("644x344")
Label(root,text="Welcom to My travel",font="comicsansms 13 bold",pady=5).grid(row=0,column=3)
name=Label(root,text="Name")
phone=Label(root,text="Phone")
gender=Label(root,text="Gender")
emergency=Label(root,text="Emergence Contact")
paymenetMode=Label(root,text="Payment Mode")
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
emergency.grid(row=4,column=2)
paymenetMode.grid(row=5,column=2)
namevalue=StringVar()
phoenvalue=StringVar()
gendervalue=StringVar()
emergencyvalue=StringVar()
paymenetmodevalue=StringVar()
foodservicevalue=IntVar()

nameentry=Entry(root,textvariable=namevalue)
phoneentry=Entry(root,textvariable=phoenvalue)
genderentry=Entry(root,textvariable=gendervalue)
paymenetModeentry=Entry(root,textvariable=paymenetmodevalue)
emergencyentry=Entry(root,textvariable=emergencyvalue)

nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
emergencyentry.grid(row=4,column=3)
paymenetModeentry.grid(row=5,column=3)

foodservice=Checkbutton(text="Add mill",variable=foodservicevalue)
foodservice.grid(row=6,column=3)

Button(text="Submit",command=getvals).grid(row=7,column=3)
mainloop()
