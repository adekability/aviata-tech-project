import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='.env')

DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
SQLALCHEMY_DATABASE_URI = 'postgresql://'+DB_USER+':'+DB_PASS+'@'+DB_HOST+":"+DB_PORT+'/'+DB_NAME+'?client_encoding=utf-8'
CELERY_BROKER = os.getenv('CELERY_BROKER')
CELERY_BACKEND = os.getenv('CELERY_BACKEND')
CELERY_CONFIG = {"timezone": "Asia/Almaty"}
CPU_COUNT = os.cpu_count()
