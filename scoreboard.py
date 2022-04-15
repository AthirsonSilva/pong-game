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

    def add_point(self):
        """ Adds one points to the player """

        self.score += 1

    def game_over(self, winner, loser):
        """ Prints the game over screen """

        self.color('white')
        self.write(f'Winner: {winner}', align='center', font='Arial', x=200, y=0)
        self.write(f'Loser: {loser}', align='center', font='Arial', x=-200, y=0)
