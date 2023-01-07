from flask import Blueprint, request
from flasgger import swag_from
from ..service.event import save_events
from flask_restx import Resource, Api
import json

blueprint = Blueprint('api', __name__)
analytics_api = Api(blueprint)

@analytics_api.route('/event', methods=["POST"])
class AnalyticsEvent(Resource):
    def post(self):
        if len(request.data) == 0:
            return {"status": "success"}, 200
        data = json.loads(request.data)
        return save_events(data)
