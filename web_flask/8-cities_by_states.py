#!/usr/bin/python3
"""
Flask web application to display cities by states.
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


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
    Display an HTML page with a list of all State objects 
    and their linked City objects.
    """
    states = storage.all("State")
    states = sorted(states.values(), key=lambda state: state.name)
    
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)