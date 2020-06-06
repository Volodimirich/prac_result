from tkinter import *
from tkinter import filedialog


def click_dir():
    window.filename = filedialog.askopenfilename(initialdir = "/",title = "Select file")
    lb.configure(text=str(window.filename))

def click_save():
    pass


window = Tk()
window.title("Welcome to the xxd")
window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(0,weight=1)
#window.geometry("800x600")
Label(text="Выбранный файл:").grid(row=0, column=0,padx = 10, pady = 10,sticky = W+N+S)
lb = Label(window, text=".", font=("Arial Bold", 10))
lb.grid(row=0, column=1,sticky = N+S)
Button(text = "Open",command = click_dir).grid(row = 1, column = 1,sticky = E+S,padx = 10,pady = 10)
Button(text = "Save",command = click_save).grid(row = 1, column = 0,sticky = W+S,padx = 10,pady = 10)

mainloop()
