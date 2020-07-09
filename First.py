from tkinter import *
window=Tk()
window.geometry("300x300")
window.title("Welcome")
labell=Label(window,text="Welcome to Tkinter",fg='blue',bg='yellow',relief="solid",font=("arial",12,"bold"))
#labell.pack(fill=BOTH,pady=2,padx=2,expand=True)
#labell.place(x=100,y=80)
labell.grid(row=1,column=1)
button1=Button(window,text="Demo",fg='white',bg='brown',relief=RIDGE,font=("arial",12,"bold"))
button1.place(x=110,y=110) #GROOVE, RIDGE,SUNKEN,RAISE are the few relief command
window.mainloop()
# from tkinter import *
# window=Tk()
# window.geometry("300x300")
# window.title("Welcome")
# window.mainloop()
# For creating window only this much command is used