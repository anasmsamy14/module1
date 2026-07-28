from tkinter import *

def convert():
    inches = float(entry.get())
    centimeters = inches * 2.54
    result.config(text=f"{centimeters:.2f} cm")

window = Tk()
window.title("Length Converter")
window.geometry("300x200")

Label(window, text="Enter length in inches:").pack(pady=10)

entry = Entry(window)
entry.pack()

Button(window, text="Convert", command=convert).pack(pady=10)

result = Label(window, text="")
result.pack()

window.mainloop()