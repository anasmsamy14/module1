from tkinter import *

from tkinter import messagebox

from PIL import Image, ImageTk

root = Tk()

root.geometry('650x400')

root.title('denomination counter')

root.configure(bg='light blue')


upload = Image.open('Screenshot 2026-07-21 170936.png')

upload = upload.resize((300, 300))

img = ImageTk.PhotoImage(upload)

label = Label(root, image=img, bg='light gray')

label.place(x=180, y=20)

label1 = Label(root, text='hey there! welcome to denomination counter', font=('Arial', 15, 'bold'), bg='lime green')

label1.place(relx=0.5, y=340, anchor=CENTER)

def msg():
    msg1 =  messagebox.showinfo('Alert', "do you want to calculate the denomination of your amount?")

    if msg1 == 'ok':
        topwin()


button1 = Button(root, text='lets get started', font=('Arial', 15, 'bold'), bg='light gray', command=msg)

button1.place(x=260, y=360)


def topwin():
    top=Toplevel()
    top.title('denomination counter')
    top.configure(bg='light yellow' )
    top.geometry('650x400')


    label = Label(top, text='enter your amount', font=('Arial', 15, 'bold'), bg='lavender')
    entry = Entry(top)
    lbl = Label(top, text='here are number of notes for each denomination', font=('Arial', 15, 'bold'), bg='black')

    l1 = Label(top, text='2000:', font=('Arial', 15, 'bold'), bg='black')

    l2 = Label(top, text='500:', font=('Arial', 15, 'bold'), bg='black')

    l3 = Label(top, text='100:', font=('Arial', 15, 'bold'), bg='black')



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

    label.place(x=230, y=50)
    Entry.place(x=200, y=80)
    btn.place(x=240, y=120)


    lbl.place(x=140, y=170)


    l1.place(x=180, y=170)
    l2.place(x=180, y=230)
    l3.place(x=180, y=260)

    t1.place(x=270, y=200)
    t2.place(x=270, y=230)
    t3.place(x=270, y=260)

    top.mainloop()




root.mainloop()