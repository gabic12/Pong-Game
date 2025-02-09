from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, x_cord, y_cord):
        """Paddle class inherits the Turtle class"""
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setheading(90)
        self.color("white")
        self.penup()
        self.goto(x_cord, y_cord)

    def move_up(self):
        """Paddle moves up by 20 pixels"""
        self.forward(20)

    def move_down(self):
        """Paddle moves down by 20 pixels"""
        self.backward(20)