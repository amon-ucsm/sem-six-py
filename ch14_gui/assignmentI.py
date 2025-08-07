# Use default constant as 1 US dollar = 4500 Kyat
import tkinter

def Calculator():
    get_dollar = dollar.get()
    const = 4500
    val_kyat = const * get_dollar
    entry1.delete(0, "end")
    result.configure(text= val_kyat)

top = tkinter.Tk()
top.title("US Dollar to Kyat")
top.geometry("500x150")

dollar = tkinter.IntVar()
entry1 = tkinter.Entry(top, textvariable= dollar, width= 12)
entry1.delete(0, "end")
entry1.grid(row= 0, column= 1)

text_dollar = tkinter.Label(top, text="Dollar")
text_dollar.grid(row= 0, column= 2)

equivalent = tkinter.Label(top, text="is equivalent to", width= 15)
equivalent.grid(row= 1, column= 0)

result = tkinter.Label(top, text="", width= 12)
result.grid(row= 1, column= 1)

text_kyat = tkinter.Label(top, text="Kyat")
text_kyat.grid(row= 1, column= 2)

button1 = tkinter.Button(top, text="Calculate", command= Calculator)
button1.grid(row= 2, column= 2)

tkinter.mainloop()