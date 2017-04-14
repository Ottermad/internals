"""List of all services."""


class Service:
    """Class representing a microservice."""

    def __init__(self, host):
        """Store URL of service."""
        self.host = host

USER_SERVICE = Service('http://user')
