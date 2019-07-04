from models.Jobs import Jobs
from flask import Blueprint, request, jsonify


class JobController():

    def post(self, data):
        job = Jobs(data)

        try:
            result = job.insert()
        except Exception as identifier:
            return jsonify({"error": str(identifier), "code": 500})

        if isinstance(result, list):
            return jsonify({
                "error": result,
                "code": 400
            }), 400

        return jsonify({
            "message": "Vaga adicionada com sucesso",
            "response": result
        }), 201
