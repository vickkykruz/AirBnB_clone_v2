#!/usr/bin/python3
"""
Write a script that starts a Flask web application:

    => Your web application must be listening on 0.0.0.0, port 5000
    => Routes:
        => /: display “Hello HBNB!”
        => /hbnb: display “HBNB”
        => /c/<text>: display “C ”, followed by the value of the text
            variable (replace underscore _ symbols with a space )
        => /python/<text>: display “Python ”, followed by the value of the
            text variable (replace underscore _ symbols with a space )
        => The default value of text is “is cool”
    => You must use the option strict_slashes=False in your route definition
"""


from flask import Flask, redirect, url_for
from markupsafe import escape


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """
        This is a function that return the index page and dispay Hello HBNB
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ This is a function that return the hbnb page and display HBNB to the
        user
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """ This is a function that return the page and display C then the <text>
        variable
    """
    text = text.replace('_', ' ')
    return f'C {escape(text)}'


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python", strict_slashes=False)
def python_text(text="is cool"):
    """ This is a fuction that return the page and display Python then the
        <text> variable
    """
    text = text.replace('_', ' ')
    return f'Python {escape(text)}'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
