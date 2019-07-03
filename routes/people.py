from flask import Blueprint, request, jsonify
from models.People import People

people = Blueprint('people', __name__)


@people.route("/v1/pessoas", methods=["POST"])
def people_create():
    data = request.json

    person = People(data)

    # try:
    result = person.insert()
    # except Exception as identifier:
    #     return jsonify({"error": str(identifier), "code": 500})

    if len(result) == 0:
        return jsonify({
            "error": result,
            "code": 400
        }), 400

    return jsonify({
        "message": "Pessoa adicionada com sucesso",
        "_id": "blah"
    }), 201
