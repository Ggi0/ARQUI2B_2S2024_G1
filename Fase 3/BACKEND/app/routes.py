from flask import request,jsonify
from .data_base import BaseData
from .predictor import Predictor
import logging

# Crear instancia de BaseData
base_data = BaseData()

# Crear instancia de Predictor
predictor = Predictor()

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
            data = base_data.consulta_general(actualizar=False)  # Obtiene datos de la API o archivo local
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
        
    @app.route('/consulta_prediccion/<int:fecha_timestamp>', methods=['GET'])
    def obtener_predicciones(fecha_timestamp): 
        """
        Ruta que obtiene predicciones basado en el timestamp pasado como parámetro.
        """
        """
            Como buena practica se debe hacer: 
                request.args: Este es un objeto en Flask que contiene los 
                parámetros de consulta de la solicitud HTTP. Los parámetros 
                de consulta son aquellos que vienen en la URL después del 
                signo de interrogación (?). En una URL como:
                
                http://example.com/consulta_prediccion?timestamp=1728933351
        """
        # fecha_timestamp = request.args.get('fecha_timestamp')
       
        if not fecha_timestamp:
            return jsonify({"error": "Falta el parámetro 'fecha_timestamp'."}), 400

        
        try:
            predicciones = predictor.ObtenerPredicciones(fecha_timestamp)
            logger.info("Predicciones obtenidas con éxito.")
            return predicciones, 200
        except Exception as e:
            logger.error(f"Error al obtener predicciones: {str(e)}")
            return jsonify({"error": str(e)}), 500

    @app.route('/consulta_usuario/<string:user>/<int:password>', methods=['GET'])
    def consulta_usuario(user, password): 
        try:
            data_respuesta, mensaje = base_data.consulta_usuario(user, password)
            logger.info("Apretura incrementada con exito")
            return jsonify({"ok": data_respuesta, 'mensaje': mensaje}), 200
        except Exception as e:
            logger.error(f"Error al incrementar aperturas: {str(e)}")
            return jsonify({"error": str(e)}), 500
        
    @app.route('/consulta_cant_talanquera', methods=['GET'])
    def consulta_cant_talanquera(): 
        try:
            cantidad_ingreso = base_data.consulta_parqueo()
            logger.info("Consulta realizada con exito")
            return jsonify({"ok": True, 'cantidad': cantidad_ingreso}), 200
        except Exception as e:
            logger.error(f"Error al realizar consulta: {str(e)}")
            return jsonify({"ok": False, 'cantidad': 0}), 500