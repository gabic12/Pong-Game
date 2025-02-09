from turtle import Turtle

SPEED_INCREASE = 0.9 #Lower this number to increase difficulty

class Ball(Turtle):

    def __init__(self):
        """Ball class inherits the Turtle class"""
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.goto(50, 50)
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def move(self):
        """At the start of the game, the ball will start to move right"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_x(self):
        """After a collision with a paddle, the ball will move in the opposite direction and increase its speed """
        self.x_move *= -1
        self.ball_speed *= SPEED_INCREASE

    def bounce_y(self):
        """After a collision with a wall, the ball will bounce"""
        self.y_move *= -1

    def reset_position(self):
        """After a point is scored, the ball will go to the center (0, 0) and will start moving in the player direction"""
        self.goto(0, 0)
        self.ball_speed = 0.1 #Speed of the ball is reset after a point is scored
        self.bounce_x()