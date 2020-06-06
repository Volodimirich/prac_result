from tkinter import *
from tkinter import filedialog
import subprocess


def click_dir():
    window.filename = filedialog.askopenfilename(initialdir = "/",title = "Select file")
    lb.configure(text=str(window.filename))

def file_open():
    return open(window.filename,'wr')

def click_save():
    file_copy = open(window.filename + ".tmp", "wb")
    file_copy.write(txt.get("@0,0", END).encode("utf-8"))
    proc = subprocess.run(["xxd", "-r", window.filename + ".tmp"], stdout = subprocess.PIPE)
    result = proc.stdout.decode("utf-8")
    file = open(window.filename, "w").write(result)
    file_copy.close()
    file.close()
    subprocess.run(["rm", window.filename + ".tmp"])

def text_start():
    txt.delete('1.0', END)
    proc = subprocess.run(["xxd", window.filename ], stdout=subprocess.PIPE)
    result = proc.stdout.decode("utf-8")
    txt.insert(END, result)


window = Tk()
window.title("Welcome to the xxd")
window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(0,weight=1)
window.filename=""
#window.geometry("800x600")

Label(text="Выбранный файл:").grid(row=0, column=0,padx = 10, pady = 10,sticky = W+N+S)
lb = Label(window, text=".", font=("Arial Bold", 10))
lb.grid(row=0, column=1,sticky = N+S)

txt = Text(width=70, height=10)
txt.grid(columnspan=3,padx=10,pady=10)

Button(text = "Open",command = click_dir).grid(row = 2, column = 2,sticky = E+S,padx = 10,pady = 10)
Button(text = "Start",command = text_start).grid(row=2,column=1,sticky = E+W+S,padx = 10,pady = 10)
Button(text = "Save",command = click_save).grid(row = 2, column = 0,sticky = W+S,padx = 10,pady = 10)

window.mainloop()
