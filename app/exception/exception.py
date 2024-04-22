class ApiException(Exception):
    """Class for API exceptions."""

    def __init__(self, user_friendly_message, status_code=500, message=None):
        """
        Initialize ApiException.

        Args:
            user_friendly_message (str): User-friendly message describing the error.
            status_code (int, optional): HTTP status code associated with the error. Defaults to 500.
            message (str, optional): Detailed error message. Defaults to None.
        """
        super().__init__(user_friendly_message)
        self.user_friendly_message = user_friendly_message
        self.status_code = status_code
        self.message = message

    def __str__(self):
        """
        Return a string representation of the exception.

        Returns:
            str: String representation of the exception.
        """
        return f"{self.__class__.__name__}(user_friendly_message={self.user_friendly_message}, status_code={self.status_code}, message={self.message})"


class JsonDecodeError(ValueError):
    """
    Class to identify an exception raised if json.loads method fails due to non-serializable data.
    """

    def __init__(self, text):
        """
        Initialize JsonDecodeError.

        Args:
            text (str): Name of the parameter involved in the error.
        """
        self.text = text
        self.message = f"The received text couldn't be decoded: {self.text}"

    def __str__(self):
        """
        Return a string representation of the exception.

        Returns:
            str: String representation of the exception.
        """
        return f"{self.__class__.__name__}(text={self.text}, message={self.message})"
