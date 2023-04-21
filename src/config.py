import os

from dotenv import load_dotenv

load_dotenv()

db_name: str = os.getenv('DB_NAME', default='postgres')
db_user: str = os.getenv('DB_USERNAME', default='postgres')
db_pass: str = os.getenv('DB_PASSWORD', default='postgres')
db_host: str = os.getenv('DB_HOST', default='localhost')
db_port: str = os.getenv('DB_PORT', default='5432')
redis_host: str = os.getenv('REDIS_HOST', default='localhost')
origins: str = os.getenv('ORIGINS', default=['127.0.0.1'])
allow_credentials: str = os.getenv('ALLOW_CREDENTIALS', default=True)
allow_methods: str = os.getenv('ALLOW_METHODS', default=['*'])
allow_headers: str = os.getenv('ALLOW_HEADERS', default=['*'])
