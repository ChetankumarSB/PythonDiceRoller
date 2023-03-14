from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/roll_dice", methods=["POST"])
def roll_dice():
    num_dice = int(request.form["num_dice"])
    num_sides = int(request.form["num_sides"])
    rolls = []
    for i in range(num_dice):
        roll = random.randint(1, num_sides)
        rolls.append(roll)
    return render_template("roll_dice.html", rolls=rolls)

if __name__ == "__main__":
    app.run(debug=True)
