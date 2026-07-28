from tkinter import *

root =Tk()
root.geometry('400x300')
root.title('main')


def topwindow():
    top = Toplevel()
    top.geometry('100x100')
    top.title('top window')


    L2 = Label(top, text='this is top window')
    L2.pack()

    top.mainloop()

L1 = Label(root, text='this is root window')

btn = Button(root, text='click me to open new window', command=topwindow)

L1.pack()
btn.pack()
root.mainloop()