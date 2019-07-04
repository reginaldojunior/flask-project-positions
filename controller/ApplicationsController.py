from models.Applications import Applications
from flask import Blueprint, request, jsonify


class ApplicationsController():

    def post(self, data):
        application = Applications(data)

        try:
            result = application.insert()
        except Exception as identifier:
            return jsonify({"error": str(identifier), "code": 500})

        if isinstance(result, list):
            return jsonify({
                "error": result,
                "code": 400
            }), 400

        return jsonify({
            "message": "Candidatura adicionada com sucesso",
            "response": result
        }), 201
