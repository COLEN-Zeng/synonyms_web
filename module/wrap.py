from sanic import json
from functools import wraps
from sanic.log import logger
from json import dumps, loads


def wrap():
    def decorator(f):
        @wraps(f)
        async def decorated_function(request, *args, **kwargs):
            logger.info('request: ' + str(request.json))
            response = await f(request.json, *args, **kwargs)
            logger.info('response: ' + dumps(response, ensure_ascii=False))
            return json(response, ensure_ascii=False)  # ensure_ascii=False

        return decorated_function

    return decorator
