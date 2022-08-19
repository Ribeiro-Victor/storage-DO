from app.extensions import db, ma, migrate
from app.config import Config
from flask import Flask

from app.file.routes import file_api
from app.storageDireto.routes import storageDireto_api
from app.storagePreSigned.routes import storagePreSigned_api

def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(file_api)
    app.register_blueprint(storageDireto_api)
    app.register_blueprint(storagePreSigned_api)
    
    return app