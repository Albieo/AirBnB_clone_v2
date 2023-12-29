#!/usr/bin/python3
"""
A script that starts a Flask web application:
    -> web application must be listening on 0.0.0.0, port 5000
    -> Routes:
        /: display “Hello HBNB!”
        /hbnb: display “HBNB”
        /c/<text>: display “C ” followed by the value of
            the text variable (replace underscore _ symbols with a space )
"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ Display 'Hello HBNB!' """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Display 'HBNB!' """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """ Display 'C {and some text input}' """
    new_text = escape(text).replace("_", " ")
    return "C {}".format(new_text)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
