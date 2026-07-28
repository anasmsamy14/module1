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

        self.exchange_rate = 50.50

        self.setup_background()

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
            



            
