from turtle import Turtle



class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt") as file:
            self.high_score = int(file.read())

        self.hideturtle()
        self.sety(350)
        self.color("yellow")
        self.write(f"Score = {self.score}, HighScore = {self.high_score}", align="center", font=("Arial", 24, "normal"))



    def add_point(self):
        self.score += 1
        self.clear()
        self.write(f"Score = {self.score}, Highscore = {self.high_score}",  align="center", font=("Arial", 24, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highscore.txt", mode= "w") as file:
                file.truncate()
                file.write(str(self.score))

        self.score = 0
        self.add_point()

        # self.write("f High_Score:{self.score}", align= "center", font=("Arial", 24, "bold"))

