from flask import Flask, redirect, url_for, request, render_template
from routes.people import people
from routes.jobs import jobs
from routes.applications import applications

app = Flask(__name__)

app.register_blueprint(people)
app.register_blueprint(jobs)
app.register_blueprint(applications)


@app.route('/')
def todo():
    return "See documentation"


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
