from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

game_is_on = True
BALL_SPEED = 0.1
screen = Screen()
screen.screensize(800, 600, "black")
screen.title("pong")
screen.tracer(0)
screen.listen()

# always remember that you  have to add () at the end of the class when you any create a object
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

while game_is_on:
    time.sleep(BALL_SPEED)
    screen.update()
    ball.move()
    #
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        BALL_SPEED *= 0.9

    if ball.xcor() > 360:
        scoreboard.l_point()
        ball.refresh()
        BALL_SPEED = 0.1

    if ball.xcor() < -360:
        scoreboard.r_point()
        ball.refresh()
        BALL_SPEED = 0.1

screen.exitonclick()
