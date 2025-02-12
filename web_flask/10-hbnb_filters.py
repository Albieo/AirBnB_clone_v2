#!/usr/bin/python3
"""
A script that starts a Flask web application:
    -> web application must be listening on 0.0.0.0, port 5000
    -> Routes:
        /hbnb_filters: display a HTML page: (inside the tag BODY)
            => H1 tag: “States”
            => UL tag: with the list of all State objects present
               in DBStorage sorted by name (A->Z)
                => LI tag: description of one State:
                           <state.id>: <B><state.name></B> +
                   UL tag: with the list of City objects linked
                           to the State sorted by name (A->Z)
                      => LI tag: description of one
                         City: <city.id>: <B><city.name></B>
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """
    display a HTML page:
        The main HBnB filters HTML page"
    """
    from models import storage
    all_states = storage.all("State")
    sorted_states = sorted(all_states.values(), key=lambda state: state.name)
    all_amenities = storage.all("Amenity")
    sorted_amenities = sorted(all_amenities.values(),
                              key=lambda amenity: amenity.name)
    return render_template('10-hbnb_filters.html',
                           states=sorted_states, amenities=sorted_amenities)


@app.teardown_appcontext
def teardown_storage(exception):
    """ Close the storage session after each request """
    from models import storage
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
