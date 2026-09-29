# This file controls how the paddles move.
# We keep all movement rules here so the main file stays easier to read.
# The actual paddle objects themselves are created in main.py.

from .settings import PADDLE_LIMIT, PADDLE_SPEED, AI_SPEED


def move_paddle(paddle, amount):
    """Move a paddle up or down without letting it leave the screen.
    
    Parameters:
        paddle: the turtle object that represents one paddle
        amount: how many pixels to move in the y direction

    Example:
        move_paddle(paddle, 20) moves the paddle upward
        move_paddle(paddle, -20) moves the paddle downward
    """
    # read the paddle's current position.
    current_y = paddle.ycor()

    # add the movement amount to its current position.
    new_y = current_y + amount

    # Keep the paddle inside the screen.
    # max(...) makes sure it doesn't go too low.
    # min(...) makes sure it doesn't go too high.
    new_y = max(-PADDLE_LIMIT, min(PADDLE_LIMIT, new_y))

    # Move the paddle to the new position.
    paddle.sety(new_y)


def move_paddle_up(paddle):
    """Moves a paddle upward."""
    move_paddle(paddle, PADDLE_SPEED)


def move_paddle_down(paddle):
    """Moves a paddle downward"""
    move_paddle(paddle, -PADDLE_SPEED)


def move_ai(paddle, ball):
    """Make the AI paddle follow the ball's y-position.
    
    This is a simple AI:
    - if the ball is above the paddle, the paddle moves up
    - if the ball is below the paddle, the paddle moves down
    - if they are level, the paddle does not move

    Paramters:
        paddle: the AI paddle object
        ball: the ball object
    """
    # If the ball is above the paddle, move upward
    if ball.ycor() > paddle.ycor():
        move_paddle(paddle, AI_SPEED)

    # If the ball is below the paddle, move downward.
    elif ball.ycor() < paddle.ycor():
        move_paddle(paddle, -AI_SPEED)

    # If the ball and paddle are not the same height, do nothing.
    # That keeps the AI stable and easier to understand.