from turtle import Turtle


class Paddle(Turtle):
    """ Paddle model class """

    def __init__(self):
        super().__init__()

    def create_paddle(self, color, x, y):
        """ Creating the two paddles """
        self.shape('square')
        self.penup()
        self.color(color)
        self.shapesize(stretch_wid=5, stretch_len=0.75)
        self.speed('fast')
        self.goto(x=x, y=y)

    def up(self):
        """ Move the paddle up """
        new_y = self.ycor() + 20
        self.goto(x=self.xcor(), y=new_y)

    def down(self):
        """ Move the paddle down """
        new_y = self.ycor() - 20
        self.goto(x=self.xcor(), y=new_y)
