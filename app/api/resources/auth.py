from flask_restful import Resource, reqparse
from ascend.app.utils.jwt_helper import JWTHelper
from ascend.database.managers.user import UserManager


class AuthAPI(Resource):
    """
    Auth API.

    Handles user authentication.
    """

    @classmethod
    def post(cls):
        """
        Make an authentication request.

        Returns:
            dict: Authentication response including user data if valid token,
                  otherwise returns an error.
        """
        try:
            token = cls._get_token_from_request()
            is_valid, user_data = JWTHelper.validate(token)

            if is_valid and user_data:
                username = user_data.get("email")
                if not UserManager.get(filter_values={"username": username}):
                    UserManager.create({"username": username, "email": username})

                return {"userData": user_data}, 200
            else:
                return {"error": "Invalid token"}, 401

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return {"error": "An unexpected error occurred"}, 500

    @classmethod
    def _get_token_from_request(cls):
        """
        Get the token from the request.

        Returns:
            str: Token string.
        """
        parser = reqparse.RequestParser()
        parser.add_argument("token", type=str, required=True)
        args = parser.parse_args()
        return args.get("token")
