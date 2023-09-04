from utils.meta_client import AWSConfig
from config.config import config_env

user_pool_id = config_env['aws']['cognito']['user_pool_id']

class UsersController:
    @staticmethod
    def list_users():
        return AWSConfig().cognito.list_users(UserPoolId=user_pool_id)
