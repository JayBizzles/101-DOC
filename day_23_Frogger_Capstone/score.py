from turtle import Turtle

COORDS = (-300, 300)


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(COORDS)
        self.display()




    def display(self):
        self.clear()
        self.write(f"Level {self.level}", align="left", font=("Arial", 30,"normal" ))

    def increment(self):
        self.level += 1

    def game_over(self):
        self.home()
        self.write("Game Over", align= "center", font=("Arial", 20 , "normal"))