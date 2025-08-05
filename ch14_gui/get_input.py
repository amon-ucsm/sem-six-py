# Getting input from user
import tkinter

def quit(top):
    top.destroy()

def display():
    name = var.get()


top = tkinter.Tk()
var = tkinter.StringVar()
entry1 = tkinter.Entry(top, textvariable= var, width= 20)
entry1.grid(row=0, column=0)