from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
import subprocess

class Error(Exception):
    def __init__(self, text):
        self.txt = text


def click_dir():
    window.filename = filedialog.askopenfilename(initialdir = "~",title = "Select file")
    lb.configure(text=str(window.filename))


def click_save():
    try:
        if (window.filename == ""):
            raise Error("You must select a file before saving it")
        file_copy = open(window.filename + ".tmp", "wb")
        file_copy.write(txt.get("@0,0", END).encode("utf-8"))
        proc = subprocess.run(["xxd", "-r", window.filename + ".tmp"], stdout = subprocess.PIPE)
        result = proc.stdout.decode("utf-8")
        file = open(window.filename, "w")
        file.write(result)
        file_copy.close()
        file.close()
        subprocess.run(["rm", window.filename + ".tmp"])
    except Exception as er:
        window.filename == ""
        messagebox.showerror("Houston we have a problem",er)

def click_undo():
    try:
        txt.edit_undo()
    except Exception as er:
        messagebox.showerror("Houston we have a problem",er)

def click_redo():
    try:
        txt.edit_redo()
    except Exception as er:
        messagebox.showerror("Houston we have a problem",er)
        
def click_save_as():
    try:
        name = filedialog.asksaveasfilename(initialdir = "/",title = "Select file")
        file_copy = open(name + ".tmp", "wb")
        file_copy.write(txt.get("@0,0", END).encode("utf-8"))
        proc = subprocess.run(["xxd", "-r", name + ".tmp"], stdout = subprocess.PIPE)
        result = proc.stdout.decode("utf-8")
        file = open(name, "w")
        file.write(result)
        file_copy.close()
        file.close()
        subprocess.run(["rm", name + ".tmp"])
    except Exception as er:
        messagebox.showerror("Houston we have a problem",er)
        
def text_start():
    try:
        if (window.filename == ""):
            raise Error("Before starting, you must select a file")
        txt.delete('1.0', END)
        proc = subprocess.run(["xxd", window.filename ], stdout=subprocess.PIPE)
        result = proc.stdout.decode("utf-8")
        txt.insert(END, result)
    except Exception as er:
        window.filename == ""
        messagebox.showerror("Houston we have a problem",er)


window = Tk()
window.title("Welcome to the xxd")
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)
window.grid_columnconfigure(3, weight=1)
window.grid_columnconfigure(4, weight=1)
window.grid_columnconfigure(5, weight=1)
window.grid_rowconfigure(0,weight=1)
window.filename=""

Label(text="Файл:").grid(row=0, column=0,padx = 10, pady = 10,sticky = W+N+S)
lb = Label(window, text=".", font=("Arial Bold", 10))
lb.grid(row=0, column=4,sticky = N+S)

txt = ScrolledText(width=70, height=10,undo=True)
txt.grid(columnspan=6,padx=10,pady=10)

Button(text = "Open",command = click_dir).grid(row = 2, column = 5,padx = 10,pady = 10)
Button(text = "Start",command = text_start).grid(row=2,column=4,padx = 10,pady = 10)
Button(text = "Redo",command = click_redo).grid(row=2,column=3,padx = 10,pady = 10)
Button(text = "Undo",command = click_undo).grid(row = 2, column = 2,padx = 10,pady = 10)
Button(text = "Save As",command = click_save_as).grid(row=2,column=1,padx = 10,pady = 10)
Button(text = "Save",command = click_save).grid(row = 2, column = 0,padx = 10,pady = 10)

window.mainloop()
