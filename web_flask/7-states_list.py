#!/usr/bin/python3
"""
A script that starts a Flask web application:
    -> web application must be listening on 0.0.0.0, port 5000
    -> Routes:
        /states_list: display a HTML page: (inside the tag BODY)
            => H1 tag: “States”
            => UL tag: with the list of all State objects present 
               in DBStorage sorted by name (A->Z)
                => LI tag: description of one State: <state.id>: <B><state.name></B>
"""
from flask import Flask, render_template
from sqlalchemy.sql.expression import text

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """
    display a HTML page:
        H1 tag: 'State'
        UL tag: 'List of states in DBStorage'
    """
    from models import storage
    all_data = storage.all()
    sorted_states = sorted(all_data.values(), key=lambda state: state.name)

    return render_template('7-states_list.html', states=sorted_states)


@app.teardown_appcontext
def teardown_storage(exception):
    """ Close the storage session after each request """
    from models import storage
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
