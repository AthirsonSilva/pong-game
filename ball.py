from turtle import Turtle


class Ball(Turtle):
    """ Creating the ball """

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('yellow')
        self.speed('fast')
        self.goto(0, 0)
