import json

import redis
import requests
from decorator import decorator

from contrib.redis_config import redis_config

r = redis.StrictRedis(**redis_config)


@decorator
# 10 seconds on expiration were set to facilitate testing
def cache(func, http='GET', expiration=10, *args, **kwargs):
    """ Stores data in Redis """
    url = args[0]
    key = f'{http}_{url}'
    if not r.exists(key):
        response = func(*args, **kwargs)
        data = json.dumps(response)
        r.setex(key, expiration, data)
        return response
    else:
        return json.loads(r.get(key))


@cache
def get(url, parameters=None):
    """ Fetches an URL and returns the response """
    return requests.get(url, params=parameters).json()


@cache(http='POST')
def post(url, parameters=None, data=None):
    """ Post data to an URL and returns the response """
    return requests.post(url, params=parameters).json()


@cache(http='PUT')
def put(url, parameters=None, data=None):
    """ Put data to an resource and returns the response """
    return requests.put(url, params=parameters).json()


@cache(http='PATCH')
def patch(url, parameters=None, data=None):
    """ Patches an resource and returns the response """
    return requests.patch(url, params=parameters).json()


@cache(http='DELETE')
def delete(url, parameters=None, data=None):
    """ Requests the deletion of an resource and returns the response """
    return requests.delete(url, params=parameters).json()
