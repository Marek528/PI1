import turtle
t = turtle.Turtle()

def stvorec():
    for i in range(4):
        t.forward(50)
        t.left(90)

stvorec()
t.left(20)
stvorec()
t.left(25)
stvorec()

turtle.exitonclick()