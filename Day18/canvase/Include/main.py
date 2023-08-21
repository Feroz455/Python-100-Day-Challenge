from turtle import Turtle, Screen
import random

# Create a turtle instance
timmy_the_turtle = Turtle()

# Set the turtle's speed
timmy_the_turtle.speed("fastest")  # Use "fastest" for quicker drawing

# Set the pen width
timmy_the_turtle.width(2)

# Get the screen dimensions
screen_width = timmy_the_turtle.screen.window_width()
screen_height = timmy_the_turtle.screen.window_height()

# Calculate the step size based on the dot size
dot_size = 10  # Adjust the dot size as needed
step_size = dot_size * 1.5

# Calculate the number of rows and columns
num_columns = int(screen_width // step_size)
num_rows = int(screen_height // step_size)

# Set the starting position at the top-left corner
start_x = -screen_width / 2 + dot_size / 2
start_y = screen_height / 2 - dot_size / 2
timmy_the_turtle.penup()
timmy_the_turtle.goto(start_x, start_y)  # Set the starting position
timmy_the_turtle.pendown()

# List of colors to alternate between
dot_colors = ["blue", "green", "red", "orange", "purple"]

# Draw dots to fill the entire page
for row in range(num_rows):
    for column in range(num_columns):
        timmy_the_turtle.color(random.choice(dot_colors))  # Set a random color
        dot_size = random.randint(5, 15)  # Generate a random dot size
        timmy_the_turtle.dot(dot_size)  # Draw a dot with the chosen size
        timmy_the_turtle.penup()   # Lift the pen
        timmy_the_turtle.forward(step_size)  # Move forward to create the next dot
        timmy_the_turtle.pendown()   # Lower the pen
    timmy_the_turtle.penup()  # Move to the start of the next row
    timmy_the_turtle.goto(start_x, start_y - (row + 1) * step_size)
    timmy_the_turtle.pendown()

# Hide the turtle
timmy_the_turtle.hideturtle()

# Create the screen
screen = Screen()
screen.exitonclick()
