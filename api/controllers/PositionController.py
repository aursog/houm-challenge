from http import HTTPStatus
from flask import request
from flask_restful import Resource, reqparse
from api.services.PositionService import PositionService
from api.utils.logz import create_logger


class PositionController(Resource):
    parser = reqparse.RequestParser()

    def __init__(self):
        self.logger = create_logger()

    def post(self):
        self.logger.info(f'parsed args: {request.get_json()}')
        return PositionService.registry_position(request.get_json()), HTTPStatus.OK
