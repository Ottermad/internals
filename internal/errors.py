from flask import jsonify

class HTTPError:
    """Class representing an error HTTP response."""

    def __init__(self, status_code=None, error_dict={}):
        """Initialise with status code and error_dict."""
        self.status_code = status_code
        self.error_dict = error_dict

    def add_error(self, key, error_message):
        """Add error to object."""
        if key in self.error_dict.keys():
            self.error_dict[key].append(error_message)
        else:
            self.error_dict[key] = [error_message]

    def json_response(self):
        """Return a reponse for Flask views."""
        return jsonify(self.error_dict), self.status_code


class HTTPException(Exception):
    """Exception that contains a status code and can be easily converted to json."""

    def __init__(self, status_code, error_dict={}):
        self.status_code = status_code
        self.error_response = HTTPError(
            status_code=status_code,
            error_dict=error_dict
        )


class MissingKeyError(HTTPException):
    """Error for when a request is missing a key."""

    def __init__(self, key):
        super().__init__(409)
        self.error_response.add_error(key, 'Required.')


class FieldInUseError(HTTPException):
    """Error for when a value for a property on a model is already in use."""

    def __init__(self, property, **kwargs):
        super().__init__(409)
        self.error_response.add_error(property, "Already in use.")


class NoJSONError(HTTPException):
    """Error for when no JSON is received."""

    def __init__(self):
        super().__init__(401)
        self.error_response.add_error(
            'message',
            "No JSON received. Please check Content-Type."
        )


class UnauthorizedError(HTTPException):
    """Return a generic 401 Unauthorized error."""

    def __init__(self):
        super().__init__(401)
        self.error_response.add_error(
            'message',
            "Unauthorized."
        )


class NotFoundError(HTTPException):
    """Return a generic 404 error."""

    def __init__(self):
        super().__init__(401)
        self.error_response.add_error(
            'message',
            "Not Found."
        )
