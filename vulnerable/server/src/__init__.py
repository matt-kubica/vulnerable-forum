from flask import Flask
import logging

logging.basicConfig(level=logging.DEBUG)


def create_app():
    app = Flask(__name__, template_folder="templates")
    app.config['SECRET_KEY'] = 'extremely-secret-key'

    from .auth import auth as auth_blueprint
    from .main import main as main_blueprint
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)

    logging.debug('App initialized')
    return app