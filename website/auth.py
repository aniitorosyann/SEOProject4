from flask import Flask

DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'our secret key'

    from .views import views
    from .auth import auth
    from .data import data

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(data, url_prefix='/api')

    return app
