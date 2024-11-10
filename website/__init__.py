from flask import Flask

def crear_aplicacio():
    app = Flask(__name__)
    app.config['SECRET_KEY']= 'Hola'
    from .auth import auth
    app.register_blueprint(auth, url_prefix='/')
    return app