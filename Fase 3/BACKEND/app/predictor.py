import requests
import logging

# Configuración del logger
logger = logging.getLogger(__name__)

class Predictor:
    def __init__(self):
        self.ruta_api = "http://34.29.61.196:8000/api/"
    
    def ObtenerPredicciones(self, fecha_timestamp) -> list:
        """
        Obtiene predicciones de la API para cada una de las colecciones, basadas en la fecha proporcionada.

        :param fecha_timestamp: Timestamp en formato UNIX.
        :return: Lista de respuestas con predicciones.
        """
        array_respuestas = []

        try:
            # Obtener todas las colecciones
            array_colecciones = requests.get(self.ruta_api + "colecciones/")
            array_colecciones.raise_for_status()  # Verifica si hubo un error HTTP
            array_colecciones = array_colecciones.json()
            logger.info(f"Se obtuvieron {len(array_colecciones)} colecciones.")
        except requests.RequestException as e:
            logger.error(f"Error al obtener colecciones: {str(e)}")
            return {"error": f"Error al obtener colecciones: {str(e)}"}

        # Iterar sobre las colecciones para obtener predicciones
        for temp in array_colecciones:
            try:
                ruta = self.ruta_api + f"Prediccion?fecha_timestamp={fecha_timestamp}&id_coleccion={temp['id']}"
                respuesta = requests.get(ruta)
                respuesta.raise_for_status()
                respuesta_json = respuesta.json()
                
                temp_data = {
                    "sensor": temp["nombre"],
                    "valor": respuesta_json.get("resultado"),
                    "mensaje": respuesta_json.get("mensaje")
                }
                array_respuestas.append(temp_data)
                logger.info(f"Predicción obtenida para colección {temp['nombre']}.")
            except requests.RequestException as e:
                logger.error(f"Error al obtener predicción para colección {temp['nombre']}: {str(e)}")
                array_respuestas.append({
                    "sensor": temp["nombre"],
                    "error": f"Error al obtener predicción: {str(e)}"
                })
            except KeyError as e:
                logger.error(f"Error en los datos de la predicción: {str(e)}")
                array_respuestas.append({
                    "sensor": temp["nombre"],
                    "error": f"Error en los datos de la predicción: {str(e)}"
                })

        return array_respuestas
