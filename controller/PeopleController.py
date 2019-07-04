from models.People import People
from flask import Blueprint, request, jsonify


class PeopleController():

    def post(self, data):
        person = People(data)

        try:
            result = person.insert()
        except Exception as identifier:
            return jsonify({"error": str(identifier), "code": 500})

        if isinstance(result, list):
            return jsonify({
                "error": result,
                "code": 400
            }), 400

        return jsonify({
            "message": "Pessoa adicionada com sucesso",
            "response": result
        }), 201
