from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1,stretch_len=6)
        self.color("white")
        self.setheading(90)
        self.goto(0,0)

    def move_up(self):
        self.forward(10)

    def move_down(self):
        self.backward(10)


