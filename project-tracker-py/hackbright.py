"""Hackbright Project Tracker.

A front-end for a database that allows users to work with students, class
projects, and the grades students receive in class projects.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()


def connect_to_db(app):
    """Connect the database to our Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///hackbright'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


def get_student_by_github(github):
    """Given a GitHub account name, print info about the matching student."""

    QUERY = """
        SELECT first_name, last_name, github
        FROM students
        WHERE github = :github
        """

    db_cursor = db.session.execute(QUERY, {'github': github})

    row = db_cursor.fetchone()
    if row:
        print("Student: {} {}\nGitHub account: {}".format(row[0], row[1], row[2]))
    else:
        print('That student does not exist.')


def make_new_student(first_name, last_name, github):
    """Add a new student and print confirmation.

    Given a first name, last name, and GitHub account, add student to the
    database and print a confirmation message.
    """
    QUERY = """
            INSERT INTO students (first_name, last_name, github)
            VALUES (:first_name, :last_name, :github)
    """
    db.session.execute(QUERY, {'first_name': first_name,
                               'last_name': last_name,
                               'github': github})
    db.session.commit()
    print(f'Successfully added student: {first_name} {last_name}')

def add_new_project(title, description, grade):
    QUERY = """
            INSERT INTO projects (title, description, max_grade)
            VALUES (:title, :description, :grade)
    """
    db.session.execute(QUERY, {'title': title,
                               'description': description,
                               'grade': grade})
    db.session.commit()
    print(f'Successfully added: {title}')


def get_project_by_title(title):
    """Given a project title, print information about the project."""
    
    QUERY = """
        SELECT title, description, max_grade
        FROM projects
        WHERE title = :title
    """

    db_cursor = db.session.execute(QUERY, {'title': title})
    row = db_cursor.fetchone()
    if row:
        print(f'Title: {row[0]}\nDescription: {row[1]}\nMax Grade: {row[2]}')
    else:
        print('That project does not exist.')


def get_grade_by_github_title(github, title):
    """Print grade student received for a project."""
    QUERY = """
            SELECT grade
            FROM grades
            WHERE student_github = :github AND project_title = :title
    """
    db_cursor = db.session.execute(QUERY, {'github': github,
                                           'title': title})
    row = db_cursor.fetchone()
    if row:
        print(f'Grade: {row[0]}')
    else:
        print('Project not found.')


def get_grades_by_student(name):
    """Print all grades a student has received"""
    QUERY = """
            SELECT project_title, grade
            FROM grades AS g
            JOIN students AS s ON (g.student_github = s.github)
            WHERE s.first_name = :name
    """
    db_cursor = db.session.execute(QUERY, {'name': name})
    rows = db_cursor.fetchall()
    if rows:
        print(f'Grades for student {name}:')
        for row in rows:
            print(f'Project: {row[0]}, Grade: {row[1]}')
    else:
        print('That student does not exist.')


def assign_grade(github, title, grade):
    """Assign a student a grade on an assignment and print a confirmation."""
    QUERY = """
        INSERT INTO grades(student_github, project_title, grade)
        VALUES (:github, :title, :grade)
    """
    db.session.execute(QUERY, {'github': github,
                               'title': title,
                               'grade': grade})
    db.session.commit()
    print(f'Project {title} assigned grade of {grade}.')


def handle_input():
    """Main loop.

    Repeatedly prompt for commands, performing them, until 'quit' is received
    as a command.
    """

    command = None

    while command != "quit":
        input_string = input("HBA Database> ")
        tokens = input_string.split()
        command = tokens[0]
        args = tokens[1:]

        if command == "student":
            github = args[0]
            get_student_by_github(github)

        elif command == "new_student":
            if len(args) == 3:
                first_name, last_name, github = args  # unpack!
                make_new_student(first_name, last_name, github)
            else:
                print('Please provide a first name, last name, and github.')

        elif command == "get_project":
            title = args[0]
            get_project_by_title(title)

        elif command == "get_grade":
            if len(args) == 2:
                github, title = args
                get_grade_by_github_title(github, title)
            else:
                print('Provide github and title')

        elif command == "assign_grade":
            if len(args) == 3:
                github, title, grade = args
                assign_grade(github, title, grade)
            else:
                print('Provide github, title and grade')

        elif command == "new_project":
            if len(args) >= 3:
                if type(args[1]) == int:
                    title = args[0]
                    grade = args[1]
                    description = ""
                    for arg in args[2:]:
                        description = description + " " + arg
                    add_new_project(title, description, grade)
                else:
                    print('Provide grade after title')
            else:
                print('Provide title, grade and description')

        elif command == "get_grade_by_student":
            name = args[0]
            get_grades_by_student(name)

        else:
            if command != "quit":
                print("Invalid Entry. Try again.")



if __name__ == "__main__":
    connect_to_db(app)

    handle_input()

    # To be tidy, we close our database connection -- though,
    # since this is where our program ends, we'd quit anyway.

    db.session.close()
