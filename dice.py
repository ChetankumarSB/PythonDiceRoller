# Import the random module and render_template function from Flask
import random
from flask import render_template

# Define a function to roll a dice and return the result as an HTML string
def roll_dice():
    # Generate a random number between 1 and 6
    dice_number = random.randint(1, 6)
    # Render the dice.html template with the dice number
    return render_template('dice.html', dice_number=dice_number)
