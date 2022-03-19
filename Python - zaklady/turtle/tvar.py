import turtle
t = turtle.Turtle()

velkost_mnohouholnika = 60

def cast_mnohouholnika():        
    t.right(velkost_mnohouholnika)
    t.forward(velkost_mnohouholnika)
    t.left(velkost_mnohouholnika)
    t.forward(velkost_mnohouholnika)
    t.left(velkost_mnohouholnika)
    t.forward(velkost_mnohouholnika)

def mnohouholnik():
    cast_mnohouholnika()
    t.left(120)
    cast_mnohouholnika()




mnohouholnik()


turtle.exitonclick()