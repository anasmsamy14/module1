from tkinter import *

def product():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    answer.config(text="Product = " + str(num1 * num2))

window = Tk()
window.title("Product Calculator")
window.geometry("300x200")

Label(window, text="First Number").pack()
entry1 = Entry(window)
entry1.pack()

Label(window, text="Second Number").pack()
entry2 = Entry(window)
entry2.pack()

Button(window, text="Calculate", command=product).pack(pady=10)

answer = Label(window, text="")
answer.pack()

window.mainloop()