from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.shapesize(5, 1)
        self.goto(position)

    def move_up(self):
        if self.ycor() > 230:
            pass
        else:
            new_y = self.ycor() + 20
            new_x = self.xcor()
            self.goto(new_x, new_y)

    def move_down(self):
        if self.ycor() < -215:
            pass
        else:
            new_y = self.ycor() - 20
            new_x = self.xcor()
            self.goto(new_x, new_y)
