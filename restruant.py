import tkinter as tk
from tkinter import ttk ,messagebox


class ResturantOrderManagement:

    def __init__(self, root):
        self.root = root
        self.root.title("Resturant Order Management Application")

        self.menu_items = {
            "Burger": 5.99,
            "Fish and chips": 7.99,
            "Pizza": 8.99,
            "Salad": 4.99,
            "Soda": 1.99,
            "Coffee": 2.49,
            "Ice Cream": 3.49,
            "Pasta": 6.99,
            "Steak": 14.99,
            "Chicken Wings": 9.99,
            "Tacos": 6.49,
            "Fries": 2.99,
            "Sandwich": 5.49,
            "Soup": 3.99,
            "Smoothie": 4.49,
            "Milkshake": 3.99
        }

        self.exchange_rate = 49.78

        self.setup_background(root)

        frame = tk.Frame(root)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        ttk.Label(frame, text="Resturant Order Management", font=("Helvetica", 16)).grid(row=0,columnspan=3,padx=10,pady=10)

        self.menu_labels = {}
        self.menu_quantities = {}

        for i, (item,price) in enumerate(self.menu_items.items(), start=1 ):
            label= ttk.Label(

                frame,
                text=f'{item} (${price}):',
                font=("Helvetica",16)
            )
            label.grid(row=i,column=0 , padx=10, pady=5)
            self.menu_labels[item]=label

            quantity_entry = ttk.Entry(frame, width=5)
            quantity_entry.grid(row=i,column=1,padx=10,pady=5)
            self.menu_quantities[item]=quantity_entry



        self.currency_var = tk.StringVar()
        ttk.Label(frame, text="Select Currency:", font=("Helvetica", 12)).grid(row=len(self.menu_items) + 1, column=0, padx=10, pady=5)


        currency_dropdown = ttk.Combobox(frame, textvariable=self.currency_var, state="readonly",width=18,value=["USD", "egp"])

        currency_dropdown.grid(row=len(self.menu_items) + 1, column=1, padx=10, pady=5)

        currency_dropdown.current(0)
        self.currency_var.trace("w", self.update_prices)

        order_button = ttk.Button(frame, text="Place Order", command=self.place_order)

        order_button.grid(row=len(self.menu_items) + 2, columnspan=3, padx=10, pady=10)

    def setup_background(self,root):
        bg_width,bg_height=800,600
        canvas = tk.Canvas(root, width=bg_width, height=bg_height)
        canvas.pack()

        orginal_image = tk.PhotoImage(file="aa.png")
        background_image = orginal_image.subsample(orginal_image.width() // bg_width, orginal_image.height() // bg_height)

        canvas.create_image(0, 0, anchor=tk.NW, image=background_image)
        canvas.image = background_image

    def update_prices(self, *args):
        currency = self.currency_var.get()
        sympol = "$" if currency == "USD" else "E£"
        rate = self.exchange_rate if currency == "egp" else 1

        for item,label in self.menu_labels.items():
            price = self.menu_items[item] * rate
            label.config(text=f'{item} ({sympol}{price}):')


    def place_order(self):
        total_cost = 0
        order_summary = "Order Summary:\n"
        currency = self.currency_var.get()
        sympol = "$" if currency == "USD" else "E£"
        rate = self.exchange_rate if currency == "egp" else 1


        for item, entry in self.menu_quantities.items():
            quantity = entry.get()
            if quantity.isdigit():
                quantity = int(quantity)
                price = self.menu_items[item] * rate
                cost = quantity * price
                total_cost += cost

                if quantity > 0:
                    order_summary += f"{item}: {quantity} x {sympol}{price} = {sympol}{cost}\n"


                if total_cost > 0:
                    order_summary += f"\nTotal Cost: {sympol}{total_cost}"
                    messagebox.showinfo("Order placed", order_summary)

                else:
                    messagebox.showwarning("Place Order Atlest One Item")

if __name__ == "__main__":

    root = tk.Tk()
    app = ResturantOrderManagement(root)
    root.geometry("800x600")
    root.mainloop()