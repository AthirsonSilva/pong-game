from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
from time import sleep
from turtle import Screen


# Creating the screen
screen = Screen()
screen.bgcolor('black')
screen.title('Pong')
screen.setup(height=600, width=800)


def draw_dashed():
    """Drawing dashed lines challenge
        """
    from turtle import Turtle

    turtle = Turtle(shape='square')
    turtle.color('white')
    turtle.penup()
    turtle.shapesize(stretch_wid=0.75, stretch_len=0.33)
    turtle.setposition(x=0, y=315)
    turtle.setheading(270)
    turtle.shapesize(stretch_wid=0.33, stretch_len=0.75)

    for i in range(1, 32):
        turtle.fd(10)
        turtle.penup()
        turtle.fd(10)
        turtle.pendown()


draw_dashed()


# Creating paddles
paddle1 = Paddle()
paddle1.create_paddle('blue', 350, 0)
paddle2 = Paddle()
paddle2.create_paddle('red', -350, 0)


# Creating scoreboard
scoreboard_p1 = Scoreboard()
scoreboard_p2 = Scoreboard()

# Creating the ball
ball = Ball()

# Key strokes
screen.listen()

# Paddle 1 movements
screen.onkey(paddle1.up, 'w')
screen.onkey(paddle1.down, 's')

# Paddle 2 movements
screen.onkey(paddle2.up, 'Up')
screen.onkey(paddle2.down, 'Down')

# Game screen loop
game_is_on = True
while game_is_on:
    sleep(0.05)
    screen.update()
    scoreboard_p1.write_score(arg=scoreboard_p1.score,
                              align='center', x=-50, y=270)
    scoreboard_p2.write_score(arg=scoreboard_p2.score,
                              align='center', x=50, y=270)

    ball.move(x=10, y=10)

    # Detect collision with walls
    if ball.ycor() > 290 or ball.ycor() < -290:
        # Bounce the ball
        ball.bounce_y()

    # Detect collision with the paddles
    if ball.distance(paddle1) < 35 and ball.xcor() > 325 or ball.distance(paddle2) < 30 and ball.xcor() < -330:
        # Bounce the ball
        ball.bounce_x()

    # Detect if the ball gets out off-bounds
    if ball.xcor() > 400:
        # Game over
        ball.refresh()
        scoreboard_p1.clear()
        scoreboard_p1.add_point()

    if ball.xcor() < -400:
        # Add points
        ball.refresh()
        scoreboard_p2.clear()
        scoreboard_p2.add_point()

    if scoreboard_p1 == 5:
        # Game over
        game_is_on = False
        scoreboard_p1.game_over(winner='Player 1', loser='Player 2')

    if scoreboard_p1 == 5:
        # Game over
        game_is_on = False
        scoreboard_p1.game_over(winner='Player 2', loser='Player 1')

    print(f'X: {ball.xcor()}, Y: {ball.ycor()}')

# Keeping the screen up till user click
screen.exitonclick()
