#!/usr/bin/python3
"""
A script that starts a Flask web application:
    -> web application must be listening on 0.0.0.0, port 5000
    -> Routes:
        /cities_by_states: display a HTML page: (inside the tag BODY)
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
from sqlalchemy.sql.expression import text

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """
    display a HTML page:
        H1 tag: 'State'
        UL tag: 'List of states in DBStorage'
            LI tag: "State: <state.id>: <state.name>
            UL tag : 'List of City'
                LI tag: "City: <city.id>: <city.name>"
    """
    from models import storage
    all_states = storage.all("State")
    sorted_states = sorted(all_states.values(), key=lambda state: state.name)

    return render_template('8-cities_by_states.html', states=sorted_states)


@app.teardown_appcontext
def teardown_storage(exception):
    """ Close the storage session after each request """
    from models import storage
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
