from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("virus detector")
window.geometry('200x200')


def msg():
    messagebox.showwarning("Alert!", "Virus detected! Please take action immediately.")

button = Button(window, text="check for virus", command=msg)
button.pack()
window.mainloop()

