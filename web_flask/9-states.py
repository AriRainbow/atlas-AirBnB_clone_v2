#!/usr/bin/python3
"""
Flask web application to display states and their cities.
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """
    Remove the current SQLAlchemy Session.
    """
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    """
    Display an HTML page with a list of all State objects
    from the database, sorted by name.
    """
    states = storage.all("State").values()
    states = sorted(states, key=lambda state: state.name)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def state_cities(id):
    """
    Display an HTML page with the State and its linked cities
    if the State with the given id exists, otherwise display 'Not found!'.
    """
    state = None
    for st in storage.all("State").values():
        if st.id == id:
            state = st
            break

    return render_template('9-states.html', state=state)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
