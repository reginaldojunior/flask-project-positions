from flask import Blueprint, request
from controller.ApplicationsController import ApplicationsController

applications = Blueprint('applications', __name__)


@applications.route("/v1/candidaturas", methods=["POST"])
def applications_create():
    data = request.json

    return ApplicationsController().post(data)
