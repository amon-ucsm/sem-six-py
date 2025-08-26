import turtle
turtle.bgcolor('black')
turtle.colormode(255)

def square():
    for i in range (4):
        turtle.fd(100)
        turtle.rt(90)
        
        
# Display text
turtle.penup()
turtle.goto(90, 100)
turtle.color('white')
style = ('Arial', 15, 'italic')
turtle.write("Windows 10 Operatiung System", font= style, align= 'center')

# Yellow box
turtle.lt(90)
turtle.penup()
turtle.goto(100, -150)
turtle.pendown()
turtle.color('yellow')
turtle.begin_fill()
square()
turtle.end_fill()

# Green box
turtle.penup()
turtle.goto(100, -40)
turtle.pendown()
turtle.color('green')
turtle.begin_fill()
square()
turtle.end_fill()

# red box
turtle.penup()
turtle.goto(-10, -40)
turtle.pendown()
turtle.color('red')
turtle.begin_fill()
square()
turtle.end_fill()

# Yellow box
turtle.penup()
turtle.goto(-10, -150)
turtle.pendown()
turtle.color('blue')
turtle.begin_fill()
square()
turtle.end_fill()

turtle.hideturtle()
turtle.done()