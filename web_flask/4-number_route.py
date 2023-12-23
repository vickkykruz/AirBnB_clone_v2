#!/usr/bin/python3
"""
Write a script that starts a Flask web application:

    => Your web application must be listening on 0.0.0.0, port 5000
    => Routes:
        => /: display “Hello HBNB!”
        => /hbnb: display “HBNB”
        => /c/<text>: display “C ”, followed by the value of the text
            variable (replace underscore _ symbols with a space )
        => /python/(<text>): display “Python ”, followed by the value of
            the text variable (replace underscore _ symbols with a space )
        => The default value of text is “is cool”
        => /number/<n>: display “n is a number” only if n is an integer
    => You must use the option strict_slashes=False in your route definition
"""


from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """ This is a function that retun the index page and display Hello HBNB!
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ This is a function that return the hbnb page and display HBNB """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """ This is a function that return the /c/text page and display C followed
        by the text variable
    """
    text = text.replace('_', ' ')
    return f'C {escape(text)}'


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python", strict_slashes=False)
def python_text(text="is cool"):
    """ This is a function that reurn the /python/<text> page or /python page
        and display Python followed by the text variable
    """
    text = text.replace('_', ' ')
    return f'Python {escape(text)}'


@app.route("/number/<int:n>", strict_slashes=False)
def number_n(n):
    """ This is a function that return the /number/<n> page and display the
        number
    """
    return f'{n} is a number'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
