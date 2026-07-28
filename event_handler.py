from tkinter import *

window = Tk()
window.title("Event handler")
window.geometry('200x300')

def handle_keypress(event):
    print(event.char)

window.bind('<Key>', handle_keypress)


def handle_click(event):
    print("\nThe button was clicked")

button = Button(window, text="Click me")
button.pack()
button.bind('<Button-1>', handle_click)

window.mainloop()

