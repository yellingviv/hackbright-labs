"""Greeting Flask app."""
from random import choice
from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']

awesome_str = ''

for compliment in AWESOMENESS:
    awesome_str = awesome_str + '<option value="' + compliment + '">' + compliment + '</option>'


@app.route("/")
def start_here():
    """Home page."""

    return '''"<!doctype html><html><a href="/hello">
    Hi! This is the home page with a link.</a> </html>"'''


@app.route("/hello")
def say_hello():
    """Say hello and prompt for user's name."""

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1><BR>
        <BR>
        <b>Do you want to be praised?:</b>
        <BR>
        <form action="/greet">
          What's your name? <input type="text" name="person"><BR>
          Preferred superlative: 
          <select name="compliment">
            {awesome_str}
            </select><BR>
            <input type="radio" name="animal" value="cat">Cat
            <input type="radio" name="animal" value="dog">Dog<BR>
          <input type="submit" value="Submit">
          </form><BR>
          <BR>
          <b>Do you want to be dissed?:</b>
          <BR>
          <form action="/diss">
          What's your name? <input type="text" name="person"><BR>
          Preferred superlative: 
          <select name="compliment">
            {awesome_str}
            </select><BR>
            <input type="radio" name="animal" value="cat">Cat
            <input type="radio" name="animal" value="dog">Dog<BR>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route("/greet")
def greet_person():
    """Get user by name."""

    player = request.args.get("person")
    compliment = request.args.get("compliment")
    animal = request.args.get("animal")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're a {} {}!
      </body>
    </html>
    """.format(player, compliment, animal)


@app.route("/diss")
def insult_person():
    """Insult user by name."""

    player = request.args.get("person")
    compliment = request.args.get("compliment")
    animal = request.args.get("animal")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! You're the exact opposite of a {} {}!
      </body>
    </html>
    """.format(player, compliment, animal)


if __name__ == "__main__":
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
