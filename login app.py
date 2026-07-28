from tkinter import *

root = Tk()
root.title("login application")
root.geometry("400x400")


frame = Frame(master=root, width=360, height=200, bg="#d0efff")

lbl1 = Label(frame, text="full name", font=("Arial", 12), bg="#3895D3",width=12)

lbl2 = Label(frame, text="email id", font=("Arial", 12), bg="#3895D3",width=12)

lbl3 = Label(frame, text="password", font=("Arial", 12), bg="#3895D3",width=12)

name_entry = Entry(frame)
email_entry = Entry(frame)
password_entry = Entry(frame, show="*")

def display():
    name = name_entry.get()
    greeting = "Hello, " + name + "!"
    message = '\ncongrats for your new account'
    textbox.insert(END, greeting)
    textbox.insert(END, message)


textbox = Text( bg="#BEBEBE",fg='black', font=("Arial", 12), width=40, height=5)

btn = Button(text = 'create account', command=display, bg="red")

frame.place(x=20, y=0)
lbl1.place(x=20, y=20)
name_entry.place(x=150, y=20)
lbl2.place(x=20, y=80)
email_entry.place(x=150, y=80)
lbl3.place(x=20, y=140)
password_entry.place(x=150, y=140)
btn.place(x=150, y=200)
textbox.place(y=250)


root.mainloop()