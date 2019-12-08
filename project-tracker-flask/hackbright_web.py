"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)

@app.route("/")
def homepage():
    """Show homepage with list of students and list of projects, with links"""

    students = hackbright.get_student_list()
    projects = hackbright.get_project_list()

    html = render_template('homepage.html',
                            projects=projects,
                            students=students)
    return html


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)
    projects = hackbright.get_grades_by_github(github)

    html = render_template('student_info.html',
                            first=first,
                            last=last,
                            github=github,
                            projects=projects)

    # return "{} is the GitHub account for {} {}".format(github, first, last)
    return html

@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")


@app.route("/add-student", methods=['POST'])
def add_student():
    """add a student from form"""

    fname = request.form.get('fname')
    lname = request.form.get('lname')
    github = request.form.get('github')

    hackbright.make_new_student(fname, lname, github)

    html = render_template('new_student_added.html',
                            github=github)
    return html


@app.route("/student-add")
def new_student():
    """render form to add new student"""

    return render_template("student_add.html")


@app.route("/project")
def get_project():
    """get project information page"""
    title = request.args.get('title')
    information = hackbright.get_project_by_title(title)
    grades = hackbright.get_grades_by_title(title)

    html = render_template('project_info.html',
                          information=information,
                          grades=grades)
    return html

if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")
