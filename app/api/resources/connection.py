from flask_restful import Resource


class ConnectionAPI(Resource):
    def get(self):
        """
        Get connection check
        :return: {"message": "Service ON"}
        """
        return {"message": "Service ON!"}, 200
