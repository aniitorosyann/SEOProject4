from flask import Flask

#name database
DB_NAME = "database.db"

#define function to create flask application
def create_app():
    #create instance of Flask class
    app = Flask(__name__)
    #create secret key
    app.config['SECRET_KEY'] = 'our secret key'

    #import modules
    from .views import views
    from .auth import auth
    from .data import data

    #create file blueprints
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(data, url_prefix='/api')

    #return the app
    return app
