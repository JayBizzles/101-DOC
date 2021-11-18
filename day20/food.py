from turtle import Turtle
import random
from snake_game import Snake

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("yellow")
        self.speed("fastest")
        self.set_val()


    def set_val(self):
        x_val = random.randint(-220, 220)
        y_val = random.randint(-220, 220)

        self.goto(x_val, y_val)