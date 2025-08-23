import tkinter as tk
from tkinter import colorchooser
import turtle 

def draw_star():
    pen_size = int(pen_size_var.get())
    pen_color = pen_color_var.get()
    fill_color = fill_color_var.get()
    bg_color = bg_color_var.get()

    screen = turtle.Screen()
    screen.bgcolor(bg_color)
    t = turtle.Turtle()
    t.pensize(pen_size)
    t.pencolor(pen_color)
    t.fillcolor(fill_color)
    t.begin_fill()
    for i in range(5):
        t.forward(150)
        t.right(144)
    t.end_fill()
    t.hideturtle()
    turtle.done()

def choose_color(var):
    color = colorchooser.askcolor()[1]
    if color:
        var.set(color)

root = tk.Tk()
root.title("Star Drawer")

tk.Label(root, text="Pen Size:").grid(row=0, column=0, padx=5, pady=5)
pen_size_var = tk.StringVar(value="")
tk.Entry(root, textvariable=pen_size_var).grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Pen Color:").grid(row=1, column=0, padx=5, pady=5)
pen_color_var = tk.StringVar(value="#000000")
tk.Entry(root, textvariable=pen_color_var, width=10).grid(row=1, column=1, padx=5, pady=5)
tk.Button(root, text="Choose", command=lambda: choose_color(pen_color_var)).grid(row=1, column=2, padx=5, pady=5)

tk.Label(root, text="Fill Color:").grid(row=2, column=0, padx=5, pady=5)
fill_color_var = tk.StringVar(value="#00FFDD")
tk.Entry(root, textvariable=fill_color_var, width=10).grid(row=2, column=1, padx=5, pady=5)
tk.Button(root, text="Choose", command=lambda: choose_color(fill_color_var)).grid(row=2, column=2, padx=5, pady=5)

tk.Label(root, text="Background Color:").grid(row=3, column=0, padx=5, pady=5)
bg_color_var = tk.StringVar(value="#602B09")
tk.Entry(root, textvariable=bg_color_var, width=10).grid(row=3, column=1, padx=5, pady=5)
tk.Button(root, text="Choose", command=lambda: choose_color(bg_color_var)).grid(row=3, column=2, padx=5, pady=5)

tk.Button(root, text="Draw Star", command=draw_star).grid(row=4, column=0, columnspan=3, pady=10)

root.mainloop()