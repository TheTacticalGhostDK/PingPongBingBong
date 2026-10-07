"""
=====================================================================
PONG-SPIL - Programmering er sjovt!
=====================================================================

Beskrivelse:
    Dette program implementerer det klassiske Pong-spil ved hjælp af
    Pythons turtle-modul. Spillet er et enkeltspiller-spil, hvor
    brugeren styrer den venstre paddle med piletasterne op og ned,
    mens computeren (AI'en) styrer den højre paddle.

Formål:
    At demonstrere hvordan man kan bruge turtle-modulet til at bygge
    et interaktivt spil med:
        - Bevægelige objekter (paddle og bold)
        - Tastaturinput (piletaster)
        - Simpel AI (følger bolden)
        - Kollisionsdetektion (bold mod paddle, top og bund)
        - Score-system (point vises øverst på skærmen)

Styring:
    - Pil op   : Flyt venstre paddle opad
    - Pil ned  : Flyt venstre paddle nedad
    - Escape   : Afslut spillet

Spilleregler:
    - Bolden bevæger sig diagonalt og hopper ved kollision.
    - Hvis bolden rammer top eller bund, ændrer den retning.
    - Hvis bolden rammer en paddle, ændrer den retning.
    - Hvis bolden går bag en paddle, får modstanderen 1 point,
      og bolden nulstilles til midten.

Tekniske detaljer:
    - skærm.tracer(0) slår automatisk opdatering fra, så vi selv
      kalder skærm.update() i spillets hovedløkke.
    - Spillet kører i en while-løkke, indtil brugeren trykker Escape.

Forfatter: [Dit navn]
Dato:      [Dato]
Version:   1.0
=====================================================================
"""

import turtle

from game.controllers import (
    move_ai,
    move_paddle_down,
    move_paddle_up,
)

from game.physics import (
    bounce_from_walls,
    check_paddle_collision,
    get_scoring_side,
    move_ball,
    reset_ball,
)

from game.settings import (
    BALL_SPEED_X,
    BALL_SPEED_Y,
    FRAME_DELAY,
    MODE_AI_PLAYER,
    PADDLE_X_OFFSET,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
)

# Opsætning af skærmen
skærm = turtle.Screen()
skærm.title("Pong - Programmering er sjovt!")
skærm.bgcolor("black")
skærm.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
skærm.tracer(0)  # Slår automatisk opdatering fra

# Left paddle: player-controlled
paddle_venstre = turtle.Turtle()
paddle_venstre.speed(0)
paddle_venstre.shape("square")
paddle_venstre.color("white")
paddle_venstre.shapesize(stretch_wid=5, stretch_len=1)
paddle_venstre.penup()
paddle_venstre.goto(-PADDLE_X_OFFSET, 0)

# Right paddle: AI-controlled
paddle_højre = turtle.Turtle()
paddle_højre.speed(0)
paddle_højre.shape("square")
paddle_højre.color("white")
paddle_højre.shapesize(stretch_wid=5, stretch_len=1)
paddle_højre.penup()
paddle_højre.goto(PADDLE_X_OFFSET, 0)

# Ball
bold = turtle.Turtle()
bold.speed(0)
bold.shape("circle")
bold.color("white")
bold.penup()
bold.goto(0, 0)
bold.dx = BALL_SPEED_X  # Hastighed i x-retning
bold.dy = BALL_SPEED_Y  # Hastighed i y-retning

# Score
score_venstre = 0
score_højre = 0
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write(f"{score_venstre} : {score_højre}", align="center", font=("Arial", 24, "bold"))

def paddle_op():
    move_paddle_up(paddle_venstre)

def paddle_ned():
    move_paddle_down(paddle_venstre)

def stop():
    global running
    running = False

# Tastaturbinding
skærm.listen()
skærm.onkeypress(paddle_op, "Up")
skærm.onkeypress(paddle_ned, "Down")
skærm.onkeypress(stop, "Escape")

keys = {"Up": False, "Down": False}

def set_key(key_name, is_pressed):
    keys[key_name] = is_pressed

def paddle_up_pressed():
    keys["Up"] = True

def paddle_up_released():
    keys["Up"] = False

def paddle_down_pressed():
    keys["Down"] = True

def paddle_down_released():
    keys["Down"] = False

skærm.onkeypress(paddle_up_pressed, "Up")
skærm.onkeyrelease(paddle_up_released, "Up")
skærm.onkeypress(paddle_down_pressed, "Down")
skærm.onkeyrelease(paddle_down_released, "Down")

running = True

score_venstre = 0
score_højre = 0

# Hovedspil-løkke
while running:
    if keys["Up"] and not keys["Down"]:
        move_paddle_up(paddle_venstre)
    elif keys["Down"] and not keys["Up"]:
        move_paddle_down(paddle_venstre)

    # Move the ball
    move_ball(bold)

    # Bounce from top and bottom
    bounce_from_walls(bold)

    # Left paddle collision
    check_paddle_collision(bold, paddle_venstre, moving_right=False)

    # Right paddle collision
    check_paddle_collision(bold, paddle_højre, moving_right=True)

    # Simple AI: right paddle follows the ball
    move_ai(paddle_højre, bold)

    # Check if someone scored
    winner = get_scoring_side(bold)

    if winner == "left":
        score_venstre += 1
        reset_ball(bold, 1)

    elif winner == "right":
        score_højre += 1
        reset_ball(bold, -1)

    skærm.update()

skærm.bye()
