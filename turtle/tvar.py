import turtle
t = turtle.Turtle()

def mnohouholnik():
    for i in range(1):
        t.right(45)
        t.forward(50)
    for i in range(1):
        t.left(45)
        t.forward(50)
        t.left(45)
        t.forward(50)

mnohouholnik()
t.left(100)

mnohouholnik()



turtle.exitonclick()