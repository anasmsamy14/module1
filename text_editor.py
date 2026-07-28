from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

window = Tk()
window.title("Text Editor")
window.geometry("600x500")
window.rowconfigure(0, weight=1, minsize=800)
window.columnconfigure(1, weight=1, minsize=800)


def open_file():
    filepath = askopenfilename(
        filetypes = [
            ("All Allowed Files", "*.png;*.jpg;*.jpeg;*.py;*.txt"),  # Both types together
            ("Code & Text Files", "*.py;*.txt"),                     # Just code and text
            ("Image Files", "*.png;*.jpg;*.jpeg"),                   # Just images
            ("Python Files", "*.py"),                                # Python files only
            ("Text Files", "*.txt"),                                 # Text files only
            ("All Files", "*.*")                                     # Any file type
    ]
    )

    if not filepath:
        return
    text_edit.delete(1.0, END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        text_edit.insert(END, text)
        input_file.close()
    
    window.title(f"Text Editor - {filepath}")

def save_file():
    filepath = asksaveasfilename(
        defaultextension="py",
        filetypes=[("Python Files", "*.py"), ("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = text_edit.get(1.0, END)
        output_file.write(text)
    
    window.title(f"Text Editor - {filepath}")

text_edit = Text(window)
fr_buttons = Frame(window, relief=RAISED, bd=2)
btn_open = Button(fr_buttons, text="Open", command=open_file)
btn_save = Button(fr_buttons, text="Save As...", command=save_file)


btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
text_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()