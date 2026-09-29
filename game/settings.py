# This file stores all the important numbers for the game.
# We put them here so we can change things easily later.
# For example, if we want a bigger screen or faster paddle, we change
# the numbers here instead of changing the game logic itself.

# Teh screen is 800 pixels wide and 600 pixels tall.
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# This controls how far from the left and right sides the paddles sit.
# The paddles are placed near the left and right edge of the screen.
PADDLE_X_OFFSET = 350

# How fast the player can move a paddle
PADDLE_SPEED = 20

# How fast the AI moves toward the ball.
AI_SPEED = 4

# The paddle is 100 pixels tall.
# This value is halft of that height, so we can keep it inside the screen.
PADDLE_HALF_HEIGHT = 50

# This tells us the highest or lowest y-position a paddle can have
# While still staying visible on the screen
PADDLE_LIMIT = SCREEN_HEIGHT // 2 - PADDLE_HALF_HEIGHT

# ball movement speed on the x and y axis.
# The ball moves diagonally.
BALL_SPEED_X = 4
BALL_SPEED_Y = 4

# Ball size.
BALL_RADIUS = 10

# This controls how often the game updates.
# Lower numbers = faster updates, higher numbers = slower updates
FRAME_DELAY = 16

# These are names for the different game modes.
# We use strings so it is easy to check which mode is active.
MODE_AI_AI = "ai_ai"
MODE_AI_PLAYER = "ai_player"
MODE_PLAYER_PLAYER = "player_player"

