import requests
import json
from datetime import datetime
import logging

# Configuración del logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Si no existe un manejador de archivos ya configurado, lo añadimos
if not logger.handlers:
    file_handler = logging.FileHandler('logs/app.log')
    file_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

class BaseData:
    
    def __init__(self):
        # Diccionario que va a funcionar como base de datos
        self.diccionario = []
        self.base_url = "http://34.29.61.196:8000/api/colecciones/"  # URL de la API

    def _abrir_json(self) -> None:
        try:
            with open("database.json", "r") as archivo:
                self.diccionario = json.load(archivo)
            logger.info("Archivo JSON abierto correctamente.")
        except FileNotFoundError:
            logger.error("El archivo 'database.json' no se pudo abrir.")
        except Exception as e:
            logger.error(f"Error al abrir 'database.json': {str(e)}")

    def _escribir_json(self) -> None:
        """
        Escribe los datos en el archivo JSON en el formato especificado por el usuario.
        Maneja errores en caso de que la escritura falle.
        """
        # Reorganizar los datos en el formato que se muestra en la imagen
        datos_formateados = [
            ["sensor", "coleccion", "timestamp"]
        ]
        
        # Verificar que cada 'coleccion' es un diccionario
        for coleccion in self.diccionario:
            if isinstance(coleccion, dict) and 'data' in coleccion:
                """
                     "id": 7,
                    "nombre": "co2-collection",
                    "data": [
                        {
                            "id": 3907,
                            "coleccion": 7,
                            "sensorValue": 394.0,
                            "timestamp": 1725674794
                        }
                """
                for dato in coleccion['data']:
                     # Verificar si 'dato' es un diccionario y contiene los campos necesarios
                    if isinstance(dato, dict) and 'sensorValue' in dato and 'timestamp' in dato:
                        sensor = dato['sensorValue']
                        nombre_coleccion = coleccion['nombre']
                        timestamp = self._formateo_fechas(dato['timestamp'])
                        datos_formateados.append([sensor, nombre_coleccion, timestamp])
                    else:
                        logger.error(f"El dato '{dato}' no es válido o le faltan campos.")
            else:
                logger.error(f"La colección '{coleccion}' no es un diccionario.")
        
        try:
            with open("database.json", "w") as archivo:
                json.dump(datos_formateados, archivo, indent=4)
            logger.info("Datos escritos correctamente en 'database.json'.")
        except Exception as e:
            logger.error(f"Error al escribir en 'database.json': {str(e)}")

    def _formateo_fechas(self, timestamp) -> str:
        """
        Convierte un timestamp de milisegundos en una fecha formateada.

        :param timestamp: Timestamp en milisegundos.
        :return: Fecha en formato DD/MM/AAAA HH:MM:SS.
        """
        try:
            data_stamp = datetime.fromtimestamp(timestamp)
            fecha_formateada = data_stamp.strftime("%d/%m/%Y %H:%M:%S")
            return fecha_formateada
        except Exception as e:
            logger.error(f"Error al formatear la fecha: {str(e)}")
            raise
        
    def _ordenar_por_fecha(self, diccionario) -> None:
        """
        Ordena los datos de 'diccionario' por fecha en orden ascendente.

        :param diccionario: Diccionario con los datos de la API.
        """
        try:
            for coleccion in diccionario:
                if isinstance(coleccion, dict) and 'data' in coleccion:
                    coleccion['data'] = sorted(coleccion['data'], key=lambda x: x['timestamp'])
            logger.info("Datos ordenados por fecha correctamente.")
        except Exception as e:
            logger.error(f"Error al ordenar los datos por fecha: {str(e)}")
            raise

    def consulta_general(self, actualizar=False):
        if actualizar:
            try:
                logger.info(f"Haciendo solicitud a la API: {self.base_url}")
                response = requests.get(self.base_url)

                if response.status_code == 200:
                    if response.text:  # Verifica que no esté vacía
                        try:
                            self.diccionario = response.json()
                            self._ordenar_por_fecha(self.diccionario)  # Ordenar por fecha
                            self._escribir_json()  # Guardar datos en archivo
                            logger.info("Datos obtenidos y guardados desde la API correctamente.")
                            return self.diccionario
                        except json.JSONDecodeError as e:
                            logger.error(f"Error al decodificar JSON: {str(e)}")
                            raise
                    else:
                        logger.error("La respuesta de la API está vacía.")
                        raise Exception("La respuesta de la API está vacía")
                else:
                    logger.error(f"Error al obtener datos de la API: {response.status_code}")
                    raise Exception(f"Error al obtener datos de la API: {response.status_code}")
            except Exception as e:
                logger.error(f"Error en la solicitud a la API: {str(e)}")
                raise
        else:
            logger.info("Leyendo datos desde archivo local 'database.json'.")
            self._abrir_json()  # Leer datos desde archivo local
            return self.diccionario
