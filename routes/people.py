from flask import Blueprint, request
from controller.PeopleController import PeopleController

people = Blueprint('people', __name__)


@people.route("/v1/pessoas", methods=["POST"])
def people_create():
    data = request.json

    return PeopleController().post(data)
