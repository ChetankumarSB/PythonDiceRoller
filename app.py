# Import Flask module and other required libraries
from flask import Flask, render_template
import random

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def index():
    # Render the index.html template
    return render_template('index.html')

# Define a route for the dice roll page
@app.route('/dice')
def dice():
    # Generate a random number between 1 and 6
    random_number = random.randint(1, 6)
    # Render the dice.html template with the random number
    return render_template('dice.html', random_number=random_number)

# Start the Flask application if this file is executed directly
if __name__ == '__main__':
    app.run(debug=True)