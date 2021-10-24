import turtle
from turtle import Turtle, Screen

# using event listeners


jamal = Turtle()
screen = turtle.Screen()


def move_forwards():
    jamal.forward(10)

def move_backwards():
    jamal.backward(10)

def move_right():
    new_heading = jamal.heading() - 10
    jamal.setheading(new_heading)

def move_left():
    new_heading = jamal.heading() + 10
    jamal.setheading(new_heading)

def clear():
    jamal.reset()

def do_shit():
    screen.onkey(key="w", fun=move_forwards) #don't call move_forwards with a ()
    screen.onkey(key ="s", fun=move_backwards)
    screen.onkey(key="a", fun=move_left)
    screen.onkey(key="d", fun=move_right)
    screen.onkey(key ="c", fun=clear)


screen.listen()
do_shit()


screen.exitonclick()
