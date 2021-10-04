from turtle import Turtle

FONT = ("Courier", 50, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()


    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"{self.r_score}", align="center", font=FONT)
        self.goto(100, 200)
        self.write(f"{self.l_score}", align="center", font=FONT)

    def r_increase(self):
        self.r_score += 1
        self.update_score()

    def l_increase(self):
        self.l_score += 1
        self.update_score()