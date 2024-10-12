from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Registro de rutas
    from .routes import configure_routes
    configure_routes(app)

    return app
