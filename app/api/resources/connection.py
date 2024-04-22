from flask_restful import Resource
from flask import jsonify


class ConnectionAPI(Resource):
    @classmethod
    def get(cls):
        """
        Get connection check.

        Returns:
            dict: A JSON object indicating that the service is ON.
                Example: {"message": "Service ON!"}
        """
        return jsonify({"message": "Service ON!"}), 200
