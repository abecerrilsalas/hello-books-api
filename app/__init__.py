from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)

    from .routes import hello_world_bp #hey flask, from this file, go ahead and imort this variable
    app.register_blueprint(hello_world_bp)#this registers that variable with flask, so that it knows to use this blueprint for our roots.

    return app
    
