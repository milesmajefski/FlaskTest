"""
repo: 
https://github.com/milesmajefski/FlaskTest.git

"""

import os
from collections import namedtuple
from flask import Flask, render_template, send_from_directory, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import todo_model
import csv


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

import_filename = 'import.csv'
imported_data = []

def chk_import():
    if (os.path.isfile(import_filename)):
        print('Found import file')
        do_import()        
    else:
        print('Didn\'t find file!')


Row = namedtuple('Row', ['title', 'details'])

def do_import():
    with open(import_filename, 'r', newline='') as fh:
        reader = csv.reader(fh)
        # reading into list of named tuples
        header = next(reader)
        for title, details in reader:
            imported_data.append(Row(title, details))
        print("len of data", len(imported_data))


class HttpException(Exception):
    def __repr__(self):
        return 'HttpException()'


@app.errorhandler(HttpException)
def page_not_found(e):
    return render_template('405.html'), 405


@app.route('/todos/add', methods=['POST'])
def add_todos():
    if request.method == 'POST':
        return do_the_add(request.form)
    else:
        # unnecessary?
        raise HttpException()


def do_the_add(form):
    # add data to database and reshow page
    todo_model.add_todo((form['Title'], form['Detail']))
    return redirect(url_for('main_page'))


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route("/")
def main_page():
    return render_template('index.html', 
        user='Somebody', 
        todos=todo_model.get_todos(), 
        imported_data=imported_data
        )


if __name__ == "__main__":
    chk_import()
    todo_model.init_db()
    app.run()
