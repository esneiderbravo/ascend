from flask_restful import Api
from ascend.app import app
from ascend.app.api.resources.auth import AuthAPI
from ascend.app.api.resources.connection import ConnectionAPI

# Create an instance of the Api class
api = Api(app)

# Register resources with the API
api.add_resource(ConnectionAPI, "/connection/check")
api.add_resource(AuthAPI, "/auth")
