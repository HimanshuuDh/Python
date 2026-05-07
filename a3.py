import turtle
import random

# Constants for window size and layout
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
SPOT_SIZE = 40
ROWS = 3
COLS = 10
START_X = -350
START_Y = 200

# Availability percentages based on check-in hour
AVAILABILITY_RATES = {
    '7-11': 0.2,
    '12-17': 0.5,
    '18-23': 0.8,
    '0-6': 0.8
}

# Get availability percentage based on check-in hour
def get_availability_percentage(hour):
    if 7 <= hour <= 11:
        return AVAILABILITY_RATES['7-11']
    elif 12 <= hour <= 17:
        return AVAILABILITY_RATES['12-17']
    elif 18 <= hour <= 23 or 0 <= hour <= 6:
        return AVAILABILITY_RATES['18-23']
    else:
        return 0.8

# Decide if a spot is available or not
def generate_spot_status(hour):
    availability = get_availability_percentage(hour)
    return 'unavailable' if random.random() > availability else 'available'

# Draw a parking spot
def draw_spot(t, x, y, status, color_available='green', color_unavailable='red'):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color_available if status == 'available' else color_unavailable)
    t.begin_fill()
    for _ in range(4):
        t.forward(SPOT_SIZE)
        t.right(90)
    t.end_fill()

# Show legend
def display_legend(t):
    display_text(t, 'Green: Available', START_X - 100, START_Y + 20)
    display_text(t, 'Red: Unavailable', START_X - 100, START_Y)

# Display text helper
def display_text(t, message, x, y, font=('Arial', 12, 'normal')):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.write(message, align='center', font=font)

# Main function
def main():
    # Setup screen
    screen = turtle.Screen()
    screen.setup(WINDOW_WIDTH, WINDOW_HEIGHT)

    # Create turtle
    t = turtle.Turtle()
    t.speed(0)
    turtle.tracer(0)

    # Set check-in hour (change this for testing)
    check_in_hour = 10
    # OR Uncomment below for user input:
    # print("Enter check-in hour (0-23):")
    # check_in_hour = int(input())

    spots = []

    # Generate spots
    for row in range(ROWS):
        for col in range(COLS):
            x = START_X + col * (SPOT_SIZE + 10)
            y = START_Y - row * (SPOT_SIZE + 20)
            status = generate_spot_status(check_in_hour)
            spots.append((x, y, status))

    # Draw spots
    for (x, y, status) in spots:
        draw_spot(t, x, y, status)

    # Show legend
    display_legend(t)

    # Finalize drawing
    turtle.update()

    # Wait for click to close
    screen.exitonclick()

if __name__ == "__main__":
    main()