from flask import jsonify
from .models import BaseData
import logging

# Crear instancia de BaseData
base_data = BaseData()

# Configura el logger
logger = logging.getLogger(__name__)

# Función para registrar las rutas en la app
def configure_routes(app):

    @app.route('/consulta_general', methods=['GET'])
    def obtener_colecciones():
        """
        Ruta que devuelve los datos de las colecciones en formato JSON.
        """
        try:
            data = base_data.consulta_general()  # Obtiene datos de la API o archivo local
            return jsonify(data), 200
        except Exception as e:
            # Registra el error en los logs con detalles
            logger.error(f"Error en obtener_colecciones: {str(e)}")
            return jsonify({"error": f"Error interno: {str(e)}"}), 500
    
    @app.route("/actualizar_datos", methods=["GET"])
    def actualizar_colecciones():
        """
        Ruta que fuerza la actualización de los datos desde la API.
        """
        try:
            data = base_data.consulta_general(actualizar=True)  # Fuerza la actualización desde la API
            return jsonify({"message": "Datos actualizados con éxito."}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
