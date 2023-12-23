#!/usr/bin/python3
"""
Write a script that starts a Flask web application:

    => Your web application must be listening on 0.0.0.0, port 5000
    => Routes:
        => /: display “Hello HBNB!”
        => /hbnb: display “HBNB”
        => /c/<text>: display “C ” followed by the value of the text
            variable (replace underscore _ symbols with a space )
    => You must use the option strict_slashes=False in your route definition
"""


from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """
        This function return the index page and deplay Hello HBNB to the user
    """
    return "Hello HBNB"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ This function return the hbnb page and display HBNB to the user """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """This function return C followed by the text to the user """
    text = text.replace('_', ' ')
    return f'C {escape(text)}'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
