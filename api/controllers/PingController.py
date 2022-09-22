from http import HTTPStatus
from flask_restful import Resource
from api.utils.logz import create_logger


class PingController(Resource):
    def __init__(self):
        self.logger = create_logger()

    def get(self):
        return {"message": "pong"}, HTTPStatus.OK

    def post(self):
        return {"error": "Error, method not allowed"}, HTTPStatus.METHOD_NOT_ALLOWED

    def put(self):
        return {"error": "Error, method not allowed"}, HTTPStatus.METHOD_NOT_ALLOWED

    def delete(self):
        return {"error": "Error, method not allowed"}, HTTPStatus.METHOD_NOT_ALLOWED

    def patch(self):
        return {"error": "Error, method not allowed"}, HTTPStatus.METHOD_NOT_ALLOWED
