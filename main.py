from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

#Setting the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

#Setting the game variables
game_on = True
right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

#Screen will listen for key inputs
screen.listen()
screen.onkey(fun=right_paddle.move_up, key="Up")
screen.onkey(fun=right_paddle.move_down, key="Down")
screen.onkey(fun=left_paddle.move_up, key="w")
screen.onkey(fun=left_paddle.move_down, key="s")

while game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    #Collision with the walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Collision with the paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Scoring points
    if ball.xcor() > 380: #Point for left player
        ball.reset_position()
        scoreboard.point_for_left()
    if ball.xcor() < -380: #Point for right player
        ball.reset_position()
        scoreboard.point_for_right()

screen.exitonclick()