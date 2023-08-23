from turtle import Turtle, Screen, shape
import pandas
import sys
import tkinter.simpledialog as simpledialog

# Set up the screen
screen = Screen()
screen.title("U.S States Game")
t = Turtle()
t.turtlesize(0.1)

# Load the image of the blank U.S. states map
img = "blank_states_img.gif"
screen.addshape(img)
shape(img)

# Read data from the CSV file
data = pandas.read_csv("50_states.csv")

# Loop for guessing states
for i in range(50):
    guessed_state = simpledialog.askstring(
        "Guess the State", f"Enter the name of a state ({i+1}/{50}):")

    if guessed_state is None:
        sys.exit("Game terminated by user.")

    guessed_state = guessed_state.title()

    if guessed_state == "Exit":
        sys.exit("Game terminated by user.")

    # Find the row in the DataFrame for the guessed state
    state_row = data[data["state"] == guessed_state]

    if not state_row.empty:
        x_coordinate = int(state_row['x'])
        y_coordinate = int(state_row['y'])
        t.penup()
        t.goto(x_coordinate, y_coordinate)
        t.write(guessed_state)

# Keep the screen open until it's clicked
screen.mainloop()
