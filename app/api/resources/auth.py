from flask_restful import Resource, reqparse

from ascend.app.utils.jwt_helper import JWTHelper
from ascend.database.managers.user import UserManager


class AuthAPI(Resource):
    """
    Auth API
    """

    @classmethod
    def post(cls):
        """
        Make authentication request
        :return: Authentication response
        """
        try:
            params = cls.__get_post_params()
            token = params.get("token")
            isValid, userData = JWTHelper.validate(token)
            if isValid and userData:
                username = userData["email"]
                userStored = UserManager.get(filter_values={"username": username})
                if not userStored:
                    UserManager.create({"username": username, "email": username})
                return {"userData": userData}, 200
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            raise

    @classmethod
    def __get_post_params(cls):
        """
        Returns post params
        :return: request params
        """
        parser = reqparse.RequestParser()
        parser.add_argument("token", type=str, required=True)
        params = dict(parser.parse_args())
        return params
