from os import environ
from dotenv import load_dotenv, find_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path, override=False)
AWS_ACCESS_KEY = environ.get('AWS_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = environ.get('AWS_SECRET_ACCESS_KEY')
AWS_BUCKET_NAME = environ.get('AWS_BUCKET_NAME')
AWS_PROJECT_NAME = environ.get('AWS_PROJECT_NAME')
AWS_REGION = environ.get('AWS_REGION')
AWS_BUCKET_ENDPOINT = environ.get('AWS_BUCKET_ENDPOINT')


class Config:

    # Configuracoes flask e sql 
    DEBUG = environ.get("DEBUG")
    SQLALCHEMY_TRACK_MODIFICATIONS = environ.get("SQLALCHEMY_TRACK_MODIFICATIONS")
    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
