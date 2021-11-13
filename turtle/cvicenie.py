import turtle
from random import randrange, uniform
turtle.delay(0)

t = turtle.Turtle()
t.pencolor()
dlzka = randrange(20, 80)
uhol = randrange(20, 80)
t.penup()
t.setheading(uhol)
t.pendown()
t.pensize(4)

height = 800
width = 500

turtle.setup(800, 600)

def stvorec(dlzka):
    position_x = randrange(-200, 200)
    position_y = randrange(-200, 200)
    t.penup()
    t.setpos(position_y, position_x)
    t.setheading(randrange(0, 360))
    t.pencolor("blue")
    t.pensize(5)
    t.pendown()
    for i in range(dlzka):
        t.forward(dlzka)
        t.left(90)

def triangel(dlzka):
    position_x = randrange(-200, 200)
    position_y = randrange(-200, 200)
    t.penup()
    t.setpos(position_y, position_x)
    t.pendown()
    t.pencolor('red')
    for i in range(dlzka):
        t.forward(dlzka)
        t.left(120)


number_of_stvorec = randrange(1, 10)
number_of_triangel = randrange(1, 10)

for i in range(number_of_stvorec):
    triangel(dlzka)
    stvorec(dlzka)

turtle.exitonclick()