"""
# Using config methods
import tkinter

top = tkinter.Tk()
label1 = tkinter.Label(top, text="Hello World")
label1.pack()
label1.config(text="Hello, Saw")
top.mainloop()"""

# Using text variable
import tkinter

top = tkinter.Tk()
var = tkinter.StringVar()
label1 = tkinter.Label(top, textvariable= var)
label1.pack()

var.set("Hello Saw")
print(var.get())
top.mainloop()