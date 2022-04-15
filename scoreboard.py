from turtle import Turtle


class Scoreboard(Turtle):
    """ Scoreboard printing and manipulation """

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()

    def write_score(self, arg, align, x, y):
        """ Write the score of the player 1 """

        self.write(arg=arg, align=align, font='Arial')
        self.color('white')
        self.goto(x, y)
