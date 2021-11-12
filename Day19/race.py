from turtle import Turtle, Screen, textinput
import random

def DrawFinishLine(finish_line):
    t = Turtle()
    t.speed("fastest")
    t.hideturtle()
    t.pencolor("red")
    t.pensize(5)
    t.penup()
    t.setx(finish_line + 10)
    t.sety(-300)
    t.pendown()
    t.goto(finish_line + 10, 300)

def GetStartPositions(screen, num_turtles):
    starting_positions = []
    for x in range(num_turtles):
        screen_height = screen.window_height()
        # Find the even space between turtles over half the screen
        turtle_space = (screen_height / 2) / num_turtles
        # Start the turtles to the left of the screen
        xpos = (-screen.window_width() /2) + 20
        # Spread the turtles evenly 
        ypos = (screen_height / 4) - (x * turtle_space)
        new_pos = (xpos, ypos)
        starting_positions.append(new_pos)
    return starting_positions

screen = Screen()
colors = ['red', 'blue', 'green', 'orange', 'yellow', 'purple', 'black']
turtles = []
num_turtles = 6
winner = ""
user_choice = ""

# Assign the x position of the finish line to a variable and draw it.
finish_line = (screen.window_width() / 2) - 40
DrawFinishLine(finish_line)
# Get the list of starting positions
starting_positions = GetStartPositions(screen, num_turtles)

# Create a number of turtles 
for x in range(num_turtles):
    # Create a new turtle with a unique color from the list
    turtle = Turtle(shape='turtle')
    turtle.color(colors[x])
    # Move the turtle to it's starting position
    turtle.penup()
    turtle.goto(starting_positions[x])
    # Add a turtle to the list of turtles
    turtles.append(turtle)

# Ask the user to pick who they think will win
while user_choice == "":
    input = textinput("Make a Choice", "Who do you think will win?: ")
    # Verify that the answer is an available option.
    if colors.__contains__(input.lower()):
        user_choice = input.lower()

# While no winner is found, continue racing
while winner == "":
    for x in range(num_turtles):
        # All turtles stop moving when a winner is found.
        if winner == "":
            cur_turtle = turtles[x]
            pos = cur_turtle.pos()
            random_move = random.randint(1, 10)
            # Check to see if the turtle will win during it's next move.
            if pos[0] + random_move >= finish_line:
                # If it will win, only move it to the finish line
                cur_turtle.setx((screen.window_width() / 2) - 40)
                winner = colors[x]
            else:
                # If it will not win, move the turtle its full move
                cur_turtle.forward(random_move)
                
print(f"{winner.upper()} is the winner!")
if(user_choice == winner):
    print(f"You chose correctly! Good Job {user_choice.upper()}!")
else:
    print(f"Better luck next time {user_choice.upper()}!")

screen.exitonclick()