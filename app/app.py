from flask import Flask

"""
pip install Flask
"""

app = Flask(__name__)


@app.route('/')
def hello():
    return "hello"
