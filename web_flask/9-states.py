#!/usr/bin/python3
"""
A script that starts a Flask web application:
    -> web application must be listening on 0.0.0.0, port 5000
    -> Routes:
        /states: display a HTML page: (inside the tag BODY)
            => H1 tag: “States”
            => UL tag: with the list of all State objects present
               in DBStorage sorted by name (A->Z)
                => LI tag: description of one State:
                           <state.id>: <B><state.name></B> +
        /states/<id>: display a HTML page: (inside the tag BODY)
            *** If State exist with id ***
            => H1 tag: "State:"
            => H3 tag: "Cities:"
            => UL tag: list of City linked to State
                => LI tag: City: <city.id>: <B><city.name></B>
        Otherwise
            H1 tag: "Not found"
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """
    display a HTML page:
        H1 tag: 'State'
        UL tag: 'List of states in DBStorage'
    """
    from models import storage
    all_states = storage.all("State")
    sorted_states = sorted(all_states.values(), key=lambda state: state.name)

    return render_template('9-states.html', states=sorted_states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """
    display a HTML page:
        H1 tag: 'State'
        H3 tag: 'Cities'
        UL tag: list of 'City' objects - State
            LI tag: "City: <city.id>: <city.name>"
    """
    from models import storage
    for state in sorted(storage.all("State").values(),
                        key=lambda state: state.name):
        if state.id == id:
            return render_template('9-states.html', state=state)
    return render_template('9-states.html')


@app.teardown_appcontext
def teardown_storage(exception):
    """ Close the storage session after each request """
    from models import storage
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
