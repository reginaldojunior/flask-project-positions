import os
from flask import Flask, redirect, url_for, request, render_template
from routes.people import people

app = Flask(__name__)

app.register_blueprint(people)


@app.route('/')
def todo():
    return "See a doc"


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
