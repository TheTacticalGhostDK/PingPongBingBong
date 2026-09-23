from .settings import PADDLE_LIMIT, PADDLE_SPEED, AI_SPEED


def move_paddle(paddle, amount):
    """Move a paddle and keep it inside the screen."""


def move_paddle_up(paddle):
    """"""


def move_paddle_down(paddle):
    """"""


def move_ai(paddle, ball):
    """Move the paddle toward the ball's y-coordinate."""
    if ball.ycor() > paddle.ycor():
        move_paddle(paddle, AI_SPEED)
    elif ball.ycor() < paddle.ycor():
        move_paddle(paddle, -AI_SPEED)