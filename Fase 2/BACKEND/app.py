# Importa la base de datos
from services.vercel_db_service import BaseData

# Librerías de Flask
from flask import Flask, jsonify
from flask_cors import CORS
import logging

# Configuración del logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Inicializa la aplicación Flask
app = Flask(__name__)
CORS(app)

# Controlador de base de datos
base_data = BaseData()

@app.route("/consulta_general", methods=["GET"])
def consulta_general():
    """
    Ruta que devuelve los datos en el formato JSON desde el archivo local o la API.
    """
    try:
        datos = base_data.consulta_general(actualizar=False)  # Obtiene datos desde el archivo local o API
        logger.info("Consulta general realizada con éxito.")
        return jsonify(datos), 200
    except Exception as e:
        logger.error(f"Error al realizar la consulta general: {e}")
        return jsonify({"error": str(e)}), 500

@app.route("/actualizar_datos", methods=["GET"])
def actualizar_datos():
    """
    Ruta que fuerza la actualización de los datos desde la API de Vercel y los guarda en el archivo JSON.
    """
    try:
        datos = base_data.consulta_general(actualizar=True)  # Fuerza la actualización desde la API
        logger.info("Datos actualizados correctamente desde la API.")
        return jsonify({"message": "Datos actualizados con éxito."}), 200
    except Exception as e:
        logger.error(f"Error al actualizar los datos desde la API: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
