from tkinter import *
from datetime import date

def calculate_age():
    birth_day = int(day_entry.get())
    birth_month = int(month_entry.get())
    birth_year = int(year_entry.get())

    today = date.today()

    age = today.year - birth_year

    if (today.month, today.day) < (birth_month, birth_day):
        age -= 1

    result.config(text="Age: " + str(age))

window = Tk()
window.title("Age Calculator")
window.geometry("300x220")

Label(window, text="Day").grid(row=0, column=0, padx=5, pady=5)
day_entry = Entry(window)
day_entry.grid(row=0, column=1)

Label(window, text="Month").grid(row=1, column=0, padx=5, pady=5)
month_entry = Entry(window)
month_entry.grid(row=1, column=1)

Label(window, text="Year").grid(row=2, column=0, padx=5, pady=5)
year_entry = Entry(window)
year_entry.grid(row=2, column=1)

Button(window, text="Calculate Age", command=calculate_age).grid(row=3, column=0, columnspan=2, pady=10)

result = Label(window, text="")
result.grid(row=4, column=0, columnspan=2)

window.mainloop()