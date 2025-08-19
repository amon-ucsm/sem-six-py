import turtle as t
t.pencolor("red")

for i in range(4):
    if  i % 2 == 0:
        t.forward(150)
        t.left(90)
    else:
        t.forward(100)
        t.left(90)