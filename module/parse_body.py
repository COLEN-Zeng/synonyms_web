from sanic import json
from functools import wraps


def parse_body(request, response):
    request = request.json
    # ...
    # return
