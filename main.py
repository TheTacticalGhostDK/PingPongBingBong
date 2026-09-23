"""
=====================================================================
PONG-SPIL – Programmering er sjovt!
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
import random       # ref.: https://docs.python.org/3/library/random.html#module-random
                    # Ref.: https://pypi.org/project/keyboard/

# Opsætning af skærmen
skærm = turtle.Screen()
skærm.title("Pong - Programmering er sjovt!")
skærm.bgcolor("black")
skærm.setup(width=800, height=600)
skærm.tracer(0)  # Slår automatisk opdatering fra

# Venstre paddle (spilleren)
paddle_venstre = turtle.Turtle()
paddle_venstre.speed(0)
paddle_venstre.shape("square")
paddle_venstre.color("white")
paddle_venstre.shapesize(stretch_wid=5, stretch_len=1)
paddle_venstre.penup()
paddle_venstre.goto(-350, 0)

# Højre paddle (væggen - AI)
paddle_højre = turtle.Turtle()
paddle_højre.speed(0)
paddle_højre.shape("square")
paddle_højre.color("white")
paddle_højre.shapesize(stretch_wid=5, stretch_len=1)
paddle_højre.penup()
paddle_højre.goto(350, 0)

# Bolden
bold = turtle.Turtle()
bold.speed(0)
bold.shape("circle")
bold.color("white")
bold.penup()
bold.goto(0, 0)
bold.dx = .2  # Hastighed i x-retning
bold.dy = .2  # Hastighed i y-retning

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


running = True



### Funktioner til at bevæge paddle
##def paddle_op():
##  skriv koden
##  
##def paddle_ned():
##  skriv koden

def stop():
    global running
    running = False


# Tastaturbinding
skærm.listen()
##skærm.onkeypress(paddle_op, "Up")
##skærm.onkeypress(paddle_ned, "Down")
skærm.onkeypress(stop, "Escape")

# Hovedspil-løkke
while running:
    skærm.update()

    # Tastaturbinding
    
    
        
    # Flyt bolden
    
    
    # Kollision med top og bund
    
    
    # Kollision med venstre paddle
    
    
    # Kollision med højre paddle (AI)
    
    
    # AI-bevægelse (følger bolden)
    
    
    # Scoring
    
skærm.bye()
