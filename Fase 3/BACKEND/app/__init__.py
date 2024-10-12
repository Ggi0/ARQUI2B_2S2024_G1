from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    # Habilitar CORS para permitir solicitudes desde cualquier origen
    # O específicamente desde http://localhost:3000
    CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

    # Registro de rutas
    from .routes import configure_routes
    configure_routes(app)

    return app
