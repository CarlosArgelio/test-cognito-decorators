from boto3 import client
from functools import wraps
from config.config import config_env

region_name = config_env['aws']['region']

def singleton(cls):
    instances = {}

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper

@singleton
class AWSConfig():
    def __init__(self):
      try:
        self.cognito = client('cognito-idp', region_name=region_name)
      except ValueError as e:
        print('Error: ', e)
