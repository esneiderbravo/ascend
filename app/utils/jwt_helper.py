import time
import jwt
import logging

from ascend.app import app


class JWTHelper:
    @classmethod
    def encode_user(cls, user):
        """
        Encode user payload as a JWT.

        Args:
            user (dict): User payload to encode.

        Returns:
            str: Encoded user payload as JWT.
        """
        encoded_data = jwt.encode(payload=user, key=app.config["TOKEN_SECRET_KEY"])
        return encoded_data

    @classmethod
    def decode_user(cls, token):
        """
        Decode JWT token.

        Args:
            token (str): JWT token to decode.

        Returns:
            dict: Decoded token data.

        Raises:
            jwt.ExpiredSignatureError: If token has expired.
            jwt.InvalidTokenError: If token is invalid.
            Exception: For any unexpected errors.
        """
        try:
            decoded_data = jwt.decode(
                token, algorithms=["RS256"], options={"verify_signature": False}
            )
            return decoded_data
        except jwt.ExpiredSignatureError:
            logging.error("Token has expired")
            raise
        except jwt.InvalidTokenError:
            logging.error("Invalid token")
            raise
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            raise

    @classmethod
    def validate(cls, access_token):
        """
        Validate access token.

        Args:
            access_token (str): Access token to validate.

        Returns:
            tuple: Tuple containing a boolean indicating validity and decoded token data.

        Raises:
            jwt.DecodeError: If token decoding fails.
        """
        try:
            decoded_token = cls.decode_user(access_token)
            expiration_timestamp = decoded_token["exp"]
            current_timestamp = time.time()
            return expiration_timestamp > current_timestamp, decoded_token
        except jwt.DecodeError:
            logging.error("Token decoding failed")
            raise
