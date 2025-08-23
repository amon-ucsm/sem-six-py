from turtle import *
import turtle

t = turtle.Turtle()
colors = ('blue', 'red', 'orange', 'yellow')
for i in range(4):
    t.fillcolor(colors[i])
    t.begin_fill()
    t.circle(80, 180)
    t.lt(90)
    t.fd(160)
    t.end_fill()
t.hideturtle()
turtle.done()
    