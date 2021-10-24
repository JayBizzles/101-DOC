import turtle
import random
import colorgram
from turtle import Turtle, Screen

# extracting most prevelant colors from this image
colors = colorgram.extract("hirst.jpg", 10)

# creating a dot painting
tim = Turtle()

turtle.colormode(255)


# each color has 3 ints that decide what they are

# so we just need to call all 3 and them put them into a tuple and use that to

# change the color of the turtle

# now I just have to set the directions for the turtle

# start from bottom left and go to the right and then loop

# Code for directing the instance
screen = Screen()



windowheight, windowwidth =  screen.screensize()


tim.setpos(-windowheight, -windowwidth)

tim.hideturtle()


# tim.forward(50)

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

for i in range(2,13):





    for j in range(20):
        tim.penup()
        sel_color = random.choice(colors)
        color_set = [sel_color.rgb.r, sel_color.rgb.g, sel_color.rgb.b]
        color_tuple = tuple(color_set)
        tim.color(color_tuple)
        tim.dot(30)
        tim.penup()
        tim.forward(40)
    if is_even(i):
        tim.forward(1)
        tim.left(90)
        tim.forward(40)
        tim.left(90)
        print(i)
    else:
        tim.forward(1)
        tim.right(90)
        tim.forward(40)
        tim.right(90)
        print("odd: ", format(i))

print("done")


screen.exitonclick()



