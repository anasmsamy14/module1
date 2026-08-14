import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("Stationery Order Management App")
root.geometry("850x700")
root.configure(bg="#f4f6f8")

stationery = [
    ("Notebook", 70),
    ("Pen", 20),
    ("Pencil", 15),
    ("Eraser", 10),
    ("Ruler", 30),
    ("Marker", 35),
    ("Glue", 40),
    ("Scissors", 60)
]

rates = {
    "EGP": 1,
    "SAR": 13.6,
    "USD": 50,
    "EUR": 58,
    "GBP": 67,
    "INR": 0.59,
    "JPY": 0.34,
    "AUD": 34.56,
    "CAD": 38.90,
    "CHF": 52.34,
    "CNY": 7.23,
    "SEK": 5.67,
    "NZD": 32.18

}

style = ttk.Style()
style.theme_use("clam")

style.configure(
    "Title.TLabel",
    font=("Arial", 24, "bold"),
    foreground="#243447",
    background="#f4f6f8"
)

style.configure(
    "Heading.TLabel",
    font=("Arial", 12, "bold"),
    foreground="#243447",
    background="#f4f6f8"
)

style.configure(
    "TLabel",
    font=("Arial", 11),
    background="#f4f6f8"
)

style.configure(
    "TButton",
    font=("Arial", 11, "bold"),
    padding=8
)

canvas = tk.Canvas(
    root,
    width=850,
    height=100,
    bg="#4c78a8",
    highlightthickness=0
)

canvas.pack(fill="x")

canvas.create_text(
    425,
    35,
    text="STATIONERY STORE",
    fill="white",
    font=("Arial", 25, "bold")
)

canvas.create_text(
    425,
    72,
    text="Order Management System",
    fill="white",
    font=("Arial", 14)
)

title = ttk.Label(
    root,
    text="Stationery Order Management App",
    style="Title.TLabel"
)

title.pack(pady=12)

currency_frame = ttk.Frame(root)
currency_frame.pack(pady=5)

ttk.Label(
    currency_frame,
    text="Currency:",
    style="Heading.TLabel"
).grid(row=0, column=0, padx=10)
9
currency = tk.StringVar(value="EGP")

currency_box = ttk.Combobox(
    currency_frame,
    textvariable=currency,
    values=["EGP", "SAR", "USD", "EUR", "GBP",'INR','JPY','AUD','CAD','CHF','CNY','SEK','NZD'],
    state="readonly",
    width=12
)

currency_box.grid(row=0, column=1)

table_frame = ttk.Frame(root)
table_frame.pack(pady=10)

ttk.Label(
    table_frame,
    text="Item",
    style="Heading.TLabel",
    width=20
).grid(row=0, column=0)

ttk.Label(
    table_frame,
    text="Price",
    style="Heading.TLabel",
    width=15
).grid(row=0, column=1)

ttk.Label(
    table_frame,
    text="Quantity",
    style="Heading.TLabel",
    width=15
).grid(row=0, column=2)

quantity_entries = []
price_labels = []

for index, item in enumerate(stationery):
    name = item[0]
    price = item[1]

    ttk.Label(
        table_frame,
        text=name,
        width=20
    ).grid(
        row=index + 1,
        column=0,
        pady=4
    )

    price_label = ttk.Label(
        table_frame,
        text=f"EGP {price:.2f}",
        width=15
    )

    price_label.grid(
        row=index + 1,
        column=1,
        pady=4
    )

    price_labels.append(price_label)

    quantity = ttk.Entry(
        table_frame,
        width=15
    )

    quantity.grid(
        row=index + 1,
        column=2,
        pady=4
    )

    quantity_entries.append(quantity)

def update_prices(event=None):
    for index, item in enumerate(stationery):
        price = item[1]

        converted_price = (
            price
            if currency.get() == "EGP"
            else price / rates[currency.get()]
        )

        price_labels[index].config(
            text=f"{currency.get()} {converted_price:.2f}"
        )

def calculate_total():
    total = 0

    for index, item in enumerate(stationery):
        quantity_text = quantity_entries[index].get()

        if quantity_text == "":
            quantity = 0

        elif quantity_text.isdigit():
            quantity = int(quantity_text)

        else:
            messagebox.showerror(
                "Invalid Quantity",
                "Please enter numbers only."
            )
            return

        total += item[1] * quantity

    final_total = (
        total
        if currency.get() == "EGP"
        else total / rates[currency.get()]
    )

    total_label.config(
        text=f"TOTAL: {currency.get()} {final_total:.2f}"
    )

def clear_orders():
    for entry in quantity_entries:
        entry.delete(0, tk.END)

    total_label.config(
        text="TOTAL: EGP 0.00"
    )

currency_box.bind(
    "<<ComboboxSelected>>",
    update_prices
)

button_frame = ttk.Frame(root)
button_frame.pack(pady=15)

calculate_button = ttk.Button(
    button_frame,
    text="Calculate Total",
    command=calculate_total
)

calculate_button.grid(
    row=0,
    column=0,
    padx=10
)

clear_button = ttk.Button(
    button_frame,
    text="Clear",
    command=clear_orders
)

clear_button.grid(
    row=0,
    column=1,
    padx=10
)

total_label = tk.Label(
    root,
    text="TOTAL: EGP 0.00",
    font=("Arial", 22, "bold"),
    bg="#243447",
    fg="white",
    padx=30,
    pady=10
)

total_label.pack(pady=10)

root.mainloop()