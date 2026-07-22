from tkinter import *

root = Tk()
root.title("Password Check")
root.geometry("400x400")

input_label = Label(root, text="Enter your password:")
input_label.pack(pady=10)

password_entry = Entry(root, show="*")
password_entry.pack(pady=10)

def check_password():
    password = password_entry.get()
    length = len(password)
    
    # Logic corrected from longest/strongest to shortest/weakest
    if length < 5:
        result_label.config(text="Password is too short", fg="red")
    elif length <= 6:
        result_label.config(text="Password is weak", fg="orange")
    elif length <= 8:
        result_label.config(text="Password is moderate", fg="blue")
    else:
        result_label.config(text="Password is strong", fg="green")

check_button = Button(root, text="Check Password", command=check_password)
check_button.pack(pady=10)

result_label = Label(root, text="")
result_label.pack(pady=10)

root.mainloop()