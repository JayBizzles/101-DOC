from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.shape("turtle")
        self.setheading(90)
        self.goto(0, -300)
        self.speed("slow")

    def move(self):
        self.forward(5)