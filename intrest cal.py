from tkinter import *


def calculate():
    p = float(principal_entry.get())
    t = float(time_entry.get())
    r = float(rate_entry.get())

    
    si = (p * t * r) / 100

    
    ci = p * ((1 + r / 100) ** t) - p

    si_result.config(text=f"Simple Interest = {si:.2f}")
    ci_result.config(text=f"Compound Interest = {ci:.2f}")


window = Tk()
window.title("Age Calculator App")
window.geometry("400x400")
window.configure(bg="lightblue")


Label(window, text="Interest Calculator",
      font=("Arial", 16, "bold"),
      bg="lightblue", fg="darkblue").pack(pady=10)


Label(window, text="Principal:", bg="lightblue").pack()
principal_entry = Entry(window, width=20)
principal_entry.pack()


Label(window, text="Time (Years):", bg="lightblue").pack()
time_entry = Entry(window, width=20)
time_entry.pack()


Label(window, text="Rate (%):", bg="lightblue").pack()
rate_entry = Entry(window, width=20)
rate_entry.pack()

Button(window,
       text="Calculate",
       command=calculate,
       bg="green",
       fg="white").pack(pady=15)


si_result = Label(window, text="", bg="lightblue", fg="red", font=("Arial", 11))
si_result.pack(pady=5)

ci_result = Label(window, text="", bg="lightblue", fg="purple", font=("Arial", 11))
ci_result.pack(pady=5)

window.mainloop()