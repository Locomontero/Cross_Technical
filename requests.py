import requests
import redis

redis_config = {
    'host': '<host>',
    'port': 6379,
    'db': 0
}

r = redis.StrictRedis(**redis_config)

redis_key = '<requests_params>_<time>'
data = json.dumps(vacancies_data)   #You have to serialize the data to json!
r.setex(
    redis_key,
    60*60,        # time to store data
    data
)

def get(url, parameters=None):
    """ Fetches an URL and returns the response """
    return requests.get(url, params=parameters).json()

def post(url, parameters=None, data=None):
    """ Post data to an URL and returns the response """
    return requests.post(url, params=parameters, data=data).json()

def put(url, parameters=None, data=None):
    """ Put data to an resource and returns the response """
    return requests.put(url, params=parameters, data=data).json()

def patch(url, parameters=None, data=None):
    """ Patches an resource and returns the response """
    return requests.patch(url, params=parameters, data=data).json()

def delete(url, parameters=None, data=None):
    """ Requests the deletion of an resource and returns the response """
    return requests.delete(url, params=parameters, data=data).json()


