"""Websocket for Gateway"""

from enum import Enum

class HTTP_CODES(Enum):
    OK = 200
    CREATED = 201
    NO_CONTENT = 204
    NOT_MODIFIED = 304
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    METHOD_NOT_ALLOWED = 405
    TOO_MANY_REQUESTS = 429
    INTERNAL_SERVER_ERROR = 500
    GATEWAY_UNAVAILABLE = 502

class Socket:
    ...