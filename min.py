from tkinter import *
from tkinter import filedialog

def click_dir():
    window.filename = filedialog.askopenfilename(initialdir = "/",title = "Select file")
    lb.configure(text=str(window.filename))

def click_save():
    pass


window = Tk()
window.title("Welcome to the xxd")
#window.geometry("800x600")
Label(text="Выбранный файл:").grid(row=0, column=0)
lb = Label(window, text=".", font=("Arial Bold", 10))
lb.grid(row=0, column=1)
Button(text = "Open",command =click_dir).grid(row = 1, column = 1)
Button(text = "Save",command =click_save).grid(row = 1, column = 0)

mainloop()
