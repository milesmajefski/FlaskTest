"""

"""
from webapp import db


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=False, nullable=False)
    detail = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return '<Todo %r>' % self.title



def init_db():
    db.create_all()
    if not Todo.query.all():
        todo1 = Todo(title='go to store', detail='get organic milk')
        todo2 = Todo(title='pickup kids', detail='@ 3:30 and 4:15')
        todo3 = Todo(title='feed lizard', detail='live food this week')
        db.session.add(todo1)
        db.session.add(todo2)
        db.session.add(todo3)
        db.session.commit()
    print(Todo.query.all())


def get_todos():
    """should return a list of todos"""
    return Todo.query.all()


def add_todo(todo):
    """ todo has to be a tuple of 2 things """
    todo1 = Todo(title=todo[0], detail=todo[1])
    db.session.add(todo1)
    db.session.commit()