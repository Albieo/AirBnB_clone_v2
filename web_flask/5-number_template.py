#!/usr/bin/python3
"""
A script that starts a Flask web application:
    -> web application must be listening on 0.0.0.0, port 5000
    -> Routes:
        /: display “Hello HBNB!”
        /hbnb: display “HBNB”
        /c/<text>: display “C ” followed by the value of
            the text variable (replace underscore _ symbols with a space )
        /python/<text>: display “Python ”, followed by the value of
            the text variable (replace underscore _ symbols with a space )
            => The default value of text is “is cool”
        /number/<n>: display “n is a number” only if n is an integer
        /number_template/<n>: display a HTML page only if n is an integer:
            => H1 tag: “Number: n” inside the tag BODY
"""
from flask import Flask, render_template
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


@app.route("/python/", defaults={'text': "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text):
    """
    Display 'Python {and some text input}'

    Default text: 'Python is cool'
    """
    new_text = escape(text).replace("_", " ")
    return "Python {}".format(new_text)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """ Display '{some number} is a number' """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """
    Displays standard HTML with a dynamic h1 tag:

    <h1>Number: {some number}</h1>
    """
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
