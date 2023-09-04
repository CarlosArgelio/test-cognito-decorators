import os
from dotenv import load_dotenv

load_dotenv()

config_env = {
    'aws': {
        'region': os.getenv('REGION'),
        'cognito': {
            'user_pool_id': os.getenv('COGNITO_USER_POOL_ID'),
            'client_id': os.getenv('COGNITO_CLIENT_ID')
        }
    }
}
