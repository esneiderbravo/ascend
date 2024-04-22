import json
import requests

from ascend.app.exception.exception import ApiException, JsonDecodeError


def get(url):
    """
    Perform a GET request to the specified URL and handle response.
    """
    response = requests.get(url)
    return deserialize_and_verify_errors(response)


def deserialize_and_verify_errors(response, return_status_code=False):
    """
    Deserialize the HTTP response and verify for errors.
    """
    json_response = deserialize_json(response.text)
    verify_error_in_status_code(response.status_code, json_response)

    if return_status_code:
        json_response["status_code"] = response.status_code

    return json_response


def deserialize_json(text):
    """
    Deserialize a JSON string.
    """
    try:
        return json.loads(text)
    except ValueError as e:
        raise JsonDecodeError(text)


def verify_error_in_status_code(status, json_response):
    """
    Verify if the HTTP status code indicates an error and raise ApiException if needed.
    """
    if status in [400, 500]:
        verify_error_message_in_response(json_response)


def verify_error_message_in_response(json_response):
    """
    Verify the presence of error message in the JSON response and raise ApiException.
    """
    error_message = (
        json_response.get("message")
        or json_response.get("detail", {}).get("message")
        or "No error message found in the response: {}".format(json_response)
    )

    raise ApiException(error_message)
