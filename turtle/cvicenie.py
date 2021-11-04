import turtle
from random import randrange, uniform

t = turtle.Turtle()

height = 800
width = 500
turtle.setup(800, 500)

def stvorec():
    position_x = randrange(-200, 200)
    position_y = randrange(-200, 200)
    t.penup()
    t.setpos(position_y, position_x)
    t.setheading(randrange(0, 360))
    t.pencolor("blue")
    t.pensize(5)
    t.pendown()
    for i in range(4):
        t.forward(50)
        t.left(90)

number_of_stvorec =  

stvorec()

turtle.exitonclick()