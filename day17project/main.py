import turtle
from turtle import Turtle, Screen
import random

# colors = ["light blue", "deep sky blue", "dodger blue", "powder blue", "sky blue", "light sky blue"]
# angles = [0, 90, 180, 270]

tim = Turtle()
turtle.colormode(255)
tim.shape("arrow")


# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color_tuple = (r, g, b)
#     tim.pencolor(color_tuple)




#drawing different shapes

# def draw_shape(num_sides):
#     angle = 360/num_sides
#     for _ in range(num_sides):
#         tim.forward(90)
#         tim.right(angle)
#
#
# for shape_side_n in range(3, 11):
#     rand_choice = random.choice(colors)
#     tim.color(rand_choice)
#     draw_shape(shape_side_n)

#draw a spinogram

# tim.pen(pensize=1)
# turtle.speed("fastest")
# start_pos = tim.position()
# tim.circle(90)
# tim.setheading(tim.heading() + 10)
# while tim.heading != 0:
#     random_color()
#     tim.circle(90)
#     current_heading = tim.heading()
#     tim.setheading(current_heading+10)
#     # rand_angle = random.choice(angles)
#     # tim.setheading(rand_angle)










screen = Screen()
screen.exitonclick()