from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    # Habilitar CORS para permitir solicitudes desde cualquier origen
    # O específicamente desde http://localhost:3000
    CORS(app, resources={r"/*": {"origins": ["https://astro-vercel-lkvr72rv2-202010040s-projects.vercel.app","https://astro-vercel-pi-three.vercel.app","https://2483-2800-98-1111-1327-00-7.ngrok-free.app"]}})

    # Registro de rutas
    from .routes import configure_routes
    configure_routes(app)

    return app
