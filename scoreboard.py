from turtle import Turtle
FONT = ("Courier", 22, "normal")


class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.score = 0
        self.display_score()

    def calculate_score(self):
        self.score += 1

    def display_score(self):
        self.clear()
        self.write(f"SCORE : {self.score}", font=FONT)
