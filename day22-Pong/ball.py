from turtle import Turtle

SCREEN_SIZE = [float(400), float(500), float(-400), float(-500)]



class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("circle")
        self.xmove = 10
        self.ymove = 10
        print(SCREEN_SIZE)


    def move(self):
            new_x = self.xcor() + self.xmove
            new_y = self.ycor() + self.ymove
            self.goto(new_x, new_y)
            # self.forward(5)
            # if self.ycor() in SCREEN_SIZE:
            #     self.setheading(self.heading() + 90)

    def bounceup(self):
        self.ymove = self.ymove * -1

    def bounceright(self):
        self.xmove = self.xmove * -1
