# Python GUI program to
# calculate the exam result# Using Labels, Entry and Button
# widgets - Python 3 tkinter module
from tkinter import *
def exam_result():
    s1=int(e1.get())
    s2=int(e2.get())
    s3=int(e3.get())
    if(s1>=50 and s2>=50 and s3>=50):
        label_text.set("Pass the Exam!")
    else:
        label_text.set("Fail the Exam!")
window = Tk()
label_text=StringVar();
Label(window, text="Enter Subject 1:").grid(row=0, sticky=W)
Label(window, text="Enter Subject 2:").grid(row=1, sticky=W)
Label(window, text="Enter Subject 3:").grid(row=2, sticky=W)
Label(window, text="Result:").grid(row=3, sticky=W)
result=Label(window, text="", textvariable=label_text).grid(row=3,column=1, sticky=W)
e1 = Entry(window)
e2 = Entry(window)
e3 = Entry(window)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
b = Button(window, text="Result", command=exam_result)
b.grid(row=0, column=2,columnspan=2, rowspan=2,sticky=W+E+N+S, padx=5, pady=5)
mainloop()