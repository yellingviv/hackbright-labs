"""Movie Ratings."""

from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request, flash, session
# from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, User, Ratings, Movie
from datetime import datetime


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails
# silently. This is horrible. Fix this so that, instead, it raises an
# error.
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Homepage."""
    return render_template('homepage.html')


@app.route('/users')
def user_list():
    """Show list of users"""

    users = User.query.all()
    return render_template("user_list.html",
                           users=users)


@app.route('/users/<user_id>')
def show_user_page(user_id):
    """Shows page with user info including movies and ratings"""

    user = User.query.get(user_id)
    email = user.email
    zipcode = user.zipcode
    age = user.age
    movies = {}
    for rating in user.ratings:
        movie = rating.movie
        movies[movie.title] = rating.score
    return render_template("user_page.html",
                           user_id=user_id,
                           email=email,
                           zipcode=zipcode,
                           age=age,
                           movies=movies)


@app.route('/movies')
def show_all_movies():
    movie = Movie.query.order_by('title').all()
    return render_template("movie_list.html",
                           movies=movie)


@app.route('/movies/<movie_id>')
def show_movie_page(movie_id):
    """Shows page with movie info, including ratings"""
    movie = Movie.query.get(movie_id)
    title = movie.title
    release_date = datetime.strftime(movie.released_at, "%B %d, %Y")
    url = movie.imdb_url

    score_list = []
    for rating in movie.ratings:
        movie_score = rating.score
        score_list.append(movie_score)

    return render_template("movie_page.html",
                           title=title,
                           release_date=release_date,
                           url=url,
                           score_list=score_list)


@app.route('/register', methods=['POST'])
def register_user():
    """register a new user"""

    email = request.form['email']
    pw = request.form['password']
    in_db = User.query.filter_by(email=email).first()

    if in_db:
        flash('This email is already associated with an account.')
    else:
        user = User(email=email, password=pw)
        db.session.add(user)
        db.session.commit()
        flash('Account creation successful! You can now login.')

    return render_template("register_form.html")


@app.route('/register', methods=['GET'])
def register_form():
    """serve form for new user registration"""

    return render_template("register_form.html")


@app.route('/login', methods=['GET'])
def login_form():
    """shows login form for user to login"""

    return render_template("login.html")


@app.route('/login', methods=['POST'])
def attempt_login():
    """processes user login and allows them in or not"""
    email = request.form['email']
    pw = request.form['password']
    user = User.query.filter_by(email=email).first()
    if validity_check(user, pw):
        user_id = user.user_id
        session["user_id"] = user_id
        flash('Successful login')
        return redirect(f'/users/{user_id}')
    else:
        flash('Incorrect login information, please try again')
        return render_template('login.html')


def validity_check(user, pw):
    """check if user exists"""
    return user and user.password == pw


@app.route('/logout')
def logout():
    """Logs out user and returns to homepage"""

    if session.get('user_id'):
        session.pop("user_id")
        flash('Logged out successfully')
    return redirect('/')


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True
    # make sure templates, etc. are not cached in debug mode
    app.jinja_env.auto_reload = app.debug

    connect_to_db(app)

    # Use the DebugToolbar
    # DebugToolbarExtension(app)

    app.run(port=5000, host='0.0.0.0')
