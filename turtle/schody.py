import turtle
t = turtle.Turtle()

def schody():
    for i in range(7):
        t.forward(50)
        t.left(90)
        t.forward(50)
        t.right(90)

schody()




turtle.exitonclick()