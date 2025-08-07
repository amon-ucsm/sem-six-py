import tkinter
import random
class IntergerMultiply:
    def __init__(self):
        self.intmultiply = tkinter.Tk()
        self.intmultiply.title("Integer Multiply")
        
        self.var1 = tkinter.IntVar()
        self.entry1 = tkinter.Entry(self.intmultiply, textvariable= self.var1, width= 20)
        self.entry1.pack()
        
        self.mu1button = tkinter.Button(self.intmultiply, text="Multiply", command= self.multiply)
        self.mu1button.pack()
    
    def multiply(self):
        a = random.randint(1, 100)
        b = int(self.entry1.get())
        self.entry1.delete(0, "end")
        self.entry1.insert(0, a * b)
        #self.intmultiply.mainloop()
    
top = tkinter.Tk()
top.title("Assignment")
top.geometry("500x500")

IMbutton = tkinter.Button(top, text="Integer Multiply", command= IntergerMultiply)
IMbutton.pack()
tkinter.mainloop()