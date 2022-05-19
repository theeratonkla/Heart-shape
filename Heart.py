from turtle import *

shape("turtle")
speed(1)
color("red", "pink")
pensize(5)


def curve():
    for i in range(200):
        right(1)
        forward(1)
        speed(0)


begin_fill()
left(140)
forward(111.65)
curve()
left(120)
curve()
forward(111.65)
end_fill()
hideturtle()
done()
