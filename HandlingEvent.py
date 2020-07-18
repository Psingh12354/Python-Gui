from tkinter import *
root=Tk()
def priyanshu(event):
    print(f"You clicked on the button {event.x},{event.y}") # if you want to know where the user press the button at what posiotin use this command {event.x},{event.y}
    # f is formated string
root.title("Events in TKinter")
root.geometry("644x334")
widget=Button(root,text="Click me")
widget.pack()
# search all button widget in google for better knowledge
widget.bind('<Button-1>',priyanshu)
widget.bind('<Double-1>',quit) # to quit the code when double click
mainloop()