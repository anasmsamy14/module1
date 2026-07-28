from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.geometry('650x450') # Slightly increased height to avoid overlapping elements
root.title('denomination counter')
root.configure(bg='light blue')

# Load and place image
upload = Image.open('Screenshot 2026-07-21 170936.png')
upload = upload.resize((300, 300))
img = ImageTk.PhotoImage(upload)
label = Label(root, image=img, bg='light gray')
label.place(x=180, y=20)

label1 = Label(root, text='hey there! welcome to denomination counter', font=('Arial', 15, 'bold'), bg='lime green')
label1.place(relx=0.5, y=340, anchor=CENTER)

def msg():
    msg1 = messagebox.showinfo('Alert', "do you want to calculate the denomination of your amount?")
    if msg1 == 'ok':
        topwin()

button1 = Button(root, text='lets get started', font=('Arial', 15, 'bold'), bg='light gray', command=msg)
button1.place(x=260, y=380)

# Global tracking variable to handle previous open windows
top = None

def topwin():
    global top
    # Close existing top window if already open
    if top is not None and top.winfo_exists():
        top.destroy()
        
    top = Toplevel()
    top.title('denomination counter')
    top.configure(bg='light yellow')
    top.geometry('650x400')

    # Input elements
    label = Label(top, text='enter your amount', font=('Arial', 15, 'bold'), bg='lavender')
    entry = Entry(top)

    # Result layout title
    lbl = Label(top, text='here are number of notes for each denomination', font=('Arial', 12, 'bold'), bg='white', fg='black')

    # Denomination Labels
    l1 = Label(top, text='2000:', font=('Arial', 15, 'bold'), bg='black', fg='white')
    l2 = Label(top, text='500:', font=('Arial', 15, 'bold'), bg='black', fg='white')
    l3 = Label(top, text='100:', font=('Arial', 15, 'bold'), bg='black', fg='white')

    # Result Boxes
    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)

    def calculate():
        try:
            amount = int(entry.get())
            notes_2000 = amount // 2000
            amount %= 2000
            notes_500 = amount // 500
            amount %= 500
            notes_100 = amount // 100
            
            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)
            
            t1.insert(END, str(notes_2000))
            t2.insert(END, str(notes_500))
            t3.insert(END, str(notes_100))
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid integer amount.")

    btn = Button(top, text='calculate', font=('Arial', 15, 'bold'), bg='brown', fg='white', command=calculate)

    # Placement of UI elements
    label.place(x=230, y=20)
    entry.place(x=250, y=60)
    btn.place(x=260, y=100)
    
    lbl.place(x=140, y=160)
    
    # Adjusted layout coordinates to prevent overlapping
    l1.place(x=180, y=210)
    t1.place(x=270, y=215)
    
    l2.place(x=180, y=250)
    t2.place(x=270, y=255)
    
    l3.place(x=180, y=290)
    t3.place(x=270, y=295)

    top.mainloop()

root.mainloop()
