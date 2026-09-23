from .settings import PADDLE_LIMIT, PADDLE_SPEED, AI_SPEED


def move_paddle(paddle, amount):
    """Move a paddle and keep it inside the screen."""
    new_y = paddle.ycor() + amount
    new_y = max(-PADDLE_LIMIT, min(PADDLE_LIMIT, new_y))
    paddle.sety(new_y)


def move_paddle_up(paddle):
    move_paddle(paddle, PADDLE_SPEED)


def move_paddle_down(paddle):
    move_paddle(paddle, -PADDLE_SPEED)


def move_ai(paddle, ball):
    """Move the paddle toward the ball's y-coordinate."""
    if ball.ycor() > paddle.ycor():
        move_paddle(paddle, AI_SPEED)
    elif ball.ycor() < paddle.ycor():
        move_paddle(paddle, -AI_SPEED)