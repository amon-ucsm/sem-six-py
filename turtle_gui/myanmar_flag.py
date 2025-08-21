from turtle import *
import turtle

penup()
goto(50, 100)
turtle.color("black")
style = ("Arial", 30, "italic")
turtle.write("Myanmar", font=style, align= "center")

penup()
goto(-250, 100)
pendown()

color("yellow")
begin_fill()

forward(500)
right(90)
forward(100)
right(90)
forward(500)
right(90)

end_fill()

right(180)
color("green")
begin_fill()

forward(100)
left(90)
forward(500)
left(90)
forward(100)
end_fill()

penup()
right(180)
forward(100)
pendown()

color("red")
begin_fill()
forward(100)
right(90)
forward(500)
right(90)
forward(100)
end_fill()

right(90)
penup()
goto(-100, -10)
pendown()
begin_fill()
fillcolor("white")
pencolor("white")
for x in range(5):
    forward(200)
    right(144)
end_fill()
hideturtle()
done()