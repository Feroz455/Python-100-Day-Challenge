from turtle import Turtle, Screen
import random

# Create screen and set up the turtles
screen = Screen()
screen.setup(width=500, height=400)

turtle_colors = ["red", "blue", "green", "orange", "purple"]
turtles = []

for color in turtle_colors:
    turtle = Turtle(shape="turtle")
    turtle.color(color)
    turtle.penup()
    turtles.append(turtle)

# Position the turtles at the starting line
start_line = -100
for turtle in turtles:
    turtle.goto(x=-230, y=start_line)
    start_line += 50

# Player's betting functionality
player_bet = screen.textinput(
    "Place Your Bet", "Which turtle will win? Enter color:").lower()

# Race the turtles
race_on = True

while race_on:
    for turtle in turtles:
        distance = random.randint(1, 10)
        turtle.forward(distance)

        if turtle.xcor() >= 230:
            winner_color = turtle.color()[0]
            race_on = False
            break

# Declare the winner
winner_turtle = [turtle for turtle in turtles if turtle.color()[
    0] == winner_color][0]
winner_turtle.goto(0, 0)
winner_turtle.color("black")
winner_turtle.write(f"Winner: {winner_color.capitalize()} Turtle",
                    align="center", font=("Arial", 16, "bold"))

# Determine the result of the player's bet
if player_bet == winner_color:
    result = "Congratulations! You won!"
else:
    result = "Sorry, you lost."

# Close the screen on click
screen.exitonclick()
