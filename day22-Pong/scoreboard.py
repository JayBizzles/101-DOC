from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.player_1_score = 0
        self.player_2_score = 0
        self.color("white")
        self.goto(0, 300)
        self.display()


    def display(self):
        self.write(f"{self.player_1_score} \t {self.player_2_score}",align="center", font=("Arial", 60, "normal"))

    def update_score_1(self):
        self.clear()
        self.player_1_score += 1
        self.display()

    def update_score_2(self):
        self.clear()
        self.player_2_score += 1
        self.display()