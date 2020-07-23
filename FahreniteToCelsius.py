from tkinter import *
import tkinter.font as font
root=Tk()
root.geometry("500x250")
def convert_to_celsius():
    fahrenheit = float(input_box.get())
    celsius = (fahrenheit-32)*5/9
    output_label.config(text=round(celsius, 2))
window = tkinter.Tk()
window.title("C to F Converter")
window.minsize(width=250, height=50)

input_box = tkinter.Entry(justify=tkinter.RIGHT)
output_label = tkinter.Label(text="", justify=tkinter.RIGHT, width=8)
action_button = tkinter.Button(text='Convert', command=convert_to_celsius)

input_box.pack(padx=20, pady=20)
output_label.pack(padx=20, pady=20, side=tkinter.RIGHT)
action_button.pack(padx=20, pady=20)