# Getting input from user
import tkinter

def quit(top):
    top.destroy()

def display():
    name = var.get()
    label1.configure(text="Hello " + name)


top = tkinter.Tk()
var = tkinter.StringVar()
entry1 = tkinter.Entry(top, textvariable= var, width= 20)
entry1.grid(row=0, column=0)

label1 = tkinter.Label(top, text="", width= 20)
label1.grid(row=0 ,column= 1)

button1 = tkinter.Button(top, text="Display", command=display)
button1.grid(row=1, column= 0)

button2 = tkinter.Button(top, text="Quit", command=lambda top=top:quit(top), bg="red", fg="white")
button2.grid(row=1, column=1)
top.mainloop()