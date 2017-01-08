"""Helper Functions."""
from .errors import NoJSONError, MissingKeyError, HTTPException


def get_integer_from_query_args(request, key, default_int):
    """Get an integer from query args."""
    value = request.args.get(key, default_int)
    try:
        value = int(value)
    except ValueError:
        raise HTTPException(
            409,
            {"message": "Value for {} is not a valid integer.".format(key)}
        )
    return value


def json_from_request(request):
    """Get JSON data from request."""
    data = request.get_json()
    if data is None:
        raise NoJSONError()
    return data


def check_keys(expected_keys, data):
    """Check keys are present in request."""
    for key in expected_keys:
        if key not in data.keys():
            raise MissingKeyError(key)
