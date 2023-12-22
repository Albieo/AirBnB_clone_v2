from flask import Flask
from markupsafe import escape
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    new_text = escape(text).replace("_", " ")
    return "C {}".format(new_text)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
