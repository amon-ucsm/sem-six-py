"""import tkinter

def main():
    top = tkinter.Tk()
    label1 = tkinter.Label(top, text="Hello")
    label1.pack()
    
    # Create another widget
    button1 = tkinter.Button(top, text="Press me", command=top.quit)
    button1.pack(side="left")
    
    tkinter.mainloop()
main()"""

"""
# Modified with function
import tkinter
import sys

# Callback function
def quit():
    print("Bye. I am getting out of here")
    sys.exit(0)
    
def main():
    top = tkinter.Tk()
    label1 = tkinter.Label(top, text="Hello")
    label1.pack()
    
    # Create another widget
    button1 = tkinter.Button(top, text="Press me", command=quit)
    button1.pack(side="left")
    
    tkinter.mainloop()
main()"""

"""
# Callback class
import tkinter
import sys

class HelloClass():
    def __init__(self):
        self.top = tkinter.Tk()
        self.button1 = tkinter.Button(self.top, text="Press me to quit", command=self.quit)
        
        self.button1.pack()
        self.top.mainloop()
        
    def quit(self):
        print("Bye.")
        sys.exit(0)
        
HelloClass()"""


# Binding method
import tkinter
import sys

def hello(event):
    print("Double click to exit")

def quit(event):
    print("Someone double-clicked! Bye!")
    sys.exit(0)

top = tkinter.Tk()
button1 = tkinter.Button(top, text="Hello Event World")
button1.pack()

# Begin binding
button1.bind("<Button-1>", hello)
button1.bind("<Double-1>", quit)
top.mainloop()