#!/usr/bin/python3
"""
Flask web application to display filters for States, Cities, and Amenities.
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


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """
    Display a HTML page with filters for State, City, and Amenity objects.
    """
    states = sorted(storage.all("State").values(), key=lambda state: state.name)
    amenities = sorted(storage.all("Amenity").values(), key=lambda amenity: amenity.name)
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
