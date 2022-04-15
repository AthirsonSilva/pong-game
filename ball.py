from random import choice
from time import sleep
from turtle import Turtle


class Ball(Turtle):
    """ Creating the ball """

    def __init__(self):
        super().__init__()
        self.directions_y = [10, -10]
        self.directions_x = [10, -10]
        self.shape('circle')
        self.color('yellow')
        self.shapesize(stretch_len=-0.5, stretch_wid=-0.5)
        self.penup()
        self.speed('fastest')
        self.goto(0, 0)
        self.x_speed = choice(self.directions_x)
        self.y_speed = choice(self.directions_y)

    def move(self, x, y):
        """" Moves the ball """

        new_x = self.xcor() + self.x_speed
        new_y = self.ycor() + self.y_speed
        self.goto(x=new_x, y=new_y)

    def bounce_y(self):
        """ Bounces the ball in the y axis """

        self.y_speed *= -1

    def bounce_x(self):
        """ Bounces the ball in the x axis """

        self.x_speed *= -1

    def refresh(self):
        """ Refresh the ball to the middle """

        self.goto(0, 0)
        sleep(1)
        self.move(x=choice(self.directions_x), y=choice(self.directions_y))
