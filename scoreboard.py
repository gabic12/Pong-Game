from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        """Scoreboard class inherits the Turtle class"""
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.right_score = 0
        self.left_score = 0
        self.update_score()

    def update_score(self):
        """Updates the score"""
        self.clear()
        self.goto(-100, 200)
        self.write(self.right_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.left_score, align="center", font=("Courier", 80, "normal"))

    def point_for_left(self):
        """Adds 1 point for the left player"""
        self.left_score += 1
        self.update_score()

    def point_for_right(self):
        """Adds 1 point for the right player"""
        self.right_score += 1
        self.update_score()