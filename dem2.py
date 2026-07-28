from tkinter import *
from datetime import date


root = Tk()
root.title("knowing each other")
root.geometry("400x400")

lbl =Label(text="Hey there!", fg = 'white', bg = '#072F5F', height=1, width=400)
name_lbl = Label(text="Enter your name: ", bg = '#3895D3')
name_entry = Entry()

def display():

    name = name_entry.get()
    
    global message
    message = 'welcome! \nToday is :'
    greet = 'Hello ' + name + '!'

    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())

text_box = Text(height=3)


btn = Button(text='begin', command=display,height=1,bg = '#1261A0',fg = 'white')

lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()

root.mainloop()