from bson.json_util import dumps
from models.Jobs import Jobs
from models.RankingJobs import RankingJobs
from flask import Blueprint, request, jsonify


class JobController():

    def post(self, data):
        job = Jobs(data)

        try:
            result = job.insert()
        except Exception as identifier:
            return jsonify({"error": str(identifier), "code": 500}), 500

        if isinstance(result, list):
            return jsonify({
                "error": result,
                "code": 400
            }), 400

        return jsonify({
            "message": "Vaga adicionada com sucesso",
            "response": result
        }), 201

    def getRanking(self, job_id):
        ranking = RankingJobs()
        ranks = ranking.getByJobId(job_id)

        return jsonify(
            ranks
        ), 200
