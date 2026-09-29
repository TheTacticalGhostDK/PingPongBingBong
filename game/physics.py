# This file contains the rules for the ball.
# It does not create the screen, paddles or ball.
# Those objects are created in main.py.

from .settings import (
    BALL_RADIUS,
    BALL_SPEED_X,
    BALL_SPEED_Y,
    PADDLE_HALF_HEIGHT,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
)


# A square turtle is 20 pixels wide by default.
# The paddle is stretched vertically, but not horisontally.
PADDLE_HALF_WIDTH = 10


def move_ball(ball):
    """Move the ball using its current horizontal and vertical speed."""

    # dx controls movement from left to right
    # dy controls movement from bottom to top.
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


def bounce_from_walls(ball):
    """Bounce the ball when it touches the top or bottom wall."""


def check_paddle_collision(ball, paddle, moving_right):
    """Check whether the ball has hit a paddle.
    
    moving_right tells us which direction the ball is travelling:
        True means the ball is moving toward the right paddle.
        False means the ball is moving toward the left paddle.

    The function returns True when a collision happens.
    It returns false when there is no collision.
    """

    # Find the top and bottom edges of the paddle.
    paddle_top = paddle.ycor() + PADDLE_HALF_HEIGHT
    paddle_bottom = paddle.ycor() - PADDLE_HALF_HEIGHT

    # Check whether the ball is beside the paddle horizontally.
    ball_left = ball.xcor() - BALL_RADIUS
    ball_right = ball.xcor() + BALL_RADIUS
    paddle_left = paddle.xcor() - PADDLE_HALF_WIDTH
    paddle_right = paddle.xcor() + PADDLE_HALF_WIDTH

    horizontal_overlap = (
        ball_right >= paddle_left
        and ball_left <= paddle_right
    )

    # Check whether the ball is beside the paddle vertically.
    vertical_overlap = (
        ball.ycor() + BALL_RADIUS >= paddle_bottom
        and ball.ycor() - BALL_RADIUS <= paddle_top
    )

    # The ball must be moving toward the paddle.
    # This prevents it from bouncing repeatedly while overlapping.
    moving_toward_paddle = (
        moving_right and ball.dx > 0
        or not moving_right and ball.dx < 0
    )

    if horizontal_overlap and vertical_overlap and moving_toward_paddle:
        # Reverse the horizontal direction.
        ball.dx *= -1

        # Place the ball outside the paddle.
        # This prevents another collision in the next frame.
        if moving_right:
            ball.setx(paddle_left - BALL_RADIUS)
        else:
            ball.setx(paddle_right + BALL_RADIUS)

        return True

    return False


def get_scoring_side(ball):
    """Return which side scores when the ball leaaves the screen.
    
    The returned value means:
        "left"  = the left player gets a point
        "right" = the right player gets a point
        None    = nobody scores yet
    """

    left_boundary = -SCREEN_WIDTH / 2
    right_boundary = SCREEN_WIDTH / 2

    # if the ball leaeves through the left side,
    # the right player receives the point.
    if ball.xcor() < left_boundary:
        return "right"

    # if the ball leaves through the right side,
    # the left player recieves the point.
    if ball.xcor() > right_boundary:
        return "left"

    return None


def reset_ball(ball, direction):
    """Place the ball in the center and give it a new direction.
    
    direction should be:
        1 for movement toward the right
        -1 for movement toweard the left
    """

    # Put the ball back in the middle of the screen.
    ball.goto(0, 0)

    # Set the ball's horizontal and vertical speed again.
    ball.dx = BALL_SPEED_X * direction
    ball.dy = BALL_SPEED_Y