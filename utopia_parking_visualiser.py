# Utopia Parking Spot Visualiser (FINAL VERSION)

import turtle
import random

# ---------------- CONSTANTS ----------------
SPOT = 25
GAP = 5

LEFT_START_X = -300
RIGHT_START_X = 50

TOP_Y = 180
BLOCK_GAP = 40

ROWS_PER_BLOCK = 2
BLOCKS = 3
COLS = 6

# ---------------- SETUP ----------------
turtle.setup(900, 600)
turtle.speed(0)
turtle.hideturtle()
turtle.tracer(0)

# ---------------- FUNCTIONS ----------------
# Returns parking availability percentage
def get_availability(hour):
    if 7 <= hour <= 11:
        return 0.2
    elif 12 <= hour <= 17:
        return 0.5
    else:
        return 0.8

# Draws one parking spot square
def draw_spot(x, y, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(SPOT)
        turtle.right(90)
    turtle.end_fill()


def draw_block(start_x, start_y, availability, avail_c, unavail_c):
    for r in range(ROWS_PER_BLOCK):
        for c in range(COLS):

            x = start_x + c * (SPOT + GAP)
            y = start_y - r * (SPOT + GAP)

            if random.random() <= availability:
                color = avail_c
            else:
                color = unavail_c

            draw_spot(x, y, color)


def draw_all_blocks(availability, avail_c, unavail_c):
    current_y = TOP_Y

    for b in range(BLOCKS):
        # LEFT SIDE (A–F)
        draw_block(LEFT_START_X, current_y, availability, avail_c, unavail_c)

        # RIGHT SIDE (G–L)
        draw_block(RIGHT_START_X, current_y, availability, avail_c, unavail_c)

        current_y -= (ROWS_PER_BLOCK * (SPOT + GAP) + BLOCK_GAP)


def draw_labels():
    # Bottom labels A–L
    letters = "ABCDEFGHIJKL"

    # Left side (A–F)
    for i in range(6):
        turtle.penup()
        turtle.goto(LEFT_START_X + i * (SPOT + GAP) + 10, -200)
        turtle.write(letters[i], align="center", font=("Arial", 10, "bold"))

    # Right side (G–L)
    for i in range(6, 12):
        turtle.penup()
        turtle.goto(RIGHT_START_X + (i-6) * (SPOT + GAP) + 10, -200)
        turtle.write(letters[i], align="center", font=("Arial", 10, "bold"))

    # Side numbers 1–6
    y = TOP_Y - 10
    num = 6
    for b in range(BLOCKS):
        for r in range(2):
            turtle.penup()
            turtle.goto(0, y - r*(SPOT+GAP))
            turtle.write(str(num), align="center", font=("Arial", 10, "bold"))
            num -= 1

        y -= (ROWS_PER_BLOCK * (SPOT + GAP) + BLOCK_GAP)


def draw_legend(avail_c, unavail_c):
    # Available
    turtle.penup()
    turtle.goto(-150, -250)
    turtle.write("Available", font=("Arial", 12, "normal"))

    draw_spot(-200, -240, avail_c)

    # Unavailable
    turtle.penup()
    turtle.goto(50, -250)
    turtle.write("Unavailable", font=("Arial", 12, "normal"))

    draw_spot(0, -240, unavail_c)


# ---------------- MAIN ----------------

print("Utopia Parking Visualiser")

hour = int(input("Enter check-in hour (0–23): "))
availability = get_availability(hour)

avail_color = input("Available color: ")
unavail_color = input("Unavailable color: ")

draw_all_blocks(availability, avail_color, unavail_color)
draw_labels()
draw_legend(avail_color, unavail_color)

turtle.update()
turtle.done()