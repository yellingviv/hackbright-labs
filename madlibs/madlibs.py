"""A madlib game that compliments its users."""
from random import choice, sample
from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]

MADLIBS = [1, 2]

@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")
    compliment = sample(AWESOMENESS, 3)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)


@app.route('/game')
def show_madlib_form():
    """Send user to game or goodbye"""

    choice = request.args.get("choice")

    if choice == 'yes':
        return render_template("game.html")
    else:
        return render_template("goodbye.html")


@app.route('/madlib', methods=["POST"])
def show_madlib():
    """render the madlib page with the user input"""

    name = request.form.get("name")
    color = request.form.get("color")
    noun = request.form.get("noun")
    adjective = request.form.get("adjective")
    nounchoice = request.form.get("nounchoice")
    animal_list = request.form.getlist("animal")
    madlib_rand = choice(MADLIBS)

    return render_template("madlib.html",
                           par=madlib_rand,
                           name=name,
                           color=color,
                           noun=noun,
                           adjective=adjective,
                           nounchoice=nounchoice,
                           animal_list=animal_list
                           )


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
