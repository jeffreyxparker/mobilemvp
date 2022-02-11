import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    CORS_HEADERS = 'Content-Type'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI ='postgresql://postgres:12345678@localhost:5432/market'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
