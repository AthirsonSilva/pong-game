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

    def move(self):
        new_x = self.xcor() + 10
        new_y = self.xcor() + 10
        self.goto(x=new_x, y=new_y)
