import os
from flask import Flask, render_template, send_from_directory, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import todo_model

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class HttpException(Exception):
    pass


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
    return redirect(url_for('hello'))

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/greeting")
def greeting():
    return "<h1>Hello</h1>"


@app.route("/")
def hello():
    return render_template('index.html', user='Somebody', data={'todos': todo_model.get_todos()})


if __name__ == "__main__":
    todo_model.init_db()
    app.run()
