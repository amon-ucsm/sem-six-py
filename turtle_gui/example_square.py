import turtle as t

"""for i in range(4):
    t.forward(50)
    t.left(90)"""
    
for i in range(4):
    if i % 2 == 0:
        t.forward(100)
        t.left(90)
    else:
        t.forward(50)
        t.left(90)
t.done()