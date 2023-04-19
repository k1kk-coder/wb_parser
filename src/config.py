import os
from dotenv import load_dotenv

load_dotenv()

db_name: str = os.getenv('DB_NAME', default='postgres')
db_user: str = os.getenv('DB_USERNAME', default='postgres')
db_pass: str = os.getenv('DB_PASSWORD', default='postgres')
db_host: str = os.getenv('DB_HOST', default='localhost')
db_port: str = os.getenv('DB_PORT', default='5432')