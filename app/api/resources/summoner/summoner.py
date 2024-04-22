from flask import jsonify
from flask_restful import Resource, reqparse
from ascend.app.api.controllers.summoner import SummonerController


class SummonerAPI(Resource):
    """
    Summoner API.

    Handles summoner API methods.
    """

    @classmethod
    def get(cls):
        """
        Get summoner information.

        Returns:
            dict: Summoner response.
        """
        try:
            params = cls._parse_request_args()
            data = SummonerController.get_summoner_info(params)
            return jsonify({"data": data}), 200

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return {"error": "An unexpected error occurred"}, 500

    @classmethod
    def _parse_request_args(cls):
        """
        Parse request arguments.

        Returns:
            dict: Parsed request arguments.
        """
        parser = reqparse.RequestParser()
        parser.add_argument("tagLine", type=str, required=True)
        parser.add_argument("summonerName", type=str, required=True)
        args = parser.parse_args()
        return args
