# * libreria json para manejar archivos json 
import json
# * libreria requests para hacer peticiones http
import requests
# * libreria os para manejar variables de entorno
import os
# * libreria datetime para manejar fechas
from datetime import datetime
# * libreria typing para manejar tipos de datos
from typing import List, Dict

class BaseData:
    
    def __init__(self, api_url: str = "http://34.29.61.196:8000/api/colecciones/", json_file: str = "database.json"):
        """
        Inicializa la clase con la URL de la API y el archivo JSON que servirá como base de datos.
        
        :param api_url: URL de la API de Vercel que se utilizará como fuente de datos.
        :param json_file: Nombre del archivo JSON que se utilizará para almacenar los datos.
        """
        self.api_url = api_url
        self.json_file = json_file
        self.diccionario: List[Dict] = []

    def _obtener_datos_api(self) -> None:
        """
        Hace una solicitud GET a la API para obtener los datos y los guarda en el archivo JSON.
        Maneja errores en caso de que la solicitud falle.
        """
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()  # Verifica si hubo errores en la solicitud
            self.diccionario = response.json()  # Carga los datos de la API en formato JSON
            self._escribir_json()  # Guarda los datos en el archivo JSON
            print(f"Datos obtenidos desde la API y guardados en {self.json_file}.")
        except requests.exceptions.RequestException as e:
            print(f"Error al obtener los datos desde la API: {e}")

    def _abrir_json(self) -> None:
        """
        Abre el archivo JSON y carga los datos en el diccionario.
        Si el archivo no existe, realiza una solicitud a la API para obtener los datos.
        """
        if not os.path.exists(self.json_file):
            print(f"El archivo '{self.json_file}' no existe. Obteniendo datos desde la API...")
            self._obtener_datos_api()
        else:
            try:
                with open(self.json_file, "r") as archivo:
                    self.diccionario = json.load(archivo)
                    print(f"Datos cargados desde el archivo '{self.json_file}'.")
            except FileNotFoundError:
                print(f"El archivo '{self.json_file}' no se pudo abrir.")
            except json.JSONDecodeError:
                print("Error al decodificar el archivo JSON. Verifica su formato.")

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
            if isinstance(coleccion, dict) and "data" in coleccion:
                for item in coleccion.get("data", []):
                    datos_formateados.append([
                        item.get("sensorValue", None),  # ID del sensor o valor del sensor
                        coleccion.get("nombre", "N/A"),  # Nombre de la colección
                        self.formateo_fechas(item.get("timestamp", 0))  # Formateo de la fecha
                    ])

        # Escribir en formato JSON
        try:
            with open(self.json_file, "w") as archivo:
                json.dump(datos_formateados, archivo, indent=4)
            print(f"Datos guardados en el archivo '{self.json_file}' en el formato deseado.")
        except IOError as e:
            print(f"Error al escribir en el archivo '{self.json_file}': {e}")

    @staticmethod
    def formateo_fechas(timestamp: int) -> str:
        """
        Convierte un timestamp de milisegundos en una fecha formateada.

        :param timestamp: Timestamp en milisegundos.
        :return: Fecha en formato DD/MM/AAAA HH:MM:SS.
        """
        data_stamp = datetime.fromtimestamp(timestamp)
        return data_stamp.strftime("%d/%m/%Y %H:%M:%S")

    def ordenar_por_fecha(self) -> None:
        """
        Ordena los datos del diccionario por la columna de fecha 'timestamp' usando el valor original del timestamp.
        """
        if len(self.diccionario) > 0:
            for coleccion in self.diccionario:
                # Verificar que 'coleccion' es un diccionario y que tiene la clave 'data'
                if isinstance(coleccion, dict) and "data" in coleccion:
                    # Ordenar los datos por timestamp (milisegundos, no formateado)
                    coleccion['data'] = sorted(
                        coleccion['data'], 
                        key=lambda x: x.get("timestamp", 0)
                    )
        self._escribir_json()

    def consulta_general(self, actualizar: bool = False) -> List[Dict]:
        """
        Realiza una consulta general de los datos. Si actualizar es True, se hará una nueva solicitud a la API.
        
        :param actualizar: Booleano que indica si se deben actualizar los datos desde la API.
        :return: Lista de diccionarios con los datos consultados.
        """
        if actualizar or not os.path.exists(self.json_file):
            self._obtener_datos_api()
        else:
            self._abrir_json()
            
        # Ordena los datos por fechas (timestamp) antes de formatear
        self.ordenar_por_fecha()

        print("Consulta de datos completa.")
        return self.diccionario
