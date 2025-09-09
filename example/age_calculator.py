from tkinter import *
from tkinter import messagebox
def clearAll():
    dayField.delete(0, END)
    monthField.delete(0, END)
    yearField.delete(0, END)
    givenDayField(0, END)
    givenMonthField(0, END)
    givenYearField(0, END)
    rsltDayField.delete(0, END)
    rsltMonthField.delete(0, END)
    resltYearField(0, END)
   
   
def checkError():
    if(dayField.get() == "" or monthField.get() == "" 
       or yearField.get() == "" or givenDayField() == "" 
       or givenMonthField() == "" or givenYearField == ""):
        
        messagebox.showerror("Input Error")
        clearAll()
        return -1
    
def calculateAge():
    pass