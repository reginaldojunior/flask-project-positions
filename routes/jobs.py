from flask import Blueprint, request
from controller.JobController import JobController

jobs = Blueprint('jobs', __name__)


@jobs.route("/v1/vagas", methods=["POST"])
def jobs_create():
    data = request.json

    return JobController().post(data)
