from turtle import Turtle, position, tilt
WIDTH = -380
MAX_Y = 380
MIN_Y = -380
class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.goto(position)
    def go_up(self):
        new_y = self.ycor() + 20
        if new_y < MAX_Y:
            self.goto((self.xcor(),new_y))
    def go_down(self):
        new_y = self.ycor() - 20
        if new_y > MIN_Y:
            self.goto((self.xcor(),new_y))

        



