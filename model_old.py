"""

"""
import pickle
import dbm


db_file = 'database'

def init_db():
    with dbm.open(db_file, 'c') as db:
        init_list = [
        ('feed dog', 'remember to mix the two kinds'),
        ('go to store', 'need mustard and hot dogs'),
        ('clean house', 'vacuum both rugs'),
        ]

        db['todos'] = pickle.dumps(init_list)


def get_todos():
    """should return a list of todos"""
    with dbm.open(db_file, 'r') as db:
        return pickle.loads(db['todos'])

def add_todo(todo):
    """ todo has to be a tuple of 2 things """

    with dbm.open(db_file, 'w') as db:
        todos = pickle.loads(db['todos'])
        todos.append(todo)
        db['todos'] = pickle.dumps(todos)