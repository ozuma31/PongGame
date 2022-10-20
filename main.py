from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

is_game_on = True


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
l_score = Scoreboard((-250, 270))
r_score = Scoreboard((150, 270))

screen.update()

screen.listen()
screen.onkey(fun=r_paddle.move_up, key="Up")
screen.onkey(fun=r_paddle.move_down, key="Down")
screen.onkey(fun=l_paddle.move_up, key="w")
screen.onkey(fun=l_paddle.move_down, key="s")

while is_game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # make the ball bounce if it hits top or bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # check if the ball hits the paddle
    if ball.distance(r_paddle) < 60 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # check if the ball has gone pass the R wall
    if ball.xcor() > 380:
        l_score.calculate_score()
        l_score.display_score()
        ball.ball_reset()

    # check if the ball has gone pass the L wall
    if ball.xcor() < -380:
        r_score.calculate_score()
        r_score.display_score()
        ball.ball_reset()


screen.exitonclick()
