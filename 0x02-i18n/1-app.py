#!/usr/bin/env python3
"""module task 1"""
from flask_babel import Babel
from flask import Flask, render_template


class Config:
    """Install the Babel Flask extension:"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@app.route('/')
def get_index() -> str:
    """1-index.html"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
