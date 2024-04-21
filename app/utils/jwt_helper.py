import time

import jwt

from ascend.app import TOKEN_SECRET_KEY


class JWTHelper(object):
    @classmethod
    def encode_user(cls, user):
        """
        encode user payload as a jwt
        :param user:
        :return: encoded user payload
        """
        encoded_data = jwt.encode(payload=user, key=TOKEN_SECRET_KEY)

        return encoded_data

    @classmethod
    def decode_user(cls, token):
        """
        :param token: jwt token
        :return:
        """
        try:
            # Decode the JWT token
            decoded_data = jwt.decode(
                token, algorithms=["RS256"], options={"verify_signature": False}
            )
            return decoded_data
        except jwt.ExpiredSignatureError:
            print("Token has expired")
            raise
        except jwt.InvalidTokenError:
            print("Invalid token")
            raise
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            raise

    @classmethod
    def validate(cls, access_token):
        try:
            decoded_token = cls.decode_user(access_token)
            expiration_timestamp = decoded_token["exp"]
            current_timestamp = time.time()
            return expiration_timestamp > current_timestamp, decoded_token
        except jwt.DecodeError:
            raise
