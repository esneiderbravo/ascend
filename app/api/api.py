from flask_restful import Api

from ascend.app import app
from ascend.app.api.resources.auth import AuthAPI
from ascend.app.api.resources.connection import ConnectionAPI

api = Api(app)
api.add_resource(ConnectionAPI, "/connection/check")
api.add_resource(AuthAPI, "/auth")
