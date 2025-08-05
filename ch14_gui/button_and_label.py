import tkinter

def quit(top):
    top.destroy()

top = tkinter.Tk()

label1 = tkinter.Label(top, text="Hello World")
label1.pack()

button1 = tkinter.Button(top, text="Quit", command= lambda top= top:quit(top), bg="red", fg="white")

button1.pack(fill=tkinter.X, expand= 1)
top.mainloop()