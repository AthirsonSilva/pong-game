from turtle import Turtle


class Ball(Turtle):
    """ Creating the ball """

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('yellow')
        self.shapesize(stretch_len=-0.5, stretch_wid=-0.5)
        self.penup()
        self.speed('fast')
        self.goto(0, 0)
        self.x_speed = -10
        self.y_speed = -10

    def move(self, x, y):
        new_x = self.xcor() + self.x_speed
        new_y = self.ycor() + self.y_speed
        self.goto(x=new_x, y=new_y)

    def bounce_y(self):
        self.y_speed *= -1

    def bounce_x(self):
        self.x_speed *= -1
