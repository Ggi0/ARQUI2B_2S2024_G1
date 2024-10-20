import firebase_admin
from firebase_admin import credentials, firestore
import requests
import json

'''class FirebaseToApiMigration:
    def __init__(self):
        # Inicializa Firebase con las credenciales
        self.credenciales = credentials.Certificate("clave.json")
        firebase_admin.initialize_app(self.credenciales)
        self.db = firestore.client()

        # URLs de la API
        self.api_base_url = "https://vercel-bd.vercel.app/api/"
        self.colecciones_url = f"{self.api_base_url}colecciones/"
        self.data_url = f"{self.api_base_url}data/"

    def obtener_datos_firebase(self):
        """Obtiene las colecciones y sus documentos desde Firebase."""
        colecciones = self.db.collections()
        datos = {}

        for coleccion in colecciones:
            # Ignora las colecciones no válidas
            if coleccion.id in ["arduino-collection", "counter-collection"]:
                continue
            
            # Obtiene todos los documentos en la colección
            documentos = coleccion.stream()
            datos[coleccion.id] = []

            for doc in documentos:
                datos[coleccion.id].append(doc.to_dict())
        
        return datos

    def obtener_colecciones_api(self):
        """Obtiene las colecciones existentes de la API para verificar duplicados."""
        response = requests.get(self.colecciones_url)
        if response.status_code == 200:
            colecciones = response.json()
            return colecciones  # Retorna la lista completa de colecciones
        else:
            print(f"Error al obtener las colecciones existentes: {response.text}")
            return []

    def crear_coleccion_api(self, nombre_coleccion):
        """Crea una colección en la API si no existe, y devuelve su ID."""
        colecciones_existentes = self.obtener_colecciones_api()

        # Busca si la colección ya existe
        for coleccion in colecciones_existentes:
            if coleccion['nombre'] == nombre_coleccion:
                print(f"La colección '{nombre_coleccion}' ya existe en la API.")
                return coleccion['id']  # Retorna el ID de la colección existente

        # Si la colección no existe, se crea una nueva
        payload = {'nombre': nombre_coleccion}
        response = requests.post(self.colecciones_url, json=payload)

        if response.status_code == 201:  # Created
            print(f"Colección '{nombre_coleccion}' creada exitosamente en la API.")
            return response.json()['id']  # Retorna el ID de la colección creada
        else:
            print(f"Error al crear la colección '{nombre_coleccion}': {response.text}")
            return None

    def crear_dato_api(self, dato, coleccion_id):
        """Crea un dato en la API."""
        # Convierte el timestamp de milisegundos a segundos
        timestamp_segundos = dato['timestamp'] // 1000

        # Prepara el payload para el dato
        payload = {
            'sensorValue': dato['sensorValue'],
            'timestamp': timestamp_segundos,  # Enviar el timestamp en segundos
            'coleccion': coleccion_id  # Usar el ID de la colección
        }

        response = requests.post(self.data_url, json=payload)

        if response.status_code == 201:  # Created
            print(f"Dato creado exitosamente: {dato}")
        else:
            print(f"Error al crear el dato: {response.text}")

    def migrar_datos(self):
        """Migra los datos de Firebase a la API proporcionada."""
        datos = self.obtener_datos_firebase()

        for coleccion_nombre, documentos in datos.items():
            # Obtén el ID de la colección (o crea una nueva si no existe)
            coleccion_id = self.crear_coleccion_api(coleccion_nombre)

            # Inserta los datos en la API usando el ID de la colección
            for documento in documentos:
                self.crear_dato_api(documento, coleccion_id)


# Ejecuta la migración
if __name__ == "__main__":
    migracion = FirebaseToApiMigration()
    migracion.migrar_datos()
'''

import requests
from datetime import datetime

# Array de ejemplo
array_json = [
    [
        "sensor",
        "coleccion",
        "timestamp"
    ],
    [
        1,
        "hum-collection",
        "04/09/2024 21:29:31"
    ],
    [
        2,
        "co2-collection",
        "04/09/2024 21:29:38"
    ],
    [
        7,
        "luz-collection",
        "04/09/2024 21:29:38"
    ],
    [
        3,
        "temp-collection",
        "04/09/2024 21:29:38"
    ],
    [
        11,
        "dist-collection",
        "04/09/2024 21:29:39"
    ],
    [
        4,
        "co2-collection",
        "04/09/2024 21:29:41"
    ],
    [
        2,
        "hum-collection",
        "04/09/2024 21:29:41"
    ],
    [
        6,
        "temp-collection",
        "04/09/2024 21:29:41"
    ],
    [
        22,
        "dist-collection",
        "04/09/2024 21:29:42"
    ],
    [
        14,
        "luz-collection",
        "04/09/2024 21:29:42"
    ],
    [
        6,
        "co2-collection",
        "04/09/2024 21:29:53"
    ],
    [
        3,
        "hum-collection",
        "04/09/2024 21:29:53"
    ],
    [
        33,
        "dist-collection",
        "04/09/2024 21:29:54"
    ],
    [
        21,
        "luz-collection",
        "04/09/2024 21:29:54"
    ],
    [
        9,
        "temp-collection",
        "04/09/2024 21:29:54"
    ],
    [
        8,
        "co2-collection",
        "04/09/2024 21:30:06"
    ],
    [
        44,
        "dist-collection",
        "04/09/2024 21:30:06"
    ],
    [
        4,
        "hum-collection",
        "04/09/2024 21:30:06"
    ],
    [
        28,
        "luz-collection",
        "04/09/2024 21:30:06"
    ],
    [
        12,
        "temp-collection",
        "04/09/2024 21:30:06"
    ],
    [
        5,
        "hum-collection",
        "04/09/2024 21:30:18"
    ],
    [
        10,
        "co2-collection",
        "04/09/2024 21:30:22"
    ],
    [
        55,
        "dist-collection",
        "04/09/2024 21:30:22"
    ],
    [
        35,
        "luz-collection",
        "04/09/2024 21:30:22"
    ],
    [
        15,
        "temp-collection",
        "04/09/2024 21:30:22"
    ],
    [
        12,
        "co2-collection",
        "04/09/2024 21:30:30"
    ],
    [
        6,
        "hum-collection",
        "04/09/2024 21:30:30"
    ],
    [
        66,
        "dist-collection",
        "04/09/2024 21:30:31"
    ],
    [
        42,
        "luz-collection",
        "04/09/2024 21:30:31"
    ],
    [
        18,
        "temp-collection",
        "04/09/2024 21:30:31"
    ],
    [
        14,
        "co2-collection",
        "04/09/2024 21:30:42"
    ],
    [
        7,
        "hum-collection",
        "04/09/2024 21:30:42"
    ],
    [
        77,
        "dist-collection",
        "04/09/2024 21:30:43"
    ],
    [
        49,
        "luz-collection",
        "04/09/2024 21:30:43"
    ],
    [
        21,
        "temp-collection",
        "04/09/2024 21:30:43"
    ],
    [
        8,
        "hum-collection",
        "04/09/2024 21:30:55"
    ],
    [
        16,
        "co2-collection",
        "04/09/2024 21:31:00"
    ],
    [
        88,
        "dist-collection",
        "04/09/2024 21:31:00"
    ],
    [
        56,
        "luz-collection",
        "04/09/2024 21:31:00"
    ],
    [
        24,
        "temp-collection",
        "04/09/2024 21:31:00"
    ],
    [
        18,
        "co2-collection",
        "04/09/2024 21:31:07"
    ],
    [
        99,
        "dist-collection",
        "04/09/2024 21:31:07"
    ],
    [
        9,
        "hum-collection",
        "04/09/2024 21:31:07"
    ],
    [
        63,
        "luz-collection",
        "04/09/2024 21:31:07"
    ],
    [
        27,
        "temp-collection",
        "04/09/2024 21:31:07"
    ],
    [
        20,
        "co2-collection",
        "04/09/2024 21:31:19"
    ],
    [
        10,
        "hum-collection",
        "04/09/2024 21:31:19"
    ],
    [
        30,
        "temp-collection",
        "04/09/2024 21:31:19"
    ],
    [
        10,
        "dist-collection",
        "04/09/2024 21:31:20"
    ],
    [
        70,
        "luz-collection",
        "04/09/2024 21:31:20"
    ],
    [
        22,
        "co2-collection",
        "04/09/2024 21:31:32"
    ],
    [
        21,
        "dist-collection",
        "04/09/2024 21:31:32"
    ],
    [
        11,
        "hum-collection",
        "04/09/2024 21:31:32"
    ],
    [
        77,
        "luz-collection",
        "04/09/2024 21:31:32"
    ],
    [
        33,
        "temp-collection",
        "04/09/2024 21:31:32"
    ],
    [
        83,
        "hum-collection",
        "04/09/2024 21:40:08"
    ],
    [
        23.8,
        "temp-collection",
        "04/09/2024 21:40:08"
    ],
    [
        390,
        "co2-collection",
        "04/09/2024 21:40:09"
    ],
    [
        9,
        "dist-collection",
        "04/09/2024 21:40:09"
    ],
    [
        848,
        "luz-collection",
        "04/09/2024 21:40:09"
    ],
    [
        390,
        "co2-collection",
        "04/09/2024 21:40:10"
    ],
    [
        9,
        "dist-collection",
        "04/09/2024 21:40:10"
    ],
    [
        82,
        "hum-collection",
        "04/09/2024 21:40:10"
    ],
    [
        83,
        "hum-collection",
        "04/09/2024 21:40:10"
    ],
    [
        665,
        "luz-collection",
        "04/09/2024 21:40:10"
    ],
    [
        23.8,
        "temp-collection",
        "04/09/2024 21:40:10"
    ],
    [
        390,
        "co2-collection",
        "04/09/2024 21:40:11"
    ],
    [
        390,
        "co2-collection",
        "04/09/2024 21:40:11"
    ],
    [
        9,
        "dist-collection",
        "04/09/2024 21:40:11"
    ],
    [
        82,
        "hum-collection",
        "04/09/2024 21:40:11"
    ],
    [
        565,
        "luz-collection",
        "04/09/2024 21:40:11"
    ],
    [
        650,
        "luz-collection",
        "04/09/2024 21:40:11"
    ],
    [
        23.8,
        "temp-collection",
        "04/09/2024 21:40:11"
    ],
    [
        23.8,
        "temp-collection",
        "04/09/2024 21:40:11"
    ],
    [
        390,
        "co2-collection",
        "04/09/2024 21:40:12"
    ],
    [
        9,
        "dist-collection",
        "04/09/2024 21:40:12"
    ],
    [
        9,
        "dist-collection",
        "04/09/2024 21:40:12"
    ],
    [
        82,
        "hum-collection",
        "04/09/2024 21:40:12"
    ],
    [
        82,
        "hum-collection",
        "04/09/2024 21:40:12"
    ],
    [
        578,
        "luz-collection",
        "04/09/2024 21:40:12"
    ],
    [
        23.8,
        "temp-collection",
        "04/09/2024 21:40:12"
    ],
    [
        23.8,
        "temp-collection",
        "04/09/2024 21:40:12"
    ],
    [
        390,
        "co2-collection",
        "04/09/2024 21:40:13"
    ],
    [
        390,
        "co2-collection",
        "04/09/2024 21:40:13"
    ],
    [
        9,
        "dist-collection",
        "04/09/2024 21:40:13"
    ],
    [
        83,
        "hum-collection",
        "04/09/2024 21:40:13"
    ],
    [
        585,
        "luz-collection",
        "04/09/2024 21:40:13"
    ],
    [
        621,
        "luz-collection",
        "04/09/2024 21:40:13"
    ],
    [
        23.8,
        "temp-collection",
        "04/09/2024 21:40:13"
    ],
    [
        390,
        "co2-collection",
        "04/09/2024 21:40:14"
    ],
    [
        9,
        "dist-collection",
        "04/09/2024 21:40:14"
    ],
    [
        9,
        "dist-collection",
        "04/09/2024 21:40:14"
    ],
    [
        83,
        "hum-collection",
        "04/09/2024 21:40:14"
    ],
    [
        83,
        "hum-collection",
        "04/09/2024 21:40:14"
    ],
    [
        649,
        "luz-collection",
        "04/09/2024 21:40:14"
    ],
    [
        23.8,
        "temp-collection",
        "04/09/2024 21:40:14"
    ],
    [
        23.8,
        "temp-collection",
        "04/09/2024 21:40:14"
    ],
    [
        390,
        "co2-collection",
        "04/09/2024 21:40:15"
    ],
    [
        390,
        "co2-collection",
        "04/09/2024 21:40:15"
    ],
    [
        9,
        "dist-collection",
        "04/09/2024 21:40:15"
    ],
    [
        83,
        "hum-collection",
        "04/09/2024 21:40:15"
    ],
    [
        617,
        "luz-collection",
        "04/09/2024 21:40:15"
    ],
    [
        573,
        "luz-collection",
        "04/09/2024 21:40:15"
    ],
    [
        23.8,
        "temp-collection",
        "04/09/2024 21:40:15"
    ],
    [
        390,
        "co2-collection",
        "04/09/2024 21:40:16"
    ],
    [
        9,
        "dist-collection",
        "04/09/2024 21:40:16"
    ],
    [
        9,
        "dist-collection",
        "04/09/2024 21:40:16"
    ],
    [
        83,
        "hum-collection",
        "04/09/2024 21:40:16"
    ],
    [
        83,
        "hum-collection",
        "04/09/2024 21:40:16"
    ],
    [
        656,
        "luz-collection",
        "04/09/2024 21:40:16"
    ],
    [
        23.8,
        "temp-collection",
        "04/09/2024 21:40:16"
    ],
    [
        23.8,
        "temp-collection",
        "04/09/2024 21:40:16"
    ],
    [
        390,
        "co2-collection",
        "04/09/2024 21:40:17"
    ],
    [
        390,
        "co2-collection",
        "04/09/2024 21:40:17"
    ],
    [
        9,
        "dist-collection",
        "04/09/2024 21:40:17"
    ],
    [
        83,
        "hum-collection",
        "04/09/2024 21:40:17"
    ],
    [
        622,
        "luz-collection",
        "04/09/2024 21:40:17"
    ],
    [
        577,
        "luz-collection",
        "04/09/2024 21:40:17"
    ],
    [
        23.8,
        "temp-collection",
        "04/09/2024 21:40:17"
    ],
    [
        391,
        "co2-collection",
        "04/09/2024 21:40:18"
    ],
    [
        9,
        "dist-collection",
        "04/09/2024 21:40:18"
    ],
    [
        9,
        "dist-collection",
        "04/09/2024 21:40:18"
    ],
    [
        83,
        "hum-collection",
        "04/09/2024 21:40:18"
    ],
    [
        83,
        "hum-collection",
        "04/09/2024 21:40:18"
    ],
    [
        650,
        "luz-collection",
        "04/09/2024 21:40:18"
    ],
    [
        23.8,
        "temp-collection",
        "04/09/2024 21:40:18"
    ],
    [
        23.8,
        "temp-collection",
        "04/09/2024 21:40:18"
    ],
    [
        391,
        "co2-collection",
        "04/09/2024 21:40:19"
    ],
    [
        391,
        "co2-collection",
        "04/09/2024 21:40:19"
    ],
    [
        9,
        "dist-collection",
        "04/09/2024 21:40:19"
    ],
    [
        8,
        "dist-collection",
        "04/09/2024 21:40:19"
    ],
    [
        83,
        "hum-collection",
        "04/09/2024 21:40:19"
    ],
    [
        603,
        "luz-collection",
        "04/09/2024 21:40:19"
    ],
    [
        615,
        "luz-collection",
        "04/09/2024 21:40:19"
    ],
    [
        23.8,
        "temp-collection",
        "04/09/2024 21:40:19"
    ],
    [
        391,
        "co2-collection",
        "04/09/2024 21:40:20"
    ],
    [
        9,
        "dist-collection",
        "04/09/2024 21:40:20"
    ],
    [
        83,
        "hum-collection",
        "04/09/2024 21:40:20"
    ],
    [
        83,
        "hum-collection",
        "04/09/2024 21:40:20"
    ],
    [
        572,
        "luz-collection",
        "04/09/2024 21:40:20"
    ],
    [
        23.8,
        "temp-collection",
        "04/09/2024 21:40:20"
    ],
    [
        23.8,
        "temp-collection",
        "04/09/2024 21:40:20"
    ],
    [
        392,
        "co2-collection",
        "04/09/2024 21:40:21"
    ],
    [
        394,
        "co2-collection",
        "04/09/2024 21:40:21"
    ],
    [
        9,
        "dist-collection",
        "04/09/2024 21:40:21"
    ],
    [
        9,
        "dist-collection",
        "04/09/2024 21:40:21"
    ],
    [
        83,
        "hum-collection",
        "04/09/2024 21:40:21"
    ],
    [
        572,
        "luz-collection",
        "04/09/2024 21:40:21"
    ],
    [
        625,
        "luz-collection",
        "04/09/2024 21:40:21"
    ],
    [
        23.8,
        "temp-collection",
        "04/09/2024 21:40:21"
    ],
    [
        393,
        "co2-collection",
        "04/09/2024 21:40:22"
    ],
    [
        9,
        "dist-collection",
        "04/09/2024 21:40:22"
    ],
    [
        83,
        "hum-collection",
        "04/09/2024 21:40:22"
    ],
    [
        83,
        "hum-collection",
        "04/09/2024 21:40:22"
    ],
    [
        620,
        "luz-collection",
        "04/09/2024 21:40:22"
    ],
    [
        23.8,
        "temp-collection",
        "04/09/2024 21:40:22"
    ],
    [
        23.8,
        "temp-collection",
        "04/09/2024 21:40:22"
    ],
    [
        394,
        "co2-collection",
        "04/09/2024 21:40:23"
    ],
    [
        395,
        "co2-collection",
        "04/09/2024 21:40:23"
    ],
    [
        9,
        "dist-collection",
        "04/09/2024 21:40:23"
    ],
    [
        83,
        "hum-collection",
        "04/09/2024 21:40:23"
    ],
    [
        651,
        "luz-collection",
        "04/09/2024 21:40:23"
    ],
    [
        626,
        "luz-collection",
        "04/09/2024 21:40:23"
    ],
    [
        23.8,
        "temp-collection",
        "04/09/2024 21:40:23"
    ],
    [
        392,
        "co2-collection",
        "04/09/2024 21:40:24"
    ],
    [
        9,
        "dist-collection",
        "04/09/2024 21:40:24"
    ],
    [
        9,
        "dist-collection",
        "04/09/2024 21:40:24"
    ],
    [
        83,
        "hum-collection",
        "04/09/2024 21:40:24"
    ],
    [
        83,
        "hum-collection",
        "04/09/2024 21:40:24"
    ],
    [
        642,
        "luz-collection",
        "04/09/2024 21:40:24"
    ],
    [
        23.8,
        "temp-collection",
        "04/09/2024 21:40:24"
    ],
    [
        23.8,
        "temp-collection",
        "04/09/2024 21:40:24"
    ],
    [
        393,
        "co2-collection",
        "04/09/2024 21:40:25"
    ],
    [
        388,
        "co2-collection",
        "04/09/2024 21:40:25"
    ],
    [
        9,
        "dist-collection",
        "04/09/2024 21:40:25"
    ],
    [
        9,
        "dist-collection",
        "04/09/2024 21:40:25"
    ],
    [
        83,
        "hum-collection",
        "04/09/2024 21:40:25"
    ],
    [
        569,
        "luz-collection",
        "04/09/2024 21:40:25"
    ],
    [
        574,
        "luz-collection",
        "04/09/2024 21:40:25"
    ],
    [
        23.8,
        "temp-collection",
        "04/09/2024 21:40:25"
    ],
    [
        392,
        "co2-collection",
        "04/09/2024 21:40:26"
    ],
    [
        9,
        "dist-collection",
        "04/09/2024 21:40:26"
    ],
    [
        83,
        "hum-collection",
        "04/09/2024 21:40:26"
    ],
    [
        83,
        "hum-collection",
        "04/09/2024 21:40:26"
    ],
    [
        616,
        "luz-collection",
        "04/09/2024 21:40:26"
    ],
    [
        23.8,
        "temp-collection",
        "04/09/2024 21:40:26"
    ],
    [
        23.8,
        "temp-collection",
        "04/09/2024 21:40:26"
    ],
    [
        392,
        "co2-collection",
        "04/09/2024 21:40:27"
    ],
    [
        393,
        "co2-collection",
        "04/09/2024 21:40:27"
    ],
    [
        9,
        "dist-collection",
        "04/09/2024 21:40:27"
    ],
    [
        9,
        "dist-collection",
        "04/09/2024 21:40:27"
    ],
    [
        83,
        "hum-collection",
        "04/09/2024 21:40:27"
    ],
    [
        584,
        "luz-collection",
        "04/09/2024 21:40:27"
    ],
    [
        650,
        "luz-collection",
        "04/09/2024 21:40:27"
    ],
    [
        23.8,
        "temp-collection",
        "04/09/2024 21:40:27"
    ],
    [
        393,
        "co2-collection",
        "04/09/2024 21:40:28"
    ],
    [
        9,
        "dist-collection",
        "04/09/2024 21:40:28"
    ],
    [
        83,
        "hum-collection",
        "04/09/2024 21:40:28"
    ],
    [
        83,
        "hum-collection",
        "04/09/2024 21:40:28"
    ],
    [
        618,
        "luz-collection",
        "04/09/2024 21:40:28"
    ],
    [
        23.8,
        "temp-collection",
        "04/09/2024 21:40:28"
    ],
    [
        23.8,
        "temp-collection",
        "04/09/2024 21:40:28"
    ],
    [
        392,
        "co2-collection",
        "04/09/2024 21:40:29"
    ],
    [
        393,
        "co2-collection",
        "04/09/2024 21:40:29"
    ],
    [
        9,
        "dist-collection",
        "04/09/2024 21:40:29"
    ],
    [
        9,
        "dist-collection",
        "04/09/2024 21:40:29"
    ],
    [
        83,
        "hum-collection",
        "04/09/2024 21:40:29"
    ],
    [
        572,
        "luz-collection",
        "04/09/2024 21:40:29"
    ],
    [
        654,
        "luz-collection",
        "04/09/2024 21:40:29"
    ],
    [
        23.8,
        "temp-collection",
        "04/09/2024 21:40:29"
    ],
    [
        391,
        "co2-collection",
        "04/09/2024 21:40:30"
    ],
    [
        9,
        "dist-collection",
        "04/09/2024 21:40:30"
    ],
    [
        83,
        "hum-collection",
        "04/09/2024 21:40:30"
    ],
    [
        83,
        "hum-collection",
        "04/09/2024 21:40:30"
    ],
    [
        581,
        "luz-collection",
        "04/09/2024 21:40:30"
    ],
    [
        23.8,
        "temp-collection",
        "04/09/2024 21:40:30"
    ],
    [
        23.8,
        "temp-collection",
        "04/09/2024 21:40:30"
    ],
    [
        390,
        "co2-collection",
        "04/09/2024 21:40:31"
    ],
    [
        391,
        "co2-collection",
        "04/09/2024 21:40:31"
    ],
    [
        9,
        "dist-collection",
        "04/09/2024 21:40:31"
    ],
    [
        9,
        "dist-collection",
        "04/09/2024 21:40:31"
    ],
    [
        83,
        "hum-collection",
        "04/09/2024 21:40:31"
    ],
    [
        628,
        "luz-collection",
        "04/09/2024 21:40:31"
    ],
    [
        649,
        "luz-collection",
        "04/09/2024 21:40:31"
    ],
    [
        23.8,
        "temp-collection",
        "04/09/2024 21:40:31"
    ],
    [
        390,
        "co2-collection",
        "04/09/2024 21:40:32"
    ],
    [
        9,
        "dist-collection",
        "04/09/2024 21:40:32"
    ],
    [
        83,
        "hum-collection",
        "04/09/2024 21:40:32"
    ],
    [
        83,
        "hum-collection",
        "04/09/2024 21:40:32"
    ],
    [
        611,
        "luz-collection",
        "04/09/2024 21:40:32"
    ],
    [
        23.8,
        "temp-collection",
        "04/09/2024 21:40:32"
    ],
    [
        23.8,
        "temp-collection",
        "04/09/2024 21:40:32"
    ],
    [
        390,
        "co2-collection",
        "04/09/2024 21:40:33"
    ],
    [
        389,
        "co2-collection",
        "04/09/2024 21:40:33"
    ],
    [
        9,
        "dist-collection",
        "04/09/2024 21:40:33"
    ],
    [
        9,
        "dist-collection",
        "04/09/2024 21:40:33"
    ],
    [
        83,
        "hum-collection",
        "04/09/2024 21:40:33"
    ],
    [
        605,
        "luz-collection",
        "04/09/2024 21:40:33"
    ],
    [
        564,
        "luz-collection",
        "04/09/2024 21:40:33"
    ],
    [
        23.8,
        "temp-collection",
        "04/09/2024 21:40:33"
    ],
    [
        389,
        "co2-collection",
        "04/09/2024 21:40:34"
    ],
    [
        9,
        "dist-collection",
        "04/09/2024 21:40:34"
    ],
    [
        83,
        "hum-collection",
        "04/09/2024 21:40:34"
    ],
    [
        83,
        "hum-collection",
        "04/09/2024 21:40:34"
    ],
    [
        584,
        "luz-collection",
        "04/09/2024 21:40:34"
    ],
    [
        23.8,
        "temp-collection",
        "04/09/2024 21:40:34"
    ],
    [
        386,
        "co2-collection",
        "04/09/2024 21:40:35"
    ],
    [
        387,
        "co2-collection",
        "04/09/2024 21:40:35"
    ],
    [
        9,
        "dist-collection",
        "04/09/2024 21:40:35"
    ],
    [
        9,
        "dist-collection",
        "04/09/2024 21:40:35"
    ],
    [
        83,
        "hum-collection",
        "04/09/2024 21:40:35"
    ],
    [
        640,
        "luz-collection",
        "04/09/2024 21:40:35"
    ],
    [
        611,
        "luz-collection",
        "04/09/2024 21:40:35"
    ],
    [
        23.8,
        "temp-collection",
        "04/09/2024 21:40:35"
    ],
    [
        23.8,
        "temp-collection",
        "04/09/2024 21:40:35"
    ],
    [
        386,
        "co2-collection",
        "04/09/2024 21:40:36"
    ],
    [
        9,
        "dist-collection",
        "04/09/2024 21:40:36"
    ],
    [
        83,
        "hum-collection",
        "04/09/2024 21:40:36"
    ],
    [
        83,
        "hum-collection",
        "04/09/2024 21:40:36"
    ],
    [
        605,
        "luz-collection",
        "04/09/2024 21:40:36"
    ],
    [
        645,
        "luz-collection",
        "04/09/2024 21:40:36"
    ],
    [
        23.8,
        "temp-collection",
        "04/09/2024 21:40:36"
    ],
    [
        23.8,
        "temp-collection",
        "04/09/2024 21:40:36"
    ],
    [
        386,
        "co2-collection",
        "04/09/2024 21:40:37"
    ],
    [
        386,
        "co2-collection",
        "04/09/2024 21:40:37"
    ],
    [
        9,
        "dist-collection",
        "04/09/2024 21:40:37"
    ],
    [
        9,
        "dist-collection",
        "04/09/2024 21:40:37"
    ],
    [
        83,
        "hum-collection",
        "04/09/2024 21:40:37"
    ],
    [
        658,
        "luz-collection",
        "04/09/2024 21:40:37"
    ],
    [
        23.8,
        "temp-collection",
        "04/09/2024 21:40:37"
    ],
    [
        386,
        "co2-collection",
        "04/09/2024 21:40:38"
    ],
    [
        9,
        "dist-collection",
        "04/09/2024 21:40:38"
    ],
    [
        83,
        "hum-collection",
        "04/09/2024 21:40:38"
    ],
    [
        83,
        "hum-collection",
        "04/09/2024 21:40:38"
    ],
    [
        564,
        "luz-collection",
        "04/09/2024 21:40:38"
    ],
    [
        593,
        "luz-collection",
        "04/09/2024 21:40:38"
    ],
    [
        23.8,
        "temp-collection",
        "04/09/2024 21:40:38"
    ],
    [
        23.8,
        "temp-collection",
        "04/09/2024 21:40:38"
    ],
    [
        386,
        "co2-collection",
        "04/09/2024 21:40:39"
    ],
    [
        386,
        "co2-collection",
        "04/09/2024 21:40:39"
    ],
    [
        9,
        "dist-collection",
        "04/09/2024 21:40:39"
    ],
    [
        9,
        "dist-collection",
        "04/09/2024 21:40:39"
    ],
    [
        83,
        "hum-collection",
        "04/09/2024 21:40:39"
    ],
    [
        639,
        "luz-collection",
        "04/09/2024 21:40:39"
    ],
    [
        23.8,
        "temp-collection",
        "04/09/2024 21:40:39"
    ],
    [
        386,
        "co2-collection",
        "04/09/2024 21:40:40"
    ],
    [
        9,
        "dist-collection",
        "04/09/2024 21:40:40"
    ],
    [
        83,
        "hum-collection",
        "04/09/2024 21:40:40"
    ],
    [
        83,
        "hum-collection",
        "04/09/2024 21:40:40"
    ],
    [
        641,
        "luz-collection",
        "04/09/2024 21:40:40"
    ],
    [
        587,
        "luz-collection",
        "04/09/2024 21:40:40"
    ],
    [
        23.8,
        "temp-collection",
        "04/09/2024 21:40:40"
    ],
    [
        23.8,
        "temp-collection",
        "04/09/2024 21:40:40"
    ],
    [
        386,
        "co2-collection",
        "04/09/2024 21:40:41"
    ],
    [
        386,
        "co2-collection",
        "04/09/2024 21:40:41"
    ],
    [
        9,
        "dist-collection",
        "04/09/2024 21:40:41"
    ],
    [
        9,
        "dist-collection",
        "04/09/2024 21:40:41"
    ],
    [
        83,
        "hum-collection",
        "04/09/2024 21:40:41"
    ],
    [
        598,
        "luz-collection",
        "04/09/2024 21:40:41"
    ],
    [
        23.8,
        "temp-collection",
        "04/09/2024 21:40:41"
    ],
    [
        386,
        "co2-collection",
        "04/09/2024 21:40:42"
    ],
    [
        9,
        "dist-collection",
        "04/09/2024 21:40:42"
    ],
    [
        83,
        "hum-collection",
        "04/09/2024 21:40:42"
    ],
    [
        83,
        "hum-collection",
        "04/09/2024 21:40:42"
    ],
    [
        647,
        "luz-collection",
        "04/09/2024 21:40:42"
    ],
    [
        564,
        "luz-collection",
        "04/09/2024 21:40:42"
    ],
    [
        23.8,
        "temp-collection",
        "04/09/2024 21:40:42"
    ],
    [
        23.8,
        "temp-collection",
        "04/09/2024 21:40:42"
    ],
    [
        387,
        "co2-collection",
        "04/09/2024 21:40:43"
    ],
    [
        386,
        "co2-collection",
        "04/09/2024 21:40:43"
    ],
    [
        9,
        "dist-collection",
        "04/09/2024 21:40:43"
    ],
    [
        9,
        "dist-collection",
        "04/09/2024 21:40:43"
    ],
    [
        83,
        "hum-collection",
        "04/09/2024 21:40:43"
    ],
    [
        593,
        "luz-collection",
        "04/09/2024 21:40:43"
    ],
    [
        23.8,
        "temp-collection",
        "04/09/2024 21:40:43"
    ],
    [
        386,
        "co2-collection",
        "04/09/2024 21:40:44"
    ],
    [
        9,
        "dist-collection",
        "04/09/2024 21:40:44"
    ],
    [
        83,
        "hum-collection",
        "04/09/2024 21:40:44"
    ],
    [
        83,
        "hum-collection",
        "04/09/2024 21:40:44"
    ],
    [
        636,
        "luz-collection",
        "04/09/2024 21:40:44"
    ],
    [
        648,
        "luz-collection",
        "04/09/2024 21:40:44"
    ],
    [
        23.8,
        "temp-collection",
        "04/09/2024 21:40:44"
    ],
    [
        23.8,
        "temp-collection",
        "04/09/2024 21:40:44"
    ],
    [
        386,
        "co2-collection",
        "04/09/2024 21:40:45"
    ],
    [
        386,
        "co2-collection",
        "04/09/2024 21:40:45"
    ],
    [
        9,
        "dist-collection",
        "04/09/2024 21:40:45"
    ],
    [
        9,
        "dist-collection",
        "04/09/2024 21:40:45"
    ],
    [
        83,
        "hum-collection",
        "04/09/2024 21:40:45"
    ],
    [
        607,
        "luz-collection",
        "04/09/2024 21:40:45"
    ],
    [
        23.8,
        "temp-collection",
        "04/09/2024 21:40:45"
    ],
    [
        386,
        "co2-collection",
        "04/09/2024 21:40:46"
    ],
    [
        9,
        "dist-collection",
        "04/09/2024 21:40:46"
    ],
    [
        83,
        "hum-collection",
        "04/09/2024 21:40:46"
    ],
    [
        83,
        "hum-collection",
        "04/09/2024 21:40:46"
    ],
    [
        615,
        "luz-collection",
        "04/09/2024 21:40:46"
    ],
    [
        573,
        "luz-collection",
        "04/09/2024 21:40:46"
    ],
    [
        23.8,
        "temp-collection",
        "04/09/2024 21:40:46"
    ],
    [
        23.8,
        "temp-collection",
        "04/09/2024 21:40:46"
    ],
    [
        386,
        "co2-collection",
        "04/09/2024 21:40:47"
    ],
    [
        9,
        "dist-collection",
        "04/09/2024 21:40:47"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:26:55"
    ],
    [
        392,
        "co2-collection",
        "05/09/2024 17:26:56"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:26:56"
    ],
    [
        841,
        "luz-collection",
        "05/09/2024 17:26:56"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:26:56"
    ],
    [
        405,
        "co2-collection",
        "05/09/2024 17:26:57"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:26:57"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:26:57"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:26:57"
    ],
    [
        660,
        "luz-collection",
        "05/09/2024 17:26:57"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:26:57"
    ],
    [
        400,
        "co2-collection",
        "05/09/2024 17:26:58"
    ],
    [
        401,
        "co2-collection",
        "05/09/2024 17:26:58"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:26:58"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:26:58"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:26:58"
    ],
    [
        652,
        "luz-collection",
        "05/09/2024 17:26:58"
    ],
    [
        612,
        "luz-collection",
        "05/09/2024 17:26:58"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:26:58"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:26:58"
    ],
    [
        403,
        "co2-collection",
        "05/09/2024 17:26:59"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:26:59"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:26:59"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:26:59"
    ],
    [
        632,
        "luz-collection",
        "05/09/2024 17:26:59"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:26:59"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:26:59"
    ],
    [
        403,
        "co2-collection",
        "05/09/2024 17:27:00"
    ],
    [
        406,
        "co2-collection",
        "05/09/2024 17:27:00"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:27:00"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:27:00"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:00"
    ],
    [
        619,
        "luz-collection",
        "05/09/2024 17:27:00"
    ],
    [
        650,
        "luz-collection",
        "05/09/2024 17:27:00"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:00"
    ],
    [
        403,
        "co2-collection",
        "05/09/2024 17:27:01"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:27:01"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:01"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:01"
    ],
    [
        670,
        "luz-collection",
        "05/09/2024 17:27:01"
    ],
    [
        655,
        "luz-collection",
        "05/09/2024 17:27:01"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:01"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:01"
    ],
    [
        403,
        "co2-collection",
        "05/09/2024 17:27:02"
    ],
    [
        403,
        "co2-collection",
        "05/09/2024 17:27:02"
    ],
    [
        15,
        "dist-collection",
        "05/09/2024 17:27:02"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:27:02"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:02"
    ],
    [
        668,
        "luz-collection",
        "05/09/2024 17:27:02"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:02"
    ],
    [
        409,
        "co2-collection",
        "05/09/2024 17:27:03"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:27:03"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:03"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:03"
    ],
    [
        618,
        "luz-collection",
        "05/09/2024 17:27:03"
    ],
    [
        665,
        "luz-collection",
        "05/09/2024 17:27:03"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:03"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:03"
    ],
    [
        407,
        "co2-collection",
        "05/09/2024 17:27:04"
    ],
    [
        402,
        "co2-collection",
        "05/09/2024 17:27:04"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:27:04"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:27:04"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:04"
    ],
    [
        649,
        "luz-collection",
        "05/09/2024 17:27:04"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:04"
    ],
    [
        405,
        "co2-collection",
        "05/09/2024 17:27:05"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:27:05"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:05"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:05"
    ],
    [
        626,
        "luz-collection",
        "05/09/2024 17:27:05"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:05"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:05"
    ],
    [
        412,
        "co2-collection",
        "05/09/2024 17:27:06"
    ],
    [
        406,
        "co2-collection",
        "05/09/2024 17:27:06"
    ],
    [
        9,
        "dist-collection",
        "05/09/2024 17:27:06"
    ],
    [
        15,
        "dist-collection",
        "05/09/2024 17:27:06"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:06"
    ],
    [
        616,
        "luz-collection",
        "05/09/2024 17:27:06"
    ],
    [
        662,
        "luz-collection",
        "05/09/2024 17:27:06"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:06"
    ],
    [
        406,
        "co2-collection",
        "05/09/2024 17:27:07"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:27:07"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:07"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:07"
    ],
    [
        587,
        "luz-collection",
        "05/09/2024 17:27:07"
    ],
    [
        593,
        "luz-collection",
        "05/09/2024 17:27:07"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:07"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:07"
    ],
    [
        402,
        "co2-collection",
        "05/09/2024 17:27:08"
    ],
    [
        404,
        "co2-collection",
        "05/09/2024 17:27:08"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:27:08"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:08"
    ],
    [
        670,
        "luz-collection",
        "05/09/2024 17:27:08"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:08"
    ],
    [
        402,
        "co2-collection",
        "05/09/2024 17:27:09"
    ],
    [
        15,
        "dist-collection",
        "05/09/2024 17:27:09"
    ],
    [
        15,
        "dist-collection",
        "05/09/2024 17:27:09"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:09"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:09"
    ],
    [
        608,
        "luz-collection",
        "05/09/2024 17:27:09"
    ],
    [
        595,
        "luz-collection",
        "05/09/2024 17:27:09"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:09"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:09"
    ],
    [
        400,
        "co2-collection",
        "05/09/2024 17:27:10"
    ],
    [
        401,
        "co2-collection",
        "05/09/2024 17:27:10"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:27:10"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:27:10"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:10"
    ],
    [
        625,
        "luz-collection",
        "05/09/2024 17:27:10"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:10"
    ],
    [
        398,
        "co2-collection",
        "05/09/2024 17:27:11"
    ],
    [
        9,
        "dist-collection",
        "05/09/2024 17:27:11"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:11"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:11"
    ],
    [
        642,
        "luz-collection",
        "05/09/2024 17:27:11"
    ],
    [
        638,
        "luz-collection",
        "05/09/2024 17:27:11"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:11"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:11"
    ],
    [
        399,
        "co2-collection",
        "05/09/2024 17:27:12"
    ],
    [
        398,
        "co2-collection",
        "05/09/2024 17:27:12"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:27:12"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:27:12"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:12"
    ],
    [
        655,
        "luz-collection",
        "05/09/2024 17:27:12"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:12"
    ],
    [
        397,
        "co2-collection",
        "05/09/2024 17:27:13"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:27:13"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:13"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:13"
    ],
    [
        611,
        "luz-collection",
        "05/09/2024 17:27:13"
    ],
    [
        669,
        "luz-collection",
        "05/09/2024 17:27:13"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:13"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:13"
    ],
    [
        396,
        "co2-collection",
        "05/09/2024 17:27:14"
    ],
    [
        397,
        "co2-collection",
        "05/09/2024 17:27:14"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:27:14"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:27:14"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:14"
    ],
    [
        669,
        "luz-collection",
        "05/09/2024 17:27:14"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:14"
    ],
    [
        397,
        "co2-collection",
        "05/09/2024 17:27:15"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:27:15"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:15"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:15"
    ],
    [
        662,
        "luz-collection",
        "05/09/2024 17:27:15"
    ],
    [
        668,
        "luz-collection",
        "05/09/2024 17:27:15"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:15"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:15"
    ],
    [
        397,
        "co2-collection",
        "05/09/2024 17:27:16"
    ],
    [
        397,
        "co2-collection",
        "05/09/2024 17:27:16"
    ],
    [
        9,
        "dist-collection",
        "05/09/2024 17:27:16"
    ],
    [
        9,
        "dist-collection",
        "05/09/2024 17:27:16"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:16"
    ],
    [
        634,
        "luz-collection",
        "05/09/2024 17:27:16"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:16"
    ],
    [
        400,
        "co2-collection",
        "05/09/2024 17:27:17"
    ],
    [
        9,
        "dist-collection",
        "05/09/2024 17:27:17"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:17"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:17"
    ],
    [
        609,
        "luz-collection",
        "05/09/2024 17:27:17"
    ],
    [
        638,
        "luz-collection",
        "05/09/2024 17:27:17"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:17"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:17"
    ],
    [
        400,
        "co2-collection",
        "05/09/2024 17:27:18"
    ],
    [
        401,
        "co2-collection",
        "05/09/2024 17:27:18"
    ],
    [
        9,
        "dist-collection",
        "05/09/2024 17:27:18"
    ],
    [
        9,
        "dist-collection",
        "05/09/2024 17:27:18"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:18"
    ],
    [
        586,
        "luz-collection",
        "05/09/2024 17:27:18"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:18"
    ],
    [
        405,
        "co2-collection",
        "05/09/2024 17:27:19"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:27:19"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:19"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:19"
    ],
    [
        675,
        "luz-collection",
        "05/09/2024 17:27:19"
    ],
    [
        591,
        "luz-collection",
        "05/09/2024 17:27:19"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:19"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:19"
    ],
    [
        404,
        "co2-collection",
        "05/09/2024 17:27:20"
    ],
    [
        399,
        "co2-collection",
        "05/09/2024 17:27:20"
    ],
    [
        15,
        "dist-collection",
        "05/09/2024 17:27:20"
    ],
    [
        15,
        "dist-collection",
        "05/09/2024 17:27:20"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:20"
    ],
    [
        599,
        "luz-collection",
        "05/09/2024 17:27:20"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:20"
    ],
    [
        398,
        "co2-collection",
        "05/09/2024 17:27:21"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:27:21"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:21"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:21"
    ],
    [
        648,
        "luz-collection",
        "05/09/2024 17:27:21"
    ],
    [
        614,
        "luz-collection",
        "05/09/2024 17:27:21"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:21"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:21"
    ],
    [
        399,
        "co2-collection",
        "05/09/2024 17:27:22"
    ],
    [
        400,
        "co2-collection",
        "05/09/2024 17:27:22"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:27:22"
    ],
    [
        9,
        "dist-collection",
        "05/09/2024 17:27:22"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:22"
    ],
    [
        618,
        "luz-collection",
        "05/09/2024 17:27:22"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:22"
    ],
    [
        400,
        "co2-collection",
        "05/09/2024 17:27:23"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:27:23"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:23"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:23"
    ],
    [
        651,
        "luz-collection",
        "05/09/2024 17:27:23"
    ],
    [
        667,
        "luz-collection",
        "05/09/2024 17:27:23"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:23"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:23"
    ],
    [
        400,
        "co2-collection",
        "05/09/2024 17:27:24"
    ],
    [
        400,
        "co2-collection",
        "05/09/2024 17:27:24"
    ],
    [
        9,
        "dist-collection",
        "05/09/2024 17:27:24"
    ],
    [
        9,
        "dist-collection",
        "05/09/2024 17:27:24"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:24"
    ],
    [
        615,
        "luz-collection",
        "05/09/2024 17:27:24"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:24"
    ],
    [
        400,
        "co2-collection",
        "05/09/2024 17:27:25"
    ],
    [
        9,
        "dist-collection",
        "05/09/2024 17:27:25"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:25"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:25"
    ],
    [
        660,
        "luz-collection",
        "05/09/2024 17:27:25"
    ],
    [
        624,
        "luz-collection",
        "05/09/2024 17:27:25"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:25"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:25"
    ],
    [
        400,
        "co2-collection",
        "05/09/2024 17:27:26"
    ],
    [
        400,
        "co2-collection",
        "05/09/2024 17:27:26"
    ],
    [
        9,
        "dist-collection",
        "05/09/2024 17:27:26"
    ],
    [
        9,
        "dist-collection",
        "05/09/2024 17:27:26"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:26"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:26"
    ],
    [
        590,
        "luz-collection",
        "05/09/2024 17:27:26"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:26"
    ],
    [
        400,
        "co2-collection",
        "05/09/2024 17:27:27"
    ],
    [
        401,
        "co2-collection",
        "05/09/2024 17:27:27"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:27:27"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:27"
    ],
    [
        593,
        "luz-collection",
        "05/09/2024 17:27:27"
    ],
    [
        674,
        "luz-collection",
        "05/09/2024 17:27:27"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:27"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:27"
    ],
    [
        402,
        "co2-collection",
        "05/09/2024 17:27:28"
    ],
    [
        9,
        "dist-collection",
        "05/09/2024 17:27:28"
    ],
    [
        9,
        "dist-collection",
        "05/09/2024 17:27:28"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:28"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:28"
    ],
    [
        628,
        "luz-collection",
        "05/09/2024 17:27:28"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:28"
    ],
    [
        403,
        "co2-collection",
        "05/09/2024 17:27:29"
    ],
    [
        402,
        "co2-collection",
        "05/09/2024 17:27:29"
    ],
    [
        9,
        "dist-collection",
        "05/09/2024 17:27:29"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:29"
    ],
    [
        614,
        "luz-collection",
        "05/09/2024 17:27:29"
    ],
    [
        666,
        "luz-collection",
        "05/09/2024 17:27:29"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:29"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:29"
    ],
    [
        400,
        "co2-collection",
        "05/09/2024 17:27:30"
    ],
    [
        9,
        "dist-collection",
        "05/09/2024 17:27:30"
    ],
    [
        9,
        "dist-collection",
        "05/09/2024 17:27:30"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:30"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:30"
    ],
    [
        655,
        "luz-collection",
        "05/09/2024 17:27:30"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:30"
    ],
    [
        400,
        "co2-collection",
        "05/09/2024 17:27:31"
    ],
    [
        400,
        "co2-collection",
        "05/09/2024 17:27:31"
    ],
    [
        9,
        "dist-collection",
        "05/09/2024 17:27:31"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:31"
    ],
    [
        585,
        "luz-collection",
        "05/09/2024 17:27:31"
    ],
    [
        617,
        "luz-collection",
        "05/09/2024 17:27:31"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:31"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:31"
    ],
    [
        400,
        "co2-collection",
        "05/09/2024 17:27:32"
    ],
    [
        9,
        "dist-collection",
        "05/09/2024 17:27:32"
    ],
    [
        9,
        "dist-collection",
        "05/09/2024 17:27:32"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:32"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:32"
    ],
    [
        671,
        "luz-collection",
        "05/09/2024 17:27:32"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:32"
    ],
    [
        401,
        "co2-collection",
        "05/09/2024 17:27:33"
    ],
    [
        401,
        "co2-collection",
        "05/09/2024 17:27:33"
    ],
    [
        15,
        "dist-collection",
        "05/09/2024 17:27:33"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:33"
    ],
    [
        628,
        "luz-collection",
        "05/09/2024 17:27:33"
    ],
    [
        605,
        "luz-collection",
        "05/09/2024 17:27:33"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:33"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:33"
    ],
    [
        402,
        "co2-collection",
        "05/09/2024 17:27:34"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:27:34"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:27:34"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:34"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:34"
    ],
    [
        651,
        "luz-collection",
        "05/09/2024 17:27:34"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:34"
    ],
    [
        402,
        "co2-collection",
        "05/09/2024 17:27:35"
    ],
    [
        402,
        "co2-collection",
        "05/09/2024 17:27:35"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:27:35"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:35"
    ],
    [
        662,
        "luz-collection",
        "05/09/2024 17:27:35"
    ],
    [
        612,
        "luz-collection",
        "05/09/2024 17:27:35"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:35"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:35"
    ],
    [
        403,
        "co2-collection",
        "05/09/2024 17:27:36"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:27:36"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:27:36"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:36"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:36"
    ],
    [
        667,
        "luz-collection",
        "05/09/2024 17:27:36"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:36"
    ],
    [
        403,
        "co2-collection",
        "05/09/2024 17:27:37"
    ],
    [
        403,
        "co2-collection",
        "05/09/2024 17:27:37"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:27:37"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:37"
    ],
    [
        633,
        "luz-collection",
        "05/09/2024 17:27:37"
    ],
    [
        656,
        "luz-collection",
        "05/09/2024 17:27:37"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:37"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:37"
    ],
    [
        403,
        "co2-collection",
        "05/09/2024 17:27:38"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:27:38"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:27:38"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:38"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:38"
    ],
    [
        643,
        "luz-collection",
        "05/09/2024 17:27:38"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:38"
    ],
    [
        404,
        "co2-collection",
        "05/09/2024 17:27:39"
    ],
    [
        403,
        "co2-collection",
        "05/09/2024 17:27:39"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:27:39"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:39"
    ],
    [
        618,
        "luz-collection",
        "05/09/2024 17:27:39"
    ],
    [
        594,
        "luz-collection",
        "05/09/2024 17:27:39"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:39"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:39"
    ],
    [
        402,
        "co2-collection",
        "05/09/2024 17:27:40"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:27:40"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:27:40"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:40"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:40"
    ],
    [
        677,
        "luz-collection",
        "05/09/2024 17:27:40"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:40"
    ],
    [
        402,
        "co2-collection",
        "05/09/2024 17:27:41"
    ],
    [
        403,
        "co2-collection",
        "05/09/2024 17:27:41"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:27:41"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:41"
    ],
    [
        592,
        "luz-collection",
        "05/09/2024 17:27:41"
    ],
    [
        584,
        "luz-collection",
        "05/09/2024 17:27:41"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:41"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:41"
    ],
    [
        401,
        "co2-collection",
        "05/09/2024 17:27:42"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:27:42"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:27:42"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:42"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:42"
    ],
    [
        611,
        "luz-collection",
        "05/09/2024 17:27:42"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:42"
    ],
    [
        402,
        "co2-collection",
        "05/09/2024 17:27:43"
    ],
    [
        401,
        "co2-collection",
        "05/09/2024 17:27:43"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:27:43"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:43"
    ],
    [
        624,
        "luz-collection",
        "05/09/2024 17:27:43"
    ],
    [
        643,
        "luz-collection",
        "05/09/2024 17:27:43"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:43"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:43"
    ],
    [
        402,
        "co2-collection",
        "05/09/2024 17:27:44"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:27:44"
    ],
    [
        15,
        "dist-collection",
        "05/09/2024 17:27:44"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:44"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:44"
    ],
    [
        646,
        "luz-collection",
        "05/09/2024 17:27:44"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:44"
    ],
    [
        402,
        "co2-collection",
        "05/09/2024 17:27:45"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:27:45"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:45"
    ],
    [
        610,
        "luz-collection",
        "05/09/2024 17:27:45"
    ],
    [
        665,
        "luz-collection",
        "05/09/2024 17:27:45"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:45"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:45"
    ],
    [
        402,
        "co2-collection",
        "05/09/2024 17:27:46"
    ],
    [
        403,
        "co2-collection",
        "05/09/2024 17:27:46"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:27:46"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:27:46"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:46"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:46"
    ],
    [
        669,
        "luz-collection",
        "05/09/2024 17:27:46"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:46"
    ],
    [
        402,
        "co2-collection",
        "05/09/2024 17:27:47"
    ],
    [
        403,
        "co2-collection",
        "05/09/2024 17:27:47"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:27:47"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:47"
    ],
    [
        663,
        "luz-collection",
        "05/09/2024 17:27:47"
    ],
    [
        654,
        "luz-collection",
        "05/09/2024 17:27:47"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:47"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:47"
    ],
    [
        403,
        "co2-collection",
        "05/09/2024 17:27:48"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:27:48"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:27:48"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:48"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:48"
    ],
    [
        629,
        "luz-collection",
        "05/09/2024 17:27:48"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:48"
    ],
    [
        403,
        "co2-collection",
        "05/09/2024 17:27:49"
    ],
    [
        403,
        "co2-collection",
        "05/09/2024 17:27:49"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:27:49"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:49"
    ],
    [
        637,
        "luz-collection",
        "05/09/2024 17:27:49"
    ],
    [
        652,
        "luz-collection",
        "05/09/2024 17:27:49"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:49"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:49"
    ],
    [
        403,
        "co2-collection",
        "05/09/2024 17:27:50"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:27:50"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:27:50"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:50"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:50"
    ],
    [
        620,
        "luz-collection",
        "05/09/2024 17:27:50"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:50"
    ],
    [
        402,
        "co2-collection",
        "05/09/2024 17:27:51"
    ],
    [
        401,
        "co2-collection",
        "05/09/2024 17:27:51"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:27:51"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:51"
    ],
    [
        655,
        "luz-collection",
        "05/09/2024 17:27:51"
    ],
    [
        621,
        "luz-collection",
        "05/09/2024 17:27:51"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:51"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:51"
    ],
    [
        400,
        "co2-collection",
        "05/09/2024 17:27:52"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:27:52"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:27:52"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:52"
    ],
    [
        78,
        "hum-collection",
        "05/09/2024 17:27:52"
    ],
    [
        605,
        "luz-collection",
        "05/09/2024 17:27:52"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:52"
    ],
    [
        402,
        "co2-collection",
        "05/09/2024 17:27:53"
    ],
    [
        402,
        "co2-collection",
        "05/09/2024 17:27:53"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:27:53"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:27:53"
    ],
    [
        590,
        "luz-collection",
        "05/09/2024 17:27:53"
    ],
    [
        678,
        "luz-collection",
        "05/09/2024 17:27:53"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:53"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:53"
    ],
    [
        402,
        "co2-collection",
        "05/09/2024 17:27:54"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:27:54"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:27:54"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:27:54"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:27:54"
    ],
    [
        590,
        "luz-collection",
        "05/09/2024 17:27:54"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:54"
    ],
    [
        402,
        "co2-collection",
        "05/09/2024 17:27:55"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:27:55"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:27:55"
    ],
    [
        584,
        "luz-collection",
        "05/09/2024 17:27:55"
    ],
    [
        589,
        "luz-collection",
        "05/09/2024 17:27:55"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:55"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:55"
    ],
    [
        403,
        "co2-collection",
        "05/09/2024 17:27:56"
    ],
    [
        401,
        "co2-collection",
        "05/09/2024 17:27:56"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:27:56"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:27:56"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:27:56"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:27:56"
    ],
    [
        671,
        "luz-collection",
        "05/09/2024 17:27:56"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:56"
    ],
    [
        404,
        "co2-collection",
        "05/09/2024 17:27:57"
    ],
    [
        403,
        "co2-collection",
        "05/09/2024 17:27:57"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:27:57"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:27:57"
    ],
    [
        589,
        "luz-collection",
        "05/09/2024 17:27:57"
    ],
    [
        597,
        "luz-collection",
        "05/09/2024 17:27:57"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:57"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:57"
    ],
    [
        403,
        "co2-collection",
        "05/09/2024 17:27:58"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:27:58"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:27:58"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:27:58"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:27:58"
    ],
    [
        612,
        "luz-collection",
        "05/09/2024 17:27:58"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:58"
    ],
    [
        404,
        "co2-collection",
        "05/09/2024 17:27:59"
    ],
    [
        404,
        "co2-collection",
        "05/09/2024 17:27:59"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:27:59"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:27:59"
    ],
    [
        645,
        "luz-collection",
        "05/09/2024 17:27:59"
    ],
    [
        615,
        "luz-collection",
        "05/09/2024 17:27:59"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:59"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:27:59"
    ],
    [
        404,
        "co2-collection",
        "05/09/2024 17:28:00"
    ],
    [
        9,
        "dist-collection",
        "05/09/2024 17:28:00"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:00"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:00"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:00"
    ],
    [
        647,
        "luz-collection",
        "05/09/2024 17:28:00"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:00"
    ],
    [
        403,
        "co2-collection",
        "05/09/2024 17:28:01"
    ],
    [
        403,
        "co2-collection",
        "05/09/2024 17:28:01"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:01"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:01"
    ],
    [
        663,
        "luz-collection",
        "05/09/2024 17:28:01"
    ],
    [
        607,
        "luz-collection",
        "05/09/2024 17:28:01"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:01"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:01"
    ],
    [
        404,
        "co2-collection",
        "05/09/2024 17:28:02"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:02"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:02"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:02"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:02"
    ],
    [
        665,
        "luz-collection",
        "05/09/2024 17:28:02"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:02"
    ],
    [
        403,
        "co2-collection",
        "05/09/2024 17:28:03"
    ],
    [
        403,
        "co2-collection",
        "05/09/2024 17:28:03"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:03"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:03"
    ],
    [
        663,
        "luz-collection",
        "05/09/2024 17:28:03"
    ],
    [
        654,
        "luz-collection",
        "05/09/2024 17:28:03"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:03"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:03"
    ],
    [
        404,
        "co2-collection",
        "05/09/2024 17:28:04"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:04"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:04"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:04"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:04"
    ],
    [
        622,
        "luz-collection",
        "05/09/2024 17:28:04"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:04"
    ],
    [
        402,
        "co2-collection",
        "05/09/2024 17:28:05"
    ],
    [
        402,
        "co2-collection",
        "05/09/2024 17:28:05"
    ],
    [
        9,
        "dist-collection",
        "05/09/2024 17:28:05"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:05"
    ],
    [
        653,
        "luz-collection",
        "05/09/2024 17:28:05"
    ],
    [
        622,
        "luz-collection",
        "05/09/2024 17:28:05"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:05"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:05"
    ],
    [
        402,
        "co2-collection",
        "05/09/2024 17:28:06"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:06"
    ],
    [
        9,
        "dist-collection",
        "05/09/2024 17:28:06"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:06"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:06"
    ],
    [
        592,
        "luz-collection",
        "05/09/2024 17:28:06"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:06"
    ],
    [
        403,
        "co2-collection",
        "05/09/2024 17:28:07"
    ],
    [
        402,
        "co2-collection",
        "05/09/2024 17:28:07"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:07"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:07"
    ],
    [
        590,
        "luz-collection",
        "05/09/2024 17:28:07"
    ],
    [
        676,
        "luz-collection",
        "05/09/2024 17:28:07"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:07"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:07"
    ],
    [
        403,
        "co2-collection",
        "05/09/2024 17:28:08"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:08"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:08"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:08"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:08"
    ],
    [
        582,
        "luz-collection",
        "05/09/2024 17:28:08"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:08"
    ],
    [
        401,
        "co2-collection",
        "05/09/2024 17:28:09"
    ],
    [
        401,
        "co2-collection",
        "05/09/2024 17:28:09"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:09"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:09"
    ],
    [
        667,
        "luz-collection",
        "05/09/2024 17:28:09"
    ],
    [
        587,
        "luz-collection",
        "05/09/2024 17:28:09"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:09"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:09"
    ],
    [
        401,
        "co2-collection",
        "05/09/2024 17:28:10"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:10"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:10"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:10"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:10"
    ],
    [
        587,
        "luz-collection",
        "05/09/2024 17:28:10"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:10"
    ],
    [
        401,
        "co2-collection",
        "05/09/2024 17:28:11"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:11"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:11"
    ],
    [
        621,
        "luz-collection",
        "05/09/2024 17:28:11"
    ],
    [
        600,
        "luz-collection",
        "05/09/2024 17:28:11"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:11"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:11"
    ],
    [
        403,
        "co2-collection",
        "05/09/2024 17:28:12"
    ],
    [
        401,
        "co2-collection",
        "05/09/2024 17:28:12"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:12"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:12"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:12"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:12"
    ],
    [
        633,
        "luz-collection",
        "05/09/2024 17:28:12"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:12"
    ],
    [
        402,
        "co2-collection",
        "05/09/2024 17:28:13"
    ],
    [
        403,
        "co2-collection",
        "05/09/2024 17:28:13"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:13"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:13"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:13"
    ],
    [
        627,
        "luz-collection",
        "05/09/2024 17:28:13"
    ],
    [
        647,
        "luz-collection",
        "05/09/2024 17:28:13"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:13"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:13"
    ],
    [
        402,
        "co2-collection",
        "05/09/2024 17:28:14"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:14"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:14"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:14"
    ],
    [
        663,
        "luz-collection",
        "05/09/2024 17:28:14"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:14"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:14"
    ],
    [
        403,
        "co2-collection",
        "05/09/2024 17:28:15"
    ],
    [
        402,
        "co2-collection",
        "05/09/2024 17:28:15"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:15"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:15"
    ],
    [
        667,
        "luz-collection",
        "05/09/2024 17:28:15"
    ],
    [
        607,
        "luz-collection",
        "05/09/2024 17:28:15"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:15"
    ],
    [
        403,
        "co2-collection",
        "05/09/2024 17:28:16"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:16"
    ],
    [
        9,
        "dist-collection",
        "05/09/2024 17:28:16"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:16"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:16"
    ],
    [
        660,
        "luz-collection",
        "05/09/2024 17:28:16"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:16"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:16"
    ],
    [
        404,
        "co2-collection",
        "05/09/2024 17:28:17"
    ],
    [
        402,
        "co2-collection",
        "05/09/2024 17:28:17"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:17"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:17"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:17"
    ],
    [
        645,
        "luz-collection",
        "05/09/2024 17:28:17"
    ],
    [
        633,
        "luz-collection",
        "05/09/2024 17:28:17"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:17"
    ],
    [
        405,
        "co2-collection",
        "05/09/2024 17:28:18"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:18"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:18"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:18"
    ],
    [
        626,
        "luz-collection",
        "05/09/2024 17:28:18"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:18"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:18"
    ],
    [
        408,
        "co2-collection",
        "05/09/2024 17:28:19"
    ],
    [
        411,
        "co2-collection",
        "05/09/2024 17:28:19"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:19"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:19"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:19"
    ],
    [
        606,
        "luz-collection",
        "05/09/2024 17:28:19"
    ],
    [
        587,
        "luz-collection",
        "05/09/2024 17:28:19"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:19"
    ],
    [
        407,
        "co2-collection",
        "05/09/2024 17:28:20"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:20"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:20"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:20"
    ],
    [
        677,
        "luz-collection",
        "05/09/2024 17:28:20"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:20"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:20"
    ],
    [
        406,
        "co2-collection",
        "05/09/2024 17:28:21"
    ],
    [
        405,
        "co2-collection",
        "05/09/2024 17:28:21"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:21"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:21"
    ],
    [
        587,
        "luz-collection",
        "05/09/2024 17:28:21"
    ],
    [
        584,
        "luz-collection",
        "05/09/2024 17:28:21"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:21"
    ],
    [
        407,
        "co2-collection",
        "05/09/2024 17:28:22"
    ],
    [
        9,
        "dist-collection",
        "05/09/2024 17:28:22"
    ],
    [
        9,
        "dist-collection",
        "05/09/2024 17:28:22"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:22"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:22"
    ],
    [
        613,
        "luz-collection",
        "05/09/2024 17:28:22"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:22"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:22"
    ],
    [
        407,
        "co2-collection",
        "05/09/2024 17:28:23"
    ],
    [
        405,
        "co2-collection",
        "05/09/2024 17:28:23"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:23"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:23"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:23"
    ],
    [
        626,
        "luz-collection",
        "05/09/2024 17:28:23"
    ],
    [
        643,
        "luz-collection",
        "05/09/2024 17:28:23"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:23"
    ],
    [
        406,
        "co2-collection",
        "05/09/2024 17:28:24"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:24"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:24"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:24"
    ],
    [
        664,
        "luz-collection",
        "05/09/2024 17:28:24"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:24"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:24"
    ],
    [
        405,
        "co2-collection",
        "05/09/2024 17:28:25"
    ],
    [
        405,
        "co2-collection",
        "05/09/2024 17:28:25"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:25"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:25"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:25"
    ],
    [
        662,
        "luz-collection",
        "05/09/2024 17:28:25"
    ],
    [
        617,
        "luz-collection",
        "05/09/2024 17:28:25"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:25"
    ],
    [
        406,
        "co2-collection",
        "05/09/2024 17:28:26"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:26"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:26"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:26"
    ],
    [
        653,
        "luz-collection",
        "05/09/2024 17:28:26"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:26"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:26"
    ],
    [
        406,
        "co2-collection",
        "05/09/2024 17:28:27"
    ],
    [
        405,
        "co2-collection",
        "05/09/2024 17:28:27"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:27"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:27"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:27"
    ],
    [
        629,
        "luz-collection",
        "05/09/2024 17:28:27"
    ],
    [
        604,
        "luz-collection",
        "05/09/2024 17:28:27"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:27"
    ],
    [
        406,
        "co2-collection",
        "05/09/2024 17:28:28"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:28"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:28"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:28"
    ],
    [
        674,
        "luz-collection",
        "05/09/2024 17:28:28"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:28"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:28"
    ],
    [
        410,
        "co2-collection",
        "05/09/2024 17:28:29"
    ],
    [
        408,
        "co2-collection",
        "05/09/2024 17:28:29"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:29"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:29"
    ],
    [
        586,
        "luz-collection",
        "05/09/2024 17:28:29"
    ],
    [
        586,
        "luz-collection",
        "05/09/2024 17:28:29"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:29"
    ],
    [
        409,
        "co2-collection",
        "05/09/2024 17:28:30"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:30"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:30"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:30"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:30"
    ],
    [
        600,
        "luz-collection",
        "05/09/2024 17:28:30"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:30"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:30"
    ],
    [
        408,
        "co2-collection",
        "05/09/2024 17:28:31"
    ],
    [
        404,
        "co2-collection",
        "05/09/2024 17:28:31"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:31"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:31"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:31"
    ],
    [
        624,
        "luz-collection",
        "05/09/2024 17:28:31"
    ],
    [
        645,
        "luz-collection",
        "05/09/2024 17:28:31"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:31"
    ],
    [
        405,
        "co2-collection",
        "05/09/2024 17:28:32"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:32"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:32"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:32"
    ],
    [
        651,
        "luz-collection",
        "05/09/2024 17:28:32"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:32"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:32"
    ],
    [
        405,
        "co2-collection",
        "05/09/2024 17:28:33"
    ],
    [
        404,
        "co2-collection",
        "05/09/2024 17:28:33"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:33"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:33"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:33"
    ],
    [
        613,
        "luz-collection",
        "05/09/2024 17:28:33"
    ],
    [
        669,
        "luz-collection",
        "05/09/2024 17:28:33"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:33"
    ],
    [
        402,
        "co2-collection",
        "05/09/2024 17:28:34"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:34"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:34"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:34"
    ],
    [
        662,
        "luz-collection",
        "05/09/2024 17:28:34"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:34"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:34"
    ],
    [
        404,
        "co2-collection",
        "05/09/2024 17:28:35"
    ],
    [
        401,
        "co2-collection",
        "05/09/2024 17:28:35"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:35"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:35"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:35"
    ],
    [
        644,
        "luz-collection",
        "05/09/2024 17:28:35"
    ],
    [
        617,
        "luz-collection",
        "05/09/2024 17:28:35"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:35"
    ],
    [
        408,
        "co2-collection",
        "05/09/2024 17:28:36"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:36"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:36"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:36"
    ],
    [
        674,
        "luz-collection",
        "05/09/2024 17:28:36"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:36"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:36"
    ],
    [
        407,
        "co2-collection",
        "05/09/2024 17:28:37"
    ],
    [
        406,
        "co2-collection",
        "05/09/2024 17:28:37"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:37"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:37"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:37"
    ],
    [
        593,
        "luz-collection",
        "05/09/2024 17:28:37"
    ],
    [
        587,
        "luz-collection",
        "05/09/2024 17:28:37"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:37"
    ],
    [
        400,
        "co2-collection",
        "05/09/2024 17:28:38"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:38"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:38"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:38"
    ],
    [
        601,
        "luz-collection",
        "05/09/2024 17:28:38"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:38"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:38"
    ],
    [
        401,
        "co2-collection",
        "05/09/2024 17:28:39"
    ],
    [
        403,
        "co2-collection",
        "05/09/2024 17:28:39"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:39"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:39"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:39"
    ],
    [
        645,
        "luz-collection",
        "05/09/2024 17:28:39"
    ],
    [
        627,
        "luz-collection",
        "05/09/2024 17:28:39"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:39"
    ],
    [
        402,
        "co2-collection",
        "05/09/2024 17:28:40"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:40"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:40"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:40"
    ],
    [
        653,
        "luz-collection",
        "05/09/2024 17:28:40"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:40"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:40"
    ],
    [
        400,
        "co2-collection",
        "05/09/2024 17:28:41"
    ],
    [
        398,
        "co2-collection",
        "05/09/2024 17:28:41"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:41"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:41"
    ],
    [
        665,
        "luz-collection",
        "05/09/2024 17:28:41"
    ],
    [
        616,
        "luz-collection",
        "05/09/2024 17:28:41"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:41"
    ],
    [
        398,
        "co2-collection",
        "05/09/2024 17:28:42"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:42"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:42"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:42"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:42"
    ],
    [
        653,
        "luz-collection",
        "05/09/2024 17:28:42"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:42"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:42"
    ],
    [
        404,
        "co2-collection",
        "05/09/2024 17:28:43"
    ],
    [
        402,
        "co2-collection",
        "05/09/2024 17:28:43"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:43"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:43"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:43"
    ],
    [
        594,
        "luz-collection",
        "05/09/2024 17:28:43"
    ],
    [
        625,
        "luz-collection",
        "05/09/2024 17:28:43"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:43"
    ],
    [
        403,
        "co2-collection",
        "05/09/2024 17:28:44"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:44"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:44"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:44"
    ],
    [
        676,
        "luz-collection",
        "05/09/2024 17:28:44"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:44"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:44"
    ],
    [
        400,
        "co2-collection",
        "05/09/2024 17:28:45"
    ],
    [
        399,
        "co2-collection",
        "05/09/2024 17:28:45"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:45"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:45"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:45"
    ],
    [
        587,
        "luz-collection",
        "05/09/2024 17:28:45"
    ],
    [
        582,
        "luz-collection",
        "05/09/2024 17:28:45"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:45"
    ],
    [
        400,
        "co2-collection",
        "05/09/2024 17:28:46"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:46"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:46"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:46"
    ],
    [
        601,
        "luz-collection",
        "05/09/2024 17:28:46"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:46"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:46"
    ],
    [
        399,
        "co2-collection",
        "05/09/2024 17:28:47"
    ],
    [
        399,
        "co2-collection",
        "05/09/2024 17:28:47"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:47"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:47"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:47"
    ],
    [
        649,
        "luz-collection",
        "05/09/2024 17:28:47"
    ],
    [
        609,
        "luz-collection",
        "05/09/2024 17:28:47"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:47"
    ],
    [
        399,
        "co2-collection",
        "05/09/2024 17:28:48"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:48"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:48"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:48"
    ],
    [
        634,
        "luz-collection",
        "05/09/2024 17:28:48"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:48"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:48"
    ],
    [
        399,
        "co2-collection",
        "05/09/2024 17:28:49"
    ],
    [
        399,
        "co2-collection",
        "05/09/2024 17:28:49"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:49"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:49"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:49"
    ],
    [
        606,
        "luz-collection",
        "05/09/2024 17:28:49"
    ],
    [
        658,
        "luz-collection",
        "05/09/2024 17:28:49"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:49"
    ],
    [
        399,
        "co2-collection",
        "05/09/2024 17:28:50"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:50"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:50"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:50"
    ],
    [
        663,
        "luz-collection",
        "05/09/2024 17:28:50"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:50"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:50"
    ],
    [
        400,
        "co2-collection",
        "05/09/2024 17:28:51"
    ],
    [
        400,
        "co2-collection",
        "05/09/2024 17:28:51"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:51"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:51"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:51"
    ],
    [
        633,
        "luz-collection",
        "05/09/2024 17:28:51"
    ],
    [
        653,
        "luz-collection",
        "05/09/2024 17:28:51"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:51"
    ],
    [
        401,
        "co2-collection",
        "05/09/2024 17:28:52"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:52"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:52"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:52"
    ],
    [
        644,
        "luz-collection",
        "05/09/2024 17:28:52"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:52"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:52"
    ],
    [
        401,
        "co2-collection",
        "05/09/2024 17:28:53"
    ],
    [
        400,
        "co2-collection",
        "05/09/2024 17:28:53"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:53"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:53"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:53"
    ],
    [
        592,
        "luz-collection",
        "05/09/2024 17:28:53"
    ],
    [
        618,
        "luz-collection",
        "05/09/2024 17:28:53"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:53"
    ],
    [
        399,
        "co2-collection",
        "05/09/2024 17:28:54"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:54"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:54"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:54"
    ],
    [
        581,
        "luz-collection",
        "05/09/2024 17:28:54"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:54"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:54"
    ],
    [
        403,
        "co2-collection",
        "05/09/2024 17:28:55"
    ],
    [
        402,
        "co2-collection",
        "05/09/2024 17:28:55"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:55"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:55"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:55"
    ],
    [
        667,
        "luz-collection",
        "05/09/2024 17:28:55"
    ],
    [
        590,
        "luz-collection",
        "05/09/2024 17:28:55"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:55"
    ],
    [
        401,
        "co2-collection",
        "05/09/2024 17:28:56"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:56"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:56"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:56"
    ],
    [
        615,
        "luz-collection",
        "05/09/2024 17:28:56"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:56"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:56"
    ],
    [
        400,
        "co2-collection",
        "05/09/2024 17:28:57"
    ],
    [
        401,
        "co2-collection",
        "05/09/2024 17:28:57"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:57"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:57"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:57"
    ],
    [
        605,
        "luz-collection",
        "05/09/2024 17:28:57"
    ],
    [
        641,
        "luz-collection",
        "05/09/2024 17:28:57"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:57"
    ],
    [
        403,
        "co2-collection",
        "05/09/2024 17:28:58"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:58"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:58"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:58"
    ],
    [
        661,
        "luz-collection",
        "05/09/2024 17:28:58"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:58"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:58"
    ],
    [
        405,
        "co2-collection",
        "05/09/2024 17:28:59"
    ],
    [
        404,
        "co2-collection",
        "05/09/2024 17:28:59"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:59"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:28:59"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:28:59"
    ],
    [
        632,
        "luz-collection",
        "05/09/2024 17:28:59"
    ],
    [
        655,
        "luz-collection",
        "05/09/2024 17:28:59"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:28:59"
    ],
    [
        402,
        "co2-collection",
        "05/09/2024 17:29:00"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:00"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:00"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:00"
    ],
    [
        651,
        "luz-collection",
        "05/09/2024 17:29:00"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:00"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:00"
    ],
    [
        402,
        "co2-collection",
        "05/09/2024 17:29:01"
    ],
    [
        401,
        "co2-collection",
        "05/09/2024 17:29:01"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:01"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:01"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:01"
    ],
    [
        603,
        "luz-collection",
        "05/09/2024 17:29:01"
    ],
    [
        580,
        "luz-collection",
        "05/09/2024 17:29:01"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:01"
    ],
    [
        400,
        "co2-collection",
        "05/09/2024 17:29:02"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:02"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:02"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:02"
    ],
    [
        588,
        "luz-collection",
        "05/09/2024 17:29:02"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:02"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:02"
    ],
    [
        400,
        "co2-collection",
        "05/09/2024 17:29:03"
    ],
    [
        400,
        "co2-collection",
        "05/09/2024 17:29:03"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:03"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:03"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:03"
    ],
    [
        650,
        "luz-collection",
        "05/09/2024 17:29:03"
    ],
    [
        612,
        "luz-collection",
        "05/09/2024 17:29:03"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:03"
    ],
    [
        399,
        "co2-collection",
        "05/09/2024 17:29:04"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:04"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:04"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:04"
    ],
    [
        640,
        "luz-collection",
        "05/09/2024 17:29:04"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:04"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:04"
    ],
    [
        402,
        "co2-collection",
        "05/09/2024 17:29:05"
    ],
    [
        401,
        "co2-collection",
        "05/09/2024 17:29:05"
    ],
    [
        9,
        "dist-collection",
        "05/09/2024 17:29:05"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:05"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:05"
    ],
    [
        609,
        "luz-collection",
        "05/09/2024 17:29:05"
    ],
    [
        662,
        "luz-collection",
        "05/09/2024 17:29:05"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:05"
    ],
    [
        400,
        "co2-collection",
        "05/09/2024 17:29:06"
    ],
    [
        9,
        "dist-collection",
        "05/09/2024 17:29:06"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:06"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:06"
    ],
    [
        643,
        "luz-collection",
        "05/09/2024 17:29:06"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:06"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:06"
    ],
    [
        400,
        "co2-collection",
        "05/09/2024 17:29:07"
    ],
    [
        401,
        "co2-collection",
        "05/09/2024 17:29:07"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:07"
    ],
    [
        9,
        "dist-collection",
        "05/09/2024 17:29:07"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:07"
    ],
    [
        601,
        "luz-collection",
        "05/09/2024 17:29:07"
    ],
    [
        581,
        "luz-collection",
        "05/09/2024 17:29:07"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:07"
    ],
    [
        413,
        "co2-collection",
        "05/09/2024 17:29:08"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:08"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:08"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:08"
    ],
    [
        595,
        "luz-collection",
        "05/09/2024 17:29:08"
    ],
    [
        661,
        "luz-collection",
        "05/09/2024 17:29:08"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:08"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:08"
    ],
    [
        397,
        "co2-collection",
        "05/09/2024 17:29:09"
    ],
    [
        397,
        "co2-collection",
        "05/09/2024 17:29:09"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:09"
    ],
    [
        9,
        "dist-collection",
        "05/09/2024 17:29:09"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:09"
    ],
    [
        637,
        "luz-collection",
        "05/09/2024 17:29:09"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:09"
    ],
    [
        397,
        "co2-collection",
        "05/09/2024 17:29:10"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:10"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:10"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:10"
    ],
    [
        607,
        "luz-collection",
        "05/09/2024 17:29:10"
    ],
    [
        660,
        "luz-collection",
        "05/09/2024 17:29:10"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:10"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:10"
    ],
    [
        397,
        "co2-collection",
        "05/09/2024 17:29:11"
    ],
    [
        397,
        "co2-collection",
        "05/09/2024 17:29:11"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:11"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:11"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:11"
    ],
    [
        653,
        "luz-collection",
        "05/09/2024 17:29:11"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:11"
    ],
    [
        399,
        "co2-collection",
        "05/09/2024 17:29:12"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:12"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:12"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:12"
    ],
    [
        629,
        "luz-collection",
        "05/09/2024 17:29:12"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:12"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:12"
    ],
    [
        397,
        "co2-collection",
        "05/09/2024 17:29:13"
    ],
    [
        397,
        "co2-collection",
        "05/09/2024 17:29:13"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:13"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:13"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:13"
    ],
    [
        600,
        "luz-collection",
        "05/09/2024 17:29:13"
    ],
    [
        672,
        "luz-collection",
        "05/09/2024 17:29:13"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:13"
    ],
    [
        397,
        "co2-collection",
        "05/09/2024 17:29:14"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:14"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:14"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:14"
    ],
    [
        580,
        "luz-collection",
        "05/09/2024 17:29:14"
    ],
    [
        584,
        "luz-collection",
        "05/09/2024 17:29:14"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:14"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:14"
    ],
    [
        397,
        "co2-collection",
        "05/09/2024 17:29:15"
    ],
    [
        397,
        "co2-collection",
        "05/09/2024 17:29:15"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:15"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:15"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:15"
    ],
    [
        607,
        "luz-collection",
        "05/09/2024 17:29:15"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:15"
    ],
    [
        395,
        "co2-collection",
        "05/09/2024 17:29:16"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:16"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:16"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:16"
    ],
    [
        632,
        "luz-collection",
        "05/09/2024 17:29:16"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:16"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:16"
    ],
    [
        398,
        "co2-collection",
        "05/09/2024 17:29:17"
    ],
    [
        398,
        "co2-collection",
        "05/09/2024 17:29:17"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:17"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:17"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:17"
    ],
    [
        655,
        "luz-collection",
        "05/09/2024 17:29:17"
    ],
    [
        630,
        "luz-collection",
        "05/09/2024 17:29:17"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:17"
    ],
    [
        397,
        "co2-collection",
        "05/09/2024 17:29:18"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:18"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:18"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:18"
    ],
    [
        658,
        "luz-collection",
        "05/09/2024 17:29:18"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:18"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:18"
    ],
    [
        403,
        "co2-collection",
        "05/09/2024 17:29:19"
    ],
    [
        403,
        "co2-collection",
        "05/09/2024 17:29:19"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:19"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:19"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:19"
    ],
    [
        650,
        "luz-collection",
        "05/09/2024 17:29:19"
    ],
    [
        614,
        "luz-collection",
        "05/09/2024 17:29:19"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:19"
    ],
    [
        400,
        "co2-collection",
        "05/09/2024 17:29:20"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:20"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:20"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:20"
    ],
    [
        625,
        "luz-collection",
        "05/09/2024 17:29:20"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:20"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:20"
    ],
    [
        401,
        "co2-collection",
        "05/09/2024 17:29:21"
    ],
    [
        401,
        "co2-collection",
        "05/09/2024 17:29:21"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:21"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:21"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:21"
    ],
    [
        601,
        "luz-collection",
        "05/09/2024 17:29:21"
    ],
    [
        670,
        "luz-collection",
        "05/09/2024 17:29:21"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:21"
    ],
    [
        402,
        "co2-collection",
        "05/09/2024 17:29:22"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:22"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:22"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:22"
    ],
    [
        584,
        "luz-collection",
        "05/09/2024 17:29:22"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:22"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:22"
    ],
    [
        400,
        "co2-collection",
        "05/09/2024 17:29:23"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:23"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:23"
    ],
    [
        591,
        "luz-collection",
        "05/09/2024 17:29:23"
    ],
    [
        580,
        "luz-collection",
        "05/09/2024 17:29:23"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:23"
    ],
    [
        399,
        "co2-collection",
        "05/09/2024 17:29:24"
    ],
    [
        399,
        "co2-collection",
        "05/09/2024 17:29:24"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:24"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:24"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:24"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:24"
    ],
    [
        605,
        "luz-collection",
        "05/09/2024 17:29:24"
    ],
    [
        647,
        "luz-collection",
        "05/09/2024 17:29:24"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:24"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:24"
    ],
    [
        398,
        "co2-collection",
        "05/09/2024 17:29:25"
    ],
    [
        397,
        "co2-collection",
        "05/09/2024 17:29:25"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:25"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:25"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:25"
    ],
    [
        629,
        "luz-collection",
        "05/09/2024 17:29:25"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:25"
    ],
    [
        394,
        "co2-collection",
        "05/09/2024 17:29:26"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:26"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:26"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:26"
    ],
    [
        651,
        "luz-collection",
        "05/09/2024 17:29:26"
    ],
    [
        603,
        "luz-collection",
        "05/09/2024 17:29:26"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:26"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:26"
    ],
    [
        393,
        "co2-collection",
        "05/09/2024 17:29:27"
    ],
    [
        394,
        "co2-collection",
        "05/09/2024 17:29:27"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:27"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:27"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:27"
    ],
    [
        659,
        "luz-collection",
        "05/09/2024 17:29:27"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:27"
    ],
    [
        398,
        "co2-collection",
        "05/09/2024 17:29:28"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:28"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:28"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:28"
    ],
    [
        653,
        "luz-collection",
        "05/09/2024 17:29:28"
    ],
    [
        636,
        "luz-collection",
        "05/09/2024 17:29:28"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:28"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:28"
    ],
    [
        398,
        "co2-collection",
        "05/09/2024 17:29:29"
    ],
    [
        400,
        "co2-collection",
        "05/09/2024 17:29:29"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:29"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:29"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:29"
    ],
    [
        637,
        "luz-collection",
        "05/09/2024 17:29:29"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:29"
    ],
    [
        400,
        "co2-collection",
        "05/09/2024 17:29:30"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:30"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:30"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:30"
    ],
    [
        618,
        "luz-collection",
        "05/09/2024 17:29:30"
    ],
    [
        594,
        "luz-collection",
        "05/09/2024 17:29:30"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:30"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:30"
    ],
    [
        398,
        "co2-collection",
        "05/09/2024 17:29:31"
    ],
    [
        399,
        "co2-collection",
        "05/09/2024 17:29:31"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:31"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:31"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:31"
    ],
    [
        576,
        "luz-collection",
        "05/09/2024 17:29:31"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:31"
    ],
    [
        401,
        "co2-collection",
        "05/09/2024 17:29:32"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:32"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:32"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:32"
    ],
    [
        579,
        "luz-collection",
        "05/09/2024 17:29:32"
    ],
    [
        667,
        "luz-collection",
        "05/09/2024 17:29:32"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:32"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:32"
    ],
    [
        397,
        "co2-collection",
        "05/09/2024 17:29:33"
    ],
    [
        398,
        "co2-collection",
        "05/09/2024 17:29:33"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:33"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:33"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:33"
    ],
    [
        594,
        "luz-collection",
        "05/09/2024 17:29:33"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:33"
    ],
    [
        401,
        "co2-collection",
        "05/09/2024 17:29:34"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:34"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:34"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:34"
    ],
    [
        616,
        "luz-collection",
        "05/09/2024 17:29:34"
    ],
    [
        620,
        "luz-collection",
        "05/09/2024 17:29:34"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:34"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:34"
    ],
    [
        400,
        "co2-collection",
        "05/09/2024 17:29:35"
    ],
    [
        400,
        "co2-collection",
        "05/09/2024 17:29:35"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:35"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:35"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:35"
    ],
    [
        639,
        "luz-collection",
        "05/09/2024 17:29:35"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:35"
    ],
    [
        400,
        "co2-collection",
        "05/09/2024 17:29:36"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:36"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:36"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:36"
    ],
    [
        648,
        "luz-collection",
        "05/09/2024 17:29:36"
    ],
    [
        657,
        "luz-collection",
        "05/09/2024 17:29:36"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:36"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:36"
    ],
    [
        400,
        "co2-collection",
        "05/09/2024 17:29:37"
    ],
    [
        400,
        "co2-collection",
        "05/09/2024 17:29:37"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:37"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:37"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:37"
    ],
    [
        618,
        "luz-collection",
        "05/09/2024 17:29:37"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:37"
    ],
    [
        400,
        "co2-collection",
        "05/09/2024 17:29:38"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:38"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:38"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:38"
    ],
    [
        607,
        "luz-collection",
        "05/09/2024 17:29:38"
    ],
    [
        633,
        "luz-collection",
        "05/09/2024 17:29:38"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:38"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:38"
    ],
    [
        400,
        "co2-collection",
        "05/09/2024 17:29:39"
    ],
    [
        399,
        "co2-collection",
        "05/09/2024 17:29:39"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:39"
    ],
    [
        9,
        "dist-collection",
        "05/09/2024 17:29:39"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:39"
    ],
    [
        571,
        "luz-collection",
        "05/09/2024 17:29:39"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:39"
    ],
    [
        399,
        "co2-collection",
        "05/09/2024 17:29:40"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:40"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:40"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:40"
    ],
    [
        576,
        "luz-collection",
        "05/09/2024 17:29:40"
    ],
    [
        662,
        "luz-collection",
        "05/09/2024 17:29:40"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:40"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:40"
    ],
    [
        400,
        "co2-collection",
        "05/09/2024 17:29:41"
    ],
    [
        396,
        "co2-collection",
        "05/09/2024 17:29:41"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:41"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:41"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:41"
    ],
    [
        592,
        "luz-collection",
        "05/09/2024 17:29:41"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:41"
    ],
    [
        399,
        "co2-collection",
        "05/09/2024 17:29:42"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:42"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:42"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:42"
    ],
    [
        603,
        "luz-collection",
        "05/09/2024 17:29:42"
    ],
    [
        620,
        "luz-collection",
        "05/09/2024 17:29:42"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:42"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:42"
    ],
    [
        399,
        "co2-collection",
        "05/09/2024 17:29:43"
    ],
    [
        400,
        "co2-collection",
        "05/09/2024 17:29:43"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:43"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:43"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:43"
    ],
    [
        637,
        "luz-collection",
        "05/09/2024 17:29:43"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:43"
    ],
    [
        400,
        "co2-collection",
        "05/09/2024 17:29:44"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:44"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:44"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:44"
    ],
    [
        646,
        "luz-collection",
        "05/09/2024 17:29:44"
    ],
    [
        631,
        "luz-collection",
        "05/09/2024 17:29:44"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:44"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:44"
    ],
    [
        400,
        "co2-collection",
        "05/09/2024 17:29:45"
    ],
    [
        400,
        "co2-collection",
        "05/09/2024 17:29:45"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:45"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:45"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:45"
    ],
    [
        611,
        "luz-collection",
        "05/09/2024 17:29:45"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:45"
    ],
    [
        399,
        "co2-collection",
        "05/09/2024 17:29:46"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:46"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:46"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:46"
    ],
    [
        601,
        "luz-collection",
        "05/09/2024 17:29:46"
    ],
    [
        573,
        "luz-collection",
        "05/09/2024 17:29:46"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:46"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:46"
    ],
    [
        400,
        "co2-collection",
        "05/09/2024 17:29:47"
    ],
    [
        401,
        "co2-collection",
        "05/09/2024 17:29:47"
    ],
    [
        15,
        "dist-collection",
        "05/09/2024 17:29:47"
    ],
    [
        15,
        "dist-collection",
        "05/09/2024 17:29:47"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:47"
    ],
    [
        552,
        "luz-collection",
        "05/09/2024 17:29:47"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:47"
    ],
    [
        401,
        "co2-collection",
        "05/09/2024 17:29:48"
    ],
    [
        15,
        "dist-collection",
        "05/09/2024 17:29:48"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:48"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:48"
    ],
    [
        551,
        "luz-collection",
        "05/09/2024 17:29:48"
    ],
    [
        641,
        "luz-collection",
        "05/09/2024 17:29:48"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:48"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:48"
    ],
    [
        400,
        "co2-collection",
        "05/09/2024 17:29:49"
    ],
    [
        400,
        "co2-collection",
        "05/09/2024 17:29:49"
    ],
    [
        15,
        "dist-collection",
        "05/09/2024 17:29:49"
    ],
    [
        15,
        "dist-collection",
        "05/09/2024 17:29:49"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:49"
    ],
    [
        563,
        "luz-collection",
        "05/09/2024 17:29:49"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:49"
    ],
    [
        399,
        "co2-collection",
        "05/09/2024 17:29:50"
    ],
    [
        15,
        "dist-collection",
        "05/09/2024 17:29:50"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:50"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:50"
    ],
    [
        593,
        "luz-collection",
        "05/09/2024 17:29:50"
    ],
    [
        588,
        "luz-collection",
        "05/09/2024 17:29:50"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:50"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:50"
    ],
    [
        399,
        "co2-collection",
        "05/09/2024 17:29:51"
    ],
    [
        400,
        "co2-collection",
        "05/09/2024 17:29:51"
    ],
    [
        15,
        "dist-collection",
        "05/09/2024 17:29:51"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:51"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:51"
    ],
    [
        605,
        "luz-collection",
        "05/09/2024 17:29:51"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:51"
    ],
    [
        399,
        "co2-collection",
        "05/09/2024 17:29:52"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:52"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:52"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:52"
    ],
    [
        626,
        "luz-collection",
        "05/09/2024 17:29:52"
    ],
    [
        627,
        "luz-collection",
        "05/09/2024 17:29:52"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:52"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:52"
    ],
    [
        399,
        "co2-collection",
        "05/09/2024 17:29:53"
    ],
    [
        400,
        "co2-collection",
        "05/09/2024 17:29:53"
    ],
    [
        9,
        "dist-collection",
        "05/09/2024 17:29:53"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:53"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:53"
    ],
    [
        581,
        "luz-collection",
        "05/09/2024 17:29:53"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:53"
    ],
    [
        399,
        "co2-collection",
        "05/09/2024 17:29:54"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:54"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:54"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:54"
    ],
    [
        608,
        "luz-collection",
        "05/09/2024 17:29:54"
    ],
    [
        583,
        "luz-collection",
        "05/09/2024 17:29:54"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:54"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:54"
    ],
    [
        399,
        "co2-collection",
        "05/09/2024 17:29:55"
    ],
    [
        399,
        "co2-collection",
        "05/09/2024 17:29:55"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:55"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:55"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:55"
    ],
    [
        558,
        "luz-collection",
        "05/09/2024 17:29:55"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:55"
    ],
    [
        398,
        "co2-collection",
        "05/09/2024 17:29:56"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:56"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:56"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:56"
    ],
    [
        639,
        "luz-collection",
        "05/09/2024 17:29:56"
    ],
    [
        545,
        "luz-collection",
        "05/09/2024 17:29:56"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:56"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:56"
    ],
    [
        400,
        "co2-collection",
        "05/09/2024 17:29:57"
    ],
    [
        400,
        "co2-collection",
        "05/09/2024 17:29:57"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:57"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:57"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:57"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:57"
    ],
    [
        553,
        "luz-collection",
        "05/09/2024 17:29:57"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:57"
    ],
    [
        399,
        "co2-collection",
        "05/09/2024 17:29:58"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:58"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:58"
    ],
    [
        572,
        "luz-collection",
        "05/09/2024 17:29:58"
    ],
    [
        603,
        "luz-collection",
        "05/09/2024 17:29:58"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:58"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:58"
    ],
    [
        399,
        "co2-collection",
        "05/09/2024 17:29:59"
    ],
    [
        403,
        "co2-collection",
        "05/09/2024 17:29:59"
    ],
    [
        15,
        "dist-collection",
        "05/09/2024 17:29:59"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:29:59"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:59"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:29:59"
    ],
    [
        589,
        "luz-collection",
        "05/09/2024 17:29:59"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:29:59"
    ],
    [
        399,
        "co2-collection",
        "05/09/2024 17:30:00"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:00"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:00"
    ],
    [
        614,
        "luz-collection",
        "05/09/2024 17:30:00"
    ],
    [
        628,
        "luz-collection",
        "05/09/2024 17:30:00"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:00"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:00"
    ],
    [
        398,
        "co2-collection",
        "05/09/2024 17:30:01"
    ],
    [
        397,
        "co2-collection",
        "05/09/2024 17:30:01"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:01"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:01"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:01"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:01"
    ],
    [
        574,
        "luz-collection",
        "05/09/2024 17:30:01"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:01"
    ],
    [
        398,
        "co2-collection",
        "05/09/2024 17:30:02"
    ],
    [
        400,
        "co2-collection",
        "05/09/2024 17:30:02"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:02"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:02"
    ],
    [
        604,
        "luz-collection",
        "05/09/2024 17:30:02"
    ],
    [
        622,
        "luz-collection",
        "05/09/2024 17:30:02"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:02"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:02"
    ],
    [
        398,
        "co2-collection",
        "05/09/2024 17:30:03"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:03"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:03"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:03"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:03"
    ],
    [
        578,
        "luz-collection",
        "05/09/2024 17:30:03"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:03"
    ],
    [
        399,
        "co2-collection",
        "05/09/2024 17:30:04"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:04"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:04"
    ],
    [
        630,
        "luz-collection",
        "05/09/2024 17:30:04"
    ],
    [
        557,
        "luz-collection",
        "05/09/2024 17:30:04"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:04"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:04"
    ],
    [
        399,
        "co2-collection",
        "05/09/2024 17:30:05"
    ],
    [
        399,
        "co2-collection",
        "05/09/2024 17:30:05"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:05"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:05"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:05"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:05"
    ],
    [
        545,
        "luz-collection",
        "05/09/2024 17:30:05"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:05"
    ],
    [
        399,
        "co2-collection",
        "05/09/2024 17:30:06"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:06"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:06"
    ],
    [
        556,
        "luz-collection",
        "05/09/2024 17:30:06"
    ],
    [
        609,
        "luz-collection",
        "05/09/2024 17:30:06"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:06"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:06"
    ],
    [
        398,
        "co2-collection",
        "05/09/2024 17:30:07"
    ],
    [
        399,
        "co2-collection",
        "05/09/2024 17:30:07"
    ],
    [
        9,
        "dist-collection",
        "05/09/2024 17:30:07"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:07"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:07"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:07"
    ],
    [
        592,
        "luz-collection",
        "05/09/2024 17:30:07"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:07"
    ],
    [
        399,
        "co2-collection",
        "05/09/2024 17:30:08"
    ],
    [
        398,
        "co2-collection",
        "05/09/2024 17:30:08"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:08"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:08"
    ],
    [
        624,
        "luz-collection",
        "05/09/2024 17:30:08"
    ],
    [
        619,
        "luz-collection",
        "05/09/2024 17:30:08"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:08"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:08"
    ],
    [
        398,
        "co2-collection",
        "05/09/2024 17:30:09"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:09"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:09"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:09"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:09"
    ],
    [
        579,
        "luz-collection",
        "05/09/2024 17:30:09"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:09"
    ],
    [
        398,
        "co2-collection",
        "05/09/2024 17:30:10"
    ],
    [
        398,
        "co2-collection",
        "05/09/2024 17:30:10"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:10"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:10"
    ],
    [
        612,
        "luz-collection",
        "05/09/2024 17:30:10"
    ],
    [
        584,
        "luz-collection",
        "05/09/2024 17:30:10"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:10"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:10"
    ],
    [
        397,
        "co2-collection",
        "05/09/2024 17:30:11"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:11"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:11"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:11"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:11"
    ],
    [
        555,
        "luz-collection",
        "05/09/2024 17:30:11"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:11"
    ],
    [
        397,
        "co2-collection",
        "05/09/2024 17:30:12"
    ],
    [
        398,
        "co2-collection",
        "05/09/2024 17:30:12"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:12"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:12"
    ],
    [
        543,
        "luz-collection",
        "05/09/2024 17:30:12"
    ],
    [
        635,
        "luz-collection",
        "05/09/2024 17:30:12"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:12"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:12"
    ],
    [
        399,
        "co2-collection",
        "05/09/2024 17:30:13"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:13"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:13"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:13"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:13"
    ],
    [
        557,
        "luz-collection",
        "05/09/2024 17:30:13"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:13"
    ],
    [
        399,
        "co2-collection",
        "05/09/2024 17:30:14"
    ],
    [
        399,
        "co2-collection",
        "05/09/2024 17:30:14"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:14"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:14"
    ],
    [
        586,
        "luz-collection",
        "05/09/2024 17:30:14"
    ],
    [
        579,
        "luz-collection",
        "05/09/2024 17:30:14"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:14"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:14"
    ],
    [
        399,
        "co2-collection",
        "05/09/2024 17:30:15"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:15"
    ],
    [
        9,
        "dist-collection",
        "05/09/2024 17:30:15"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:15"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:15"
    ],
    [
        623,
        "luz-collection",
        "05/09/2024 17:30:15"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:15"
    ],
    [
        398,
        "co2-collection",
        "05/09/2024 17:30:16"
    ],
    [
        399,
        "co2-collection",
        "05/09/2024 17:30:16"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:16"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:16"
    ],
    [
        593,
        "luz-collection",
        "05/09/2024 17:30:16"
    ],
    [
        617,
        "luz-collection",
        "05/09/2024 17:30:16"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:16"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:16"
    ],
    [
        398,
        "co2-collection",
        "05/09/2024 17:30:17"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:17"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:17"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:17"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:17"
    ],
    [
        614,
        "luz-collection",
        "05/09/2024 17:30:17"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:17"
    ],
    [
        399,
        "co2-collection",
        "05/09/2024 17:30:18"
    ],
    [
        398,
        "co2-collection",
        "05/09/2024 17:30:18"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:18"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:18"
    ],
    [
        565,
        "luz-collection",
        "05/09/2024 17:30:18"
    ],
    [
        542,
        "luz-collection",
        "05/09/2024 17:30:18"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:18"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:18"
    ],
    [
        400,
        "co2-collection",
        "05/09/2024 17:30:19"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:19"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:19"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:19"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:19"
    ],
    [
        553,
        "luz-collection",
        "05/09/2024 17:30:19"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:19"
    ],
    [
        401,
        "co2-collection",
        "05/09/2024 17:30:20"
    ],
    [
        400,
        "co2-collection",
        "05/09/2024 17:30:20"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:20"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:20"
    ],
    [
        580,
        "luz-collection",
        "05/09/2024 17:30:20"
    ],
    [
        608,
        "luz-collection",
        "05/09/2024 17:30:20"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:20"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:20"
    ],
    [
        400,
        "co2-collection",
        "05/09/2024 17:30:21"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:21"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:21"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:21"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:21"
    ],
    [
        610,
        "luz-collection",
        "05/09/2024 17:30:21"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:21"
    ],
    [
        402,
        "co2-collection",
        "05/09/2024 17:30:22"
    ],
    [
        401,
        "co2-collection",
        "05/09/2024 17:30:22"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:22"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:22"
    ],
    [
        578,
        "luz-collection",
        "05/09/2024 17:30:22"
    ],
    [
        625,
        "luz-collection",
        "05/09/2024 17:30:22"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:22"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:22"
    ],
    [
        401,
        "co2-collection",
        "05/09/2024 17:30:23"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:23"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:23"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:23"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:23"
    ],
    [
        613,
        "luz-collection",
        "05/09/2024 17:30:23"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:23"
    ],
    [
        401,
        "co2-collection",
        "05/09/2024 17:30:24"
    ],
    [
        401,
        "co2-collection",
        "05/09/2024 17:30:24"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:24"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:24"
    ],
    [
        555,
        "luz-collection",
        "05/09/2024 17:30:24"
    ],
    [
        584,
        "luz-collection",
        "05/09/2024 17:30:24"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:24"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:24"
    ],
    [
        402,
        "co2-collection",
        "05/09/2024 17:30:25"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:25"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:25"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:25"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:25"
    ],
    [
        636,
        "luz-collection",
        "05/09/2024 17:30:25"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:25"
    ],
    [
        400,
        "co2-collection",
        "05/09/2024 17:30:26"
    ],
    [
        402,
        "co2-collection",
        "05/09/2024 17:30:26"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:26"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:26"
    ],
    [
        544,
        "luz-collection",
        "05/09/2024 17:30:26"
    ],
    [
        555,
        "luz-collection",
        "05/09/2024 17:30:26"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:26"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:26"
    ],
    [
        404,
        "co2-collection",
        "05/09/2024 17:30:27"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:27"
    ],
    [
        9,
        "dist-collection",
        "05/09/2024 17:30:27"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:27"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:27"
    ],
    [
        595,
        "luz-collection",
        "05/09/2024 17:30:27"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:27"
    ],
    [
        399,
        "co2-collection",
        "05/09/2024 17:30:28"
    ],
    [
        398,
        "co2-collection",
        "05/09/2024 17:30:28"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:28"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:28"
    ],
    [
        620,
        "luz-collection",
        "05/09/2024 17:30:28"
    ],
    [
        571,
        "luz-collection",
        "05/09/2024 17:30:28"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:28"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:28"
    ],
    [
        401,
        "co2-collection",
        "05/09/2024 17:30:29"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:29"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:29"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:29"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:29"
    ],
    [
        622,
        "luz-collection",
        "05/09/2024 17:30:29"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:29"
    ],
    [
        400,
        "co2-collection",
        "05/09/2024 17:30:30"
    ],
    [
        397,
        "co2-collection",
        "05/09/2024 17:30:30"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:30"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:30"
    ],
    [
        613,
        "luz-collection",
        "05/09/2024 17:30:30"
    ],
    [
        608,
        "luz-collection",
        "05/09/2024 17:30:30"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:30"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:30"
    ],
    [
        396,
        "co2-collection",
        "05/09/2024 17:30:31"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:31"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:31"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:31"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:31"
    ],
    [
        580,
        "luz-collection",
        "05/09/2024 17:30:31"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:31"
    ],
    [
        395,
        "co2-collection",
        "05/09/2024 17:30:32"
    ],
    [
        395,
        "co2-collection",
        "05/09/2024 17:30:32"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:32"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:32"
    ],
    [
        552,
        "luz-collection",
        "05/09/2024 17:30:32"
    ],
    [
        551,
        "luz-collection",
        "05/09/2024 17:30:32"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:32"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:32"
    ],
    [
        392,
        "co2-collection",
        "05/09/2024 17:30:33"
    ],
    [
        15,
        "dist-collection",
        "05/09/2024 17:30:33"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:33"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:33"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:33"
    ],
    [
        621,
        "luz-collection",
        "05/09/2024 17:30:33"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:33"
    ],
    [
        394,
        "co2-collection",
        "05/09/2024 17:30:34"
    ],
    [
        395,
        "co2-collection",
        "05/09/2024 17:30:34"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:34"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:34"
    ],
    [
        576,
        "luz-collection",
        "05/09/2024 17:30:34"
    ],
    [
        606,
        "luz-collection",
        "05/09/2024 17:30:34"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:34"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:34"
    ],
    [
        395,
        "co2-collection",
        "05/09/2024 17:30:35"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:35"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:35"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:35"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:35"
    ],
    [
        629,
        "luz-collection",
        "05/09/2024 17:30:35"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:35"
    ],
    [
        395,
        "co2-collection",
        "05/09/2024 17:30:36"
    ],
    [
        395,
        "co2-collection",
        "05/09/2024 17:30:36"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:36"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:36"
    ],
    [
        577,
        "luz-collection",
        "05/09/2024 17:30:36"
    ],
    [
        618,
        "luz-collection",
        "05/09/2024 17:30:36"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:36"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:36"
    ],
    [
        397,
        "co2-collection",
        "05/09/2024 17:30:37"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:37"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:37"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:37"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:37"
    ],
    [
        588,
        "luz-collection",
        "05/09/2024 17:30:37"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:37"
    ],
    [
        395,
        "co2-collection",
        "05/09/2024 17:30:38"
    ],
    [
        396,
        "co2-collection",
        "05/09/2024 17:30:38"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:38"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:38"
    ],
    [
        556,
        "luz-collection",
        "05/09/2024 17:30:38"
    ],
    [
        636,
        "luz-collection",
        "05/09/2024 17:30:38"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:38"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:38"
    ],
    [
        395,
        "co2-collection",
        "05/09/2024 17:30:39"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:39"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:39"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:39"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:39"
    ],
    [
        545,
        "luz-collection",
        "05/09/2024 17:30:39"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:39"
    ],
    [
        408,
        "co2-collection",
        "05/09/2024 17:30:40"
    ],
    [
        400,
        "co2-collection",
        "05/09/2024 17:30:40"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:40"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:40"
    ],
    [
        594,
        "luz-collection",
        "05/09/2024 17:30:40"
    ],
    [
        562,
        "luz-collection",
        "05/09/2024 17:30:40"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:40"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:40"
    ],
    [
        398,
        "co2-collection",
        "05/09/2024 17:30:41"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:41"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:41"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:41"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:41"
    ],
    [
        569,
        "luz-collection",
        "05/09/2024 17:30:41"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:41"
    ],
    [
        402,
        "co2-collection",
        "05/09/2024 17:30:42"
    ],
    [
        397,
        "co2-collection",
        "05/09/2024 17:30:42"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:42"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:42"
    ],
    [
        622,
        "luz-collection",
        "05/09/2024 17:30:42"
    ],
    [
        617,
        "luz-collection",
        "05/09/2024 17:30:42"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:42"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:42"
    ],
    [
        404,
        "co2-collection",
        "05/09/2024 17:30:43"
    ],
    [
        15,
        "dist-collection",
        "05/09/2024 17:30:43"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:43"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:43"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:43"
    ],
    [
        590,
        "luz-collection",
        "05/09/2024 17:30:43"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:43"
    ],
    [
        404,
        "co2-collection",
        "05/09/2024 17:30:44"
    ],
    [
        406,
        "co2-collection",
        "05/09/2024 17:30:44"
    ],
    [
        15,
        "dist-collection",
        "05/09/2024 17:30:44"
    ],
    [
        15,
        "dist-collection",
        "05/09/2024 17:30:44"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:44"
    ],
    [
        617,
        "luz-collection",
        "05/09/2024 17:30:44"
    ],
    [
        557,
        "luz-collection",
        "05/09/2024 17:30:44"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:44"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:44"
    ],
    [
        394,
        "co2-collection",
        "05/09/2024 17:30:45"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:45"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:45"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:45"
    ],
    [
        544,
        "luz-collection",
        "05/09/2024 17:30:45"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:45"
    ],
    [
        396,
        "co2-collection",
        "05/09/2024 17:30:46"
    ],
    [
        395,
        "co2-collection",
        "05/09/2024 17:30:46"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:46"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:46"
    ],
    [
        563,
        "luz-collection",
        "05/09/2024 17:30:46"
    ],
    [
        594,
        "luz-collection",
        "05/09/2024 17:30:46"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:46"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:46"
    ],
    [
        392,
        "co2-collection",
        "05/09/2024 17:30:47"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:47"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:47"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:47"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:47"
    ],
    [
        597,
        "luz-collection",
        "05/09/2024 17:30:47"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:47"
    ],
    [
        390,
        "co2-collection",
        "05/09/2024 17:30:48"
    ],
    [
        391,
        "co2-collection",
        "05/09/2024 17:30:48"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:48"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:48"
    ],
    [
        613,
        "luz-collection",
        "05/09/2024 17:30:48"
    ],
    [
        624,
        "luz-collection",
        "05/09/2024 17:30:48"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:48"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:48"
    ],
    [
        397,
        "co2-collection",
        "05/09/2024 17:30:49"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:49"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:49"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:49"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:49"
    ],
    [
        595,
        "luz-collection",
        "05/09/2024 17:30:49"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:49"
    ],
    [
        396,
        "co2-collection",
        "05/09/2024 17:30:50"
    ],
    [
        394,
        "co2-collection",
        "05/09/2024 17:30:50"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:50"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:50"
    ],
    [
        553,
        "luz-collection",
        "05/09/2024 17:30:50"
    ],
    [
        585,
        "luz-collection",
        "05/09/2024 17:30:50"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:50"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:50"
    ],
    [
        393,
        "co2-collection",
        "05/09/2024 17:30:51"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:51"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:51"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:51"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:51"
    ],
    [
        545,
        "luz-collection",
        "05/09/2024 17:30:51"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:51"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:51"
    ],
    [
        393,
        "co2-collection",
        "05/09/2024 17:30:52"
    ],
    [
        394,
        "co2-collection",
        "05/09/2024 17:30:52"
    ],
    [
        15,
        "dist-collection",
        "05/09/2024 17:30:52"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:52"
    ],
    [
        620,
        "luz-collection",
        "05/09/2024 17:30:52"
    ],
    [
        565,
        "luz-collection",
        "05/09/2024 17:30:52"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:52"
    ],
    [
        394,
        "co2-collection",
        "05/09/2024 17:30:53"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:53"
    ],
    [
        15,
        "dist-collection",
        "05/09/2024 17:30:53"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:53"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:53"
    ],
    [
        596,
        "luz-collection",
        "05/09/2024 17:30:53"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:53"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:53"
    ],
    [
        395,
        "co2-collection",
        "05/09/2024 17:30:54"
    ],
    [
        394,
        "co2-collection",
        "05/09/2024 17:30:54"
    ],
    [
        15,
        "dist-collection",
        "05/09/2024 17:30:54"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:54"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:54"
    ],
    [
        570,
        "luz-collection",
        "05/09/2024 17:30:54"
    ],
    [
        623,
        "luz-collection",
        "05/09/2024 17:30:54"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:54"
    ],
    [
        394,
        "co2-collection",
        "05/09/2024 17:30:55"
    ],
    [
        16,
        "dist-collection",
        "05/09/2024 17:30:55"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:55"
    ],
    [
        77,
        "hum-collection",
        "05/09/2024 17:30:55"
    ],
    [
        616,
        "luz-collection",
        "05/09/2024 17:30:55"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:55"
    ],
    [
        24.1,
        "temp-collection",
        "05/09/2024 17:30:55"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:04:50"
    ],
    [
        892,
        "luz-collection",
        "06/09/2024 00:04:50"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:04:50"
    ],
    [
        367,
        "co2-collection",
        "06/09/2024 00:04:51"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 00:04:51"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:04:51"
    ],
    [
        367,
        "co2-collection",
        "06/09/2024 00:04:52"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:04:52"
    ],
    [
        82,
        "hum-collection",
        "06/09/2024 00:04:52"
    ],
    [
        572,
        "luz-collection",
        "06/09/2024 00:04:52"
    ],
    [
        629,
        "luz-collection",
        "06/09/2024 00:04:52"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:04:52"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:04:52"
    ],
    [
        366,
        "co2-collection",
        "06/09/2024 00:04:53"
    ],
    [
        366,
        "co2-collection",
        "06/09/2024 00:04:53"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:04:53"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:04:53"
    ],
    [
        82,
        "hum-collection",
        "06/09/2024 00:04:53"
    ],
    [
        82,
        "hum-collection",
        "06/09/2024 00:04:53"
    ],
    [
        554,
        "luz-collection",
        "06/09/2024 00:04:53"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:04:53"
    ],
    [
        366,
        "co2-collection",
        "06/09/2024 00:04:54"
    ],
    [
        366,
        "co2-collection",
        "06/09/2024 00:04:54"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:04:54"
    ],
    [
        82,
        "hum-collection",
        "06/09/2024 00:04:54"
    ],
    [
        625,
        "luz-collection",
        "06/09/2024 00:04:54"
    ],
    [
        588,
        "luz-collection",
        "06/09/2024 00:04:54"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:04:54"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:04:54"
    ],
    [
        363,
        "co2-collection",
        "06/09/2024 00:04:55"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:04:55"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:04:55"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:04:55"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:04:55"
    ],
    [
        564,
        "luz-collection",
        "06/09/2024 00:04:55"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:04:55"
    ],
    [
        362,
        "co2-collection",
        "06/09/2024 00:04:56"
    ],
    [
        362,
        "co2-collection",
        "06/09/2024 00:04:56"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:04:56"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:04:56"
    ],
    [
        622,
        "luz-collection",
        "06/09/2024 00:04:56"
    ],
    [
        587,
        "luz-collection",
        "06/09/2024 00:04:56"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:04:56"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:04:56"
    ],
    [
        371,
        "co2-collection",
        "06/09/2024 00:04:57"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:04:57"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:04:57"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:04:57"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:04:57"
    ],
    [
        552,
        "luz-collection",
        "06/09/2024 00:04:57"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:04:57"
    ],
    [
        370,
        "co2-collection",
        "06/09/2024 00:04:58"
    ],
    [
        369,
        "co2-collection",
        "06/09/2024 00:04:58"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:04:58"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:04:58"
    ],
    [
        627,
        "luz-collection",
        "06/09/2024 00:04:58"
    ],
    [
        562,
        "luz-collection",
        "06/09/2024 00:04:58"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:04:58"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:04:58"
    ],
    [
        370,
        "co2-collection",
        "06/09/2024 00:04:59"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:04:59"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:04:59"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:04:59"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:04:59"
    ],
    [
        600,
        "luz-collection",
        "06/09/2024 00:04:59"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:04:59"
    ],
    [
        370,
        "co2-collection",
        "06/09/2024 00:05:00"
    ],
    [
        377,
        "co2-collection",
        "06/09/2024 00:05:00"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:00"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:00"
    ],
    [
        570,
        "luz-collection",
        "06/09/2024 00:05:00"
    ],
    [
        631,
        "luz-collection",
        "06/09/2024 00:05:00"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:00"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:00"
    ],
    [
        366,
        "co2-collection",
        "06/09/2024 00:05:01"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:01"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:01"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:01"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:01"
    ],
    [
        613,
        "luz-collection",
        "06/09/2024 00:05:01"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:01"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:01"
    ],
    [
        372,
        "co2-collection",
        "06/09/2024 00:05:02"
    ],
    [
        377,
        "co2-collection",
        "06/09/2024 00:05:02"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:02"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:02"
    ],
    [
        551,
        "luz-collection",
        "06/09/2024 00:05:02"
    ],
    [
        575,
        "luz-collection",
        "06/09/2024 00:05:02"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:02"
    ],
    [
        369,
        "co2-collection",
        "06/09/2024 00:05:03"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:03"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:03"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:03"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:03"
    ],
    [
        618,
        "luz-collection",
        "06/09/2024 00:05:03"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:03"
    ],
    [
        373,
        "co2-collection",
        "06/09/2024 00:05:04"
    ],
    [
        363,
        "co2-collection",
        "06/09/2024 00:05:04"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:04"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:04"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:04"
    ],
    [
        577,
        "luz-collection",
        "06/09/2024 00:05:04"
    ],
    [
        616,
        "luz-collection",
        "06/09/2024 00:05:04"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:04"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:04"
    ],
    [
        364,
        "co2-collection",
        "06/09/2024 00:05:05"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:05"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:05"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:05"
    ],
    [
        628,
        "luz-collection",
        "06/09/2024 00:05:05"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:05"
    ],
    [
        364,
        "co2-collection",
        "06/09/2024 00:05:06"
    ],
    [
        362,
        "co2-collection",
        "06/09/2024 00:05:06"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:06"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:06"
    ],
    [
        585,
        "luz-collection",
        "06/09/2024 00:05:06"
    ],
    [
        595,
        "luz-collection",
        "06/09/2024 00:05:06"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:06"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:06"
    ],
    [
        362,
        "co2-collection",
        "06/09/2024 00:05:07"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:07"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:07"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:07"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:07"
    ],
    [
        558,
        "luz-collection",
        "06/09/2024 00:05:07"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:07"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:07"
    ],
    [
        366,
        "co2-collection",
        "06/09/2024 00:05:08"
    ],
    [
        360,
        "co2-collection",
        "06/09/2024 00:05:08"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:08"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:08"
    ],
    [
        606,
        "luz-collection",
        "06/09/2024 00:05:08"
    ],
    [
        556,
        "luz-collection",
        "06/09/2024 00:05:08"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:08"
    ],
    [
        362,
        "co2-collection",
        "06/09/2024 00:05:09"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:09"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:09"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:09"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:09"
    ],
    [
        598,
        "luz-collection",
        "06/09/2024 00:05:09"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:09"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:09"
    ],
    [
        372,
        "co2-collection",
        "06/09/2024 00:05:10"
    ],
    [
        374,
        "co2-collection",
        "06/09/2024 00:05:10"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:10"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:10"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:10"
    ],
    [
        618,
        "luz-collection",
        "06/09/2024 00:05:10"
    ],
    [
        632,
        "luz-collection",
        "06/09/2024 00:05:10"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:10"
    ],
    [
        369,
        "co2-collection",
        "06/09/2024 00:05:11"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:11"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:11"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:11"
    ],
    [
        608,
        "luz-collection",
        "06/09/2024 00:05:11"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:11"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:11"
    ],
    [
        368,
        "co2-collection",
        "06/09/2024 00:05:12"
    ],
    [
        369,
        "co2-collection",
        "06/09/2024 00:05:12"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:12"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:12"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:12"
    ],
    [
        565,
        "luz-collection",
        "06/09/2024 00:05:12"
    ],
    [
        556,
        "luz-collection",
        "06/09/2024 00:05:12"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:12"
    ],
    [
        368,
        "co2-collection",
        "06/09/2024 00:05:13"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:13"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:13"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:13"
    ],
    [
        593,
        "luz-collection",
        "06/09/2024 00:05:13"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:13"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:13"
    ],
    [
        369,
        "co2-collection",
        "06/09/2024 00:05:14"
    ],
    [
        369,
        "co2-collection",
        "06/09/2024 00:05:14"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:14"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:14"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:14"
    ],
    [
        566,
        "luz-collection",
        "06/09/2024 00:05:14"
    ],
    [
        632,
        "luz-collection",
        "06/09/2024 00:05:14"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:14"
    ],
    [
        368,
        "co2-collection",
        "06/09/2024 00:05:15"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:15"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:15"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:15"
    ],
    [
        604,
        "luz-collection",
        "06/09/2024 00:05:15"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:15"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:15"
    ],
    [
        368,
        "co2-collection",
        "06/09/2024 00:05:16"
    ],
    [
        369,
        "co2-collection",
        "06/09/2024 00:05:16"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:16"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:16"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:16"
    ],
    [
        560,
        "luz-collection",
        "06/09/2024 00:05:16"
    ],
    [
        631,
        "luz-collection",
        "06/09/2024 00:05:16"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:16"
    ],
    [
        371,
        "co2-collection",
        "06/09/2024 00:05:17"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:17"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:17"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:17"
    ],
    [
        570,
        "luz-collection",
        "06/09/2024 00:05:17"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:17"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:17"
    ],
    [
        367,
        "co2-collection",
        "06/09/2024 00:05:18"
    ],
    [
        369,
        "co2-collection",
        "06/09/2024 00:05:18"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:18"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:18"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:18"
    ],
    [
        617,
        "luz-collection",
        "06/09/2024 00:05:18"
    ],
    [
        629,
        "luz-collection",
        "06/09/2024 00:05:18"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:18"
    ],
    [
        365,
        "co2-collection",
        "06/09/2024 00:05:19"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:19"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:19"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:19"
    ],
    [
        598,
        "luz-collection",
        "06/09/2024 00:05:19"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:19"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:19"
    ],
    [
        363,
        "co2-collection",
        "06/09/2024 00:05:20"
    ],
    [
        358,
        "co2-collection",
        "06/09/2024 00:05:20"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:20"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:20"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:20"
    ],
    [
        554,
        "luz-collection",
        "06/09/2024 00:05:20"
    ],
    [
        580,
        "luz-collection",
        "06/09/2024 00:05:20"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:20"
    ],
    [
        359,
        "co2-collection",
        "06/09/2024 00:05:21"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:21"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:21"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:21"
    ],
    [
        587,
        "luz-collection",
        "06/09/2024 00:05:21"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:21"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:21"
    ],
    [
        358,
        "co2-collection",
        "06/09/2024 00:05:22"
    ],
    [
        358,
        "co2-collection",
        "06/09/2024 00:05:22"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:22"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:22"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:22"
    ],
    [
        634,
        "luz-collection",
        "06/09/2024 00:05:22"
    ],
    [
        574,
        "luz-collection",
        "06/09/2024 00:05:22"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:22"
    ],
    [
        358,
        "co2-collection",
        "06/09/2024 00:05:23"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:23"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:23"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:23"
    ],
    [
        616,
        "luz-collection",
        "06/09/2024 00:05:23"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:23"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:23"
    ],
    [
        358,
        "co2-collection",
        "06/09/2024 00:05:24"
    ],
    [
        359,
        "co2-collection",
        "06/09/2024 00:05:24"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:24"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:24"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:24"
    ],
    [
        635,
        "luz-collection",
        "06/09/2024 00:05:24"
    ],
    [
        573,
        "luz-collection",
        "06/09/2024 00:05:24"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:24"
    ],
    [
        357,
        "co2-collection",
        "06/09/2024 00:05:25"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:25"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:25"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:25"
    ],
    [
        561,
        "luz-collection",
        "06/09/2024 00:05:25"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:25"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:25"
    ],
    [
        361,
        "co2-collection",
        "06/09/2024 00:05:26"
    ],
    [
        359,
        "co2-collection",
        "06/09/2024 00:05:26"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:26"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:26"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:26"
    ],
    [
        635,
        "luz-collection",
        "06/09/2024 00:05:26"
    ],
    [
        604,
        "luz-collection",
        "06/09/2024 00:05:26"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:26"
    ],
    [
        359,
        "co2-collection",
        "06/09/2024 00:05:27"
    ],
    [
        8,
        "dist-collection",
        "06/09/2024 00:05:27"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:27"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:27"
    ],
    [
        584,
        "luz-collection",
        "06/09/2024 00:05:27"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:27"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:27"
    ],
    [
        378,
        "co2-collection",
        "06/09/2024 00:05:28"
    ],
    [
        375,
        "co2-collection",
        "06/09/2024 00:05:28"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:28"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:28"
    ],
    [
        560,
        "luz-collection",
        "06/09/2024 00:05:28"
    ],
    [
        600,
        "luz-collection",
        "06/09/2024 00:05:28"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:28"
    ],
    [
        374,
        "co2-collection",
        "06/09/2024 00:05:29"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:29"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:29"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:29"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:29"
    ],
    [
        564,
        "luz-collection",
        "06/09/2024 00:05:29"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:29"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:29"
    ],
    [
        372,
        "co2-collection",
        "06/09/2024 00:05:30"
    ],
    [
        371,
        "co2-collection",
        "06/09/2024 00:05:30"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:30"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:30"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:30"
    ],
    [
        600,
        "luz-collection",
        "06/09/2024 00:05:30"
    ],
    [
        617,
        "luz-collection",
        "06/09/2024 00:05:30"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:30"
    ],
    [
        372,
        "co2-collection",
        "06/09/2024 00:05:31"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:31"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:31"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:31"
    ],
    [
        633,
        "luz-collection",
        "06/09/2024 00:05:31"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:31"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:31"
    ],
    [
        361,
        "co2-collection",
        "06/09/2024 00:05:32"
    ],
    [
        365,
        "co2-collection",
        "06/09/2024 00:05:32"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:32"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:32"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:32"
    ],
    [
        601,
        "luz-collection",
        "06/09/2024 00:05:32"
    ],
    [
        629,
        "luz-collection",
        "06/09/2024 00:05:32"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:32"
    ],
    [
        361,
        "co2-collection",
        "06/09/2024 00:05:33"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:33"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:33"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:33"
    ],
    [
        555,
        "luz-collection",
        "06/09/2024 00:05:33"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:33"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:33"
    ],
    [
        361,
        "co2-collection",
        "06/09/2024 00:05:34"
    ],
    [
        361,
        "co2-collection",
        "06/09/2024 00:05:34"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:34"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:34"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:34"
    ],
    [
        609,
        "luz-collection",
        "06/09/2024 00:05:34"
    ],
    [
        568,
        "luz-collection",
        "06/09/2024 00:05:34"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:34"
    ],
    [
        360,
        "co2-collection",
        "06/09/2024 00:05:35"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:35"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:35"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:35"
    ],
    [
        568,
        "luz-collection",
        "06/09/2024 00:05:35"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:35"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:35"
    ],
    [
        361,
        "co2-collection",
        "06/09/2024 00:05:36"
    ],
    [
        360,
        "co2-collection",
        "06/09/2024 00:05:36"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:36"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 00:05:36"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:36"
    ],
    [
        633,
        "luz-collection",
        "06/09/2024 00:05:36"
    ],
    [
        612,
        "luz-collection",
        "06/09/2024 00:05:36"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:36"
    ],
    [
        360,
        "co2-collection",
        "06/09/2024 00:05:37"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:37"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:37"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:37"
    ],
    [
        569,
        "luz-collection",
        "06/09/2024 00:05:37"
    ],
    [
        637,
        "luz-collection",
        "06/09/2024 00:05:37"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:37"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:37"
    ],
    [
        356,
        "co2-collection",
        "06/09/2024 00:05:38"
    ],
    [
        357,
        "co2-collection",
        "06/09/2024 00:05:38"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:38"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:38"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:38"
    ],
    [
        562,
        "luz-collection",
        "06/09/2024 00:05:38"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:38"
    ],
    [
        356,
        "co2-collection",
        "06/09/2024 00:05:39"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:39"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:39"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:39"
    ],
    [
        604,
        "luz-collection",
        "06/09/2024 00:05:39"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:39"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:39"
    ],
    [
        356,
        "co2-collection",
        "06/09/2024 00:05:40"
    ],
    [
        359,
        "co2-collection",
        "06/09/2024 00:05:40"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:40"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:40"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:40"
    ],
    [
        637,
        "luz-collection",
        "06/09/2024 00:05:40"
    ],
    [
        582,
        "luz-collection",
        "06/09/2024 00:05:40"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:40"
    ],
    [
        360,
        "co2-collection",
        "06/09/2024 00:05:41"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:41"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:41"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:41"
    ],
    [
        602,
        "luz-collection",
        "06/09/2024 00:05:41"
    ],
    [
        559,
        "luz-collection",
        "06/09/2024 00:05:41"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:41"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:41"
    ],
    [
        354,
        "co2-collection",
        "06/09/2024 00:05:42"
    ],
    [
        352,
        "co2-collection",
        "06/09/2024 00:05:42"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 00:05:42"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:42"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:42"
    ],
    [
        564,
        "luz-collection",
        "06/09/2024 00:05:42"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:42"
    ],
    [
        357,
        "co2-collection",
        "06/09/2024 00:05:43"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 00:05:43"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:43"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:43"
    ],
    [
        595,
        "luz-collection",
        "06/09/2024 00:05:43"
    ],
    [
        607,
        "luz-collection",
        "06/09/2024 00:05:43"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:43"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:43"
    ],
    [
        359,
        "co2-collection",
        "06/09/2024 00:05:44"
    ],
    [
        358,
        "co2-collection",
        "06/09/2024 00:05:44"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:44"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 00:05:44"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:44"
    ],
    [
        628,
        "luz-collection",
        "06/09/2024 00:05:44"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:44"
    ],
    [
        354,
        "co2-collection",
        "06/09/2024 00:05:45"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:45"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:45"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:45"
    ],
    [
        625,
        "luz-collection",
        "06/09/2024 00:05:45"
    ],
    [
        611,
        "luz-collection",
        "06/09/2024 00:05:45"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:45"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:45"
    ],
    [
        354,
        "co2-collection",
        "06/09/2024 00:05:46"
    ],
    [
        359,
        "co2-collection",
        "06/09/2024 00:05:46"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:46"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:46"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:46"
    ],
    [
        565,
        "luz-collection",
        "06/09/2024 00:05:46"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:46"
    ],
    [
        363,
        "co2-collection",
        "06/09/2024 00:05:47"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:47"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:47"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:47"
    ],
    [
        560,
        "luz-collection",
        "06/09/2024 00:05:47"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:47"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:47"
    ],
    [
        361,
        "co2-collection",
        "06/09/2024 00:05:48"
    ],
    [
        363,
        "co2-collection",
        "06/09/2024 00:05:48"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:48"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:48"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:48"
    ],
    [
        568,
        "luz-collection",
        "06/09/2024 00:05:48"
    ],
    [
        605,
        "luz-collection",
        "06/09/2024 00:05:48"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:48"
    ],
    [
        363,
        "co2-collection",
        "06/09/2024 00:05:49"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:49"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:49"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:49"
    ],
    [
        589,
        "luz-collection",
        "06/09/2024 00:05:49"
    ],
    [
        630,
        "luz-collection",
        "06/09/2024 00:05:49"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:49"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:49"
    ],
    [
        359,
        "co2-collection",
        "06/09/2024 00:05:50"
    ],
    [
        361,
        "co2-collection",
        "06/09/2024 00:05:50"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:50"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:50"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:50"
    ],
    [
        554,
        "luz-collection",
        "06/09/2024 00:05:50"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:50"
    ],
    [
        362,
        "co2-collection",
        "06/09/2024 00:05:51"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:51"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:51"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:51"
    ],
    [
        620,
        "luz-collection",
        "06/09/2024 00:05:51"
    ],
    [
        594,
        "luz-collection",
        "06/09/2024 00:05:51"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:51"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:51"
    ],
    [
        359,
        "co2-collection",
        "06/09/2024 00:05:52"
    ],
    [
        360,
        "co2-collection",
        "06/09/2024 00:05:52"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:52"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:52"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:52"
    ],
    [
        634,
        "luz-collection",
        "06/09/2024 00:05:52"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:52"
    ],
    [
        359,
        "co2-collection",
        "06/09/2024 00:05:53"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:53"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:53"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:53"
    ],
    [
        618,
        "luz-collection",
        "06/09/2024 00:05:53"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:53"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:53"
    ],
    [
        360,
        "co2-collection",
        "06/09/2024 00:05:54"
    ],
    [
        359,
        "co2-collection",
        "06/09/2024 00:05:54"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:54"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:54"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:54"
    ],
    [
        563,
        "luz-collection",
        "06/09/2024 00:05:54"
    ],
    [
        617,
        "luz-collection",
        "06/09/2024 00:05:54"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:54"
    ],
    [
        359,
        "co2-collection",
        "06/09/2024 00:05:55"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:55"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:55"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:55"
    ],
    [
        603,
        "luz-collection",
        "06/09/2024 00:05:55"
    ],
    [
        561,
        "luz-collection",
        "06/09/2024 00:05:55"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:55"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:55"
    ],
    [
        359,
        "co2-collection",
        "06/09/2024 00:05:56"
    ],
    [
        362,
        "co2-collection",
        "06/09/2024 00:05:56"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:56"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:56"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:56"
    ],
    [
        568,
        "luz-collection",
        "06/09/2024 00:05:56"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:56"
    ],
    [
        364,
        "co2-collection",
        "06/09/2024 00:05:57"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:57"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:57"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:57"
    ],
    [
        635,
        "luz-collection",
        "06/09/2024 00:05:57"
    ],
    [
        600,
        "luz-collection",
        "06/09/2024 00:05:57"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:57"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:57"
    ],
    [
        362,
        "co2-collection",
        "06/09/2024 00:05:58"
    ],
    [
        356,
        "co2-collection",
        "06/09/2024 00:05:58"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:58"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:58"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:58"
    ],
    [
        559,
        "luz-collection",
        "06/09/2024 00:05:58"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:58"
    ],
    [
        359,
        "co2-collection",
        "06/09/2024 00:05:59"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:05:59"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:59"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:05:59"
    ],
    [
        635,
        "luz-collection",
        "06/09/2024 00:05:59"
    ],
    [
        576,
        "luz-collection",
        "06/09/2024 00:05:59"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:59"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:05:59"
    ],
    [
        360,
        "co2-collection",
        "06/09/2024 00:06:00"
    ],
    [
        359,
        "co2-collection",
        "06/09/2024 00:06:00"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:00"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:00"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:06:00"
    ],
    [
        622,
        "luz-collection",
        "06/09/2024 00:06:00"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:00"
    ],
    [
        362,
        "co2-collection",
        "06/09/2024 00:06:01"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:01"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:06:01"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:06:01"
    ],
    [
        632,
        "luz-collection",
        "06/09/2024 00:06:01"
    ],
    [
        602,
        "luz-collection",
        "06/09/2024 00:06:01"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:01"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:01"
    ],
    [
        362,
        "co2-collection",
        "06/09/2024 00:06:02"
    ],
    [
        361,
        "co2-collection",
        "06/09/2024 00:06:02"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:02"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:02"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:06:02"
    ],
    [
        583,
        "luz-collection",
        "06/09/2024 00:06:02"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:02"
    ],
    [
        360,
        "co2-collection",
        "06/09/2024 00:06:03"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:03"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:06:03"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:06:03"
    ],
    [
        558,
        "luz-collection",
        "06/09/2024 00:06:03"
    ],
    [
        594,
        "luz-collection",
        "06/09/2024 00:06:03"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:03"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:03"
    ],
    [
        363,
        "co2-collection",
        "06/09/2024 00:06:04"
    ],
    [
        363,
        "co2-collection",
        "06/09/2024 00:06:04"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:04"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:04"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:06:04"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:06:04"
    ],
    [
        583,
        "luz-collection",
        "06/09/2024 00:06:04"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:04"
    ],
    [
        358,
        "co2-collection",
        "06/09/2024 00:06:05"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:05"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:06:05"
    ],
    [
        641,
        "luz-collection",
        "06/09/2024 00:06:05"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:05"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:05"
    ],
    [
        356,
        "co2-collection",
        "06/09/2024 00:06:06"
    ],
    [
        358,
        "co2-collection",
        "06/09/2024 00:06:06"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:06"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:06"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:06:06"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:06:06"
    ],
    [
        576,
        "luz-collection",
        "06/09/2024 00:06:06"
    ],
    [
        621,
        "luz-collection",
        "06/09/2024 00:06:06"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:06"
    ],
    [
        360,
        "co2-collection",
        "06/09/2024 00:06:07"
    ],
    [
        361,
        "co2-collection",
        "06/09/2024 00:06:07"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:07"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:06:07"
    ],
    [
        569,
        "luz-collection",
        "06/09/2024 00:06:07"
    ],
    [
        643,
        "luz-collection",
        "06/09/2024 00:06:07"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:07"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:07"
    ],
    [
        359,
        "co2-collection",
        "06/09/2024 00:06:08"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:08"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:08"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:06:08"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:06:08"
    ],
    [
        611,
        "luz-collection",
        "06/09/2024 00:06:08"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:08"
    ],
    [
        361,
        "co2-collection",
        "06/09/2024 00:06:09"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:09"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:06:09"
    ],
    [
        593,
        "luz-collection",
        "06/09/2024 00:06:09"
    ],
    [
        638,
        "luz-collection",
        "06/09/2024 00:06:09"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:09"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:09"
    ],
    [
        361,
        "co2-collection",
        "06/09/2024 00:06:10"
    ],
    [
        358,
        "co2-collection",
        "06/09/2024 00:06:10"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:10"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:10"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:06:10"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:06:10"
    ],
    [
        599,
        "luz-collection",
        "06/09/2024 00:06:10"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:10"
    ],
    [
        360,
        "co2-collection",
        "06/09/2024 00:06:11"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:11"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:06:11"
    ],
    [
        572,
        "luz-collection",
        "06/09/2024 00:06:11"
    ],
    [
        559,
        "luz-collection",
        "06/09/2024 00:06:11"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:11"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:11"
    ],
    [
        359,
        "co2-collection",
        "06/09/2024 00:06:12"
    ],
    [
        358,
        "co2-collection",
        "06/09/2024 00:06:12"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:12"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:12"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:06:12"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:06:12"
    ],
    [
        595,
        "luz-collection",
        "06/09/2024 00:06:12"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:12"
    ],
    [
        358,
        "co2-collection",
        "06/09/2024 00:06:13"
    ],
    [
        358,
        "co2-collection",
        "06/09/2024 00:06:13"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:13"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:06:13"
    ],
    [
        632,
        "luz-collection",
        "06/09/2024 00:06:13"
    ],
    [
        626,
        "luz-collection",
        "06/09/2024 00:06:13"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:13"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:13"
    ],
    [
        360,
        "co2-collection",
        "06/09/2024 00:06:14"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:14"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:14"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:06:14"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:06:14"
    ],
    [
        594,
        "luz-collection",
        "06/09/2024 00:06:14"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:14"
    ],
    [
        361,
        "co2-collection",
        "06/09/2024 00:06:15"
    ],
    [
        8,
        "dist-collection",
        "06/09/2024 00:06:15"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:06:15"
    ],
    [
        638,
        "luz-collection",
        "06/09/2024 00:06:15"
    ],
    [
        556,
        "luz-collection",
        "06/09/2024 00:06:15"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:15"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:15"
    ],
    [
        354,
        "co2-collection",
        "06/09/2024 00:06:16"
    ],
    [
        358,
        "co2-collection",
        "06/09/2024 00:06:16"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:16"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:16"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:06:16"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:06:16"
    ],
    [
        583,
        "luz-collection",
        "06/09/2024 00:06:16"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:16"
    ],
    [
        354,
        "co2-collection",
        "06/09/2024 00:06:17"
    ],
    [
        355,
        "co2-collection",
        "06/09/2024 00:06:17"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:17"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:06:17"
    ],
    [
        625,
        "luz-collection",
        "06/09/2024 00:06:17"
    ],
    [
        572,
        "luz-collection",
        "06/09/2024 00:06:17"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:17"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:17"
    ],
    [
        355,
        "co2-collection",
        "06/09/2024 00:06:18"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:18"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:18"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:06:18"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:06:18"
    ],
    [
        626,
        "luz-collection",
        "06/09/2024 00:06:18"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:18"
    ],
    [
        356,
        "co2-collection",
        "06/09/2024 00:06:19"
    ],
    [
        354,
        "co2-collection",
        "06/09/2024 00:06:19"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:19"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:06:19"
    ],
    [
        557,
        "luz-collection",
        "06/09/2024 00:06:19"
    ],
    [
        584,
        "luz-collection",
        "06/09/2024 00:06:19"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:19"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:19"
    ],
    [
        352,
        "co2-collection",
        "06/09/2024 00:06:20"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:20"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:20"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:06:20"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:06:20"
    ],
    [
        619,
        "luz-collection",
        "06/09/2024 00:06:20"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:20"
    ],
    [
        357,
        "co2-collection",
        "06/09/2024 00:06:21"
    ],
    [
        357,
        "co2-collection",
        "06/09/2024 00:06:21"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:21"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:06:21"
    ],
    [
        634,
        "luz-collection",
        "06/09/2024 00:06:21"
    ],
    [
        594,
        "luz-collection",
        "06/09/2024 00:06:21"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:21"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:21"
    ],
    [
        359,
        "co2-collection",
        "06/09/2024 00:06:22"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:22"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:22"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:06:22"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:06:22"
    ],
    [
        623,
        "luz-collection",
        "06/09/2024 00:06:22"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:22"
    ],
    [
        360,
        "co2-collection",
        "06/09/2024 00:06:23"
    ],
    [
        357,
        "co2-collection",
        "06/09/2024 00:06:23"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:23"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:06:23"
    ],
    [
        571,
        "luz-collection",
        "06/09/2024 00:06:23"
    ],
    [
        611,
        "luz-collection",
        "06/09/2024 00:06:23"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:23"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:23"
    ],
    [
        350,
        "co2-collection",
        "06/09/2024 00:06:24"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:24"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:24"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:06:24"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:06:24"
    ],
    [
        559,
        "luz-collection",
        "06/09/2024 00:06:24"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:24"
    ],
    [
        356,
        "co2-collection",
        "06/09/2024 00:06:25"
    ],
    [
        355,
        "co2-collection",
        "06/09/2024 00:06:25"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:25"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:06:25"
    ],
    [
        573,
        "luz-collection",
        "06/09/2024 00:06:25"
    ],
    [
        597,
        "luz-collection",
        "06/09/2024 00:06:25"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:25"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:25"
    ],
    [
        354,
        "co2-collection",
        "06/09/2024 00:06:26"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:26"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:26"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:06:26"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:06:26"
    ],
    [
        637,
        "luz-collection",
        "06/09/2024 00:06:26"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:26"
    ],
    [
        357,
        "co2-collection",
        "06/09/2024 00:06:27"
    ],
    [
        359,
        "co2-collection",
        "06/09/2024 00:06:27"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:27"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:06:27"
    ],
    [
        572,
        "luz-collection",
        "06/09/2024 00:06:27"
    ],
    [
        615,
        "luz-collection",
        "06/09/2024 00:06:27"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:27"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:27"
    ],
    [
        356,
        "co2-collection",
        "06/09/2024 00:06:28"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:28"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:28"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:06:28"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:06:28"
    ],
    [
        637,
        "luz-collection",
        "06/09/2024 00:06:28"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:28"
    ],
    [
        359,
        "co2-collection",
        "06/09/2024 00:06:29"
    ],
    [
        357,
        "co2-collection",
        "06/09/2024 00:06:29"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:29"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:06:29"
    ],
    [
        561,
        "luz-collection",
        "06/09/2024 00:06:29"
    ],
    [
        601,
        "luz-collection",
        "06/09/2024 00:06:29"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:29"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:29"
    ],
    [
        358,
        "co2-collection",
        "06/09/2024 00:06:30"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:30"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:30"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:06:30"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:06:30"
    ],
    [
        635,
        "luz-collection",
        "06/09/2024 00:06:30"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:30"
    ],
    [
        359,
        "co2-collection",
        "06/09/2024 00:06:31"
    ],
    [
        359,
        "co2-collection",
        "06/09/2024 00:06:31"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:31"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:06:31"
    ],
    [
        611,
        "luz-collection",
        "06/09/2024 00:06:31"
    ],
    [
        577,
        "luz-collection",
        "06/09/2024 00:06:31"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:31"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:31"
    ],
    [
        354,
        "co2-collection",
        "06/09/2024 00:06:32"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:32"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:32"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:06:32"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:06:32"
    ],
    [
        571,
        "luz-collection",
        "06/09/2024 00:06:32"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:32"
    ],
    [
        361,
        "co2-collection",
        "06/09/2024 00:06:33"
    ],
    [
        363,
        "co2-collection",
        "06/09/2024 00:06:33"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:33"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:06:33"
    ],
    [
        559,
        "luz-collection",
        "06/09/2024 00:06:33"
    ],
    [
        612,
        "luz-collection",
        "06/09/2024 00:06:33"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:33"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:33"
    ],
    [
        362,
        "co2-collection",
        "06/09/2024 00:06:34"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:34"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:34"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:06:34"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:06:34"
    ],
    [
        602,
        "luz-collection",
        "06/09/2024 00:06:34"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:34"
    ],
    [
        363,
        "co2-collection",
        "06/09/2024 00:06:35"
    ],
    [
        359,
        "co2-collection",
        "06/09/2024 00:06:35"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:35"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:06:35"
    ],
    [
        623,
        "luz-collection",
        "06/09/2024 00:06:35"
    ],
    [
        636,
        "luz-collection",
        "06/09/2024 00:06:35"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:35"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:35"
    ],
    [
        362,
        "co2-collection",
        "06/09/2024 00:06:36"
    ],
    [
        8,
        "dist-collection",
        "06/09/2024 00:06:36"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:36"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:06:36"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:06:36"
    ],
    [
        611,
        "luz-collection",
        "06/09/2024 00:06:36"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:36"
    ],
    [
        360,
        "co2-collection",
        "06/09/2024 00:06:37"
    ],
    [
        362,
        "co2-collection",
        "06/09/2024 00:06:37"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:37"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:06:37"
    ],
    [
        576,
        "luz-collection",
        "06/09/2024 00:06:37"
    ],
    [
        557,
        "luz-collection",
        "06/09/2024 00:06:37"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:37"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:37"
    ],
    [
        360,
        "co2-collection",
        "06/09/2024 00:06:38"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:38"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:38"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:06:38"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:06:38"
    ],
    [
        587,
        "luz-collection",
        "06/09/2024 00:06:38"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:38"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:38"
    ],
    [
        362,
        "co2-collection",
        "06/09/2024 00:06:39"
    ],
    [
        361,
        "co2-collection",
        "06/09/2024 00:06:39"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:39"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:06:39"
    ],
    [
        634,
        "luz-collection",
        "06/09/2024 00:06:39"
    ],
    [
        584,
        "luz-collection",
        "06/09/2024 00:06:39"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:39"
    ],
    [
        357,
        "co2-collection",
        "06/09/2024 00:06:40"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:40"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:40"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:06:40"
    ],
    [
        84,
        "hum-collection",
        "06/09/2024 00:06:40"
    ],
    [
        627,
        "luz-collection",
        "06/09/2024 00:06:40"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:40"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:40"
    ],
    [
        357,
        "co2-collection",
        "06/09/2024 00:06:41"
    ],
    [
        355,
        "co2-collection",
        "06/09/2024 00:06:41"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:41"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:06:41"
    ],
    [
        588,
        "luz-collection",
        "06/09/2024 00:06:41"
    ],
    [
        639,
        "luz-collection",
        "06/09/2024 00:06:41"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:41"
    ],
    [
        355,
        "co2-collection",
        "06/09/2024 00:06:42"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:42"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:42"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:06:42"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:06:42"
    ],
    [
        556,
        "luz-collection",
        "06/09/2024 00:06:42"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:42"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:42"
    ],
    [
        357,
        "co2-collection",
        "06/09/2024 00:06:43"
    ],
    [
        355,
        "co2-collection",
        "06/09/2024 00:06:43"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:43"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:06:43"
    ],
    [
        582,
        "luz-collection",
        "06/09/2024 00:06:43"
    ],
    [
        622,
        "luz-collection",
        "06/09/2024 00:06:43"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:43"
    ],
    [
        357,
        "co2-collection",
        "06/09/2024 00:06:44"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:44"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:44"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:06:44"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:06:44"
    ],
    [
        572,
        "luz-collection",
        "06/09/2024 00:06:44"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:44"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:44"
    ],
    [
        357,
        "co2-collection",
        "06/09/2024 00:06:45"
    ],
    [
        361,
        "co2-collection",
        "06/09/2024 00:06:45"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:45"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:45"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:06:45"
    ],
    [
        629,
        "luz-collection",
        "06/09/2024 00:06:45"
    ],
    [
        588,
        "luz-collection",
        "06/09/2024 00:06:45"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:45"
    ],
    [
        358,
        "co2-collection",
        "06/09/2024 00:06:46"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:46"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:06:46"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:06:46"
    ],
    [
        555,
        "luz-collection",
        "06/09/2024 00:06:46"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:46"
    ],
    [
        357,
        "co2-collection",
        "06/09/2024 00:06:47"
    ],
    [
        351,
        "co2-collection",
        "06/09/2024 00:06:47"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:47"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:06:47"
    ],
    [
        587,
        "luz-collection",
        "06/09/2024 00:06:47"
    ],
    [
        627,
        "luz-collection",
        "06/09/2024 00:06:47"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:47"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:47"
    ],
    [
        355,
        "co2-collection",
        "06/09/2024 00:06:48"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:48"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:48"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:06:48"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:06:48"
    ],
    [
        628,
        "luz-collection",
        "06/09/2024 00:06:48"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:48"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:48"
    ],
    [
        355,
        "co2-collection",
        "06/09/2024 00:06:49"
    ],
    [
        352,
        "co2-collection",
        "06/09/2024 00:06:49"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:49"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:49"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:06:49"
    ],
    [
        606,
        "luz-collection",
        "06/09/2024 00:06:49"
    ],
    [
        629,
        "luz-collection",
        "06/09/2024 00:06:49"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:49"
    ],
    [
        354,
        "co2-collection",
        "06/09/2024 00:06:50"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:50"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:06:50"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:06:50"
    ],
    [
        579,
        "luz-collection",
        "06/09/2024 00:06:50"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:50"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:50"
    ],
    [
        353,
        "co2-collection",
        "06/09/2024 00:06:51"
    ],
    [
        354,
        "co2-collection",
        "06/09/2024 00:06:51"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:51"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:51"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:06:51"
    ],
    [
        557,
        "luz-collection",
        "06/09/2024 00:06:51"
    ],
    [
        592,
        "luz-collection",
        "06/09/2024 00:06:51"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:51"
    ],
    [
        352,
        "co2-collection",
        "06/09/2024 00:06:52"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:52"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:06:52"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:06:52"
    ],
    [
        576,
        "luz-collection",
        "06/09/2024 00:06:52"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:52"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:52"
    ],
    [
        350,
        "co2-collection",
        "06/09/2024 00:06:53"
    ],
    [
        349,
        "co2-collection",
        "06/09/2024 00:06:53"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:53"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:53"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:06:53"
    ],
    [
        638,
        "luz-collection",
        "06/09/2024 00:06:53"
    ],
    [
        614,
        "luz-collection",
        "06/09/2024 00:06:53"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:53"
    ],
    [
        353,
        "co2-collection",
        "06/09/2024 00:06:54"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:54"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:06:54"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:06:54"
    ],
    [
        571,
        "luz-collection",
        "06/09/2024 00:06:54"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:54"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:54"
    ],
    [
        356,
        "co2-collection",
        "06/09/2024 00:06:55"
    ],
    [
        356,
        "co2-collection",
        "06/09/2024 00:06:55"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:55"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:55"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:06:55"
    ],
    [
        639,
        "luz-collection",
        "06/09/2024 00:06:55"
    ],
    [
        567,
        "luz-collection",
        "06/09/2024 00:06:55"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:55"
    ],
    [
        357,
        "co2-collection",
        "06/09/2024 00:06:56"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 00:06:56"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:06:56"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:06:56"
    ],
    [
        612,
        "luz-collection",
        "06/09/2024 00:06:56"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:56"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:56"
    ],
    [
        353,
        "co2-collection",
        "06/09/2024 00:06:57"
    ],
    [
        353,
        "co2-collection",
        "06/09/2024 00:06:57"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:57"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:57"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:06:57"
    ],
    [
        583,
        "luz-collection",
        "06/09/2024 00:06:57"
    ],
    [
        637,
        "luz-collection",
        "06/09/2024 00:06:57"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:57"
    ],
    [
        351,
        "co2-collection",
        "06/09/2024 00:06:58"
    ],
    [
        15,
        "dist-collection",
        "06/09/2024 00:06:58"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:06:58"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:06:58"
    ],
    [
        604,
        "luz-collection",
        "06/09/2024 00:06:58"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:58"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:58"
    ],
    [
        355,
        "co2-collection",
        "06/09/2024 00:06:59"
    ],
    [
        356,
        "co2-collection",
        "06/09/2024 00:06:59"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 00:06:59"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:06:59"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:06:59"
    ],
    [
        556,
        "luz-collection",
        "06/09/2024 00:06:59"
    ],
    [
        575,
        "luz-collection",
        "06/09/2024 00:06:59"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:06:59"
    ],
    [
        352,
        "co2-collection",
        "06/09/2024 00:07:00"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:07:00"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:07:00"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:07:00"
    ],
    [
        621,
        "luz-collection",
        "06/09/2024 00:07:00"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:07:00"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:07:00"
    ],
    [
        355,
        "co2-collection",
        "06/09/2024 00:07:01"
    ],
    [
        349,
        "co2-collection",
        "06/09/2024 00:07:01"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:07:01"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:07:01"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:07:01"
    ],
    [
        636,
        "luz-collection",
        "06/09/2024 00:07:01"
    ],
    [
        596,
        "luz-collection",
        "06/09/2024 00:07:01"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:07:01"
    ],
    [
        357,
        "co2-collection",
        "06/09/2024 00:07:02"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:07:02"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:07:02"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:07:02"
    ],
    [
        621,
        "luz-collection",
        "06/09/2024 00:07:02"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:07:02"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:07:02"
    ],
    [
        352,
        "co2-collection",
        "06/09/2024 00:07:03"
    ],
    [
        356,
        "co2-collection",
        "06/09/2024 00:07:03"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:07:03"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:07:03"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:07:03"
    ],
    [
        567,
        "luz-collection",
        "06/09/2024 00:07:03"
    ],
    [
        618,
        "luz-collection",
        "06/09/2024 00:07:03"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:07:03"
    ],
    [
        354,
        "co2-collection",
        "06/09/2024 00:07:04"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:07:04"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:07:04"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:07:04"
    ],
    [
        565,
        "luz-collection",
        "06/09/2024 00:07:04"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:07:04"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:07:04"
    ],
    [
        351,
        "co2-collection",
        "06/09/2024 00:07:05"
    ],
    [
        352,
        "co2-collection",
        "06/09/2024 00:07:05"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:07:05"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:07:05"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:07:05"
    ],
    [
        607,
        "luz-collection",
        "06/09/2024 00:07:05"
    ],
    [
        574,
        "luz-collection",
        "06/09/2024 00:07:05"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:07:05"
    ],
    [
        355,
        "co2-collection",
        "06/09/2024 00:07:06"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:07:06"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:07:06"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:07:06"
    ],
    [
        638,
        "luz-collection",
        "06/09/2024 00:07:06"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:07:06"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:07:06"
    ],
    [
        355,
        "co2-collection",
        "06/09/2024 00:07:07"
    ],
    [
        355,
        "co2-collection",
        "06/09/2024 00:07:07"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:07:07"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:07:07"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:07:07"
    ],
    [
        604,
        "luz-collection",
        "06/09/2024 00:07:07"
    ],
    [
        563,
        "luz-collection",
        "06/09/2024 00:07:07"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:07:07"
    ],
    [
        355,
        "co2-collection",
        "06/09/2024 00:07:08"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:07:08"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:07:08"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:07:08"
    ],
    [
        638,
        "luz-collection",
        "06/09/2024 00:07:08"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:07:08"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:07:08"
    ],
    [
        358,
        "co2-collection",
        "06/09/2024 00:07:09"
    ],
    [
        352,
        "co2-collection",
        "06/09/2024 00:07:09"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:07:09"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:07:09"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:07:09"
    ],
    [
        623,
        "luz-collection",
        "06/09/2024 00:07:09"
    ],
    [
        578,
        "luz-collection",
        "06/09/2024 00:07:09"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:07:09"
    ],
    [
        357,
        "co2-collection",
        "06/09/2024 00:07:10"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:07:10"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:07:10"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:07:10"
    ],
    [
        634,
        "luz-collection",
        "06/09/2024 00:07:10"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:07:10"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:07:10"
    ],
    [
        357,
        "co2-collection",
        "06/09/2024 00:07:11"
    ],
    [
        358,
        "co2-collection",
        "06/09/2024 00:07:11"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:07:11"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:07:11"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:07:11"
    ],
    [
        590,
        "luz-collection",
        "06/09/2024 00:07:11"
    ],
    [
        601,
        "luz-collection",
        "06/09/2024 00:07:11"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:07:11"
    ],
    [
        354,
        "co2-collection",
        "06/09/2024 00:07:12"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:07:12"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:07:12"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:07:12"
    ],
    [
        556,
        "luz-collection",
        "06/09/2024 00:07:12"
    ],
    [
        578,
        "luz-collection",
        "06/09/2024 00:07:12"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:07:12"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:07:12"
    ],
    [
        355,
        "co2-collection",
        "06/09/2024 00:07:13"
    ],
    [
        355,
        "co2-collection",
        "06/09/2024 00:07:13"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:07:13"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:07:13"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:07:13"
    ],
    [
        592,
        "luz-collection",
        "06/09/2024 00:07:13"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:07:13"
    ],
    [
        356,
        "co2-collection",
        "06/09/2024 00:07:14"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:07:14"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:07:14"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:07:14"
    ],
    [
        629,
        "luz-collection",
        "06/09/2024 00:07:14"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:07:14"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:07:14"
    ],
    [
        357,
        "co2-collection",
        "06/09/2024 00:07:15"
    ],
    [
        355,
        "co2-collection",
        "06/09/2024 00:07:15"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:07:15"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:07:15"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:07:15"
    ],
    [
        632,
        "luz-collection",
        "06/09/2024 00:07:15"
    ],
    [
        594,
        "luz-collection",
        "06/09/2024 00:07:15"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:07:15"
    ],
    [
        356,
        "co2-collection",
        "06/09/2024 00:07:16"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:07:16"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:07:16"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:07:16"
    ],
    [
        639,
        "luz-collection",
        "06/09/2024 00:07:16"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:07:16"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:07:16"
    ],
    [
        357,
        "co2-collection",
        "06/09/2024 00:07:17"
    ],
    [
        358,
        "co2-collection",
        "06/09/2024 00:07:17"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:07:17"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:07:17"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:07:17"
    ],
    [
        585,
        "luz-collection",
        "06/09/2024 00:07:17"
    ],
    [
        556,
        "luz-collection",
        "06/09/2024 00:07:17"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:07:17"
    ],
    [
        358,
        "co2-collection",
        "06/09/2024 00:07:18"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:07:18"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:07:18"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:07:18"
    ],
    [
        629,
        "luz-collection",
        "06/09/2024 00:07:18"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:07:18"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:07:18"
    ],
    [
        359,
        "co2-collection",
        "06/09/2024 00:07:19"
    ],
    [
        357,
        "co2-collection",
        "06/09/2024 00:07:19"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:07:19"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:07:19"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:07:19"
    ],
    [
        578,
        "luz-collection",
        "06/09/2024 00:07:19"
    ],
    [
        631,
        "luz-collection",
        "06/09/2024 00:07:19"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:07:19"
    ],
    [
        353,
        "co2-collection",
        "06/09/2024 00:07:20"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:07:20"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:07:20"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:07:20"
    ],
    [
        560,
        "luz-collection",
        "06/09/2024 00:07:20"
    ],
    [
        588,
        "luz-collection",
        "06/09/2024 00:07:20"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:07:20"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:07:20"
    ],
    [
        355,
        "co2-collection",
        "06/09/2024 00:07:21"
    ],
    [
        356,
        "co2-collection",
        "06/09/2024 00:07:21"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:07:21"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:07:21"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:07:21"
    ],
    [
        624,
        "luz-collection",
        "06/09/2024 00:07:21"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:07:21"
    ],
    [
        354,
        "co2-collection",
        "06/09/2024 00:07:22"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:07:22"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:07:22"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:07:22"
    ],
    [
        598,
        "luz-collection",
        "06/09/2024 00:07:22"
    ],
    [
        638,
        "luz-collection",
        "06/09/2024 00:07:22"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:07:22"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:07:22"
    ],
    [
        357,
        "co2-collection",
        "06/09/2024 00:07:23"
    ],
    [
        356,
        "co2-collection",
        "06/09/2024 00:07:23"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:07:23"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:07:23"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:07:23"
    ],
    [
        626,
        "luz-collection",
        "06/09/2024 00:07:23"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:07:23"
    ],
    [
        355,
        "co2-collection",
        "06/09/2024 00:07:24"
    ],
    [
        8,
        "dist-collection",
        "06/09/2024 00:07:24"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:07:24"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:07:24"
    ],
    [
        571,
        "luz-collection",
        "06/09/2024 00:07:24"
    ],
    [
        614,
        "luz-collection",
        "06/09/2024 00:07:24"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:07:24"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:07:24"
    ],
    [
        354,
        "co2-collection",
        "06/09/2024 00:07:25"
    ],
    [
        356,
        "co2-collection",
        "06/09/2024 00:07:25"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:07:25"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:07:25"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:07:25"
    ],
    [
        560,
        "luz-collection",
        "06/09/2024 00:07:25"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:07:25"
    ],
    [
        355,
        "co2-collection",
        "06/09/2024 00:07:26"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:07:26"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:07:26"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:07:26"
    ],
    [
        572,
        "luz-collection",
        "06/09/2024 00:07:26"
    ],
    [
        600,
        "luz-collection",
        "06/09/2024 00:07:26"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:07:26"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:07:26"
    ],
    [
        354,
        "co2-collection",
        "06/09/2024 00:07:27"
    ],
    [
        354,
        "co2-collection",
        "06/09/2024 00:07:27"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:07:27"
    ],
    [
        9,
        "dist-collection",
        "06/09/2024 00:07:27"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:07:27"
    ],
    [
        637,
        "luz-collection",
        "06/09/2024 00:07:27"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:07:27"
    ],
    [
        354,
        "co2-collection",
        "06/09/2024 00:07:28"
    ],
    [
        83,
        "hum-collection",
        "06/09/2024 00:07:28"
    ],
    [
        607,
        "luz-collection",
        "06/09/2024 00:07:28"
    ],
    [
        23.4,
        "temp-collection",
        "06/09/2024 00:07:28"
    ],
    [
        75,
        "hum-collection",
        "06/09/2024 15:15:13"
    ],
    [
        548,
        "luz-collection",
        "06/09/2024 15:15:14"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:15:14"
    ],
    [
        398,
        "co2-collection",
        "06/09/2024 15:15:15"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:15:15"
    ],
    [
        401,
        "co2-collection",
        "06/09/2024 15:15:16"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:15:16"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:15:16"
    ],
    [
        484,
        "luz-collection",
        "06/09/2024 15:15:16"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:15:16"
    ],
    [
        400,
        "co2-collection",
        "06/09/2024 15:15:17"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:15:17"
    ],
    [
        405,
        "luz-collection",
        "06/09/2024 15:15:17"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:15:17"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:15:18"
    ],
    [
        75,
        "hum-collection",
        "06/09/2024 15:15:18"
    ],
    [
        401,
        "co2-collection",
        "06/09/2024 15:15:19"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:15:19"
    ],
    [
        399,
        "luz-collection",
        "06/09/2024 15:15:19"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:15:19"
    ],
    [
        402,
        "co2-collection",
        "06/09/2024 15:15:20"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:15:20"
    ],
    [
        75,
        "hum-collection",
        "06/09/2024 15:15:20"
    ],
    [
        369,
        "luz-collection",
        "06/09/2024 15:15:20"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:15:20"
    ],
    [
        75,
        "hum-collection",
        "06/09/2024 15:15:21"
    ],
    [
        422,
        "luz-collection",
        "06/09/2024 15:15:21"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:15:21"
    ],
    [
        403,
        "co2-collection",
        "06/09/2024 15:15:22"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:15:22"
    ],
    [
        403,
        "co2-collection",
        "06/09/2024 15:15:23"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:15:23"
    ],
    [
        75,
        "hum-collection",
        "06/09/2024 15:15:23"
    ],
    [
        321,
        "luz-collection",
        "06/09/2024 15:15:23"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:15:23"
    ],
    [
        400,
        "co2-collection",
        "06/09/2024 15:15:24"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:15:24"
    ],
    [
        75,
        "hum-collection",
        "06/09/2024 15:15:24"
    ],
    [
        370,
        "luz-collection",
        "06/09/2024 15:15:24"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:15:24"
    ],
    [
        75,
        "hum-collection",
        "06/09/2024 15:15:25"
    ],
    [
        376,
        "luz-collection",
        "06/09/2024 15:15:25"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:15:25"
    ],
    [
        399,
        "co2-collection",
        "06/09/2024 15:15:26"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:15:26"
    ],
    [
        398,
        "co2-collection",
        "06/09/2024 15:15:27"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:15:27"
    ],
    [
        75,
        "hum-collection",
        "06/09/2024 15:15:27"
    ],
    [
        371,
        "luz-collection",
        "06/09/2024 15:15:27"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:15:27"
    ],
    [
        384,
        "co2-collection",
        "06/09/2024 15:15:28"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:15:28"
    ],
    [
        75,
        "hum-collection",
        "06/09/2024 15:15:28"
    ],
    [
        398,
        "luz-collection",
        "06/09/2024 15:15:28"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:15:28"
    ],
    [
        75,
        "hum-collection",
        "06/09/2024 15:15:29"
    ],
    [
        428,
        "luz-collection",
        "06/09/2024 15:15:29"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:15:29"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 15:15:30"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:15:30"
    ],
    [
        386,
        "co2-collection",
        "06/09/2024 15:15:31"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:15:31"
    ],
    [
        75,
        "hum-collection",
        "06/09/2024 15:15:31"
    ],
    [
        324,
        "luz-collection",
        "06/09/2024 15:15:31"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:15:31"
    ],
    [
        384,
        "co2-collection",
        "06/09/2024 15:15:32"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:15:32"
    ],
    [
        75,
        "hum-collection",
        "06/09/2024 15:15:32"
    ],
    [
        384,
        "luz-collection",
        "06/09/2024 15:15:32"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:15:32"
    ],
    [
        75,
        "hum-collection",
        "06/09/2024 15:15:33"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:15:33"
    ],
    [
        382,
        "co2-collection",
        "06/09/2024 15:15:34"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:15:34"
    ],
    [
        363,
        "luz-collection",
        "06/09/2024 15:15:34"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 15:15:35"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:15:35"
    ],
    [
        75,
        "hum-collection",
        "06/09/2024 15:15:35"
    ],
    [
        366,
        "luz-collection",
        "06/09/2024 15:15:35"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:15:35"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 15:15:36"
    ],
    [
        75,
        "hum-collection",
        "06/09/2024 15:15:36"
    ],
    [
        400,
        "luz-collection",
        "06/09/2024 15:15:36"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:15:36"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:15:37"
    ],
    [
        75,
        "hum-collection",
        "06/09/2024 15:15:37"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:15:37"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 15:15:38"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:15:38"
    ],
    [
        425,
        "luz-collection",
        "06/09/2024 15:15:38"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 15:15:39"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:15:39"
    ],
    [
        75,
        "hum-collection",
        "06/09/2024 15:15:39"
    ],
    [
        329,
        "luz-collection",
        "06/09/2024 15:15:39"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:15:39"
    ],
    [
        403,
        "co2-collection",
        "06/09/2024 15:15:40"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:15:40"
    ],
    [
        75,
        "hum-collection",
        "06/09/2024 15:15:40"
    ],
    [
        388,
        "luz-collection",
        "06/09/2024 15:15:40"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:15:40"
    ],
    [
        75,
        "hum-collection",
        "06/09/2024 15:15:41"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:15:41"
    ],
    [
        406,
        "co2-collection",
        "06/09/2024 15:15:42"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:15:42"
    ],
    [
        362,
        "luz-collection",
        "06/09/2024 15:15:42"
    ],
    [
        405,
        "co2-collection",
        "06/09/2024 15:15:43"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:15:43"
    ],
    [
        75,
        "hum-collection",
        "06/09/2024 15:15:43"
    ],
    [
        361,
        "luz-collection",
        "06/09/2024 15:15:43"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:15:43"
    ],
    [
        404,
        "co2-collection",
        "06/09/2024 15:15:44"
    ],
    [
        75,
        "hum-collection",
        "06/09/2024 15:15:44"
    ],
    [
        397,
        "luz-collection",
        "06/09/2024 15:15:44"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:15:44"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:15:45"
    ],
    [
        75,
        "hum-collection",
        "06/09/2024 15:15:45"
    ],
    [
        406,
        "co2-collection",
        "06/09/2024 15:15:46"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:15:46"
    ],
    [
        426,
        "luz-collection",
        "06/09/2024 15:15:46"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:15:46"
    ],
    [
        405,
        "co2-collection",
        "06/09/2024 15:15:47"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:15:47"
    ],
    [
        75,
        "hum-collection",
        "06/09/2024 15:15:47"
    ],
    [
        318,
        "luz-collection",
        "06/09/2024 15:15:47"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:15:47"
    ],
    [
        75,
        "hum-collection",
        "06/09/2024 15:15:48"
    ],
    [
        371,
        "luz-collection",
        "06/09/2024 15:15:48"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:15:48"
    ],
    [
        402,
        "co2-collection",
        "06/09/2024 15:15:49"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:15:49"
    ],
    [
        75,
        "hum-collection",
        "06/09/2024 15:15:49"
    ],
    [
        401,
        "co2-collection",
        "06/09/2024 15:15:50"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:15:50"
    ],
    [
        392,
        "luz-collection",
        "06/09/2024 15:15:50"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:15:50"
    ],
    [
        404,
        "co2-collection",
        "06/09/2024 15:15:51"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:15:51"
    ],
    [
        75,
        "hum-collection",
        "06/09/2024 15:15:51"
    ],
    [
        390,
        "luz-collection",
        "06/09/2024 15:15:51"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:15:51"
    ],
    [
        398,
        "co2-collection",
        "06/09/2024 15:15:52"
    ],
    [
        75,
        "hum-collection",
        "06/09/2024 15:15:52"
    ],
    [
        373,
        "luz-collection",
        "06/09/2024 15:15:52"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:15:52"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:15:53"
    ],
    [
        75,
        "hum-collection",
        "06/09/2024 15:15:53"
    ],
    [
        403,
        "co2-collection",
        "06/09/2024 15:15:54"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:15:54"
    ],
    [
        423,
        "luz-collection",
        "06/09/2024 15:15:54"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:15:54"
    ],
    [
        75,
        "hum-collection",
        "06/09/2024 15:15:58"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:15:58"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 15:15:59"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:15:59"
    ],
    [
        369,
        "luz-collection",
        "06/09/2024 15:15:59"
    ],
    [
        386,
        "co2-collection",
        "06/09/2024 15:16:00"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:16:00"
    ],
    [
        75,
        "hum-collection",
        "06/09/2024 15:16:00"
    ],
    [
        397,
        "luz-collection",
        "06/09/2024 15:16:00"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:16:00"
    ],
    [
        370,
        "co2-collection",
        "06/09/2024 15:16:05"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:16:05"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:16:05"
    ],
    [
        362,
        "luz-collection",
        "06/09/2024 15:16:05"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:16:05"
    ],
    [
        380,
        "co2-collection",
        "06/09/2024 15:16:06"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:16:06"
    ],
    [
        405,
        "luz-collection",
        "06/09/2024 15:16:06"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:16:06"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:16:07"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:16:07"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:16:07"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 15:16:08"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:16:08"
    ],
    [
        426,
        "luz-collection",
        "06/09/2024 15:16:08"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 15:16:09"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:16:09"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:16:09"
    ],
    [
        334,
        "luz-collection",
        "06/09/2024 15:16:09"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:16:09"
    ],
    [
        387,
        "co2-collection",
        "06/09/2024 15:16:10"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:16:10"
    ],
    [
        396,
        "luz-collection",
        "06/09/2024 15:16:10"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:16:10"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:16:11"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:16:11"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:16:11"
    ],
    [
        386,
        "co2-collection",
        "06/09/2024 15:16:12"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:16:12"
    ],
    [
        363,
        "luz-collection",
        "06/09/2024 15:16:12"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 15:16:13"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:16:13"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:16:13"
    ],
    [
        372,
        "luz-collection",
        "06/09/2024 15:16:13"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:16:13"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 15:16:14"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:16:14"
    ],
    [
        399,
        "luz-collection",
        "06/09/2024 15:16:14"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:16:14"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:16:15"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:16:15"
    ],
    [
        387,
        "co2-collection",
        "06/09/2024 15:16:16"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:16:16"
    ],
    [
        432,
        "luz-collection",
        "06/09/2024 15:16:16"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:16:16"
    ],
    [
        387,
        "co2-collection",
        "06/09/2024 15:16:17"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:16:17"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:16:17"
    ],
    [
        326,
        "luz-collection",
        "06/09/2024 15:16:17"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:16:17"
    ],
    [
        385,
        "co2-collection",
        "06/09/2024 15:16:18"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:16:18"
    ],
    [
        365,
        "luz-collection",
        "06/09/2024 15:16:18"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:16:18"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:16:19"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:16:19"
    ],
    [
        380,
        "co2-collection",
        "06/09/2024 15:16:20"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:16:20"
    ],
    [
        411,
        "luz-collection",
        "06/09/2024 15:16:20"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:16:20"
    ],
    [
        380,
        "co2-collection",
        "06/09/2024 15:16:21"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:16:21"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:16:21"
    ],
    [
        421,
        "luz-collection",
        "06/09/2024 15:16:21"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:16:21"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:16:22"
    ],
    [
        343,
        "luz-collection",
        "06/09/2024 15:16:22"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:16:22"
    ],
    [
        385,
        "co2-collection",
        "06/09/2024 15:16:23"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:16:23"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:16:23"
    ],
    [
        370,
        "co2-collection",
        "06/09/2024 15:16:24"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:16:24"
    ],
    [
        397,
        "luz-collection",
        "06/09/2024 15:16:24"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:16:24"
    ],
    [
        395,
        "co2-collection",
        "06/09/2024 15:16:25"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:16:25"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:16:25"
    ],
    [
        376,
        "luz-collection",
        "06/09/2024 15:16:25"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:16:25"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:16:26"
    ],
    [
        388,
        "luz-collection",
        "06/09/2024 15:16:26"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:16:26"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 15:16:27"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:16:27"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 15:16:28"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:16:28"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:16:28"
    ],
    [
        386,
        "luz-collection",
        "06/09/2024 15:16:28"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:16:28"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 15:16:29"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:16:29"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:16:29"
    ],
    [
        429,
        "luz-collection",
        "06/09/2024 15:16:29"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:16:29"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:16:30"
    ],
    [
        343,
        "luz-collection",
        "06/09/2024 15:16:30"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:16:30"
    ],
    [
        393,
        "co2-collection",
        "06/09/2024 15:16:31"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:16:31"
    ],
    [
        394,
        "co2-collection",
        "06/09/2024 15:16:32"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:16:32"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:16:32"
    ],
    [
        374,
        "luz-collection",
        "06/09/2024 15:16:32"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:16:32"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 15:16:33"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:16:33"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:16:33"
    ],
    [
        415,
        "luz-collection",
        "06/09/2024 15:16:33"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:16:33"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:16:34"
    ],
    [
        444,
        "luz-collection",
        "06/09/2024 15:16:34"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:16:34"
    ],
    [
        396,
        "co2-collection",
        "06/09/2024 15:16:35"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:16:35"
    ],
    [
        397,
        "co2-collection",
        "06/09/2024 15:16:36"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:16:36"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:16:36"
    ],
    [
        328,
        "luz-collection",
        "06/09/2024 15:16:36"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:16:36"
    ],
    [
        394,
        "co2-collection",
        "06/09/2024 15:16:37"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:16:37"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:16:37"
    ],
    [
        374,
        "luz-collection",
        "06/09/2024 15:16:37"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:16:37"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:16:38"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:16:38"
    ],
    [
        396,
        "co2-collection",
        "06/09/2024 15:16:39"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:16:39"
    ],
    [
        408,
        "luz-collection",
        "06/09/2024 15:16:39"
    ],
    [
        398,
        "co2-collection",
        "06/09/2024 15:16:40"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:16:40"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:16:40"
    ],
    [
        413,
        "luz-collection",
        "06/09/2024 15:16:40"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:16:40"
    ],
    [
        398,
        "co2-collection",
        "06/09/2024 15:16:41"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:16:41"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:16:41"
    ],
    [
        361,
        "luz-collection",
        "06/09/2024 15:16:41"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:16:41"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:16:42"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:16:42"
    ],
    [
        402,
        "co2-collection",
        "06/09/2024 15:16:43"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:16:43"
    ],
    [
        415,
        "luz-collection",
        "06/09/2024 15:16:43"
    ],
    [
        406,
        "co2-collection",
        "06/09/2024 15:16:44"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:16:44"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:16:44"
    ],
    [
        357,
        "luz-collection",
        "06/09/2024 15:16:44"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:16:44"
    ],
    [
        394,
        "co2-collection",
        "06/09/2024 15:16:45"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:16:45"
    ],
    [
        369,
        "luz-collection",
        "06/09/2024 15:16:45"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:16:45"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:16:46"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:16:46"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:16:46"
    ],
    [
        397,
        "co2-collection",
        "06/09/2024 15:16:47"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:16:47"
    ],
    [
        414,
        "luz-collection",
        "06/09/2024 15:16:47"
    ],
    [
        397,
        "co2-collection",
        "06/09/2024 15:16:48"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:16:48"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:16:48"
    ],
    [
        448,
        "luz-collection",
        "06/09/2024 15:16:48"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:16:48"
    ],
    [
        400,
        "co2-collection",
        "06/09/2024 15:16:49"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:16:49"
    ],
    [
        347,
        "luz-collection",
        "06/09/2024 15:16:49"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:16:49"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:16:50"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:16:50"
    ],
    [
        395,
        "co2-collection",
        "06/09/2024 15:16:51"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:16:51"
    ],
    [
        411,
        "luz-collection",
        "06/09/2024 15:16:51"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:16:51"
    ],
    [
        398,
        "co2-collection",
        "06/09/2024 15:16:52"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:16:52"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:16:52"
    ],
    [
        379,
        "luz-collection",
        "06/09/2024 15:16:52"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:16:52"
    ],
    [
        396,
        "co2-collection",
        "06/09/2024 15:16:53"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:16:53"
    ],
    [
        392,
        "luz-collection",
        "06/09/2024 15:16:53"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:16:53"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:16:54"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:16:54"
    ],
    [
        400,
        "co2-collection",
        "06/09/2024 15:16:55"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:16:55"
    ],
    [
        403,
        "luz-collection",
        "06/09/2024 15:16:55"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:16:55"
    ],
    [
        401,
        "co2-collection",
        "06/09/2024 15:16:56"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:16:56"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:16:56"
    ],
    [
        445,
        "luz-collection",
        "06/09/2024 15:16:56"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:16:56"
    ],
    [
        400,
        "co2-collection",
        "06/09/2024 15:16:57"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:16:57"
    ],
    [
        338,
        "luz-collection",
        "06/09/2024 15:16:57"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:16:57"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:16:58"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:16:58"
    ],
    [
        398,
        "co2-collection",
        "06/09/2024 15:16:59"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:16:59"
    ],
    [
        372,
        "luz-collection",
        "06/09/2024 15:16:59"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:16:59"
    ],
    [
        400,
        "co2-collection",
        "06/09/2024 15:17:00"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:17:00"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:17:00"
    ],
    [
        420,
        "luz-collection",
        "06/09/2024 15:17:00"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:17:00"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:17:01"
    ],
    [
        435,
        "luz-collection",
        "06/09/2024 15:17:01"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:17:01"
    ],
    [
        402,
        "co2-collection",
        "06/09/2024 15:17:02"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:17:02"
    ],
    [
        402,
        "co2-collection",
        "06/09/2024 15:17:03"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:17:03"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:17:03"
    ],
    [
        335,
        "luz-collection",
        "06/09/2024 15:17:03"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:17:03"
    ],
    [
        402,
        "co2-collection",
        "06/09/2024 15:17:04"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:17:04"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:17:04"
    ],
    [
        383,
        "luz-collection",
        "06/09/2024 15:17:04"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:17:04"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:17:05"
    ],
    [
        409,
        "luz-collection",
        "06/09/2024 15:17:05"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:17:05"
    ],
    [
        403,
        "co2-collection",
        "06/09/2024 15:17:06"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:17:06"
    ],
    [
        399,
        "co2-collection",
        "06/09/2024 15:17:07"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:17:07"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:17:07"
    ],
    [
        426,
        "luz-collection",
        "06/09/2024 15:17:07"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:17:07"
    ],
    [
        397,
        "co2-collection",
        "06/09/2024 15:17:08"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:17:08"
    ],
    [
        337,
        "luz-collection",
        "06/09/2024 15:17:08"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:17:08"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:17:09"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:17:09"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:17:09"
    ],
    [
        397,
        "co2-collection",
        "06/09/2024 15:17:10"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:17:10"
    ],
    [
        381,
        "luz-collection",
        "06/09/2024 15:17:10"
    ],
    [
        400,
        "co2-collection",
        "06/09/2024 15:17:11"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:17:11"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:17:11"
    ],
    [
        407,
        "luz-collection",
        "06/09/2024 15:17:11"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:17:11"
    ],
    [
        400,
        "co2-collection",
        "06/09/2024 15:17:12"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:17:12"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:17:12"
    ],
    [
        424,
        "luz-collection",
        "06/09/2024 15:17:12"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:17:12"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:17:13"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:17:13"
    ],
    [
        399,
        "co2-collection",
        "06/09/2024 15:17:14"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:17:14"
    ],
    [
        338,
        "luz-collection",
        "06/09/2024 15:17:14"
    ],
    [
        400,
        "co2-collection",
        "06/09/2024 15:17:15"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:17:15"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:17:15"
    ],
    [
        388,
        "luz-collection",
        "06/09/2024 15:17:15"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:17:15"
    ],
    [
        401,
        "co2-collection",
        "06/09/2024 15:17:16"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:17:16"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:17:16"
    ],
    [
        390,
        "luz-collection",
        "06/09/2024 15:17:16"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:17:16"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:17:17"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:17:17"
    ],
    [
        410,
        "co2-collection",
        "06/09/2024 15:17:18"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:17:18"
    ],
    [
        399,
        "luz-collection",
        "06/09/2024 15:17:18"
    ],
    [
        404,
        "co2-collection",
        "06/09/2024 15:17:19"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:17:19"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:17:19"
    ],
    [
        373,
        "luz-collection",
        "06/09/2024 15:17:19"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:17:19"
    ],
    [
        399,
        "co2-collection",
        "06/09/2024 15:17:20"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:17:20"
    ],
    [
        422,
        "luz-collection",
        "06/09/2024 15:17:20"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:17:20"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:17:21"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:17:21"
    ],
    [
        401,
        "co2-collection",
        "06/09/2024 15:17:22"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:17:22"
    ],
    [
        345,
        "luz-collection",
        "06/09/2024 15:17:22"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:17:22"
    ],
    [
        396,
        "co2-collection",
        "06/09/2024 15:17:23"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:17:23"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:17:23"
    ],
    [
        366,
        "luz-collection",
        "06/09/2024 15:17:23"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:17:23"
    ],
    [
        398,
        "co2-collection",
        "06/09/2024 15:17:24"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:17:24"
    ],
    [
        408,
        "luz-collection",
        "06/09/2024 15:17:24"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:17:24"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:17:25"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:17:25"
    ],
    [
        400,
        "co2-collection",
        "06/09/2024 15:17:26"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:17:26"
    ],
    [
        439,
        "luz-collection",
        "06/09/2024 15:17:26"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:17:26"
    ],
    [
        412,
        "co2-collection",
        "06/09/2024 15:17:27"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:17:27"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:17:27"
    ],
    [
        326,
        "luz-collection",
        "06/09/2024 15:17:27"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:17:27"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:17:28"
    ],
    [
        377,
        "luz-collection",
        "06/09/2024 15:17:28"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:17:28"
    ],
    [
        399,
        "co2-collection",
        "06/09/2024 15:17:29"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:17:29"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:17:29"
    ],
    [
        401,
        "co2-collection",
        "06/09/2024 15:17:30"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:17:30"
    ],
    [
        393,
        "luz-collection",
        "06/09/2024 15:17:30"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:17:30"
    ],
    [
        400,
        "co2-collection",
        "06/09/2024 15:17:31"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:17:31"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:17:31"
    ],
    [
        398,
        "luz-collection",
        "06/09/2024 15:17:31"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:17:31"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:17:32"
    ],
    [
        371,
        "luz-collection",
        "06/09/2024 15:17:32"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:17:32"
    ],
    [
        400,
        "co2-collection",
        "06/09/2024 15:17:33"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:17:33"
    ],
    [
        396,
        "co2-collection",
        "06/09/2024 15:17:34"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:17:34"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:17:34"
    ],
    [
        423,
        "luz-collection",
        "06/09/2024 15:17:34"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:17:34"
    ],
    [
        399,
        "co2-collection",
        "06/09/2024 15:17:35"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:17:35"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:17:35"
    ],
    [
        339,
        "luz-collection",
        "06/09/2024 15:17:35"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:17:35"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:17:36"
    ],
    [
        363,
        "luz-collection",
        "06/09/2024 15:17:36"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:17:36"
    ],
    [
        398,
        "co2-collection",
        "06/09/2024 15:17:37"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:17:37"
    ],
    [
        400,
        "co2-collection",
        "06/09/2024 15:17:38"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:17:38"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:17:38"
    ],
    [
        408,
        "luz-collection",
        "06/09/2024 15:17:38"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:17:38"
    ],
    [
        403,
        "co2-collection",
        "06/09/2024 15:17:39"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:17:39"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:17:39"
    ],
    [
        437,
        "luz-collection",
        "06/09/2024 15:17:39"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:17:39"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:17:40"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:17:40"
    ],
    [
        398,
        "co2-collection",
        "06/09/2024 15:17:41"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:17:41"
    ],
    [
        325,
        "luz-collection",
        "06/09/2024 15:17:41"
    ],
    [
        397,
        "co2-collection",
        "06/09/2024 15:17:42"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:17:42"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:17:42"
    ],
    [
        377,
        "luz-collection",
        "06/09/2024 15:17:42"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:17:42"
    ],
    [
        397,
        "co2-collection",
        "06/09/2024 15:17:43"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:17:43"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:17:43"
    ],
    [
        392,
        "luz-collection",
        "06/09/2024 15:17:43"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:17:43"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:17:44"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:17:44"
    ],
    [
        399,
        "co2-collection",
        "06/09/2024 15:17:45"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:17:45"
    ],
    [
        397,
        "luz-collection",
        "06/09/2024 15:17:45"
    ],
    [
        398,
        "co2-collection",
        "06/09/2024 15:17:46"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:17:46"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:17:46"
    ],
    [
        373,
        "luz-collection",
        "06/09/2024 15:17:46"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:17:46"
    ],
    [
        397,
        "co2-collection",
        "06/09/2024 15:17:47"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:17:47"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:17:47"
    ],
    [
        423,
        "luz-collection",
        "06/09/2024 15:17:47"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:17:47"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:17:48"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:17:48"
    ],
    [
        398,
        "co2-collection",
        "06/09/2024 15:17:49"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:17:49"
    ],
    [
        334,
        "luz-collection",
        "06/09/2024 15:17:49"
    ],
    [
        398,
        "co2-collection",
        "06/09/2024 15:17:50"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:17:50"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:17:50"
    ],
    [
        360,
        "luz-collection",
        "06/09/2024 15:17:50"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:17:50"
    ],
    [
        399,
        "co2-collection",
        "06/09/2024 15:17:51"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:17:51"
    ],
    [
        408,
        "luz-collection",
        "06/09/2024 15:17:51"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:17:51"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:17:52"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:17:52"
    ],
    [
        397,
        "co2-collection",
        "06/09/2024 15:17:53"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:17:53"
    ],
    [
        407,
        "luz-collection",
        "06/09/2024 15:17:53"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:17:53"
    ],
    [
        398,
        "co2-collection",
        "06/09/2024 15:17:54"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:17:54"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:17:54"
    ],
    [
        363,
        "luz-collection",
        "06/09/2024 15:17:54"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:17:54"
    ],
    [
        398,
        "co2-collection",
        "06/09/2024 15:17:55"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:17:55"
    ],
    [
        425,
        "luz-collection",
        "06/09/2024 15:17:55"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:17:55"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:17:56"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:17:56"
    ],
    [
        397,
        "co2-collection",
        "06/09/2024 15:17:57"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:17:57"
    ],
    [
        325,
        "luz-collection",
        "06/09/2024 15:17:57"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:17:57"
    ],
    [
        398,
        "co2-collection",
        "06/09/2024 15:17:58"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:17:58"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:17:58"
    ],
    [
        375,
        "luz-collection",
        "06/09/2024 15:17:58"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:17:58"
    ],
    [
        398,
        "co2-collection",
        "06/09/2024 15:17:59"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:17:59"
    ],
    [
        374,
        "luz-collection",
        "06/09/2024 15:17:59"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:17:59"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:18:00"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:18:00"
    ],
    [
        399,
        "co2-collection",
        "06/09/2024 15:18:01"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:18:01"
    ],
    [
        369,
        "luz-collection",
        "06/09/2024 15:18:01"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:18:01"
    ],
    [
        398,
        "co2-collection",
        "06/09/2024 15:18:02"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:18:02"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:18:02"
    ],
    [
        407,
        "luz-collection",
        "06/09/2024 15:18:02"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:18:02"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:18:03"
    ],
    [
        418,
        "luz-collection",
        "06/09/2024 15:18:03"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:18:03"
    ],
    [
        399,
        "co2-collection",
        "06/09/2024 15:18:04"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:18:04"
    ],
    [
        400,
        "co2-collection",
        "06/09/2024 15:18:05"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:18:05"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:18:05"
    ],
    [
        362,
        "luz-collection",
        "06/09/2024 15:18:05"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:18:05"
    ],
    [
        400,
        "co2-collection",
        "06/09/2024 15:18:06"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:18:06"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:18:06"
    ],
    [
        427,
        "luz-collection",
        "06/09/2024 15:18:06"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:18:06"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:18:07"
    ],
    [
        326,
        "luz-collection",
        "06/09/2024 15:18:07"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:18:07"
    ],
    [
        400,
        "co2-collection",
        "06/09/2024 15:18:08"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:18:08"
    ],
    [
        400,
        "co2-collection",
        "06/09/2024 15:18:09"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:18:09"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:18:09"
    ],
    [
        379,
        "luz-collection",
        "06/09/2024 15:18:09"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:18:09"
    ],
    [
        415,
        "co2-collection",
        "06/09/2024 15:18:10"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:18:10"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:18:10"
    ],
    [
        375,
        "luz-collection",
        "06/09/2024 15:18:10"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:18:10"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:18:11"
    ],
    [
        371,
        "luz-collection",
        "06/09/2024 15:18:11"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:18:11"
    ],
    [
        402,
        "co2-collection",
        "06/09/2024 15:18:12"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:18:12"
    ],
    [
        398,
        "co2-collection",
        "06/09/2024 15:18:13"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:18:13"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:18:13"
    ],
    [
        409,
        "luz-collection",
        "06/09/2024 15:18:13"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:18:13"
    ],
    [
        399,
        "co2-collection",
        "06/09/2024 15:18:14"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:18:14"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:18:14"
    ],
    [
        406,
        "luz-collection",
        "06/09/2024 15:18:14"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:18:14"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:18:15"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:18:15"
    ],
    [
        396,
        "co2-collection",
        "06/09/2024 15:18:16"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:18:16"
    ],
    [
        387,
        "luz-collection",
        "06/09/2024 15:18:16"
    ],
    [
        396,
        "co2-collection",
        "06/09/2024 15:18:17"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:18:17"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:18:17"
    ],
    [
        433,
        "luz-collection",
        "06/09/2024 15:18:17"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:18:17"
    ],
    [
        396,
        "co2-collection",
        "06/09/2024 15:18:18"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:18:18"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:18:18"
    ],
    [
        346,
        "luz-collection",
        "06/09/2024 15:18:18"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:18:18"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:18:19"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:18:19"
    ],
    [
        395,
        "co2-collection",
        "06/09/2024 15:18:20"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:18:20"
    ],
    [
        423,
        "luz-collection",
        "06/09/2024 15:18:20"
    ],
    [
        397,
        "co2-collection",
        "06/09/2024 15:18:21"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:18:21"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:18:21"
    ],
    [
        326,
        "luz-collection",
        "06/09/2024 15:18:21"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:18:21"
    ],
    [
        408,
        "co2-collection",
        "06/09/2024 15:18:22"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:18:22"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:18:22"
    ],
    [
        380,
        "luz-collection",
        "06/09/2024 15:18:22"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:18:22"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:18:23"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:18:23"
    ],
    [
        403,
        "co2-collection",
        "06/09/2024 15:18:24"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:18:24"
    ],
    [
        367,
        "luz-collection",
        "06/09/2024 15:18:24"
    ],
    [
        412,
        "co2-collection",
        "06/09/2024 15:18:25"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:18:25"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:18:25"
    ],
    [
        366,
        "luz-collection",
        "06/09/2024 15:18:25"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:18:25"
    ],
    [
        400,
        "co2-collection",
        "06/09/2024 15:18:26"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:18:26"
    ],
    [
        413,
        "luz-collection",
        "06/09/2024 15:18:26"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:18:26"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:18:27"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:18:27"
    ],
    [
        399,
        "co2-collection",
        "06/09/2024 15:18:28"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:18:28"
    ],
    [
        410,
        "luz-collection",
        "06/09/2024 15:18:28"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:18:28"
    ],
    [
        399,
        "co2-collection",
        "06/09/2024 15:18:29"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:18:29"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:18:29"
    ],
    [
        370,
        "luz-collection",
        "06/09/2024 15:18:29"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:18:29"
    ],
    [
        398,
        "co2-collection",
        "06/09/2024 15:18:30"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:18:30"
    ],
    [
        429,
        "luz-collection",
        "06/09/2024 15:18:30"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:18:30"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:18:31"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:18:31"
    ],
    [
        400,
        "co2-collection",
        "06/09/2024 15:18:32"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:18:32"
    ],
    [
        322,
        "luz-collection",
        "06/09/2024 15:18:32"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:18:32"
    ],
    [
        400,
        "co2-collection",
        "06/09/2024 15:18:33"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:18:33"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:18:33"
    ],
    [
        386,
        "luz-collection",
        "06/09/2024 15:18:33"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:18:33"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:18:34"
    ],
    [
        367,
        "luz-collection",
        "06/09/2024 15:18:34"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:18:34"
    ],
    [
        402,
        "co2-collection",
        "06/09/2024 15:18:35"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:18:35"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:18:35"
    ],
    [
        402,
        "co2-collection",
        "06/09/2024 15:18:36"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:18:36"
    ],
    [
        369,
        "luz-collection",
        "06/09/2024 15:18:36"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:18:36"
    ],
    [
        418,
        "co2-collection",
        "06/09/2024 15:18:37"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:18:37"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:18:37"
    ],
    [
        413,
        "luz-collection",
        "06/09/2024 15:18:37"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:18:37"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:18:38"
    ],
    [
        416,
        "luz-collection",
        "06/09/2024 15:18:38"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:18:38"
    ],
    [
        396,
        "co2-collection",
        "06/09/2024 15:18:39"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:18:39"
    ],
    [
        397,
        "co2-collection",
        "06/09/2024 15:18:40"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:18:40"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:18:40"
    ],
    [
        376,
        "luz-collection",
        "06/09/2024 15:18:40"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:18:40"
    ],
    [
        398,
        "co2-collection",
        "06/09/2024 15:18:41"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:18:41"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:18:41"
    ],
    [
        439,
        "luz-collection",
        "06/09/2024 15:18:41"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:18:41"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:18:42"
    ],
    [
        335,
        "luz-collection",
        "06/09/2024 15:18:42"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:18:42"
    ],
    [
        397,
        "co2-collection",
        "06/09/2024 15:18:43"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:18:43"
    ],
    [
        397,
        "co2-collection",
        "06/09/2024 15:18:44"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:18:44"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:18:44"
    ],
    [
        411,
        "luz-collection",
        "06/09/2024 15:18:44"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:18:44"
    ],
    [
        397,
        "co2-collection",
        "06/09/2024 15:18:45"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:18:45"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:18:45"
    ],
    [
        367,
        "luz-collection",
        "06/09/2024 15:18:45"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:18:45"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:18:46"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:18:46"
    ],
    [
        397,
        "co2-collection",
        "06/09/2024 15:18:47"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:18:47"
    ],
    [
        392,
        "luz-collection",
        "06/09/2024 15:18:47"
    ],
    [
        398,
        "co2-collection",
        "06/09/2024 15:18:48"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:18:48"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:18:48"
    ],
    [
        430,
        "luz-collection",
        "06/09/2024 15:18:48"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:18:48"
    ],
    [
        399,
        "co2-collection",
        "06/09/2024 15:18:49"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:18:49"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:18:49"
    ],
    [
        424,
        "luz-collection",
        "06/09/2024 15:18:49"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:18:49"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:18:50"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:18:50"
    ],
    [
        406,
        "co2-collection",
        "06/09/2024 15:18:51"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:18:51"
    ],
    [
        425,
        "luz-collection",
        "06/09/2024 15:18:51"
    ],
    [
        405,
        "co2-collection",
        "06/09/2024 15:18:52"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:18:52"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:18:52"
    ],
    [
        460,
        "luz-collection",
        "06/09/2024 15:18:52"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:18:52"
    ],
    [
        405,
        "co2-collection",
        "06/09/2024 15:18:53"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:18:53"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:18:53"
    ],
    [
        363,
        "luz-collection",
        "06/09/2024 15:18:53"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:18:53"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:18:54"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:18:54"
    ],
    [
        403,
        "co2-collection",
        "06/09/2024 15:18:55"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:18:55"
    ],
    [
        430,
        "luz-collection",
        "06/09/2024 15:18:55"
    ],
    [
        402,
        "co2-collection",
        "06/09/2024 15:18:56"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:18:56"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:18:56"
    ],
    [
        355,
        "luz-collection",
        "06/09/2024 15:18:56"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:18:56"
    ],
    [
        402,
        "co2-collection",
        "06/09/2024 15:18:57"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:18:57"
    ],
    [
        379,
        "luz-collection",
        "06/09/2024 15:18:57"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:18:57"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:18:58"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:18:58"
    ],
    [
        403,
        "co2-collection",
        "06/09/2024 15:18:59"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:18:59"
    ],
    [
        414,
        "luz-collection",
        "06/09/2024 15:18:59"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:18:59"
    ],
    [
        404,
        "co2-collection",
        "06/09/2024 15:19:00"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:19:00"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:19:00"
    ],
    [
        409,
        "luz-collection",
        "06/09/2024 15:19:00"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:19:00"
    ],
    [
        404,
        "co2-collection",
        "06/09/2024 15:19:01"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:19:01"
    ],
    [
        413,
        "luz-collection",
        "06/09/2024 15:19:01"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:19:01"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:19:02"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:19:02"
    ],
    [
        406,
        "co2-collection",
        "06/09/2024 15:19:03"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:19:03"
    ],
    [
        459,
        "luz-collection",
        "06/09/2024 15:19:03"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:19:03"
    ],
    [
        406,
        "co2-collection",
        "06/09/2024 15:19:04"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:19:04"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:19:04"
    ],
    [
        357,
        "luz-collection",
        "06/09/2024 15:19:04"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:19:04"
    ],
    [
        405,
        "co2-collection",
        "06/09/2024 15:19:05"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:19:05"
    ],
    [
        427,
        "luz-collection",
        "06/09/2024 15:19:05"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:19:05"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:19:06"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:19:06"
    ],
    [
        403,
        "co2-collection",
        "06/09/2024 15:19:07"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:19:07"
    ],
    [
        363,
        "luz-collection",
        "06/09/2024 15:19:07"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:19:07"
    ],
    [
        403,
        "co2-collection",
        "06/09/2024 15:19:08"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:19:08"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:19:08"
    ],
    [
        383,
        "luz-collection",
        "06/09/2024 15:19:08"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:19:08"
    ],
    [
        413,
        "co2-collection",
        "06/09/2024 15:19:09"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:19:09"
    ],
    [
        422,
        "luz-collection",
        "06/09/2024 15:19:09"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:19:09"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:19:10"
    ],
    [
        405,
        "co2-collection",
        "06/09/2024 15:19:11"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:19:11"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:19:11"
    ],
    [
        414,
        "luz-collection",
        "06/09/2024 15:19:11"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:19:11"
    ],
    [
        405,
        "co2-collection",
        "06/09/2024 15:19:12"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:19:12"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:19:12"
    ],
    [
        413,
        "luz-collection",
        "06/09/2024 15:19:12"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:19:12"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:19:13"
    ],
    [
        456,
        "luz-collection",
        "06/09/2024 15:19:13"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:19:13"
    ],
    [
        404,
        "co2-collection",
        "06/09/2024 15:19:14"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:19:14"
    ],
    [
        404,
        "co2-collection",
        "06/09/2024 15:19:15"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:19:15"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:19:15"
    ],
    [
        354,
        "luz-collection",
        "06/09/2024 15:19:15"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:19:15"
    ],
    [
        404,
        "co2-collection",
        "06/09/2024 15:19:16"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:19:16"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:19:16"
    ],
    [
        426,
        "luz-collection",
        "06/09/2024 15:19:16"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:19:16"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:19:17"
    ],
    [
        372,
        "luz-collection",
        "06/09/2024 15:19:17"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:19:17"
    ],
    [
        404,
        "co2-collection",
        "06/09/2024 15:19:18"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:19:18"
    ],
    [
        404,
        "co2-collection",
        "06/09/2024 15:19:19"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:19:19"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:19:19"
    ],
    [
        397,
        "luz-collection",
        "06/09/2024 15:19:19"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:19:19"
    ],
    [
        404,
        "co2-collection",
        "06/09/2024 15:19:20"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:19:20"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:19:20"
    ],
    [
        438,
        "luz-collection",
        "06/09/2024 15:19:20"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:19:20"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:19:21"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:19:21"
    ],
    [
        403,
        "co2-collection",
        "06/09/2024 15:19:22"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:19:22"
    ],
    [
        428,
        "luz-collection",
        "06/09/2024 15:19:22"
    ],
    [
        402,
        "co2-collection",
        "06/09/2024 15:19:23"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:19:23"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:19:23"
    ],
    [
        438,
        "luz-collection",
        "06/09/2024 15:19:23"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:19:23"
    ],
    [
        404,
        "co2-collection",
        "06/09/2024 15:19:24"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:19:24"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:19:24"
    ],
    [
        471,
        "luz-collection",
        "06/09/2024 15:19:24"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:19:24"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:19:25"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:19:25"
    ],
    [
        404,
        "co2-collection",
        "06/09/2024 15:19:26"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:19:26"
    ],
    [
        375,
        "luz-collection",
        "06/09/2024 15:19:26"
    ],
    [
        403,
        "co2-collection",
        "06/09/2024 15:19:27"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:19:27"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:19:27"
    ],
    [
        438,
        "luz-collection",
        "06/09/2024 15:19:27"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:19:27"
    ],
    [
        404,
        "co2-collection",
        "06/09/2024 15:19:28"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:19:28"
    ],
    [
        355,
        "luz-collection",
        "06/09/2024 15:19:28"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:19:28"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:19:29"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:19:29"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:19:29"
    ],
    [
        404,
        "co2-collection",
        "06/09/2024 15:19:30"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:19:30"
    ],
    [
        384,
        "luz-collection",
        "06/09/2024 15:19:30"
    ],
    [
        404,
        "co2-collection",
        "06/09/2024 15:19:31"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:19:31"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:19:31"
    ],
    [
        405,
        "luz-collection",
        "06/09/2024 15:19:31"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:19:31"
    ],
    [
        421,
        "co2-collection",
        "06/09/2024 15:19:32"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:19:32"
    ],
    [
        395,
        "luz-collection",
        "06/09/2024 15:19:32"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:19:32"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:19:33"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:19:33"
    ],
    [
        418,
        "co2-collection",
        "06/09/2024 15:19:34"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:19:34"
    ],
    [
        420,
        "luz-collection",
        "06/09/2024 15:19:34"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:19:34"
    ],
    [
        404,
        "co2-collection",
        "06/09/2024 15:19:35"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:19:35"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:19:35"
    ],
    [
        442,
        "luz-collection",
        "06/09/2024 15:19:35"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:19:35"
    ],
    [
        404,
        "co2-collection",
        "06/09/2024 15:19:36"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:19:36"
    ],
    [
        383,
        "luz-collection",
        "06/09/2024 15:19:36"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:19:36"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:19:37"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:19:37"
    ],
    [
        406,
        "co2-collection",
        "06/09/2024 15:19:38"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:19:38"
    ],
    [
        451,
        "luz-collection",
        "06/09/2024 15:19:38"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:19:38"
    ],
    [
        409,
        "co2-collection",
        "06/09/2024 15:19:39"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:19:39"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:19:39"
    ],
    [
        353,
        "luz-collection",
        "06/09/2024 15:19:39"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:19:39"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:19:40"
    ],
    [
        410,
        "luz-collection",
        "06/09/2024 15:19:40"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:19:40"
    ],
    [
        410,
        "co2-collection",
        "06/09/2024 15:19:41"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:19:41"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:19:41"
    ],
    [
        422,
        "co2-collection",
        "06/09/2024 15:19:42"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:19:42"
    ],
    [
        393,
        "luz-collection",
        "06/09/2024 15:19:42"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:19:42"
    ],
    [
        405,
        "co2-collection",
        "06/09/2024 15:19:43"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:19:43"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:19:43"
    ],
    [
        392,
        "luz-collection",
        "06/09/2024 15:19:43"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:19:43"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:19:44"
    ],
    [
        431,
        "luz-collection",
        "06/09/2024 15:19:44"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:19:44"
    ],
    [
        402,
        "co2-collection",
        "06/09/2024 15:19:45"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:19:45"
    ],
    [
        402,
        "co2-collection",
        "06/09/2024 15:19:46"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:19:46"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:19:46"
    ],
    [
        449,
        "luz-collection",
        "06/09/2024 15:19:46"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:19:46"
    ],
    [
        402,
        "co2-collection",
        "06/09/2024 15:19:47"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:19:47"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:19:47"
    ],
    [
        374,
        "luz-collection",
        "06/09/2024 15:19:47"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:19:47"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:19:48"
    ],
    [
        436,
        "luz-collection",
        "06/09/2024 15:19:48"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:19:48"
    ],
    [
        401,
        "co2-collection",
        "06/09/2024 15:19:49"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:19:49"
    ],
    [
        402,
        "co2-collection",
        "06/09/2024 15:19:50"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:19:50"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:19:50"
    ],
    [
        357,
        "luz-collection",
        "06/09/2024 15:19:50"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:19:50"
    ],
    [
        405,
        "co2-collection",
        "06/09/2024 15:19:51"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:19:51"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:19:51"
    ],
    [
        383,
        "luz-collection",
        "06/09/2024 15:19:51"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:19:51"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:19:52"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:19:52"
    ],
    [
        413,
        "co2-collection",
        "06/09/2024 15:19:53"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:19:53"
    ],
    [
        426,
        "luz-collection",
        "06/09/2024 15:19:53"
    ],
    [
        414,
        "co2-collection",
        "06/09/2024 15:19:54"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:19:54"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:19:54"
    ],
    [
        423,
        "luz-collection",
        "06/09/2024 15:19:54"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:19:54"
    ],
    [
        419,
        "co2-collection",
        "06/09/2024 15:19:55"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:19:55"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:19:55"
    ],
    [
        407,
        "luz-collection",
        "06/09/2024 15:19:55"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:19:55"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:19:56"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:19:56"
    ],
    [
        409,
        "co2-collection",
        "06/09/2024 15:19:57"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:19:57"
    ],
    [
        454,
        "luz-collection",
        "06/09/2024 15:19:57"
    ],
    [
        409,
        "co2-collection",
        "06/09/2024 15:19:58"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:19:58"
    ],
    [
        74,
        "hum-collection",
        "06/09/2024 15:19:58"
    ],
    [
        349,
        "luz-collection",
        "06/09/2024 15:19:58"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:19:58"
    ],
    [
        407,
        "co2-collection",
        "06/09/2024 15:19:59"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:19:59"
    ],
    [
        423,
        "luz-collection",
        "06/09/2024 15:19:59"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:19:59"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:20:00"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:20:00"
    ],
    [
        409,
        "co2-collection",
        "06/09/2024 15:20:01"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:20:01"
    ],
    [
        370,
        "luz-collection",
        "06/09/2024 15:20:01"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:20:01"
    ],
    [
        406,
        "co2-collection",
        "06/09/2024 15:20:02"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:20:02"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:20:02"
    ],
    [
        385,
        "luz-collection",
        "06/09/2024 15:20:02"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:20:02"
    ],
    [
        406,
        "co2-collection",
        "06/09/2024 15:20:03"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:20:03"
    ],
    [
        423,
        "luz-collection",
        "06/09/2024 15:20:03"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:20:03"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:20:04"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:20:04"
    ],
    [
        409,
        "co2-collection",
        "06/09/2024 15:20:05"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:20:05"
    ],
    [
        411,
        "luz-collection",
        "06/09/2024 15:20:05"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:20:05"
    ],
    [
        412,
        "co2-collection",
        "06/09/2024 15:20:06"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:20:06"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:20:06"
    ],
    [
        408,
        "luz-collection",
        "06/09/2024 15:20:06"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:20:06"
    ],
    [
        413,
        "co2-collection",
        "06/09/2024 15:20:07"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:20:07"
    ],
    [
        445,
        "luz-collection",
        "06/09/2024 15:20:07"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:20:07"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:20:08"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:20:08"
    ],
    [
        412,
        "co2-collection",
        "06/09/2024 15:20:09"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:20:09"
    ],
    [
        347,
        "luz-collection",
        "06/09/2024 15:20:09"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:20:09"
    ],
    [
        408,
        "co2-collection",
        "06/09/2024 15:20:10"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:20:10"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:20:10"
    ],
    [
        416,
        "luz-collection",
        "06/09/2024 15:20:10"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:20:10"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:20:11"
    ],
    [
        350,
        "luz-collection",
        "06/09/2024 15:20:11"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:20:11"
    ],
    [
        411,
        "co2-collection",
        "06/09/2024 15:20:12"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:20:12"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:20:12"
    ],
    [
        409,
        "co2-collection",
        "06/09/2024 15:20:13"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:20:13"
    ],
    [
        369,
        "luz-collection",
        "06/09/2024 15:20:13"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:20:13"
    ],
    [
        406,
        "co2-collection",
        "06/09/2024 15:20:14"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:20:14"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:20:14"
    ],
    [
        409,
        "luz-collection",
        "06/09/2024 15:20:14"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:20:14"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:20:15"
    ],
    [
        405,
        "luz-collection",
        "06/09/2024 15:20:15"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:20:15"
    ],
    [
        408,
        "co2-collection",
        "06/09/2024 15:20:16"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:20:16"
    ],
    [
        406,
        "co2-collection",
        "06/09/2024 15:20:17"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:20:17"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:20:17"
    ],
    [
        394,
        "luz-collection",
        "06/09/2024 15:20:17"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:20:17"
    ],
    [
        409,
        "co2-collection",
        "06/09/2024 15:20:18"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:20:18"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:20:18"
    ],
    [
        442,
        "luz-collection",
        "06/09/2024 15:20:18"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:20:18"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:20:19"
    ],
    [
        335,
        "luz-collection",
        "06/09/2024 15:20:19"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:20:19"
    ],
    [
        408,
        "co2-collection",
        "06/09/2024 15:20:20"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:20:20"
    ],
    [
        409,
        "co2-collection",
        "06/09/2024 15:20:21"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:20:21"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:20:21"
    ],
    [
        402,
        "luz-collection",
        "06/09/2024 15:20:21"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:20:21"
    ],
    [
        409,
        "co2-collection",
        "06/09/2024 15:20:22"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:20:22"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:20:22"
    ],
    [
        368,
        "luz-collection",
        "06/09/2024 15:20:22"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:20:22"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:20:23"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:20:23"
    ],
    [
        406,
        "co2-collection",
        "06/09/2024 15:20:24"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:20:24"
    ],
    [
        377,
        "luz-collection",
        "06/09/2024 15:20:24"
    ],
    [
        406,
        "co2-collection",
        "06/09/2024 15:20:25"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:20:25"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:20:25"
    ],
    [
        424,
        "luz-collection",
        "06/09/2024 15:20:25"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:20:25"
    ],
    [
        407,
        "co2-collection",
        "06/09/2024 15:20:26"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:20:26"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:20:26"
    ],
    [
        420,
        "luz-collection",
        "06/09/2024 15:20:26"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:20:26"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:20:27"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:20:27"
    ],
    [
        407,
        "co2-collection",
        "06/09/2024 15:20:28"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:20:28"
    ],
    [
        383,
        "luz-collection",
        "06/09/2024 15:20:28"
    ],
    [
        407,
        "co2-collection",
        "06/09/2024 15:20:29"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:20:29"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:20:29"
    ],
    [
        438,
        "luz-collection",
        "06/09/2024 15:20:29"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:20:29"
    ],
    [
        407,
        "co2-collection",
        "06/09/2024 15:20:30"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:20:30"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:20:30"
    ],
    [
        330,
        "luz-collection",
        "06/09/2024 15:20:30"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:20:30"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:20:31"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:20:31"
    ],
    [
        407,
        "co2-collection",
        "06/09/2024 15:20:32"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:20:32"
    ],
    [
        390,
        "luz-collection",
        "06/09/2024 15:20:32"
    ],
    [
        406,
        "co2-collection",
        "06/09/2024 15:20:33"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:20:33"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:20:33"
    ],
    [
        379,
        "luz-collection",
        "06/09/2024 15:20:33"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:20:33"
    ],
    [
        406,
        "co2-collection",
        "06/09/2024 15:20:34"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:20:34"
    ],
    [
        382,
        "luz-collection",
        "06/09/2024 15:20:34"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:20:34"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:20:35"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:20:35"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:20:35"
    ],
    [
        408,
        "co2-collection",
        "06/09/2024 15:20:36"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:20:36"
    ],
    [
        414,
        "luz-collection",
        "06/09/2024 15:20:36"
    ],
    [
        407,
        "co2-collection",
        "06/09/2024 15:20:37"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:20:37"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:20:37"
    ],
    [
        438,
        "luz-collection",
        "06/09/2024 15:20:37"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:20:37"
    ],
    [
        407,
        "co2-collection",
        "06/09/2024 15:20:38"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:20:38"
    ],
    [
        364,
        "luz-collection",
        "06/09/2024 15:20:38"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:20:38"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:20:39"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:20:39"
    ],
    [
        407,
        "co2-collection",
        "06/09/2024 15:20:40"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:20:40"
    ],
    [
        433,
        "luz-collection",
        "06/09/2024 15:20:40"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:20:40"
    ],
    [
        407,
        "co2-collection",
        "06/09/2024 15:20:41"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:20:41"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:20:41"
    ],
    [
        357,
        "luz-collection",
        "06/09/2024 15:20:41"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:20:41"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:20:42"
    ],
    [
        384,
        "luz-collection",
        "06/09/2024 15:20:42"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:20:42"
    ],
    [
        405,
        "co2-collection",
        "06/09/2024 15:20:43"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:20:43"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:20:43"
    ],
    [
        401,
        "co2-collection",
        "06/09/2024 15:20:44"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:20:44"
    ],
    [
        425,
        "luz-collection",
        "06/09/2024 15:20:44"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:20:44"
    ],
    [
        404,
        "co2-collection",
        "06/09/2024 15:20:45"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:20:45"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:20:45"
    ],
    [
        422,
        "luz-collection",
        "06/09/2024 15:20:45"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:20:45"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:20:46"
    ],
    [
        405,
        "luz-collection",
        "06/09/2024 15:20:46"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:20:46"
    ],
    [
        403,
        "co2-collection",
        "06/09/2024 15:20:47"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:20:47"
    ],
    [
        403,
        "co2-collection",
        "06/09/2024 15:20:48"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:20:48"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:20:48"
    ],
    [
        453,
        "luz-collection",
        "06/09/2024 15:20:48"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:20:48"
    ],
    [
        397,
        "co2-collection",
        "06/09/2024 15:20:49"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:20:49"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:20:49"
    ],
    [
        343,
        "luz-collection",
        "06/09/2024 15:20:49"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:20:49"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:20:50"
    ],
    [
        397,
        "luz-collection",
        "06/09/2024 15:20:50"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:20:50"
    ],
    [
        405,
        "co2-collection",
        "06/09/2024 15:20:51"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:20:51"
    ],
    [
        407,
        "co2-collection",
        "06/09/2024 15:20:52"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:20:52"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:20:52"
    ],
    [
        395,
        "luz-collection",
        "06/09/2024 15:20:52"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:20:52"
    ],
    [
        408,
        "co2-collection",
        "06/09/2024 15:20:53"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:20:53"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:20:53"
    ],
    [
        393,
        "luz-collection",
        "06/09/2024 15:20:53"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:20:53"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:20:54"
    ],
    [
        414,
        "luz-collection",
        "06/09/2024 15:20:54"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:20:54"
    ],
    [
        402,
        "co2-collection",
        "06/09/2024 15:20:55"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:20:55"
    ],
    [
        404,
        "co2-collection",
        "06/09/2024 15:20:56"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:20:56"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:20:56"
    ],
    [
        448,
        "luz-collection",
        "06/09/2024 15:20:56"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:20:56"
    ],
    [
        404,
        "co2-collection",
        "06/09/2024 15:20:57"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:20:57"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:20:57"
    ],
    [
        349,
        "luz-collection",
        "06/09/2024 15:20:57"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:20:57"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:20:58"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:20:58"
    ],
    [
        403,
        "co2-collection",
        "06/09/2024 15:20:59"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:20:59"
    ],
    [
        416,
        "luz-collection",
        "06/09/2024 15:20:59"
    ],
    [
        405,
        "co2-collection",
        "06/09/2024 15:21:00"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:21:00"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:21:00"
    ],
    [
        364,
        "luz-collection",
        "06/09/2024 15:21:00"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:21:00"
    ],
    [
        405,
        "co2-collection",
        "06/09/2024 15:21:01"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:21:01"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:21:01"
    ],
    [
        374,
        "luz-collection",
        "06/09/2024 15:21:01"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:21:01"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:21:02"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:21:02"
    ],
    [
        403,
        "co2-collection",
        "06/09/2024 15:21:03"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:21:03"
    ],
    [
        423,
        "luz-collection",
        "06/09/2024 15:21:03"
    ],
    [
        405,
        "co2-collection",
        "06/09/2024 15:21:04"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:21:04"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:21:04"
    ],
    [
        421,
        "luz-collection",
        "06/09/2024 15:21:04"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:21:04"
    ],
    [
        405,
        "co2-collection",
        "06/09/2024 15:21:05"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:21:05"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:21:05"
    ],
    [
        386,
        "luz-collection",
        "06/09/2024 15:21:05"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:21:05"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:21:06"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:21:06"
    ],
    [
        405,
        "co2-collection",
        "06/09/2024 15:21:07"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:21:07"
    ],
    [
        444,
        "luz-collection",
        "06/09/2024 15:21:07"
    ],
    [
        405,
        "co2-collection",
        "06/09/2024 15:21:08"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:21:08"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:21:08"
    ],
    [
        346,
        "luz-collection",
        "06/09/2024 15:21:08"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:21:08"
    ],
    [
        411,
        "co2-collection",
        "06/09/2024 15:21:09"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:21:09"
    ],
    [
        397,
        "luz-collection",
        "06/09/2024 15:21:09"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:21:09"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:21:10"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:21:10"
    ],
    [
        408,
        "co2-collection",
        "06/09/2024 15:21:11"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:21:11"
    ],
    [
        418,
        "luz-collection",
        "06/09/2024 15:21:11"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:21:11"
    ],
    [
        410,
        "co2-collection",
        "06/09/2024 15:21:12"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:21:12"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:21:12"
    ],
    [
        421,
        "luz-collection",
        "06/09/2024 15:21:12"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:21:12"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:21:13"
    ],
    [
        430,
        "luz-collection",
        "06/09/2024 15:21:13"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:21:13"
    ],
    [
        404,
        "co2-collection",
        "06/09/2024 15:21:14"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:21:14"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:21:14"
    ],
    [
        406,
        "co2-collection",
        "06/09/2024 15:21:15"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:21:15"
    ],
    [
        484,
        "luz-collection",
        "06/09/2024 15:21:15"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:21:15"
    ],
    [
        408,
        "co2-collection",
        "06/09/2024 15:21:16"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:21:16"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:21:16"
    ],
    [
        373,
        "luz-collection",
        "06/09/2024 15:21:16"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:21:16"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:21:17"
    ],
    [
        438,
        "luz-collection",
        "06/09/2024 15:21:17"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:21:17"
    ],
    [
        406,
        "co2-collection",
        "06/09/2024 15:21:18"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:21:18"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:21:18"
    ],
    [
        406,
        "co2-collection",
        "06/09/2024 15:21:19"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:21:19"
    ],
    [
        429,
        "luz-collection",
        "06/09/2024 15:21:19"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:21:19"
    ],
    [
        407,
        "co2-collection",
        "06/09/2024 15:21:20"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:21:20"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:21:20"
    ],
    [
        433,
        "luz-collection",
        "06/09/2024 15:21:20"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:21:20"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:21:21"
    ],
    [
        463,
        "luz-collection",
        "06/09/2024 15:21:21"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:21:21"
    ],
    [
        410,
        "co2-collection",
        "06/09/2024 15:21:22"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:21:22"
    ],
    [
        409,
        "co2-collection",
        "06/09/2024 15:21:23"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:21:23"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:21:23"
    ],
    [
        498,
        "luz-collection",
        "06/09/2024 15:21:23"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:21:23"
    ],
    [
        408,
        "co2-collection",
        "06/09/2024 15:21:24"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:21:24"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:21:24"
    ],
    [
        388,
        "luz-collection",
        "06/09/2024 15:21:24"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:21:24"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:21:25"
    ],
    [
        445,
        "luz-collection",
        "06/09/2024 15:21:25"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:21:25"
    ],
    [
        409,
        "co2-collection",
        "06/09/2024 15:21:26"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:21:26"
    ],
    [
        410,
        "co2-collection",
        "06/09/2024 15:21:27"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:21:27"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:21:27"
    ],
    [
        447,
        "luz-collection",
        "06/09/2024 15:21:27"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:21:27"
    ],
    [
        409,
        "co2-collection",
        "06/09/2024 15:21:28"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:21:28"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:21:28"
    ],
    [
        457,
        "luz-collection",
        "06/09/2024 15:21:28"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:21:28"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:21:29"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:21:29"
    ],
    [
        407,
        "co2-collection",
        "06/09/2024 15:21:30"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:21:30"
    ],
    [
        452,
        "luz-collection",
        "06/09/2024 15:21:30"
    ],
    [
        406,
        "co2-collection",
        "06/09/2024 15:21:31"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:21:31"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:21:31"
    ],
    [
        494,
        "luz-collection",
        "06/09/2024 15:21:31"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:21:31"
    ],
    [
        406,
        "co2-collection",
        "06/09/2024 15:21:32"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:21:32"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:21:32"
    ],
    [
        392,
        "luz-collection",
        "06/09/2024 15:21:32"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:21:32"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:21:33"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:21:33"
    ],
    [
        406,
        "co2-collection",
        "06/09/2024 15:21:34"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:21:34"
    ],
    [
        433,
        "luz-collection",
        "06/09/2024 15:21:34"
    ],
    [
        407,
        "co2-collection",
        "06/09/2024 15:21:35"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:21:35"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:21:35"
    ],
    [
        468,
        "luz-collection",
        "06/09/2024 15:21:35"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:21:35"
    ],
    [
        407,
        "co2-collection",
        "06/09/2024 15:21:36"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:21:36"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:21:36"
    ],
    [
        474,
        "luz-collection",
        "06/09/2024 15:21:36"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:21:36"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:21:37"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:21:37"
    ],
    [
        406,
        "co2-collection",
        "06/09/2024 15:21:38"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:21:38"
    ],
    [
        417,
        "luz-collection",
        "06/09/2024 15:21:38"
    ],
    [
        404,
        "co2-collection",
        "06/09/2024 15:21:39"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:21:39"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:21:39"
    ],
    [
        465,
        "luz-collection",
        "06/09/2024 15:21:39"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:21:39"
    ],
    [
        404,
        "co2-collection",
        "06/09/2024 15:21:40"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:21:40"
    ],
    [
        392,
        "luz-collection",
        "06/09/2024 15:21:40"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:21:40"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:21:41"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:21:41"
    ],
    [
        405,
        "co2-collection",
        "06/09/2024 15:21:42"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:21:42"
    ],
    [
        408,
        "luz-collection",
        "06/09/2024 15:21:42"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:21:42"
    ],
    [
        406,
        "co2-collection",
        "06/09/2024 15:21:43"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:21:43"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:21:43"
    ],
    [
        442,
        "luz-collection",
        "06/09/2024 15:21:43"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:21:43"
    ],
    [
        409,
        "co2-collection",
        "06/09/2024 15:21:44"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:21:44"
    ],
    [
        463,
        "luz-collection",
        "06/09/2024 15:21:44"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:21:44"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:21:45"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:21:45"
    ],
    [
        408,
        "co2-collection",
        "06/09/2024 15:21:46"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:21:46"
    ],
    [
        353,
        "luz-collection",
        "06/09/2024 15:21:46"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:21:46"
    ],
    [
        407,
        "co2-collection",
        "06/09/2024 15:21:47"
    ],
    [
        0,
        "dist-collection",
        "06/09/2024 15:21:47"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:21:47"
    ],
    [
        407,
        "luz-collection",
        "06/09/2024 15:21:47"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:21:47"
    ],
    [
        408,
        "co2-collection",
        "06/09/2024 15:21:48"
    ],
    [
        73,
        "hum-collection",
        "06/09/2024 15:21:48"
    ],
    [
        399,
        "luz-collection",
        "06/09/2024 15:21:48"
    ],
    [
        25.8,
        "temp-collection",
        "06/09/2024 15:21:48"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:03:59"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:03:59"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:04:00"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:00"
    ],
    [
        853,
        "luz-collection",
        "06/09/2024 20:04:00"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:04:01"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:01"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:01"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:01"
    ],
    [
        638,
        "luz-collection",
        "06/09/2024 20:04:01"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:01"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:01"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:04:02"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:02"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:02"
    ],
    [
        641,
        "luz-collection",
        "06/09/2024 20:04:02"
    ],
    [
        584,
        "luz-collection",
        "06/09/2024 20:04:02"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:02"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:04:03"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:04:03"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:03"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:03"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:03"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:03"
    ],
    [
        565,
        "luz-collection",
        "06/09/2024 20:04:03"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:03"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:03"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:04:04"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:04:04"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:04"
    ],
    [
        15,
        "dist-collection",
        "06/09/2024 20:04:04"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:04"
    ],
    [
        576,
        "luz-collection",
        "06/09/2024 20:04:04"
    ],
    [
        641,
        "luz-collection",
        "06/09/2024 20:04:04"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:04"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:04:05"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:05"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:05"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:05"
    ],
    [
        585,
        "luz-collection",
        "06/09/2024 20:04:05"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:05"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:05"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:04:06"
    ],
    [
        393,
        "co2-collection",
        "06/09/2024 20:04:06"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:06"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:06"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:06"
    ],
    [
        610,
        "luz-collection",
        "06/09/2024 20:04:06"
    ],
    [
        632,
        "luz-collection",
        "06/09/2024 20:04:06"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:06"
    ],
    [
        394,
        "co2-collection",
        "06/09/2024 20:04:07"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:07"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:07"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:07"
    ],
    [
        585,
        "luz-collection",
        "06/09/2024 20:04:07"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:07"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:07"
    ],
    [
        393,
        "co2-collection",
        "06/09/2024 20:04:08"
    ],
    [
        393,
        "co2-collection",
        "06/09/2024 20:04:08"
    ],
    [
        15,
        "dist-collection",
        "06/09/2024 20:04:08"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:08"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:08"
    ],
    [
        645,
        "luz-collection",
        "06/09/2024 20:04:08"
    ],
    [
        644,
        "luz-collection",
        "06/09/2024 20:04:08"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:08"
    ],
    [
        394,
        "co2-collection",
        "06/09/2024 20:04:09"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:09"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:09"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:09"
    ],
    [
        630,
        "luz-collection",
        "06/09/2024 20:04:09"
    ],
    [
        614,
        "luz-collection",
        "06/09/2024 20:04:09"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:09"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:09"
    ],
    [
        395,
        "co2-collection",
        "06/09/2024 20:04:10"
    ],
    [
        394,
        "co2-collection",
        "06/09/2024 20:04:10"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:10"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:10"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:10"
    ],
    [
        611,
        "luz-collection",
        "06/09/2024 20:04:10"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:10"
    ],
    [
        393,
        "co2-collection",
        "06/09/2024 20:04:11"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:11"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:11"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:11"
    ],
    [
        586,
        "luz-collection",
        "06/09/2024 20:04:11"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:11"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:11"
    ],
    [
        394,
        "co2-collection",
        "06/09/2024 20:04:12"
    ],
    [
        394,
        "co2-collection",
        "06/09/2024 20:04:12"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:12"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:12"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:12"
    ],
    [
        562,
        "luz-collection",
        "06/09/2024 20:04:12"
    ],
    [
        648,
        "luz-collection",
        "06/09/2024 20:04:12"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:12"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:04:13"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:13"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:13"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:13"
    ],
    [
        567,
        "luz-collection",
        "06/09/2024 20:04:13"
    ],
    [
        588,
        "luz-collection",
        "06/09/2024 20:04:13"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:13"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:13"
    ],
    [
        395,
        "co2-collection",
        "06/09/2024 20:04:14"
    ],
    [
        397,
        "co2-collection",
        "06/09/2024 20:04:14"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:14"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:14"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:14"
    ],
    [
        614,
        "luz-collection",
        "06/09/2024 20:04:14"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:14"
    ],
    [
        395,
        "co2-collection",
        "06/09/2024 20:04:15"
    ],
    [
        15,
        "dist-collection",
        "06/09/2024 20:04:15"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:15"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:15"
    ],
    [
        585,
        "luz-collection",
        "06/09/2024 20:04:15"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:15"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:15"
    ],
    [
        397,
        "co2-collection",
        "06/09/2024 20:04:16"
    ],
    [
        395,
        "co2-collection",
        "06/09/2024 20:04:16"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:16"
    ],
    [
        15,
        "dist-collection",
        "06/09/2024 20:04:16"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:16"
    ],
    [
        640,
        "luz-collection",
        "06/09/2024 20:04:16"
    ],
    [
        639,
        "luz-collection",
        "06/09/2024 20:04:16"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:16"
    ],
    [
        395,
        "co2-collection",
        "06/09/2024 20:04:17"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:17"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:17"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:17"
    ],
    [
        617,
        "luz-collection",
        "06/09/2024 20:04:17"
    ],
    [
        627,
        "luz-collection",
        "06/09/2024 20:04:17"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:17"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:17"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 20:04:18"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 20:04:18"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:18"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:18"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:18"
    ],
    [
        586,
        "luz-collection",
        "06/09/2024 20:04:18"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:18"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:04:19"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:19"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:19"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:19"
    ],
    [
        561,
        "luz-collection",
        "06/09/2024 20:04:19"
    ],
    [
        572,
        "luz-collection",
        "06/09/2024 20:04:19"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:19"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:19"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:04:20"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:04:20"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:20"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:20"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:20"
    ],
    [
        621,
        "luz-collection",
        "06/09/2024 20:04:20"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:20"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:04:21"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:21"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:21"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:21"
    ],
    [
        603,
        "luz-collection",
        "06/09/2024 20:04:21"
    ],
    [
        634,
        "luz-collection",
        "06/09/2024 20:04:21"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:21"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:21"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:04:22"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:04:22"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:22"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:22"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:22"
    ],
    [
        642,
        "luz-collection",
        "06/09/2024 20:04:22"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:22"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:04:23"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:23"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:23"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:23"
    ],
    [
        628,
        "luz-collection",
        "06/09/2024 20:04:23"
    ],
    [
        593,
        "luz-collection",
        "06/09/2024 20:04:23"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:23"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:23"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:04:24"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:04:24"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:24"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:24"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:24"
    ],
    [
        599,
        "luz-collection",
        "06/09/2024 20:04:24"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:24"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:04:25"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:25"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:25"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:25"
    ],
    [
        648,
        "luz-collection",
        "06/09/2024 20:04:25"
    ],
    [
        568,
        "luz-collection",
        "06/09/2024 20:04:25"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:25"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:25"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:04:26"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:04:26"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:26"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:26"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:26"
    ],
    [
        564,
        "luz-collection",
        "06/09/2024 20:04:26"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:26"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:04:27"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:27"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:27"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:27"
    ],
    [
        582,
        "luz-collection",
        "06/09/2024 20:04:27"
    ],
    [
        611,
        "luz-collection",
        "06/09/2024 20:04:27"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:27"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:27"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:04:28"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:04:28"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:28"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:28"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:28"
    ],
    [
        589,
        "luz-collection",
        "06/09/2024 20:04:28"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:28"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:04:29"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:29"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:29"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:29"
    ],
    [
        642,
        "luz-collection",
        "06/09/2024 20:04:29"
    ],
    [
        636,
        "luz-collection",
        "06/09/2024 20:04:29"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:29"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:29"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:04:30"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:04:30"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:30"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:30"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:30"
    ],
    [
        627,
        "luz-collection",
        "06/09/2024 20:04:30"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:30"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:04:31"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:31"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:31"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:31"
    ],
    [
        602,
        "luz-collection",
        "06/09/2024 20:04:31"
    ],
    [
        614,
        "luz-collection",
        "06/09/2024 20:04:31"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:31"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:31"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:04:32"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:04:32"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:32"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:32"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:32"
    ],
    [
        576,
        "luz-collection",
        "06/09/2024 20:04:32"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:32"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:04:33"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:33"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:33"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:33"
    ],
    [
        562,
        "luz-collection",
        "06/09/2024 20:04:33"
    ],
    [
        642,
        "luz-collection",
        "06/09/2024 20:04:33"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:33"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:33"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:04:34"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:04:34"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:34"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:34"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:34"
    ],
    [
        573,
        "luz-collection",
        "06/09/2024 20:04:34"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:34"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:04:35"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:35"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:35"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:35"
    ],
    [
        631,
        "luz-collection",
        "06/09/2024 20:04:35"
    ],
    [
        600,
        "luz-collection",
        "06/09/2024 20:04:35"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:35"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:35"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:04:36"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:04:36"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:36"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:36"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:36"
    ],
    [
        581,
        "luz-collection",
        "06/09/2024 20:04:36"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:36"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:04:37"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:37"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:37"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:37"
    ],
    [
        643,
        "luz-collection",
        "06/09/2024 20:04:37"
    ],
    [
        631,
        "luz-collection",
        "06/09/2024 20:04:37"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:37"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:37"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:04:38"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:04:38"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:38"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:38"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:38"
    ],
    [
        602,
        "luz-collection",
        "06/09/2024 20:04:38"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:38"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:04:39"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:39"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:39"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:39"
    ],
    [
        638,
        "luz-collection",
        "06/09/2024 20:04:39"
    ],
    [
        573,
        "luz-collection",
        "06/09/2024 20:04:39"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:39"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:39"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:04:40"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:04:40"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:40"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:40"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:40"
    ],
    [
        562,
        "luz-collection",
        "06/09/2024 20:04:40"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:40"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 20:04:41"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:41"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:41"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:41"
    ],
    [
        580,
        "luz-collection",
        "06/09/2024 20:04:41"
    ],
    [
        616,
        "luz-collection",
        "06/09/2024 20:04:41"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:41"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:41"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:04:42"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:04:42"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:42"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:42"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:42"
    ],
    [
        604,
        "luz-collection",
        "06/09/2024 20:04:42"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:42"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:04:43"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:43"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:43"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:43"
    ],
    [
        635,
        "luz-collection",
        "06/09/2024 20:04:43"
    ],
    [
        641,
        "luz-collection",
        "06/09/2024 20:04:43"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:43"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:43"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:04:44"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:04:44"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:44"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:44"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:44"
    ],
    [
        593,
        "luz-collection",
        "06/09/2024 20:04:44"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:44"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:04:45"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:45"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:45"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:45"
    ],
    [
        600,
        "luz-collection",
        "06/09/2024 20:04:45"
    ],
    [
        628,
        "luz-collection",
        "06/09/2024 20:04:45"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:45"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:45"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:04:46"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 20:04:46"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:46"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:46"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:46"
    ],
    [
        571,
        "luz-collection",
        "06/09/2024 20:04:46"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:46"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 20:04:47"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:47"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:47"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:47"
    ],
    [
        561,
        "luz-collection",
        "06/09/2024 20:04:47"
    ],
    [
        650,
        "luz-collection",
        "06/09/2024 20:04:47"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:47"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:47"
    ],
    [
        397,
        "co2-collection",
        "06/09/2024 20:04:48"
    ],
    [
        393,
        "co2-collection",
        "06/09/2024 20:04:48"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:48"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:48"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:48"
    ],
    [
        575,
        "luz-collection",
        "06/09/2024 20:04:48"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:48"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:04:49"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:49"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:49"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:49"
    ],
    [
        602,
        "luz-collection",
        "06/09/2024 20:04:49"
    ],
    [
        597,
        "luz-collection",
        "06/09/2024 20:04:49"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:49"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:49"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 20:04:50"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 20:04:50"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:50"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:50"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:50"
    ],
    [
        629,
        "luz-collection",
        "06/09/2024 20:04:50"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:50"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:04:51"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:04:51"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:51"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:51"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:51"
    ],
    [
        645,
        "luz-collection",
        "06/09/2024 20:04:51"
    ],
    [
        634,
        "luz-collection",
        "06/09/2024 20:04:51"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:51"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:51"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:04:52"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:52"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:52"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:52"
    ],
    [
        607,
        "luz-collection",
        "06/09/2024 20:04:52"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:52"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:04:53"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:53"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:53"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:53"
    ],
    [
        586,
        "luz-collection",
        "06/09/2024 20:04:53"
    ],
    [
        612,
        "luz-collection",
        "06/09/2024 20:04:53"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:53"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:53"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:04:54"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:04:54"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:54"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:54"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:54"
    ],
    [
        561,
        "luz-collection",
        "06/09/2024 20:04:54"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:54"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:04:55"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:55"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:55"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:55"
    ],
    [
        646,
        "luz-collection",
        "06/09/2024 20:04:55"
    ],
    [
        568,
        "luz-collection",
        "06/09/2024 20:04:55"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:55"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:55"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:04:56"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:04:56"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:56"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:56"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:56"
    ],
    [
        589,
        "luz-collection",
        "06/09/2024 20:04:56"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:56"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:04:57"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:57"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:57"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:57"
    ],
    [
        617,
        "luz-collection",
        "06/09/2024 20:04:57"
    ],
    [
        585,
        "luz-collection",
        "06/09/2024 20:04:57"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:57"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:57"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:04:58"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:04:58"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:58"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:58"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:58"
    ],
    [
        639,
        "luz-collection",
        "06/09/2024 20:04:58"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:58"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:04:59"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:04:59"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:59"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:04:59"
    ],
    [
        642,
        "luz-collection",
        "06/09/2024 20:04:59"
    ],
    [
        629,
        "luz-collection",
        "06/09/2024 20:04:59"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:59"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:04:59"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:05:00"
    ],
    [
        394,
        "co2-collection",
        "06/09/2024 20:05:00"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:00"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:00"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:00"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:00"
    ],
    [
        609,
        "luz-collection",
        "06/09/2024 20:05:00"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:00"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:05:01"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:05:01"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:01"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:01"
    ],
    [
        616,
        "luz-collection",
        "06/09/2024 20:05:01"
    ],
    [
        595,
        "luz-collection",
        "06/09/2024 20:05:01"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:01"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:01"
    ],
    [
        394,
        "co2-collection",
        "06/09/2024 20:05:02"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:02"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:02"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:02"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:02"
    ],
    [
        572,
        "luz-collection",
        "06/09/2024 20:05:02"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:02"
    ],
    [
        394,
        "co2-collection",
        "06/09/2024 20:05:03"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:03"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:03"
    ],
    [
        651,
        "luz-collection",
        "06/09/2024 20:05:03"
    ],
    [
        566,
        "luz-collection",
        "06/09/2024 20:05:03"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:03"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:03"
    ],
    [
        393,
        "co2-collection",
        "06/09/2024 20:05:04"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:05:04"
    ],
    [
        15,
        "dist-collection",
        "06/09/2024 20:05:04"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:04"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:04"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:04"
    ],
    [
        564,
        "luz-collection",
        "06/09/2024 20:05:04"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:04"
    ],
    [
        394,
        "co2-collection",
        "06/09/2024 20:05:05"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:05"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:05"
    ],
    [
        623,
        "luz-collection",
        "06/09/2024 20:05:05"
    ],
    [
        574,
        "luz-collection",
        "06/09/2024 20:05:05"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:05"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:05"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:05:06"
    ],
    [
        396,
        "co2-collection",
        "06/09/2024 20:05:06"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:06"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:06"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:06"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:06"
    ],
    [
        580,
        "luz-collection",
        "06/09/2024 20:05:06"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:06"
    ],
    [
        397,
        "co2-collection",
        "06/09/2024 20:05:07"
    ],
    [
        396,
        "co2-collection",
        "06/09/2024 20:05:07"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:07"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:07"
    ],
    [
        622,
        "luz-collection",
        "06/09/2024 20:05:07"
    ],
    [
        602,
        "luz-collection",
        "06/09/2024 20:05:07"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:07"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:07"
    ],
    [
        397,
        "co2-collection",
        "06/09/2024 20:05:08"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:08"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:08"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:08"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:08"
    ],
    [
        588,
        "luz-collection",
        "06/09/2024 20:05:08"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:08"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 20:05:09"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:05:09"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:09"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:09"
    ],
    [
        631,
        "luz-collection",
        "06/09/2024 20:05:09"
    ],
    [
        645,
        "luz-collection",
        "06/09/2024 20:05:09"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:09"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:09"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 20:05:10"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:10"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:10"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:10"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:10"
    ],
    [
        640,
        "luz-collection",
        "06/09/2024 20:05:10"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:10"
    ],
    [
        397,
        "co2-collection",
        "06/09/2024 20:05:11"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:05:11"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:11"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:11"
    ],
    [
        634,
        "luz-collection",
        "06/09/2024 20:05:11"
    ],
    [
        594,
        "luz-collection",
        "06/09/2024 20:05:11"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:11"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:11"
    ],
    [
        401,
        "co2-collection",
        "06/09/2024 20:05:12"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:12"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:12"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:12"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:12"
    ],
    [
        613,
        "luz-collection",
        "06/09/2024 20:05:12"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:12"
    ],
    [
        394,
        "co2-collection",
        "06/09/2024 20:05:13"
    ],
    [
        398,
        "co2-collection",
        "06/09/2024 20:05:13"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:13"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:13"
    ],
    [
        642,
        "luz-collection",
        "06/09/2024 20:05:13"
    ],
    [
        590,
        "luz-collection",
        "06/09/2024 20:05:13"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:13"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:13"
    ],
    [
        394,
        "co2-collection",
        "06/09/2024 20:05:14"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:14"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:14"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:14"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:14"
    ],
    [
        578,
        "luz-collection",
        "06/09/2024 20:05:14"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:14"
    ],
    [
        401,
        "co2-collection",
        "06/09/2024 20:05:15"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:15"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:15"
    ],
    [
        561,
        "luz-collection",
        "06/09/2024 20:05:15"
    ],
    [
        566,
        "luz-collection",
        "06/09/2024 20:05:15"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:15"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:15"
    ],
    [
        399,
        "co2-collection",
        "06/09/2024 20:05:16"
    ],
    [
        400,
        "co2-collection",
        "06/09/2024 20:05:16"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:16"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:16"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:16"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:16"
    ],
    [
        641,
        "luz-collection",
        "06/09/2024 20:05:16"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:16"
    ],
    [
        397,
        "co2-collection",
        "06/09/2024 20:05:17"
    ],
    [
        394,
        "co2-collection",
        "06/09/2024 20:05:17"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:17"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:17"
    ],
    [
        567,
        "luz-collection",
        "06/09/2024 20:05:17"
    ],
    [
        584,
        "luz-collection",
        "06/09/2024 20:05:17"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:17"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:17"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:05:18"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:18"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:18"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:18"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:18"
    ],
    [
        603,
        "luz-collection",
        "06/09/2024 20:05:18"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:18"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 20:05:19"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 20:05:19"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:19"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:19"
    ],
    [
        607,
        "luz-collection",
        "06/09/2024 20:05:19"
    ],
    [
        608,
        "luz-collection",
        "06/09/2024 20:05:19"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:19"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:19"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:05:20"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:20"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:20"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:20"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:20"
    ],
    [
        627,
        "luz-collection",
        "06/09/2024 20:05:20"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:20"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 20:05:21"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 20:05:21"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:21"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:21"
    ],
    [
        581,
        "luz-collection",
        "06/09/2024 20:05:21"
    ],
    [
        642,
        "luz-collection",
        "06/09/2024 20:05:21"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:21"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:21"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 20:05:22"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:22"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:22"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:22"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:22"
    ],
    [
        643,
        "luz-collection",
        "06/09/2024 20:05:22"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:22"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:05:23"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:05:23"
    ],
    [
        15,
        "dist-collection",
        "06/09/2024 20:05:23"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:23"
    ],
    [
        638,
        "luz-collection",
        "06/09/2024 20:05:23"
    ],
    [
        623,
        "luz-collection",
        "06/09/2024 20:05:23"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:23"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:23"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:05:24"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:24"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:24"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:24"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:24"
    ],
    [
        610,
        "luz-collection",
        "06/09/2024 20:05:24"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:24"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 20:05:25"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 20:05:25"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:25"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:25"
    ],
    [
        615,
        "luz-collection",
        "06/09/2024 20:05:25"
    ],
    [
        594,
        "luz-collection",
        "06/09/2024 20:05:25"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:25"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:25"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:05:26"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:26"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:26"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:26"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:26"
    ],
    [
        572,
        "luz-collection",
        "06/09/2024 20:05:26"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:26"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 20:05:27"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:05:27"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:27"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:27"
    ],
    [
        565,
        "luz-collection",
        "06/09/2024 20:05:27"
    ],
    [
        650,
        "luz-collection",
        "06/09/2024 20:05:27"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:27"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:27"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:05:28"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:28"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:28"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:28"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:28"
    ],
    [
        564,
        "luz-collection",
        "06/09/2024 20:05:28"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:28"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:05:29"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:05:29"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:29"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:29"
    ],
    [
        627,
        "luz-collection",
        "06/09/2024 20:05:29"
    ],
    [
        574,
        "luz-collection",
        "06/09/2024 20:05:29"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:29"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:29"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:05:30"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:30"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:30"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:30"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:30"
    ],
    [
        584,
        "luz-collection",
        "06/09/2024 20:05:30"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:30"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:05:31"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 20:05:31"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:31"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:31"
    ],
    [
        606,
        "luz-collection",
        "06/09/2024 20:05:31"
    ],
    [
        628,
        "luz-collection",
        "06/09/2024 20:05:31"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:31"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:31"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 20:05:32"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:32"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:32"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:32"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:32"
    ],
    [
        580,
        "luz-collection",
        "06/09/2024 20:05:32"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:32"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:05:33"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:05:33"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:33"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:33"
    ],
    [
        642,
        "luz-collection",
        "06/09/2024 20:05:33"
    ],
    [
        639,
        "luz-collection",
        "06/09/2024 20:05:33"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:33"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:33"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 20:05:34"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:34"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:34"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:34"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:34"
    ],
    [
        631,
        "luz-collection",
        "06/09/2024 20:05:34"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:34"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 20:05:35"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 20:05:35"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:35"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:35"
    ],
    [
        604,
        "luz-collection",
        "06/09/2024 20:05:35"
    ],
    [
        621,
        "luz-collection",
        "06/09/2024 20:05:35"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:35"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:35"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:05:36"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:36"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:36"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:36"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:36"
    ],
    [
        600,
        "luz-collection",
        "06/09/2024 20:05:36"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:36"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:05:37"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:05:37"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:37"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:37"
    ],
    [
        574,
        "luz-collection",
        "06/09/2024 20:05:37"
    ],
    [
        650,
        "luz-collection",
        "06/09/2024 20:05:37"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:37"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:37"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:05:38"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:38"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:38"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:38"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:38"
    ],
    [
        565,
        "luz-collection",
        "06/09/2024 20:05:38"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:38"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:05:39"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:05:39"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:39"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:39"
    ],
    [
        564,
        "luz-collection",
        "06/09/2024 20:05:39"
    ],
    [
        578,
        "luz-collection",
        "06/09/2024 20:05:39"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:39"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:39"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:05:40"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:40"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:40"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:40"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:40"
    ],
    [
        623,
        "luz-collection",
        "06/09/2024 20:05:40"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:40"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:05:41"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 20:05:41"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:41"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:41"
    ],
    [
        610,
        "luz-collection",
        "06/09/2024 20:05:41"
    ],
    [
        587,
        "luz-collection",
        "06/09/2024 20:05:41"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:41"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:41"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:05:42"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:42"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:42"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:42"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:42"
    ],
    [
        633,
        "luz-collection",
        "06/09/2024 20:05:42"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:42"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 20:05:43"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:05:43"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:43"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:43"
    ],
    [
        642,
        "luz-collection",
        "06/09/2024 20:05:43"
    ],
    [
        581,
        "luz-collection",
        "06/09/2024 20:05:43"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:43"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:43"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 20:05:44"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:44"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:44"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:44"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:44"
    ],
    [
        640,
        "luz-collection",
        "06/09/2024 20:05:44"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:44"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 20:05:45"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 20:05:45"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:45"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:45"
    ],
    [
        625,
        "luz-collection",
        "06/09/2024 20:05:45"
    ],
    [
        613,
        "luz-collection",
        "06/09/2024 20:05:45"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:45"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:45"
    ],
    [
        393,
        "co2-collection",
        "06/09/2024 20:05:46"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:46"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:46"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:46"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:46"
    ],
    [
        610,
        "luz-collection",
        "06/09/2024 20:05:46"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:46"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:05:47"
    ],
    [
        393,
        "co2-collection",
        "06/09/2024 20:05:47"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:47"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:47"
    ],
    [
        565,
        "luz-collection",
        "06/09/2024 20:05:47"
    ],
    [
        588,
        "luz-collection",
        "06/09/2024 20:05:47"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:47"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:47"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:05:48"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:48"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:48"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:48"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:48"
    ],
    [
        649,
        "luz-collection",
        "06/09/2024 20:05:48"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:48"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:05:49"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:05:49"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:49"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:49"
    ],
    [
        574,
        "luz-collection",
        "06/09/2024 20:05:49"
    ],
    [
        565,
        "luz-collection",
        "06/09/2024 20:05:49"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:49"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:49"
    ],
    [
        393,
        "co2-collection",
        "06/09/2024 20:05:50"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:50"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:50"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:50"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:50"
    ],
    [
        598,
        "luz-collection",
        "06/09/2024 20:05:50"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:50"
    ],
    [
        394,
        "co2-collection",
        "06/09/2024 20:05:51"
    ],
    [
        394,
        "co2-collection",
        "06/09/2024 20:05:51"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:51"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:51"
    ],
    [
        608,
        "luz-collection",
        "06/09/2024 20:05:51"
    ],
    [
        614,
        "luz-collection",
        "06/09/2024 20:05:51"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:51"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:51"
    ],
    [
        394,
        "co2-collection",
        "06/09/2024 20:05:52"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:52"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:52"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:52"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:52"
    ],
    [
        640,
        "luz-collection",
        "06/09/2024 20:05:52"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:52"
    ],
    [
        393,
        "co2-collection",
        "06/09/2024 20:05:53"
    ],
    [
        394,
        "co2-collection",
        "06/09/2024 20:05:53"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:53"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:53"
    ],
    [
        592,
        "luz-collection",
        "06/09/2024 20:05:53"
    ],
    [
        643,
        "luz-collection",
        "06/09/2024 20:05:53"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:53"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:53"
    ],
    [
        393,
        "co2-collection",
        "06/09/2024 20:05:54"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:54"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:54"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:54"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:54"
    ],
    [
        638,
        "luz-collection",
        "06/09/2024 20:05:54"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:54"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:54"
    ],
    [
        393,
        "co2-collection",
        "06/09/2024 20:05:55"
    ],
    [
        393,
        "co2-collection",
        "06/09/2024 20:05:55"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:55"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:55"
    ],
    [
        616,
        "luz-collection",
        "06/09/2024 20:05:55"
    ],
    [
        590,
        "luz-collection",
        "06/09/2024 20:05:55"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:55"
    ],
    [
        393,
        "co2-collection",
        "06/09/2024 20:05:56"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:56"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:56"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:56"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:56"
    ],
    [
        646,
        "luz-collection",
        "06/09/2024 20:05:56"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:56"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:05:57"
    ],
    [
        393,
        "co2-collection",
        "06/09/2024 20:05:57"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:57"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:57"
    ],
    [
        571,
        "luz-collection",
        "06/09/2024 20:05:57"
    ],
    [
        565,
        "luz-collection",
        "06/09/2024 20:05:57"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:57"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:57"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:05:58"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:58"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:58"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:58"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:58"
    ],
    [
        576,
        "luz-collection",
        "06/09/2024 20:05:58"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:58"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:58"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:05:59"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:05:59"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:05:59"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:05:59"
    ],
    [
        593,
        "luz-collection",
        "06/09/2024 20:05:59"
    ],
    [
        625,
        "luz-collection",
        "06/09/2024 20:05:59"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:05:59"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:06:00"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:00"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:00"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:00"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:00"
    ],
    [
        617,
        "luz-collection",
        "06/09/2024 20:06:00"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:00"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:00"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:06:01"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:06:01"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:01"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:01"
    ],
    [
        583,
        "luz-collection",
        "06/09/2024 20:06:01"
    ],
    [
        640,
        "luz-collection",
        "06/09/2024 20:06:01"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:01"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:06:02"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:02"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:02"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:02"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:02"
    ],
    [
        644,
        "luz-collection",
        "06/09/2024 20:06:02"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:02"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:02"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 20:06:03"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:06:03"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:03"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:03"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:03"
    ],
    [
        633,
        "luz-collection",
        "06/09/2024 20:06:03"
    ],
    [
        609,
        "luz-collection",
        "06/09/2024 20:06:03"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:03"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:06:04"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:04"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:04"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:04"
    ],
    [
        625,
        "luz-collection",
        "06/09/2024 20:06:04"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:04"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:04"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 20:06:05"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 20:06:05"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:05"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:05"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:05"
    ],
    [
        596,
        "luz-collection",
        "06/09/2024 20:06:05"
    ],
    [
        572,
        "luz-collection",
        "06/09/2024 20:06:05"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:05"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 20:06:06"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:06"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:06"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:06"
    ],
    [
        563,
        "luz-collection",
        "06/09/2024 20:06:06"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:06"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:06"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 20:06:07"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:06:07"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:07"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:07"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:07"
    ],
    [
        646,
        "luz-collection",
        "06/09/2024 20:06:07"
    ],
    [
        565,
        "luz-collection",
        "06/09/2024 20:06:07"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:07"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:06:08"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:08"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:08"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:08"
    ],
    [
        579,
        "luz-collection",
        "06/09/2024 20:06:08"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:08"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:08"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:06:09"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:06:09"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:09"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:09"
    ],
    [
        607,
        "luz-collection",
        "06/09/2024 20:06:09"
    ],
    [
        600,
        "luz-collection",
        "06/09/2024 20:06:09"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:09"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:06:10"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:10"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:10"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:10"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:10"
    ],
    [
        611,
        "luz-collection",
        "06/09/2024 20:06:10"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:10"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:10"
    ],
    [
        394,
        "co2-collection",
        "06/09/2024 20:06:11"
    ],
    [
        393,
        "co2-collection",
        "06/09/2024 20:06:11"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:11"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:11"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:11"
    ],
    [
        645,
        "luz-collection",
        "06/09/2024 20:06:11"
    ],
    [
        633,
        "luz-collection",
        "06/09/2024 20:06:11"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:11"
    ],
    [
        394,
        "co2-collection",
        "06/09/2024 20:06:12"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:12"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:12"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:12"
    ],
    [
        584,
        "luz-collection",
        "06/09/2024 20:06:12"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:12"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:12"
    ],
    [
        395,
        "co2-collection",
        "06/09/2024 20:06:13"
    ],
    [
        394,
        "co2-collection",
        "06/09/2024 20:06:13"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:13"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:13"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:13"
    ],
    [
        645,
        "luz-collection",
        "06/09/2024 20:06:13"
    ],
    [
        634,
        "luz-collection",
        "06/09/2024 20:06:13"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:13"
    ],
    [
        394,
        "co2-collection",
        "06/09/2024 20:06:14"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:14"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:14"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:14"
    ],
    [
        613,
        "luz-collection",
        "06/09/2024 20:06:14"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:14"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:14"
    ],
    [
        394,
        "co2-collection",
        "06/09/2024 20:06:15"
    ],
    [
        394,
        "co2-collection",
        "06/09/2024 20:06:15"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:15"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:15"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:15"
    ],
    [
        623,
        "luz-collection",
        "06/09/2024 20:06:15"
    ],
    [
        600,
        "luz-collection",
        "06/09/2024 20:06:15"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:15"
    ],
    [
        394,
        "co2-collection",
        "06/09/2024 20:06:16"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:16"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:16"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:16"
    ],
    [
        576,
        "luz-collection",
        "06/09/2024 20:06:16"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:16"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:16"
    ],
    [
        393,
        "co2-collection",
        "06/09/2024 20:06:17"
    ],
    [
        394,
        "co2-collection",
        "06/09/2024 20:06:17"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:17"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:17"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:17"
    ],
    [
        650,
        "luz-collection",
        "06/09/2024 20:06:17"
    ],
    [
        562,
        "luz-collection",
        "06/09/2024 20:06:17"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:17"
    ],
    [
        393,
        "co2-collection",
        "06/09/2024 20:06:18"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:18"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:18"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:18"
    ],
    [
        565,
        "luz-collection",
        "06/09/2024 20:06:18"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:18"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:18"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:06:19"
    ],
    [
        393,
        "co2-collection",
        "06/09/2024 20:06:19"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:19"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:19"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:19"
    ],
    [
        578,
        "luz-collection",
        "06/09/2024 20:06:19"
    ],
    [
        603,
        "luz-collection",
        "06/09/2024 20:06:19"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:19"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:06:20"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:20"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:20"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:20"
    ],
    [
        605,
        "luz-collection",
        "06/09/2024 20:06:20"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:20"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:20"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 20:06:21"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:06:21"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:21"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:21"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:21"
    ],
    [
        616,
        "luz-collection",
        "06/09/2024 20:06:21"
    ],
    [
        640,
        "luz-collection",
        "06/09/2024 20:06:21"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:21"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 20:06:22"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:22"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:22"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:22"
    ],
    [
        644,
        "luz-collection",
        "06/09/2024 20:06:22"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:22"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:22"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 20:06:23"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 20:06:23"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:23"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:23"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:23"
    ],
    [
        588,
        "luz-collection",
        "06/09/2024 20:06:23"
    ],
    [
        640,
        "luz-collection",
        "06/09/2024 20:06:23"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:23"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 20:06:24"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:24"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:24"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:24"
    ],
    [
        621,
        "luz-collection",
        "06/09/2024 20:06:24"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:24"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:24"
    ],
    [
        395,
        "co2-collection",
        "06/09/2024 20:06:25"
    ],
    [
        394,
        "co2-collection",
        "06/09/2024 20:06:25"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:25"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:25"
    ],
    [
        636,
        "luz-collection",
        "06/09/2024 20:06:25"
    ],
    [
        599,
        "luz-collection",
        "06/09/2024 20:06:25"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:25"
    ],
    [
        396,
        "co2-collection",
        "06/09/2024 20:06:26"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:26"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:26"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:26"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:26"
    ],
    [
        587,
        "luz-collection",
        "06/09/2024 20:06:26"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:26"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:26"
    ],
    [
        395,
        "co2-collection",
        "06/09/2024 20:06:27"
    ],
    [
        394,
        "co2-collection",
        "06/09/2024 20:06:27"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:27"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:27"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:27"
    ],
    [
        564,
        "luz-collection",
        "06/09/2024 20:06:27"
    ],
    [
        567,
        "luz-collection",
        "06/09/2024 20:06:27"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:27"
    ],
    [
        394,
        "co2-collection",
        "06/09/2024 20:06:28"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:28"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:28"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:28"
    ],
    [
        646,
        "luz-collection",
        "06/09/2024 20:06:28"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:28"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:28"
    ],
    [
        393,
        "co2-collection",
        "06/09/2024 20:06:29"
    ],
    [
        393,
        "co2-collection",
        "06/09/2024 20:06:29"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:29"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:29"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:29"
    ],
    [
        569,
        "luz-collection",
        "06/09/2024 20:06:29"
    ],
    [
        586,
        "luz-collection",
        "06/09/2024 20:06:29"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:29"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:30"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:30"
    ],
    [
        608,
        "luz-collection",
        "06/09/2024 20:06:30"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:30"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:30"
    ],
    [
        393,
        "co2-collection",
        "06/09/2024 20:06:31"
    ],
    [
        394,
        "co2-collection",
        "06/09/2024 20:06:31"
    ],
    [
        393,
        "co2-collection",
        "06/09/2024 20:06:31"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:31"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:31"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:31"
    ],
    [
        618,
        "luz-collection",
        "06/09/2024 20:06:31"
    ],
    [
        603,
        "luz-collection",
        "06/09/2024 20:06:31"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:31"
    ],
    [
        393,
        "co2-collection",
        "06/09/2024 20:06:32"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:32"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:32"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:32"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:32"
    ],
    [
        638,
        "luz-collection",
        "06/09/2024 20:06:32"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:32"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:32"
    ],
    [
        393,
        "co2-collection",
        "06/09/2024 20:06:33"
    ],
    [
        394,
        "co2-collection",
        "06/09/2024 20:06:33"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:33"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:33"
    ],
    [
        644,
        "luz-collection",
        "06/09/2024 20:06:33"
    ],
    [
        586,
        "luz-collection",
        "06/09/2024 20:06:33"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:33"
    ],
    [
        394,
        "co2-collection",
        "06/09/2024 20:06:34"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:34"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:34"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:34"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:34"
    ],
    [
        641,
        "luz-collection",
        "06/09/2024 20:06:34"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:34"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:34"
    ],
    [
        393,
        "co2-collection",
        "06/09/2024 20:06:35"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:35"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:35"
    ],
    [
        627,
        "luz-collection",
        "06/09/2024 20:06:35"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:35"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:06:36"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:06:36"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:36"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:36"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:36"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:36"
    ],
    [
        631,
        "luz-collection",
        "06/09/2024 20:06:36"
    ],
    [
        604,
        "luz-collection",
        "06/09/2024 20:06:36"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:36"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:36"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:06:37"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:06:37"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:37"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:37"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:37"
    ],
    [
        590,
        "luz-collection",
        "06/09/2024 20:06:37"
    ],
    [
        568,
        "luz-collection",
        "06/09/2024 20:06:37"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:37"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:06:38"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:38"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:38"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:38"
    ],
    [
        565,
        "luz-collection",
        "06/09/2024 20:06:38"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:38"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:38"
    ],
    [
        393,
        "co2-collection",
        "06/09/2024 20:06:39"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:06:39"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:39"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:39"
    ],
    [
        569,
        "luz-collection",
        "06/09/2024 20:06:39"
    ],
    [
        644,
        "luz-collection",
        "06/09/2024 20:06:39"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:39"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:06:40"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:40"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:40"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:40"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:40"
    ],
    [
        590,
        "luz-collection",
        "06/09/2024 20:06:40"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:40"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:40"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:06:41"
    ],
    [
        393,
        "co2-collection",
        "06/09/2024 20:06:41"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:41"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:41"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:41"
    ],
    [
        592,
        "luz-collection",
        "06/09/2024 20:06:41"
    ],
    [
        615,
        "luz-collection",
        "06/09/2024 20:06:41"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:41"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:06:42"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:42"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:42"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:42"
    ],
    [
        632,
        "luz-collection",
        "06/09/2024 20:06:42"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:42"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:42"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:06:43"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:06:43"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:43"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:43"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:43"
    ],
    [
        647,
        "luz-collection",
        "06/09/2024 20:06:43"
    ],
    [
        640,
        "luz-collection",
        "06/09/2024 20:06:43"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:43"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:06:44"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:44"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:44"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:44"
    ],
    [
        599,
        "luz-collection",
        "06/09/2024 20:06:44"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:44"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:44"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:06:45"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:06:45"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:45"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:45"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:45"
    ],
    [
        601,
        "luz-collection",
        "06/09/2024 20:06:45"
    ],
    [
        627,
        "luz-collection",
        "06/09/2024 20:06:45"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:45"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:06:46"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:46"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:46"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:46"
    ],
    [
        573,
        "luz-collection",
        "06/09/2024 20:06:46"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:46"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:46"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:06:47"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:06:47"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:47"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:47"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:47"
    ],
    [
        651,
        "luz-collection",
        "06/09/2024 20:06:47"
    ],
    [
        562,
        "luz-collection",
        "06/09/2024 20:06:47"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:47"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:06:48"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:48"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:48"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:48"
    ],
    [
        571,
        "luz-collection",
        "06/09/2024 20:06:48"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:48"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:48"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:06:49"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:06:49"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:49"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:49"
    ],
    [
        602,
        "luz-collection",
        "06/09/2024 20:06:49"
    ],
    [
        594,
        "luz-collection",
        "06/09/2024 20:06:49"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:49"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:06:50"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:50"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:50"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:50"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:50"
    ],
    [
        632,
        "luz-collection",
        "06/09/2024 20:06:50"
    ],
    [
        644,
        "luz-collection",
        "06/09/2024 20:06:50"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:50"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:50"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:06:51"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:06:51"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:51"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:51"
    ],
    [
        628,
        "luz-collection",
        "06/09/2024 20:06:51"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:51"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:06:52"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:52"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:52"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:52"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:52"
    ],
    [
        616,
        "luz-collection",
        "06/09/2024 20:06:52"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:52"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:52"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:06:53"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:06:53"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:53"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:53"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:53"
    ],
    [
        601,
        "luz-collection",
        "06/09/2024 20:06:53"
    ],
    [
        570,
        "luz-collection",
        "06/09/2024 20:06:53"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:53"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:06:54"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:54"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:54"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:54"
    ],
    [
        566,
        "luz-collection",
        "06/09/2024 20:06:54"
    ],
    [
        635,
        "luz-collection",
        "06/09/2024 20:06:54"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:54"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:54"
    ],
    [
        393,
        "co2-collection",
        "06/09/2024 20:06:55"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:06:55"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:55"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:55"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:55"
    ],
    [
        586,
        "luz-collection",
        "06/09/2024 20:06:55"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:55"
    ],
    [
        393,
        "co2-collection",
        "06/09/2024 20:06:56"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:56"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:56"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:56"
    ],
    [
        617,
        "luz-collection",
        "06/09/2024 20:06:56"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:56"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:56"
    ],
    [
        393,
        "co2-collection",
        "06/09/2024 20:06:57"
    ],
    [
        393,
        "co2-collection",
        "06/09/2024 20:06:57"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:57"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:57"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:57"
    ],
    [
        646,
        "luz-collection",
        "06/09/2024 20:06:57"
    ],
    [
        585,
        "luz-collection",
        "06/09/2024 20:06:57"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:57"
    ],
    [
        393,
        "co2-collection",
        "06/09/2024 20:06:58"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:58"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:58"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:58"
    ],
    [
        610,
        "luz-collection",
        "06/09/2024 20:06:58"
    ],
    [
        638,
        "luz-collection",
        "06/09/2024 20:06:58"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:58"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:58"
    ],
    [
        394,
        "co2-collection",
        "06/09/2024 20:06:59"
    ],
    [
        394,
        "co2-collection",
        "06/09/2024 20:06:59"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:59"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:06:59"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:06:59"
    ],
    [
        578,
        "luz-collection",
        "06/09/2024 20:06:59"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:06:59"
    ],
    [
        394,
        "co2-collection",
        "06/09/2024 20:07:00"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:00"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:00"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:00"
    ],
    [
        563,
        "luz-collection",
        "06/09/2024 20:07:00"
    ],
    [
        651,
        "luz-collection",
        "06/09/2024 20:07:00"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:00"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:00"
    ],
    [
        395,
        "co2-collection",
        "06/09/2024 20:07:01"
    ],
    [
        394,
        "co2-collection",
        "06/09/2024 20:07:01"
    ],
    [
        15,
        "dist-collection",
        "06/09/2024 20:07:01"
    ],
    [
        15,
        "dist-collection",
        "06/09/2024 20:07:01"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:01"
    ],
    [
        578,
        "luz-collection",
        "06/09/2024 20:07:01"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:01"
    ],
    [
        395,
        "co2-collection",
        "06/09/2024 20:07:02"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:02"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:02"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:02"
    ],
    [
        610,
        "luz-collection",
        "06/09/2024 20:07:02"
    ],
    [
        586,
        "luz-collection",
        "06/09/2024 20:07:02"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:02"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:02"
    ],
    [
        395,
        "co2-collection",
        "06/09/2024 20:07:03"
    ],
    [
        394,
        "co2-collection",
        "06/09/2024 20:07:03"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:03"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:03"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:03"
    ],
    [
        641,
        "luz-collection",
        "06/09/2024 20:07:03"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:03"
    ],
    [
        395,
        "co2-collection",
        "06/09/2024 20:07:04"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:04"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:04"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:04"
    ],
    [
        638,
        "luz-collection",
        "06/09/2024 20:07:04"
    ],
    [
        614,
        "luz-collection",
        "06/09/2024 20:07:04"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:04"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:04"
    ],
    [
        395,
        "co2-collection",
        "06/09/2024 20:07:05"
    ],
    [
        394,
        "co2-collection",
        "06/09/2024 20:07:05"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:05"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:05"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:05"
    ],
    [
        631,
        "luz-collection",
        "06/09/2024 20:07:05"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:05"
    ],
    [
        395,
        "co2-collection",
        "06/09/2024 20:07:06"
    ],
    [
        15,
        "dist-collection",
        "06/09/2024 20:07:06"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:06"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:06"
    ],
    [
        564,
        "luz-collection",
        "06/09/2024 20:07:06"
    ],
    [
        581,
        "luz-collection",
        "06/09/2024 20:07:06"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:06"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:06"
    ],
    [
        395,
        "co2-collection",
        "06/09/2024 20:07:07"
    ],
    [
        394,
        "co2-collection",
        "06/09/2024 20:07:07"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:07"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:07"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:07"
    ],
    [
        579,
        "luz-collection",
        "06/09/2024 20:07:07"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:07"
    ],
    [
        394,
        "co2-collection",
        "06/09/2024 20:07:08"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:08"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:08"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:08"
    ],
    [
        607,
        "luz-collection",
        "06/09/2024 20:07:08"
    ],
    [
        621,
        "luz-collection",
        "06/09/2024 20:07:08"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:08"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:08"
    ],
    [
        394,
        "co2-collection",
        "06/09/2024 20:07:09"
    ],
    [
        395,
        "co2-collection",
        "06/09/2024 20:07:09"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:09"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:09"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:09"
    ],
    [
        637,
        "luz-collection",
        "06/09/2024 20:07:09"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:09"
    ],
    [
        394,
        "co2-collection",
        "06/09/2024 20:07:10"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:10"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:10"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:10"
    ],
    [
        643,
        "luz-collection",
        "06/09/2024 20:07:10"
    ],
    [
        597,
        "luz-collection",
        "06/09/2024 20:07:10"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:10"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:10"
    ],
    [
        393,
        "co2-collection",
        "06/09/2024 20:07:11"
    ],
    [
        393,
        "co2-collection",
        "06/09/2024 20:07:11"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:11"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:11"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:11"
    ],
    [
        626,
        "luz-collection",
        "06/09/2024 20:07:11"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:11"
    ],
    [
        393,
        "co2-collection",
        "06/09/2024 20:07:12"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:12"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:12"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:12"
    ],
    [
        597,
        "luz-collection",
        "06/09/2024 20:07:12"
    ],
    [
        567,
        "luz-collection",
        "06/09/2024 20:07:12"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:12"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:12"
    ],
    [
        393,
        "co2-collection",
        "06/09/2024 20:07:13"
    ],
    [
        393,
        "co2-collection",
        "06/09/2024 20:07:13"
    ],
    [
        15,
        "dist-collection",
        "06/09/2024 20:07:13"
    ],
    [
        15,
        "dist-collection",
        "06/09/2024 20:07:13"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:13"
    ],
    [
        649,
        "luz-collection",
        "06/09/2024 20:07:13"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:13"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:07:14"
    ],
    [
        15,
        "dist-collection",
        "06/09/2024 20:07:14"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:14"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:14"
    ],
    [
        568,
        "luz-collection",
        "06/09/2024 20:07:14"
    ],
    [
        590,
        "luz-collection",
        "06/09/2024 20:07:14"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:14"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:14"
    ],
    [
        393,
        "co2-collection",
        "06/09/2024 20:07:15"
    ],
    [
        393,
        "co2-collection",
        "06/09/2024 20:07:15"
    ],
    [
        15,
        "dist-collection",
        "06/09/2024 20:07:15"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:15"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:15"
    ],
    [
        618,
        "luz-collection",
        "06/09/2024 20:07:15"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:15"
    ],
    [
        393,
        "co2-collection",
        "06/09/2024 20:07:16"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:16"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:16"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:16"
    ],
    [
        644,
        "luz-collection",
        "06/09/2024 20:07:16"
    ],
    [
        584,
        "luz-collection",
        "06/09/2024 20:07:16"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:16"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:16"
    ],
    [
        393,
        "co2-collection",
        "06/09/2024 20:07:17"
    ],
    [
        393,
        "co2-collection",
        "06/09/2024 20:07:17"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:17"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:17"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:17"
    ],
    [
        640,
        "luz-collection",
        "06/09/2024 20:07:17"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:17"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:07:18"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:18"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:18"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:18"
    ],
    [
        628,
        "luz-collection",
        "06/09/2024 20:07:18"
    ],
    [
        614,
        "luz-collection",
        "06/09/2024 20:07:18"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:18"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:18"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:07:19"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:07:19"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:19"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:19"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:19"
    ],
    [
        589,
        "luz-collection",
        "06/09/2024 20:07:19"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:19"
    ],
    [
        393,
        "co2-collection",
        "06/09/2024 20:07:20"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:20"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:20"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:20"
    ],
    [
        564,
        "luz-collection",
        "06/09/2024 20:07:20"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:20"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:20"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:07:21"
    ],
    [
        393,
        "co2-collection",
        "06/09/2024 20:07:21"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:21"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:21"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:21"
    ],
    [
        629,
        "luz-collection",
        "06/09/2024 20:07:21"
    ],
    [
        571,
        "luz-collection",
        "06/09/2024 20:07:21"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:21"
    ],
    [
        394,
        "co2-collection",
        "06/09/2024 20:07:22"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:22"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:22"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:22"
    ],
    [
        621,
        "luz-collection",
        "06/09/2024 20:07:22"
    ],
    [
        591,
        "luz-collection",
        "06/09/2024 20:07:22"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:22"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:22"
    ],
    [
        396,
        "co2-collection",
        "06/09/2024 20:07:23"
    ],
    [
        397,
        "co2-collection",
        "06/09/2024 20:07:23"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:23"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:23"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:23"
    ],
    [
        647,
        "luz-collection",
        "06/09/2024 20:07:23"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:23"
    ],
    [
        396,
        "co2-collection",
        "06/09/2024 20:07:24"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:24"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:24"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:24"
    ],
    [
        587,
        "luz-collection",
        "06/09/2024 20:07:24"
    ],
    [
        641,
        "luz-collection",
        "06/09/2024 20:07:24"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:24"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:24"
    ],
    [
        395,
        "co2-collection",
        "06/09/2024 20:07:25"
    ],
    [
        394,
        "co2-collection",
        "06/09/2024 20:07:25"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:25"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:25"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:25"
    ],
    [
        617,
        "luz-collection",
        "06/09/2024 20:07:25"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:25"
    ],
    [
        393,
        "co2-collection",
        "06/09/2024 20:07:26"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:26"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:26"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:26"
    ],
    [
        652,
        "luz-collection",
        "06/09/2024 20:07:26"
    ],
    [
        589,
        "luz-collection",
        "06/09/2024 20:07:26"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:26"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:26"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:07:27"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 20:07:27"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:27"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:27"
    ],
    [
        566,
        "luz-collection",
        "06/09/2024 20:07:27"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:27"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 20:07:28"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:28"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:28"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:28"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:28"
    ],
    [
        569,
        "luz-collection",
        "06/09/2024 20:07:28"
    ],
    [
        593,
        "luz-collection",
        "06/09/2024 20:07:28"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:28"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:28"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 20:07:29"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 20:07:29"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:29"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:29"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:29"
    ],
    [
        610,
        "luz-collection",
        "06/09/2024 20:07:29"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:29"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 20:07:30"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:30"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:30"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:30"
    ],
    [
        645,
        "luz-collection",
        "06/09/2024 20:07:30"
    ],
    [
        619,
        "luz-collection",
        "06/09/2024 20:07:30"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:30"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:30"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 20:07:31"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 20:07:31"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:31"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:31"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:31"
    ],
    [
        641,
        "luz-collection",
        "06/09/2024 20:07:31"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:31"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 20:07:32"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:32"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:32"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:32"
    ],
    [
        605,
        "luz-collection",
        "06/09/2024 20:07:32"
    ],
    [
        618,
        "luz-collection",
        "06/09/2024 20:07:32"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:32"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:32"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 20:07:33"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 20:07:33"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:33"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:33"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:33"
    ],
    [
        589,
        "luz-collection",
        "06/09/2024 20:07:33"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:33"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 20:07:34"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:34"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:34"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:34"
    ],
    [
        562,
        "luz-collection",
        "06/09/2024 20:07:34"
    ],
    [
        650,
        "luz-collection",
        "06/09/2024 20:07:34"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:34"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:34"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 20:07:35"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 20:07:35"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:35"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:35"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:35"
    ],
    [
        568,
        "luz-collection",
        "06/09/2024 20:07:35"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:35"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 20:07:36"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:36"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:36"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:36"
    ],
    [
        589,
        "luz-collection",
        "06/09/2024 20:07:36"
    ],
    [
        618,
        "luz-collection",
        "06/09/2024 20:07:36"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:36"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:36"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 20:07:37"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 20:07:37"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:37"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:37"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:37"
    ],
    [
        586,
        "luz-collection",
        "06/09/2024 20:07:37"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:37"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 20:07:38"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:38"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:38"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:38"
    ],
    [
        641,
        "luz-collection",
        "06/09/2024 20:07:38"
    ],
    [
        641,
        "luz-collection",
        "06/09/2024 20:07:38"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:38"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:38"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 20:07:39"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 20:07:39"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:39"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:39"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:39"
    ],
    [
        619,
        "luz-collection",
        "06/09/2024 20:07:39"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:39"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 20:07:40"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:40"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:40"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:40"
    ],
    [
        595,
        "luz-collection",
        "06/09/2024 20:07:40"
    ],
    [
        621,
        "luz-collection",
        "06/09/2024 20:07:40"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:40"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:40"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 20:07:41"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 20:07:41"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:41"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:41"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:41"
    ],
    [
        566,
        "luz-collection",
        "06/09/2024 20:07:41"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:41"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:07:42"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:42"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:42"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:42"
    ],
    [
        636,
        "luz-collection",
        "06/09/2024 20:07:42"
    ],
    [
        566,
        "luz-collection",
        "06/09/2024 20:07:42"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:42"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:42"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:07:43"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:07:43"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:43"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:43"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:43"
    ],
    [
        582,
        "luz-collection",
        "06/09/2024 20:07:43"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:43"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:07:44"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:44"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:44"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:44"
    ],
    [
        641,
        "luz-collection",
        "06/09/2024 20:07:44"
    ],
    [
        612,
        "luz-collection",
        "06/09/2024 20:07:44"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:44"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:44"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:07:45"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:07:45"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:45"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:45"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:45"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:45"
    ],
    [
        584,
        "luz-collection",
        "06/09/2024 20:07:45"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:45"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:07:46"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:46"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:46"
    ],
    [
        641,
        "luz-collection",
        "06/09/2024 20:07:46"
    ],
    [
        624,
        "luz-collection",
        "06/09/2024 20:07:46"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:46"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:46"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:07:47"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:07:47"
    ],
    [
        15,
        "dist-collection",
        "06/09/2024 20:07:47"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:47"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:47"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:47"
    ],
    [
        595,
        "luz-collection",
        "06/09/2024 20:07:47"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:47"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:07:48"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:48"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:48"
    ],
    [
        568,
        "luz-collection",
        "06/09/2024 20:07:48"
    ],
    [
        647,
        "luz-collection",
        "06/09/2024 20:07:48"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:48"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:48"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:07:49"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:07:49"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:49"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:49"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:49"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:49"
    ],
    [
        567,
        "luz-collection",
        "06/09/2024 20:07:49"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:49"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:07:50"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:07:50"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:50"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:50"
    ],
    [
        592,
        "luz-collection",
        "06/09/2024 20:07:50"
    ],
    [
        609,
        "luz-collection",
        "06/09/2024 20:07:50"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:50"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:50"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:07:51"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:51"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:51"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:51"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:51"
    ],
    [
        618,
        "luz-collection",
        "06/09/2024 20:07:51"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:51"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:07:52"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:52"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:52"
    ],
    [
        646,
        "luz-collection",
        "06/09/2024 20:07:52"
    ],
    [
        653,
        "luz-collection",
        "06/09/2024 20:07:52"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:52"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:52"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:07:53"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:07:53"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:53"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:53"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:53"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:53"
    ],
    [
        614,
        "luz-collection",
        "06/09/2024 20:07:53"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:53"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:07:54"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:54"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:54"
    ],
    [
        589,
        "luz-collection",
        "06/09/2024 20:07:54"
    ],
    [
        620,
        "luz-collection",
        "06/09/2024 20:07:54"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:54"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:54"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:07:55"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:07:55"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:55"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:55"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:55"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:55"
    ],
    [
        567,
        "luz-collection",
        "06/09/2024 20:07:55"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:55"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:07:56"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:07:56"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:56"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:56"
    ],
    [
        578,
        "luz-collection",
        "06/09/2024 20:07:56"
    ],
    [
        651,
        "luz-collection",
        "06/09/2024 20:07:56"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:56"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:56"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:07:57"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:57"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:57"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:57"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:57"
    ],
    [
        607,
        "luz-collection",
        "06/09/2024 20:07:57"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:57"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:07:58"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:58"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:58"
    ],
    [
        587,
        "luz-collection",
        "06/09/2024 20:07:58"
    ],
    [
        640,
        "luz-collection",
        "06/09/2024 20:07:58"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:58"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:58"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:07:59"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:07:59"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:59"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:07:59"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:59"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:07:59"
    ],
    [
        647,
        "luz-collection",
        "06/09/2024 20:07:59"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:07:59"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:08:00"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:08:00"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:00"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:00"
    ],
    [
        600,
        "luz-collection",
        "06/09/2024 20:08:00"
    ],
    [
        629,
        "luz-collection",
        "06/09/2024 20:08:00"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:00"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:00"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:08:01"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:01"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:01"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:01"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:01"
    ],
    [
        654,
        "luz-collection",
        "06/09/2024 20:08:01"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:01"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:08:02"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:08:02"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:02"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:02"
    ],
    [
        570,
        "luz-collection",
        "06/09/2024 20:08:02"
    ],
    [
        572,
        "luz-collection",
        "06/09/2024 20:08:02"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:02"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:02"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:08:03"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:03"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:03"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:03"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:03"
    ],
    [
        590,
        "luz-collection",
        "06/09/2024 20:08:03"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:03"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:08:04"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:08:04"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:04"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:04"
    ],
    [
        616,
        "luz-collection",
        "06/09/2024 20:08:04"
    ],
    [
        616,
        "luz-collection",
        "06/09/2024 20:08:04"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:04"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:04"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:08:05"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:05"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:05"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:05"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:05"
    ],
    [
        644,
        "luz-collection",
        "06/09/2024 20:08:05"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:05"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:08:06"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:08:06"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:06"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:06"
    ],
    [
        602,
        "luz-collection",
        "06/09/2024 20:08:06"
    ],
    [
        643,
        "luz-collection",
        "06/09/2024 20:08:06"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:06"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:06"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:08:07"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:07"
    ],
    [
        15,
        "dist-collection",
        "06/09/2024 20:08:07"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:07"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:07"
    ],
    [
        627,
        "luz-collection",
        "06/09/2024 20:08:07"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:07"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:08:08"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:08:08"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:08"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:08"
    ],
    [
        600,
        "luz-collection",
        "06/09/2024 20:08:08"
    ],
    [
        570,
        "luz-collection",
        "06/09/2024 20:08:08"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:08"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:08"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:08:09"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:09"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:09"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:09"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:09"
    ],
    [
        652,
        "luz-collection",
        "06/09/2024 20:08:09"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:09"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:08:10"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:08:10"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:10"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:10"
    ],
    [
        567,
        "luz-collection",
        "06/09/2024 20:08:10"
    ],
    [
        579,
        "luz-collection",
        "06/09/2024 20:08:10"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:10"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:10"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:08:11"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:11"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:11"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:11"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:11"
    ],
    [
        605,
        "luz-collection",
        "06/09/2024 20:08:11"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:11"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:08:12"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:08:12"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:12"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:12"
    ],
    [
        626,
        "luz-collection",
        "06/09/2024 20:08:12"
    ],
    [
        601,
        "luz-collection",
        "06/09/2024 20:08:12"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:12"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:12"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:08:13"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:13"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:13"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:13"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:13"
    ],
    [
        647,
        "luz-collection",
        "06/09/2024 20:08:13"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:13"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:08:14"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:08:14"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:14"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:14"
    ],
    [
        639,
        "luz-collection",
        "06/09/2024 20:08:14"
    ],
    [
        602,
        "luz-collection",
        "06/09/2024 20:08:14"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:14"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:14"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:08:15"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:15"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:15"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:15"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:15"
    ],
    [
        625,
        "luz-collection",
        "06/09/2024 20:08:15"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:15"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:08:16"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:08:16"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:16"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:16"
    ],
    [
        574,
        "luz-collection",
        "06/09/2024 20:08:16"
    ],
    [
        601,
        "luz-collection",
        "06/09/2024 20:08:16"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:16"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:16"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:08:17"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:17"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:17"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:17"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:17"
    ],
    [
        654,
        "luz-collection",
        "06/09/2024 20:08:17"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:17"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:08:18"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:18"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:18"
    ],
    [
        563,
        "luz-collection",
        "06/09/2024 20:08:18"
    ],
    [
        570,
        "luz-collection",
        "06/09/2024 20:08:18"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:18"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:18"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:08:19"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:08:19"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:19"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:19"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:19"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:19"
    ],
    [
        591,
        "luz-collection",
        "06/09/2024 20:08:19"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:19"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:08:20"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:08:20"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:20"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:20"
    ],
    [
        609,
        "luz-collection",
        "06/09/2024 20:08:20"
    ],
    [
        616,
        "luz-collection",
        "06/09/2024 20:08:20"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:20"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:20"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:08:21"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:21"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:21"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:21"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:21"
    ],
    [
        636,
        "luz-collection",
        "06/09/2024 20:08:21"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:21"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:08:22"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:08:22"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:22"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:22"
    ],
    [
        589,
        "luz-collection",
        "06/09/2024 20:08:22"
    ],
    [
        647,
        "luz-collection",
        "06/09/2024 20:08:22"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:22"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:22"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:08:23"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:23"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:23"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:23"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:23"
    ],
    [
        640,
        "luz-collection",
        "06/09/2024 20:08:23"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:23"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:08:24"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:08:24"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:24"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:24"
    ],
    [
        595,
        "luz-collection",
        "06/09/2024 20:08:24"
    ],
    [
        620,
        "luz-collection",
        "06/09/2024 20:08:24"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:24"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:24"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:08:25"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:25"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:25"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:25"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:25"
    ],
    [
        648,
        "luz-collection",
        "06/09/2024 20:08:25"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:25"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:08:26"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:08:26"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:26"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:26"
    ],
    [
        565,
        "luz-collection",
        "06/09/2024 20:08:26"
    ],
    [
        576,
        "luz-collection",
        "06/09/2024 20:08:26"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:26"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:26"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:08:27"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:27"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:27"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:27"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:27"
    ],
    [
        574,
        "luz-collection",
        "06/09/2024 20:08:27"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:27"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:08:28"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:08:28"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:28"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:28"
    ],
    [
        590,
        "luz-collection",
        "06/09/2024 20:08:28"
    ],
    [
        633,
        "luz-collection",
        "06/09/2024 20:08:28"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:28"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:28"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:08:29"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:29"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:29"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:29"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:29"
    ],
    [
        614,
        "luz-collection",
        "06/09/2024 20:08:29"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:29"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:08:30"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:08:30"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:30"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:30"
    ],
    [
        589,
        "luz-collection",
        "06/09/2024 20:08:30"
    ],
    [
        641,
        "luz-collection",
        "06/09/2024 20:08:30"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:30"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:30"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:08:31"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:31"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:31"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:31"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:31"
    ],
    [
        654,
        "luz-collection",
        "06/09/2024 20:08:31"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:31"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:08:32"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:08:32"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:32"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:32"
    ],
    [
        652,
        "luz-collection",
        "06/09/2024 20:08:32"
    ],
    [
        631,
        "luz-collection",
        "06/09/2024 20:08:32"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:32"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:32"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:08:33"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:33"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:33"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:33"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:33"
    ],
    [
        642,
        "luz-collection",
        "06/09/2024 20:08:33"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:33"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:08:34"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:08:34"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:34"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:34"
    ],
    [
        585,
        "luz-collection",
        "06/09/2024 20:08:34"
    ],
    [
        613,
        "luz-collection",
        "06/09/2024 20:08:34"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:34"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:34"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:08:35"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:35"
    ],
    [
        15,
        "dist-collection",
        "06/09/2024 20:08:35"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:35"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:35"
    ],
    [
        578,
        "luz-collection",
        "06/09/2024 20:08:35"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:35"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:08:36"
    ],
    [
        15,
        "dist-collection",
        "06/09/2024 20:08:36"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:36"
    ],
    [
        657,
        "luz-collection",
        "06/09/2024 20:08:36"
    ],
    [
        588,
        "luz-collection",
        "06/09/2024 20:08:36"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:36"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:36"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:08:37"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:08:37"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:37"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:37"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:37"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:37"
    ],
    [
        614,
        "luz-collection",
        "06/09/2024 20:08:37"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:37"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:08:38"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:08:38"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:38"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:38"
    ],
    [
        641,
        "luz-collection",
        "06/09/2024 20:08:38"
    ],
    [
        596,
        "luz-collection",
        "06/09/2024 20:08:38"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:38"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:38"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:08:39"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:39"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:39"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:39"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:39"
    ],
    [
        655,
        "luz-collection",
        "06/09/2024 20:08:39"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:39"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:39"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:08:40"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:08:40"
    ],
    [
        15,
        "dist-collection",
        "06/09/2024 20:08:40"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:40"
    ],
    [
        653,
        "luz-collection",
        "06/09/2024 20:08:40"
    ],
    [
        632,
        "luz-collection",
        "06/09/2024 20:08:40"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:40"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:08:41"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:41"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:41"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:41"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:41"
    ],
    [
        635,
        "luz-collection",
        "06/09/2024 20:08:41"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:41"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:41"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:08:42"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:08:42"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:42"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:42"
    ],
    [
        611,
        "luz-collection",
        "06/09/2024 20:08:42"
    ],
    [
        582,
        "luz-collection",
        "06/09/2024 20:08:42"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:42"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:08:43"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:43"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:43"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:43"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:43"
    ],
    [
        575,
        "luz-collection",
        "06/09/2024 20:08:43"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:43"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:43"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:08:44"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:08:44"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:44"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:44"
    ],
    [
        585,
        "luz-collection",
        "06/09/2024 20:08:44"
    ],
    [
        652,
        "luz-collection",
        "06/09/2024 20:08:44"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:44"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:08:45"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:45"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:45"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:45"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:45"
    ],
    [
        609,
        "luz-collection",
        "06/09/2024 20:08:45"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:45"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:45"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:08:46"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:08:46"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:46"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:46"
    ],
    [
        636,
        "luz-collection",
        "06/09/2024 20:08:46"
    ],
    [
        594,
        "luz-collection",
        "06/09/2024 20:08:46"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:46"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:08:47"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:47"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:47"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:47"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:47"
    ],
    [
        655,
        "luz-collection",
        "06/09/2024 20:08:47"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:47"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:47"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:08:48"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:08:48"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:48"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:48"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:48"
    ],
    [
        649,
        "luz-collection",
        "06/09/2024 20:08:48"
    ],
    [
        628,
        "luz-collection",
        "06/09/2024 20:08:48"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:48"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:08:49"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:49"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:49"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:49"
    ],
    [
        631,
        "luz-collection",
        "06/09/2024 20:08:49"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:49"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:08:50"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:08:50"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:50"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:50"
    ],
    [
        606,
        "luz-collection",
        "06/09/2024 20:08:50"
    ],
    [
        580,
        "luz-collection",
        "06/09/2024 20:08:50"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:50"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:50"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:08:51"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:51"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:51"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:51"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:51"
    ],
    [
        575,
        "luz-collection",
        "06/09/2024 20:08:51"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:51"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:51"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:08:52"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:08:52"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:52"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:52"
    ],
    [
        650,
        "luz-collection",
        "06/09/2024 20:08:52"
    ],
    [
        587,
        "luz-collection",
        "06/09/2024 20:08:52"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:52"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:08:53"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:53"
    ],
    [
        15,
        "dist-collection",
        "06/09/2024 20:08:53"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:53"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:53"
    ],
    [
        613,
        "luz-collection",
        "06/09/2024 20:08:53"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:53"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:53"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:08:54"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:08:54"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:08:54"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:54"
    ],
    [
        591,
        "luz-collection",
        "06/09/2024 20:08:54"
    ],
    [
        643,
        "luz-collection",
        "06/09/2024 20:08:54"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:54"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:08:55"
    ],
    [
        15,
        "dist-collection",
        "06/09/2024 20:08:55"
    ],
    [
        15,
        "dist-collection",
        "06/09/2024 20:08:55"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:55"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:55"
    ],
    [
        654,
        "luz-collection",
        "06/09/2024 20:08:55"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:55"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:55"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:08:56"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:08:56"
    ],
    [
        15,
        "dist-collection",
        "06/09/2024 20:08:56"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:56"
    ],
    [
        632,
        "luz-collection",
        "06/09/2024 20:08:56"
    ],
    [
        618,
        "luz-collection",
        "06/09/2024 20:08:56"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:56"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:08:57"
    ],
    [
        15,
        "dist-collection",
        "06/09/2024 20:08:57"
    ],
    [
        15,
        "dist-collection",
        "06/09/2024 20:08:57"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:57"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:57"
    ],
    [
        641,
        "luz-collection",
        "06/09/2024 20:08:57"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:57"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:57"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:08:58"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:08:58"
    ],
    [
        15,
        "dist-collection",
        "06/09/2024 20:08:58"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:58"
    ],
    [
        572,
        "luz-collection",
        "06/09/2024 20:08:58"
    ],
    [
        596,
        "luz-collection",
        "06/09/2024 20:08:58"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:58"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:08:59"
    ],
    [
        15,
        "dist-collection",
        "06/09/2024 20:08:59"
    ],
    [
        15,
        "dist-collection",
        "06/09/2024 20:08:59"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:59"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:08:59"
    ],
    [
        578,
        "luz-collection",
        "06/09/2024 20:08:59"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:08:59"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:09:00"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:09:00"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:09:00"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:00"
    ],
    [
        641,
        "luz-collection",
        "06/09/2024 20:09:00"
    ],
    [
        597,
        "luz-collection",
        "06/09/2024 20:09:00"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:00"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:00"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:09:01"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:09:01"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:09:01"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:01"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:01"
    ],
    [
        626,
        "luz-collection",
        "06/09/2024 20:09:01"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:01"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:01"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:09:02"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:09:02"
    ],
    [
        15,
        "dist-collection",
        "06/09/2024 20:09:02"
    ],
    [
        15,
        "dist-collection",
        "06/09/2024 20:09:02"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:02"
    ],
    [
        652,
        "luz-collection",
        "06/09/2024 20:09:02"
    ],
    [
        595,
        "luz-collection",
        "06/09/2024 20:09:02"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:02"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:09:03"
    ],
    [
        15,
        "dist-collection",
        "06/09/2024 20:09:03"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:03"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:03"
    ],
    [
        656,
        "luz-collection",
        "06/09/2024 20:09:03"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:03"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:03"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:09:04"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:09:04"
    ],
    [
        15,
        "dist-collection",
        "06/09/2024 20:09:04"
    ],
    [
        15,
        "dist-collection",
        "06/09/2024 20:09:04"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:04"
    ],
    [
        643,
        "luz-collection",
        "06/09/2024 20:09:04"
    ],
    [
        618,
        "luz-collection",
        "06/09/2024 20:09:04"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:04"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:09:05"
    ],
    [
        15,
        "dist-collection",
        "06/09/2024 20:09:05"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:05"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:05"
    ],
    [
        641,
        "luz-collection",
        "06/09/2024 20:09:05"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:05"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:05"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:09:06"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:09:06"
    ],
    [
        15,
        "dist-collection",
        "06/09/2024 20:09:06"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:06"
    ],
    [
        578,
        "luz-collection",
        "06/09/2024 20:09:06"
    ],
    [
        594,
        "luz-collection",
        "06/09/2024 20:09:06"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:06"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:09:07"
    ],
    [
        15,
        "dist-collection",
        "06/09/2024 20:09:07"
    ],
    [
        15,
        "dist-collection",
        "06/09/2024 20:09:07"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:07"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:07"
    ],
    [
        583,
        "luz-collection",
        "06/09/2024 20:09:07"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:07"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:07"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:09:08"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:09:08"
    ],
    [
        15,
        "dist-collection",
        "06/09/2024 20:09:08"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:08"
    ],
    [
        597,
        "luz-collection",
        "06/09/2024 20:09:08"
    ],
    [
        645,
        "luz-collection",
        "06/09/2024 20:09:08"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:08"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:09:09"
    ],
    [
        15,
        "dist-collection",
        "06/09/2024 20:09:09"
    ],
    [
        15,
        "dist-collection",
        "06/09/2024 20:09:09"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:09"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:09"
    ],
    [
        624,
        "luz-collection",
        "06/09/2024 20:09:09"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:09"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:09"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:09:10"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:09:10"
    ],
    [
        15,
        "dist-collection",
        "06/09/2024 20:09:10"
    ],
    [
        15,
        "dist-collection",
        "06/09/2024 20:09:10"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:10"
    ],
    [
        597,
        "luz-collection",
        "06/09/2024 20:09:10"
    ],
    [
        655,
        "luz-collection",
        "06/09/2024 20:09:10"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:10"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:09:11"
    ],
    [
        15,
        "dist-collection",
        "06/09/2024 20:09:11"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:11"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:11"
    ],
    [
        659,
        "luz-collection",
        "06/09/2024 20:09:11"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:11"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:11"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:09:12"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:09:12"
    ],
    [
        15,
        "dist-collection",
        "06/09/2024 20:09:12"
    ],
    [
        15,
        "dist-collection",
        "06/09/2024 20:09:12"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:12"
    ],
    [
        621,
        "luz-collection",
        "06/09/2024 20:09:12"
    ],
    [
        645,
        "luz-collection",
        "06/09/2024 20:09:12"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:12"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:09:13"
    ],
    [
        15,
        "dist-collection",
        "06/09/2024 20:09:13"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:13"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:13"
    ],
    [
        651,
        "luz-collection",
        "06/09/2024 20:09:13"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:13"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:13"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:09:14"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:09:14"
    ],
    [
        15,
        "dist-collection",
        "06/09/2024 20:09:14"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:14"
    ],
    [
        600,
        "luz-collection",
        "06/09/2024 20:09:14"
    ],
    [
        576,
        "luz-collection",
        "06/09/2024 20:09:14"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:14"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:09:15"
    ],
    [
        15,
        "dist-collection",
        "06/09/2024 20:09:15"
    ],
    [
        15,
        "dist-collection",
        "06/09/2024 20:09:15"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:15"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:15"
    ],
    [
        577,
        "luz-collection",
        "06/09/2024 20:09:15"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:15"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:15"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:09:16"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:09:16"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:09:16"
    ],
    [
        15,
        "dist-collection",
        "06/09/2024 20:09:16"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:16"
    ],
    [
        580,
        "luz-collection",
        "06/09/2024 20:09:16"
    ],
    [
        646,
        "luz-collection",
        "06/09/2024 20:09:16"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:16"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:09:17"
    ],
    [
        15,
        "dist-collection",
        "06/09/2024 20:09:17"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:17"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:17"
    ],
    [
        600,
        "luz-collection",
        "06/09/2024 20:09:17"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:17"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:17"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:09:18"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:09:18"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:18"
    ],
    [
        594,
        "luz-collection",
        "06/09/2024 20:09:18"
    ],
    [
        622,
        "luz-collection",
        "06/09/2024 20:09:18"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:18"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:09:19"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:09:19"
    ],
    [
        15,
        "dist-collection",
        "06/09/2024 20:09:19"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:09:19"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:19"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:19"
    ],
    [
        631,
        "luz-collection",
        "06/09/2024 20:09:19"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:19"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:19"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:09:20"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:09:20"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:09:20"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:09:20"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:20"
    ],
    [
        646,
        "luz-collection",
        "06/09/2024 20:09:20"
    ],
    [
        645,
        "luz-collection",
        "06/09/2024 20:09:20"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:20"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:09:21"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:09:21"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:21"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:21"
    ],
    [
        593,
        "luz-collection",
        "06/09/2024 20:09:21"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:21"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:21"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:09:22"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:09:22"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:09:22"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:09:22"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:22"
    ],
    [
        636,
        "luz-collection",
        "06/09/2024 20:09:22"
    ],
    [
        647,
        "luz-collection",
        "06/09/2024 20:09:22"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:22"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:09:23"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:09:23"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:23"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:23"
    ],
    [
        615,
        "luz-collection",
        "06/09/2024 20:09:23"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:23"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:23"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:09:24"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:09:24"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:09:24"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:09:24"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:24"
    ],
    [
        604,
        "luz-collection",
        "06/09/2024 20:09:24"
    ],
    [
        629,
        "luz-collection",
        "06/09/2024 20:09:24"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:24"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:09:25"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:09:25"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:25"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:25"
    ],
    [
        582,
        "luz-collection",
        "06/09/2024 20:09:25"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:25"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:25"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:09:26"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:09:26"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:09:26"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:26"
    ],
    [
        652,
        "luz-collection",
        "06/09/2024 20:09:26"
    ],
    [
        564,
        "luz-collection",
        "06/09/2024 20:09:26"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:26"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:09:27"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:09:27"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:09:27"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:27"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:27"
    ],
    [
        565,
        "luz-collection",
        "06/09/2024 20:09:27"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:27"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:09:28"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:09:28"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:09:28"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:09:28"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:28"
    ],
    [
        598,
        "luz-collection",
        "06/09/2024 20:09:28"
    ],
    [
        575,
        "luz-collection",
        "06/09/2024 20:09:28"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:28"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:28"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:09:29"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:09:29"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:29"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:29"
    ],
    [
        612,
        "luz-collection",
        "06/09/2024 20:09:29"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:29"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:29"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:09:30"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:09:30"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:09:30"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:09:30"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:30"
    ],
    [
        638,
        "luz-collection",
        "06/09/2024 20:09:30"
    ],
    [
        612,
        "luz-collection",
        "06/09/2024 20:09:30"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:30"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:09:31"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:09:31"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:31"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:31"
    ],
    [
        646,
        "luz-collection",
        "06/09/2024 20:09:31"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:31"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:31"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:09:32"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:09:32"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:09:32"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:32"
    ],
    [
        642,
        "luz-collection",
        "06/09/2024 20:09:32"
    ],
    [
        590,
        "luz-collection",
        "06/09/2024 20:09:32"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:32"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:09:33"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:09:33"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:09:33"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:33"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:33"
    ],
    [
        623,
        "luz-collection",
        "06/09/2024 20:09:33"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:33"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:33"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:09:34"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:09:34"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:09:34"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:34"
    ],
    [
        645,
        "luz-collection",
        "06/09/2024 20:09:34"
    ],
    [
        598,
        "luz-collection",
        "06/09/2024 20:09:34"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:34"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:09:35"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:09:35"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:09:35"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:35"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:35"
    ],
    [
        579,
        "luz-collection",
        "06/09/2024 20:09:35"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:35"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:35"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:09:36"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:09:36"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:09:36"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:09:36"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:36"
    ],
    [
        571,
        "luz-collection",
        "06/09/2024 20:09:36"
    ],
    [
        564,
        "luz-collection",
        "06/09/2024 20:09:36"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:36"
    ],
    [
        387,
        "co2-collection",
        "06/09/2024 20:09:37"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:09:37"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:37"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:37"
    ],
    [
        635,
        "luz-collection",
        "06/09/2024 20:09:37"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:37"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:37"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:09:38"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:09:38"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:09:38"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:38"
    ],
    [
        612,
        "luz-collection",
        "06/09/2024 20:09:38"
    ],
    [
        590,
        "luz-collection",
        "06/09/2024 20:09:38"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:38"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:09:39"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:09:39"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:09:39"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:39"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:39"
    ],
    [
        639,
        "luz-collection",
        "06/09/2024 20:09:39"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:39"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:39"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:09:40"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:09:40"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:40"
    ],
    [
        586,
        "luz-collection",
        "06/09/2024 20:09:40"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:40"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:09:41"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:09:41"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:09:41"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:09:41"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:41"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:41"
    ],
    [
        641,
        "luz-collection",
        "06/09/2024 20:09:41"
    ],
    [
        648,
        "luz-collection",
        "06/09/2024 20:09:41"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:41"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:41"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:09:42"
    ],
    [
        387,
        "co2-collection",
        "06/09/2024 20:09:42"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:09:42"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:09:42"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:42"
    ],
    [
        620,
        "luz-collection",
        "06/09/2024 20:09:42"
    ],
    [
        622,
        "luz-collection",
        "06/09/2024 20:09:42"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:42"
    ],
    [
        387,
        "co2-collection",
        "06/09/2024 20:09:43"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:09:43"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:43"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:43"
    ],
    [
        604,
        "luz-collection",
        "06/09/2024 20:09:43"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:43"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:43"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:09:44"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:09:44"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:09:44"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:44"
    ],
    [
        564,
        "luz-collection",
        "06/09/2024 20:09:44"
    ],
    [
        578,
        "luz-collection",
        "06/09/2024 20:09:44"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:44"
    ],
    [
        387,
        "co2-collection",
        "06/09/2024 20:09:45"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:09:45"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:09:45"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:45"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:45"
    ],
    [
        650,
        "luz-collection",
        "06/09/2024 20:09:45"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:45"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:45"
    ],
    [
        387,
        "co2-collection",
        "06/09/2024 20:09:46"
    ],
    [
        387,
        "co2-collection",
        "06/09/2024 20:09:46"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:09:46"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:09:46"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:46"
    ],
    [
        567,
        "luz-collection",
        "06/09/2024 20:09:46"
    ],
    [
        584,
        "luz-collection",
        "06/09/2024 20:09:46"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:46"
    ],
    [
        387,
        "co2-collection",
        "06/09/2024 20:09:47"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:09:47"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:47"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:47"
    ],
    [
        601,
        "luz-collection",
        "06/09/2024 20:09:47"
    ],
    [
        607,
        "luz-collection",
        "06/09/2024 20:09:47"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:47"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:47"
    ],
    [
        387,
        "co2-collection",
        "06/09/2024 20:09:48"
    ],
    [
        387,
        "co2-collection",
        "06/09/2024 20:09:48"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:09:48"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:09:48"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:48"
    ],
    [
        625,
        "luz-collection",
        "06/09/2024 20:09:48"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:48"
    ],
    [
        387,
        "co2-collection",
        "06/09/2024 20:09:49"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:09:49"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:49"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:49"
    ],
    [
        646,
        "luz-collection",
        "06/09/2024 20:09:49"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:49"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:49"
    ],
    [
        387,
        "co2-collection",
        "06/09/2024 20:09:50"
    ],
    [
        387,
        "co2-collection",
        "06/09/2024 20:09:50"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:09:50"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:09:50"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:50"
    ],
    [
        644,
        "luz-collection",
        "06/09/2024 20:09:50"
    ],
    [
        596,
        "luz-collection",
        "06/09/2024 20:09:50"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:50"
    ],
    [
        387,
        "co2-collection",
        "06/09/2024 20:09:51"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:09:51"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:51"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:51"
    ],
    [
        637,
        "luz-collection",
        "06/09/2024 20:09:51"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:51"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:51"
    ],
    [
        387,
        "co2-collection",
        "06/09/2024 20:09:52"
    ],
    [
        387,
        "co2-collection",
        "06/09/2024 20:09:52"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:09:52"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:09:52"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:52"
    ],
    [
        592,
        "luz-collection",
        "06/09/2024 20:09:52"
    ],
    [
        614,
        "luz-collection",
        "06/09/2024 20:09:52"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:52"
    ],
    [
        387,
        "co2-collection",
        "06/09/2024 20:09:53"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:09:53"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:53"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:53"
    ],
    [
        575,
        "luz-collection",
        "06/09/2024 20:09:53"
    ],
    [
        650,
        "luz-collection",
        "06/09/2024 20:09:53"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:53"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:53"
    ],
    [
        387,
        "co2-collection",
        "06/09/2024 20:09:54"
    ],
    [
        387,
        "co2-collection",
        "06/09/2024 20:09:54"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:09:54"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:09:54"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:54"
    ],
    [
        564,
        "luz-collection",
        "06/09/2024 20:09:54"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:54"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:09:55"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:09:55"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:55"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:55"
    ],
    [
        572,
        "luz-collection",
        "06/09/2024 20:09:55"
    ],
    [
        638,
        "luz-collection",
        "06/09/2024 20:09:55"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:55"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:55"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:09:56"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:09:56"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:09:56"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:09:56"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:56"
    ],
    [
        581,
        "luz-collection",
        "06/09/2024 20:09:56"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:56"
    ],
    [
        387,
        "co2-collection",
        "06/09/2024 20:09:57"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:09:57"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:57"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:57"
    ],
    [
        604,
        "luz-collection",
        "06/09/2024 20:09:57"
    ],
    [
        625,
        "luz-collection",
        "06/09/2024 20:09:57"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:57"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:57"
    ],
    [
        387,
        "co2-collection",
        "06/09/2024 20:09:58"
    ],
    [
        387,
        "co2-collection",
        "06/09/2024 20:09:58"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:09:58"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:09:58"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:58"
    ],
    [
        590,
        "luz-collection",
        "06/09/2024 20:09:58"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:58"
    ],
    [
        387,
        "co2-collection",
        "06/09/2024 20:09:59"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:09:59"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:59"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:09:59"
    ],
    [
        639,
        "luz-collection",
        "06/09/2024 20:09:59"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:59"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:09:59"
    ],
    [
        387,
        "co2-collection",
        "06/09/2024 20:10:00"
    ],
    [
        386,
        "co2-collection",
        "06/09/2024 20:10:00"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:00"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:00"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:00"
    ],
    [
        639,
        "luz-collection",
        "06/09/2024 20:10:00"
    ],
    [
        647,
        "luz-collection",
        "06/09/2024 20:10:00"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:00"
    ],
    [
        386,
        "co2-collection",
        "06/09/2024 20:10:01"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:01"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:01"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:01"
    ],
    [
        603,
        "luz-collection",
        "06/09/2024 20:10:01"
    ],
    [
        630,
        "luz-collection",
        "06/09/2024 20:10:01"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:01"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:01"
    ],
    [
        387,
        "co2-collection",
        "06/09/2024 20:10:02"
    ],
    [
        387,
        "co2-collection",
        "06/09/2024 20:10:02"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:02"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:02"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:02"
    ],
    [
        608,
        "luz-collection",
        "06/09/2024 20:10:02"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:02"
    ],
    [
        386,
        "co2-collection",
        "06/09/2024 20:10:03"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:03"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:03"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:03"
    ],
    [
        585,
        "luz-collection",
        "06/09/2024 20:10:03"
    ],
    [
        653,
        "luz-collection",
        "06/09/2024 20:10:03"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:03"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:03"
    ],
    [
        386,
        "co2-collection",
        "06/09/2024 20:10:04"
    ],
    [
        386,
        "co2-collection",
        "06/09/2024 20:10:04"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:04"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:04"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:04"
    ],
    [
        575,
        "luz-collection",
        "06/09/2024 20:10:04"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:04"
    ],
    [
        387,
        "co2-collection",
        "06/09/2024 20:10:05"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:05"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:05"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:05"
    ],
    [
        572,
        "luz-collection",
        "06/09/2024 20:10:05"
    ],
    [
        580,
        "luz-collection",
        "06/09/2024 20:10:05"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:05"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:05"
    ],
    [
        387,
        "co2-collection",
        "06/09/2024 20:10:06"
    ],
    [
        387,
        "co2-collection",
        "06/09/2024 20:10:06"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:06"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:06"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:06"
    ],
    [
        634,
        "luz-collection",
        "06/09/2024 20:10:06"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:06"
    ],
    [
        387,
        "co2-collection",
        "06/09/2024 20:10:07"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:07"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:07"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:07"
    ],
    [
        591,
        "luz-collection",
        "06/09/2024 20:10:07"
    ],
    [
        614,
        "luz-collection",
        "06/09/2024 20:10:07"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:07"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:07"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:10:08"
    ],
    [
        387,
        "co2-collection",
        "06/09/2024 20:10:08"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:08"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:08"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:08"
    ],
    [
        639,
        "luz-collection",
        "06/09/2024 20:10:08"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:08"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:10:09"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:09"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:09"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:09"
    ],
    [
        585,
        "luz-collection",
        "06/09/2024 20:10:09"
    ],
    [
        648,
        "luz-collection",
        "06/09/2024 20:10:09"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:09"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:09"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:10:10"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:10:10"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:10"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:10"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:10"
    ],
    [
        642,
        "luz-collection",
        "06/09/2024 20:10:10"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:10"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:10:11"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:11"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:11"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:11"
    ],
    [
        619,
        "luz-collection",
        "06/09/2024 20:10:11"
    ],
    [
        623,
        "luz-collection",
        "06/09/2024 20:10:11"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:11"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:11"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:10:12"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:10:12"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:12"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:12"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:12"
    ],
    [
        608,
        "luz-collection",
        "06/09/2024 20:10:12"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:12"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:10:13"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:13"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:13"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:13"
    ],
    [
        565,
        "luz-collection",
        "06/09/2024 20:10:13"
    ],
    [
        583,
        "luz-collection",
        "06/09/2024 20:10:13"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:13"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:13"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 20:10:14"
    ],
    [
        393,
        "co2-collection",
        "06/09/2024 20:10:14"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:14"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:14"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:14"
    ],
    [
        651,
        "luz-collection",
        "06/09/2024 20:10:14"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:14"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 20:10:15"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:15"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:15"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:15"
    ],
    [
        577,
        "luz-collection",
        "06/09/2024 20:10:15"
    ],
    [
        565,
        "luz-collection",
        "06/09/2024 20:10:15"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:15"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:15"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:10:16"
    ],
    [
        393,
        "co2-collection",
        "06/09/2024 20:10:16"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:16"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:16"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:16"
    ],
    [
        598,
        "luz-collection",
        "06/09/2024 20:10:16"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:16"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:10:17"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:17"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:17"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:17"
    ],
    [
        611,
        "luz-collection",
        "06/09/2024 20:10:17"
    ],
    [
        612,
        "luz-collection",
        "06/09/2024 20:10:17"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:17"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:17"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:10:18"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 20:10:18"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:18"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:18"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:18"
    ],
    [
        635,
        "luz-collection",
        "06/09/2024 20:10:18"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:18"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:10:19"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:19"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:19"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:19"
    ],
    [
        646,
        "luz-collection",
        "06/09/2024 20:10:19"
    ],
    [
        587,
        "luz-collection",
        "06/09/2024 20:10:19"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:19"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:19"
    ],
    [
        393,
        "co2-collection",
        "06/09/2024 20:10:20"
    ],
    [
        393,
        "co2-collection",
        "06/09/2024 20:10:20"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:20"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:20"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:20"
    ],
    [
        642,
        "luz-collection",
        "06/09/2024 20:10:20"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:20"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:10:21"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:21"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:21"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:21"
    ],
    [
        631,
        "luz-collection",
        "06/09/2024 20:10:21"
    ],
    [
        608,
        "luz-collection",
        "06/09/2024 20:10:21"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:21"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:21"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:10:22"
    ],
    [
        393,
        "co2-collection",
        "06/09/2024 20:10:22"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:22"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:22"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:22"
    ],
    [
        629,
        "luz-collection",
        "06/09/2024 20:10:22"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:22"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:10:23"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:23"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:23"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:23"
    ],
    [
        572,
        "luz-collection",
        "06/09/2024 20:10:23"
    ],
    [
        598,
        "luz-collection",
        "06/09/2024 20:10:23"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:23"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:23"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:10:24"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:10:24"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:24"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:24"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:24"
    ],
    [
        565,
        "luz-collection",
        "06/09/2024 20:10:24"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:24"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:10:25"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:25"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:25"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:25"
    ],
    [
        647,
        "luz-collection",
        "06/09/2024 20:10:25"
    ],
    [
        569,
        "luz-collection",
        "06/09/2024 20:10:25"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:25"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:25"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:10:26"
    ],
    [
        385,
        "co2-collection",
        "06/09/2024 20:10:26"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:26"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:26"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:26"
    ],
    [
        587,
        "luz-collection",
        "06/09/2024 20:10:26"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:26"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:10:27"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:27"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:27"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:27"
    ],
    [
        602,
        "luz-collection",
        "06/09/2024 20:10:27"
    ],
    [
        611,
        "luz-collection",
        "06/09/2024 20:10:27"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:27"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:27"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:10:28"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:10:28"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:28"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:28"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:28"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:28"
    ],
    [
        636,
        "luz-collection",
        "06/09/2024 20:10:28"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:28"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:10:29"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:29"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:29"
    ],
    [
        650,
        "luz-collection",
        "06/09/2024 20:10:29"
    ],
    [
        638,
        "luz-collection",
        "06/09/2024 20:10:29"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:29"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:29"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:10:30"
    ],
    [
        387,
        "co2-collection",
        "06/09/2024 20:10:30"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:30"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:30"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:30"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:30"
    ],
    [
        612,
        "luz-collection",
        "06/09/2024 20:10:30"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:30"
    ],
    [
        386,
        "co2-collection",
        "06/09/2024 20:10:31"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:31"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:31"
    ],
    [
        590,
        "luz-collection",
        "06/09/2024 20:10:31"
    ],
    [
        619,
        "luz-collection",
        "06/09/2024 20:10:31"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:31"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:31"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:10:32"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:10:32"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:32"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:32"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:32"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:32"
    ],
    [
        567,
        "luz-collection",
        "06/09/2024 20:10:32"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:32"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:10:33"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:10:33"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:33"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:33"
    ],
    [
        652,
        "luz-collection",
        "06/09/2024 20:10:33"
    ],
    [
        568,
        "luz-collection",
        "06/09/2024 20:10:33"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:33"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:33"
    ],
    [
        387,
        "co2-collection",
        "06/09/2024 20:10:34"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:34"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:34"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:34"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:34"
    ],
    [
        591,
        "luz-collection",
        "06/09/2024 20:10:34"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:34"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:10:35"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:35"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:35"
    ],
    [
        585,
        "luz-collection",
        "06/09/2024 20:10:35"
    ],
    [
        620,
        "luz-collection",
        "06/09/2024 20:10:35"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:35"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:35"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:10:36"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:10:36"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:36"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:36"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:36"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:36"
    ],
    [
        645,
        "luz-collection",
        "06/09/2024 20:10:36"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:36"
    ],
    [
        387,
        "co2-collection",
        "06/09/2024 20:10:37"
    ],
    [
        387,
        "co2-collection",
        "06/09/2024 20:10:37"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:37"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:37"
    ],
    [
        638,
        "luz-collection",
        "06/09/2024 20:10:37"
    ],
    [
        613,
        "luz-collection",
        "06/09/2024 20:10:37"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:37"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:37"
    ],
    [
        387,
        "co2-collection",
        "06/09/2024 20:10:38"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:38"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:38"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:38"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:38"
    ],
    [
        634,
        "luz-collection",
        "06/09/2024 20:10:38"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:38"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:10:39"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:10:39"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:39"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:39"
    ],
    [
        564,
        "luz-collection",
        "06/09/2024 20:10:39"
    ],
    [
        580,
        "luz-collection",
        "06/09/2024 20:10:39"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:39"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:39"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:10:40"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:40"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:40"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:40"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:40"
    ],
    [
        580,
        "luz-collection",
        "06/09/2024 20:10:40"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:40"
    ],
    [
        386,
        "co2-collection",
        "06/09/2024 20:10:41"
    ],
    [
        387,
        "co2-collection",
        "06/09/2024 20:10:41"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:41"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:41"
    ],
    [
        610,
        "luz-collection",
        "06/09/2024 20:10:41"
    ],
    [
        618,
        "luz-collection",
        "06/09/2024 20:10:41"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:41"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:41"
    ],
    [
        386,
        "co2-collection",
        "06/09/2024 20:10:42"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:42"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:42"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:42"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:42"
    ],
    [
        640,
        "luz-collection",
        "06/09/2024 20:10:42"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:42"
    ],
    [
        387,
        "co2-collection",
        "06/09/2024 20:10:43"
    ],
    [
        387,
        "co2-collection",
        "06/09/2024 20:10:43"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:43"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:43"
    ],
    [
        612,
        "luz-collection",
        "06/09/2024 20:10:43"
    ],
    [
        641,
        "luz-collection",
        "06/09/2024 20:10:43"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:43"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:43"
    ],
    [
        387,
        "co2-collection",
        "06/09/2024 20:10:44"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:44"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:44"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:44"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:44"
    ],
    [
        624,
        "luz-collection",
        "06/09/2024 20:10:44"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:44"
    ],
    [
        387,
        "co2-collection",
        "06/09/2024 20:10:45"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:10:45"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:45"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:45"
    ],
    [
        569,
        "luz-collection",
        "06/09/2024 20:10:45"
    ],
    [
        593,
        "luz-collection",
        "06/09/2024 20:10:45"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:45"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:45"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:10:46"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:46"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:46"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:46"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:46"
    ],
    [
        654,
        "luz-collection",
        "06/09/2024 20:10:46"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:46"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:10:47"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:10:47"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:47"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:47"
    ],
    [
        580,
        "luz-collection",
        "06/09/2024 20:10:47"
    ],
    [
        607,
        "luz-collection",
        "06/09/2024 20:10:47"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:47"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:47"
    ],
    [
        393,
        "co2-collection",
        "06/09/2024 20:10:48"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:48"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:48"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:48"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:48"
    ],
    [
        637,
        "luz-collection",
        "06/09/2024 20:10:48"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:48"
    ],
    [
        398,
        "co2-collection",
        "06/09/2024 20:10:49"
    ],
    [
        394,
        "co2-collection",
        "06/09/2024 20:10:49"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:49"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:49"
    ],
    [
        591,
        "luz-collection",
        "06/09/2024 20:10:49"
    ],
    [
        650,
        "luz-collection",
        "06/09/2024 20:10:49"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:49"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:49"
    ],
    [
        393,
        "co2-collection",
        "06/09/2024 20:10:50"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:50"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:50"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:50"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:50"
    ],
    [
        637,
        "luz-collection",
        "06/09/2024 20:10:50"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:50"
    ],
    [
        397,
        "co2-collection",
        "06/09/2024 20:10:51"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:10:51"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:51"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:51"
    ],
    [
        608,
        "luz-collection",
        "06/09/2024 20:10:51"
    ],
    [
        644,
        "luz-collection",
        "06/09/2024 20:10:51"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:51"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:51"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:10:52"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:52"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:52"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:52"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:52"
    ],
    [
        581,
        "luz-collection",
        "06/09/2024 20:10:52"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:52"
    ],
    [
        401,
        "co2-collection",
        "06/09/2024 20:10:53"
    ],
    [
        401,
        "co2-collection",
        "06/09/2024 20:10:53"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:53"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:53"
    ],
    [
        567,
        "luz-collection",
        "06/09/2024 20:10:53"
    ],
    [
        580,
        "luz-collection",
        "06/09/2024 20:10:53"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:53"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:53"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 20:10:54"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:54"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:54"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:54"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:54"
    ],
    [
        626,
        "luz-collection",
        "06/09/2024 20:10:54"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:54"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:10:55"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:55"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:55"
    ],
    [
        638,
        "luz-collection",
        "06/09/2024 20:10:55"
    ],
    [
        607,
        "luz-collection",
        "06/09/2024 20:10:55"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:55"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:55"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:10:56"
    ],
    [
        387,
        "co2-collection",
        "06/09/2024 20:10:56"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:56"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:56"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:56"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:56"
    ],
    [
        646,
        "luz-collection",
        "06/09/2024 20:10:56"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:56"
    ],
    [
        387,
        "co2-collection",
        "06/09/2024 20:10:57"
    ],
    [
        387,
        "co2-collection",
        "06/09/2024 20:10:57"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:57"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:57"
    ],
    [
        633,
        "luz-collection",
        "06/09/2024 20:10:57"
    ],
    [
        597,
        "luz-collection",
        "06/09/2024 20:10:57"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:57"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:57"
    ],
    [
        387,
        "co2-collection",
        "06/09/2024 20:10:58"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:58"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:58"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:58"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:58"
    ],
    [
        604,
        "luz-collection",
        "06/09/2024 20:10:58"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:58"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:10:59"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:10:59"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:10:59"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:10:59"
    ],
    [
        574,
        "luz-collection",
        "06/09/2024 20:10:59"
    ],
    [
        653,
        "luz-collection",
        "06/09/2024 20:10:59"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:59"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:10:59"
    ],
    [
        387,
        "co2-collection",
        "06/09/2024 20:11:00"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:00"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:00"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:00"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:00"
    ],
    [
        565,
        "luz-collection",
        "06/09/2024 20:11:00"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:00"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:11:01"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:11:01"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:01"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:01"
    ],
    [
        580,
        "luz-collection",
        "06/09/2024 20:11:01"
    ],
    [
        606,
        "luz-collection",
        "06/09/2024 20:11:01"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:01"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:01"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:11:02"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:02"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:02"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:02"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:02"
    ],
    [
        601,
        "luz-collection",
        "06/09/2024 20:11:02"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:02"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:11:03"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:03"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:03"
    ],
    [
        645,
        "luz-collection",
        "06/09/2024 20:11:03"
    ],
    [
        626,
        "luz-collection",
        "06/09/2024 20:11:03"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:03"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:03"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:11:04"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:11:04"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:04"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:04"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:04"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:04"
    ],
    [
        640,
        "luz-collection",
        "06/09/2024 20:11:04"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:04"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:11:05"
    ],
    [
        388,
        "co2-collection",
        "06/09/2024 20:11:05"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:05"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:05"
    ],
    [
        600,
        "luz-collection",
        "06/09/2024 20:11:05"
    ],
    [
        629,
        "luz-collection",
        "06/09/2024 20:11:05"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:05"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:05"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:11:06"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:06"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:06"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:06"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:06"
    ],
    [
        608,
        "luz-collection",
        "06/09/2024 20:11:06"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:06"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:11:07"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:07"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:07"
    ],
    [
        649,
        "luz-collection",
        "06/09/2024 20:11:07"
    ],
    [
        585,
        "luz-collection",
        "06/09/2024 20:11:07"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:07"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:07"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:11:08"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 20:11:08"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:08"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:08"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:08"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:08"
    ],
    [
        573,
        "luz-collection",
        "06/09/2024 20:11:08"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:08"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 20:11:09"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:09"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:09"
    ],
    [
        563,
        "luz-collection",
        "06/09/2024 20:11:09"
    ],
    [
        572,
        "luz-collection",
        "06/09/2024 20:11:09"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:09"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:09"
    ],
    [
        394,
        "co2-collection",
        "06/09/2024 20:11:10"
    ],
    [
        397,
        "co2-collection",
        "06/09/2024 20:11:10"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:10"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:10"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:10"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:10"
    ],
    [
        636,
        "luz-collection",
        "06/09/2024 20:11:10"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:10"
    ],
    [
        404,
        "co2-collection",
        "06/09/2024 20:11:11"
    ],
    [
        405,
        "co2-collection",
        "06/09/2024 20:11:11"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:11"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:11"
    ],
    [
        579,
        "luz-collection",
        "06/09/2024 20:11:11"
    ],
    [
        601,
        "luz-collection",
        "06/09/2024 20:11:11"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:11"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:11"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:12"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:12"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:12"
    ],
    [
        624,
        "luz-collection",
        "06/09/2024 20:11:12"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:12"
    ],
    [
        402,
        "co2-collection",
        "06/09/2024 20:11:13"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:13"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:13"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:13"
    ],
    [
        400,
        "co2-collection",
        "06/09/2024 20:11:14"
    ],
    [
        404,
        "co2-collection",
        "06/09/2024 20:11:14"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:14"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:14"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:14"
    ],
    [
        634,
        "luz-collection",
        "06/09/2024 20:11:14"
    ],
    [
        645,
        "luz-collection",
        "06/09/2024 20:11:14"
    ],
    [
        588,
        "luz-collection",
        "06/09/2024 20:11:14"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:14"
    ],
    [
        393,
        "co2-collection",
        "06/09/2024 20:11:15"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:15"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:15"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:15"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:15"
    ],
    [
        396,
        "co2-collection",
        "06/09/2024 20:11:16"
    ],
    [
        396,
        "co2-collection",
        "06/09/2024 20:11:16"
    ],
    [
        399,
        "co2-collection",
        "06/09/2024 20:11:16"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:16"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:16"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:16"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:16"
    ],
    [
        634,
        "luz-collection",
        "06/09/2024 20:11:16"
    ],
    [
        639,
        "luz-collection",
        "06/09/2024 20:11:16"
    ],
    [
        597,
        "luz-collection",
        "06/09/2024 20:11:16"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:16"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:16"
    ],
    [
        399,
        "co2-collection",
        "06/09/2024 20:11:17"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:17"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:17"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:17"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:17"
    ],
    [
        615,
        "luz-collection",
        "06/09/2024 20:11:17"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:17"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:17"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:18"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:18"
    ],
    [
        594,
        "luz-collection",
        "06/09/2024 20:11:18"
    ],
    [
        398,
        "co2-collection",
        "06/09/2024 20:11:19"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:19"
    ],
    [
        583,
        "luz-collection",
        "06/09/2024 20:11:19"
    ],
    [
        641,
        "luz-collection",
        "06/09/2024 20:11:19"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:19"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:19"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 20:11:20"
    ],
    [
        397,
        "co2-collection",
        "06/09/2024 20:11:20"
    ],
    [
        399,
        "co2-collection",
        "06/09/2024 20:11:20"
    ],
    [
        395,
        "co2-collection",
        "06/09/2024 20:11:20"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:20"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:20"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:20"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:20"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:20"
    ],
    [
        567,
        "luz-collection",
        "06/09/2024 20:11:20"
    ],
    [
        563,
        "luz-collection",
        "06/09/2024 20:11:20"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:20"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:20"
    ],
    [
        394,
        "co2-collection",
        "06/09/2024 20:11:21"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:21"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:21"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:21"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:21"
    ],
    [
        640,
        "luz-collection",
        "06/09/2024 20:11:21"
    ],
    [
        574,
        "luz-collection",
        "06/09/2024 20:11:21"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:21"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:21"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:11:22"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:22"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:22"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:22"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:22"
    ],
    [
        396,
        "co2-collection",
        "06/09/2024 20:11:23"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:23"
    ],
    [
        597,
        "luz-collection",
        "06/09/2024 20:11:23"
    ],
    [
        619,
        "luz-collection",
        "06/09/2024 20:11:23"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:23"
    ],
    [
        404,
        "co2-collection",
        "06/09/2024 20:11:24"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:11:24"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:24"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:24"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:24"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:24"
    ],
    [
        589,
        "luz-collection",
        "06/09/2024 20:11:24"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:24"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:24"
    ],
    [
        396,
        "co2-collection",
        "06/09/2024 20:11:25"
    ],
    [
        400,
        "co2-collection",
        "06/09/2024 20:11:25"
    ],
    [
        400,
        "co2-collection",
        "06/09/2024 20:11:25"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:25"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:25"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:25"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:25"
    ],
    [
        634,
        "luz-collection",
        "06/09/2024 20:11:25"
    ],
    [
        644,
        "luz-collection",
        "06/09/2024 20:11:25"
    ],
    [
        635,
        "luz-collection",
        "06/09/2024 20:11:25"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:25"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:25"
    ],
    [
        394,
        "co2-collection",
        "06/09/2024 20:11:26"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:26"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:26"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:26"
    ],
    [
        604,
        "luz-collection",
        "06/09/2024 20:11:26"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:26"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:26"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:11:27"
    ],
    [
        395,
        "co2-collection",
        "06/09/2024 20:11:27"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:27"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:27"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:27"
    ],
    [
        625,
        "luz-collection",
        "06/09/2024 20:11:27"
    ],
    [
        602,
        "luz-collection",
        "06/09/2024 20:11:27"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:27"
    ],
    [
        393,
        "co2-collection",
        "06/09/2024 20:11:28"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:28"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:28"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:28"
    ],
    [
        578,
        "luz-collection",
        "06/09/2024 20:11:28"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:28"
    ],
    [
        394,
        "co2-collection",
        "06/09/2024 20:11:29"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:29"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:29"
    ],
    [
        652,
        "luz-collection",
        "06/09/2024 20:11:29"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:29"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:29"
    ],
    [
        393,
        "co2-collection",
        "06/09/2024 20:11:30"
    ],
    [
        396,
        "co2-collection",
        "06/09/2024 20:11:30"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:30"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:30"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:30"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:30"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:30"
    ],
    [
        566,
        "luz-collection",
        "06/09/2024 20:11:30"
    ],
    [
        565,
        "luz-collection",
        "06/09/2024 20:11:30"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:30"
    ],
    [
        397,
        "co2-collection",
        "06/09/2024 20:11:31"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:31"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:31"
    ],
    [
        581,
        "luz-collection",
        "06/09/2024 20:11:31"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:31"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:31"
    ],
    [
        398,
        "co2-collection",
        "06/09/2024 20:11:32"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:32"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:32"
    ],
    [
        623,
        "luz-collection",
        "06/09/2024 20:11:32"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:32"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:33"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:33"
    ],
    [
        596,
        "luz-collection",
        "06/09/2024 20:11:33"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:33"
    ],
    [
        395,
        "co2-collection",
        "06/09/2024 20:11:34"
    ],
    [
        396,
        "co2-collection",
        "06/09/2024 20:11:34"
    ],
    [
        400,
        "co2-collection",
        "06/09/2024 20:11:34"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:34"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:34"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:34"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:34"
    ],
    [
        620,
        "luz-collection",
        "06/09/2024 20:11:34"
    ],
    [
        641,
        "luz-collection",
        "06/09/2024 20:11:34"
    ],
    [
        584,
        "luz-collection",
        "06/09/2024 20:11:34"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:34"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:34"
    ],
    [
        398,
        "co2-collection",
        "06/09/2024 20:11:35"
    ],
    [
        396,
        "co2-collection",
        "06/09/2024 20:11:35"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:35"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:35"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:35"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:35"
    ],
    [
        629,
        "luz-collection",
        "06/09/2024 20:11:35"
    ],
    [
        642,
        "luz-collection",
        "06/09/2024 20:11:35"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:35"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:35"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:11:36"
    ],
    [
        394,
        "co2-collection",
        "06/09/2024 20:11:36"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:36"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:36"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:36"
    ],
    [
        604,
        "luz-collection",
        "06/09/2024 20:11:36"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:36"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:36"
    ],
    [
        389,
        "co2-collection",
        "06/09/2024 20:11:37"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:37"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:37"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:37"
    ],
    [
        634,
        "luz-collection",
        "06/09/2024 20:11:37"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:37"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:11:38"
    ],
    [
        390,
        "co2-collection",
        "06/09/2024 20:11:38"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:38"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:38"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:38"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:38"
    ],
    [
        562,
        "luz-collection",
        "06/09/2024 20:11:38"
    ],
    [
        585,
        "luz-collection",
        "06/09/2024 20:11:38"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:38"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:38"
    ],
    [
        395,
        "co2-collection",
        "06/09/2024 20:11:39"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:11:39"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:39"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:39"
    ],
    [
        634,
        "luz-collection",
        "06/09/2024 20:11:39"
    ],
    [
        568,
        "luz-collection",
        "06/09/2024 20:11:39"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:39"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 20:11:40"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:40"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:40"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:40"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:40"
    ],
    [
        581,
        "luz-collection",
        "06/09/2024 20:11:40"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:40"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:40"
    ],
    [
        395,
        "co2-collection",
        "06/09/2024 20:11:41"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:41"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:41"
    ],
    [
        610,
        "luz-collection",
        "06/09/2024 20:11:41"
    ],
    [
        637,
        "luz-collection",
        "06/09/2024 20:11:41"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:41"
    ],
    [
        394,
        "co2-collection",
        "06/09/2024 20:11:42"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:42"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:42"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:42"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:42"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:11:43"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:43"
    ],
    [
        583,
        "luz-collection",
        "06/09/2024 20:11:43"
    ],
    [
        644,
        "luz-collection",
        "06/09/2024 20:11:43"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:43"
    ],
    [
        391,
        "co2-collection",
        "06/09/2024 20:11:44"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:44"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:44"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:44"
    ],
    [
        629,
        "luz-collection",
        "06/09/2024 20:11:44"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:44"
    ],
    [
        393,
        "co2-collection",
        "06/09/2024 20:11:45"
    ],
    [
        392,
        "co2-collection",
        "06/09/2024 20:11:45"
    ],
    [
        393,
        "co2-collection",
        "06/09/2024 20:11:45"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:45"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:45"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:45"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:45"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:45"
    ],
    [
        577,
        "luz-collection",
        "06/09/2024 20:11:45"
    ],
    [
        637,
        "luz-collection",
        "06/09/2024 20:11:45"
    ],
    [
        604,
        "luz-collection",
        "06/09/2024 20:11:45"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:45"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:45"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:45"
    ],
    [
        395,
        "co2-collection",
        "06/09/2024 20:11:46"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:46"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:46"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:46"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:46"
    ],
    [
        394,
        "co2-collection",
        "06/09/2024 20:11:47"
    ],
    [
        394,
        "co2-collection",
        "06/09/2024 20:11:47"
    ],
    [
        393,
        "co2-collection",
        "06/09/2024 20:11:47"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:47"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:47"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:47"
    ],
    [
        576,
        "luz-collection",
        "06/09/2024 20:11:47"
    ],
    [
        622,
        "luz-collection",
        "06/09/2024 20:11:47"
    ],
    [
        563,
        "luz-collection",
        "06/09/2024 20:11:47"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:47"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:47"
    ],
    [
        16,
        "dist-collection",
        "06/09/2024 20:11:48"
    ],
    [
        80,
        "hum-collection",
        "06/09/2024 20:11:48"
    ],
    [
        23.8,
        "temp-collection",
        "06/09/2024 20:11:48"
    ],
    [
        82,
        "hum-collection",
        "07/09/2024 11:31:20"
    ],
    [
        82,
        "hum-collection",
        "07/09/2024 11:31:20"
    ],
    [
        82,
        "hum-collection",
        "07/09/2024 11:31:20"
    ],
    [
        82,
        "hum-collection",
        "07/09/2024 11:31:20"
    ],
    [
        364,
        "luz-collection",
        "07/09/2024 11:31:20"
    ],
    [
        391,
        "co2-collection",
        "07/09/2024 11:31:21"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:31:21"
    ],
    [
        425,
        "luz-collection",
        "07/09/2024 11:31:21"
    ],
    [
        363,
        "luz-collection",
        "07/09/2024 11:31:21"
    ],
    [
        453,
        "luz-collection",
        "07/09/2024 11:31:21"
    ],
    [
        429,
        "luz-collection",
        "07/09/2024 11:31:21"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:31:21"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:31:21"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:31:21"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:31:21"
    ],
    [
        391,
        "co2-collection",
        "07/09/2024 11:31:22"
    ],
    [
        393,
        "co2-collection",
        "07/09/2024 11:31:22"
    ],
    [
        392,
        "co2-collection",
        "07/09/2024 11:31:22"
    ],
    [
        393,
        "co2-collection",
        "07/09/2024 11:31:22"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:31:22"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:31:22"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:31:22"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:31:22"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:31:22"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:31:23"
    ],
    [
        395,
        "co2-collection",
        "07/09/2024 11:31:24"
    ],
    [
        394,
        "co2-collection",
        "07/09/2024 11:31:24"
    ],
    [
        18,
        "dist-collection",
        "07/09/2024 11:31:24"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:31:24"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:31:24"
    ],
    [
        362,
        "luz-collection",
        "07/09/2024 11:31:24"
    ],
    [
        379,
        "luz-collection",
        "07/09/2024 11:31:24"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:31:24"
    ],
    [
        18,
        "dist-collection",
        "07/09/2024 11:31:25"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:31:25"
    ],
    [
        431,
        "luz-collection",
        "07/09/2024 11:31:25"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:31:25"
    ],
    [
        392,
        "co2-collection",
        "07/09/2024 11:31:26"
    ],
    [
        392,
        "co2-collection",
        "07/09/2024 11:31:26"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:31:26"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:31:26"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:31:26"
    ],
    [
        421,
        "luz-collection",
        "07/09/2024 11:31:26"
    ],
    [
        371,
        "luz-collection",
        "07/09/2024 11:31:26"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:31:26"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:31:26"
    ],
    [
        392,
        "co2-collection",
        "07/09/2024 11:31:27"
    ],
    [
        393,
        "co2-collection",
        "07/09/2024 11:31:27"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:31:27"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:31:27"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:31:27"
    ],
    [
        433,
        "luz-collection",
        "07/09/2024 11:31:27"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:31:27"
    ],
    [
        18,
        "dist-collection",
        "07/09/2024 11:31:28"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:31:28"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:31:28"
    ],
    [
        392,
        "co2-collection",
        "07/09/2024 11:31:29"
    ],
    [
        392,
        "co2-collection",
        "07/09/2024 11:31:29"
    ],
    [
        392,
        "co2-collection",
        "07/09/2024 11:31:29"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:31:29"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:31:29"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:31:29"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:31:29"
    ],
    [
        355,
        "luz-collection",
        "07/09/2024 11:31:29"
    ],
    [
        446,
        "luz-collection",
        "07/09/2024 11:31:29"
    ],
    [
        347,
        "luz-collection",
        "07/09/2024 11:31:29"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:31:29"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:31:29"
    ],
    [
        394,
        "co2-collection",
        "07/09/2024 11:31:30"
    ],
    [
        18,
        "dist-collection",
        "07/09/2024 11:31:30"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:31:30"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:31:30"
    ],
    [
        429,
        "luz-collection",
        "07/09/2024 11:31:30"
    ],
    [
        418,
        "luz-collection",
        "07/09/2024 11:31:30"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:31:30"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:31:30"
    ],
    [
        393,
        "co2-collection",
        "07/09/2024 11:31:31"
    ],
    [
        388,
        "co2-collection",
        "07/09/2024 11:31:31"
    ],
    [
        18,
        "dist-collection",
        "07/09/2024 11:31:31"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:31:31"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:31:31"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:31:31"
    ],
    [
        389,
        "luz-collection",
        "07/09/2024 11:31:31"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:31:31"
    ],
    [
        396,
        "co2-collection",
        "07/09/2024 11:31:32"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:31:32"
    ],
    [
        496,
        "luz-collection",
        "07/09/2024 11:31:32"
    ],
    [
        416,
        "luz-collection",
        "07/09/2024 11:31:32"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:31:32"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:31:32"
    ],
    [
        397,
        "co2-collection",
        "07/09/2024 11:31:33"
    ],
    [
        18,
        "dist-collection",
        "07/09/2024 11:31:33"
    ],
    [
        18,
        "dist-collection",
        "07/09/2024 11:31:33"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:31:33"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:31:33"
    ],
    [
        396,
        "co2-collection",
        "07/09/2024 11:31:34"
    ],
    [
        396,
        "co2-collection",
        "07/09/2024 11:31:34"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:31:34"
    ],
    [
        18,
        "dist-collection",
        "07/09/2024 11:31:34"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:31:34"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:31:34"
    ],
    [
        425,
        "luz-collection",
        "07/09/2024 11:31:34"
    ],
    [
        526,
        "luz-collection",
        "07/09/2024 11:31:34"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:31:34"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:31:34"
    ],
    [
        395,
        "co2-collection",
        "07/09/2024 11:31:35"
    ],
    [
        394,
        "co2-collection",
        "07/09/2024 11:31:35"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:31:35"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:31:35"
    ],
    [
        456,
        "luz-collection",
        "07/09/2024 11:31:35"
    ],
    [
        539,
        "luz-collection",
        "07/09/2024 11:31:35"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:31:35"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:31:36"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:31:36"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:31:36"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:31:36"
    ],
    [
        396,
        "co2-collection",
        "07/09/2024 11:31:37"
    ],
    [
        396,
        "co2-collection",
        "07/09/2024 11:31:37"
    ],
    [
        18,
        "dist-collection",
        "07/09/2024 11:31:37"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:31:37"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:31:37"
    ],
    [
        540,
        "luz-collection",
        "07/09/2024 11:31:37"
    ],
    [
        623,
        "luz-collection",
        "07/09/2024 11:31:37"
    ],
    [
        509,
        "luz-collection",
        "07/09/2024 11:31:37"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:31:37"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:31:37"
    ],
    [
        396,
        "co2-collection",
        "07/09/2024 11:31:38"
    ],
    [
        395,
        "co2-collection",
        "07/09/2024 11:31:38"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:31:38"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:31:38"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:31:38"
    ],
    [
        705,
        "luz-collection",
        "07/09/2024 11:31:38"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:31:38"
    ],
    [
        396,
        "co2-collection",
        "07/09/2024 11:31:39"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:31:39"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:31:39"
    ],
    [
        645,
        "luz-collection",
        "07/09/2024 11:31:39"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:31:39"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:31:40"
    ],
    [
        722,
        "luz-collection",
        "07/09/2024 11:31:40"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:31:40"
    ],
    [
        395,
        "co2-collection",
        "07/09/2024 11:31:41"
    ],
    [
        397,
        "co2-collection",
        "07/09/2024 11:31:41"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:31:41"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:31:41"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:31:41"
    ],
    [
        643,
        "luz-collection",
        "07/09/2024 11:31:41"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:31:41"
    ],
    [
        394,
        "co2-collection",
        "07/09/2024 11:31:42"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:31:42"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:31:42"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:31:42"
    ],
    [
        433,
        "luz-collection",
        "07/09/2024 11:31:42"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:31:42"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:31:42"
    ],
    [
        394,
        "co2-collection",
        "07/09/2024 11:31:43"
    ],
    [
        395,
        "co2-collection",
        "07/09/2024 11:31:43"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:31:43"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:31:43"
    ],
    [
        452,
        "luz-collection",
        "07/09/2024 11:31:43"
    ],
    [
        430,
        "luz-collection",
        "07/09/2024 11:31:43"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:31:43"
    ],
    [
        394,
        "co2-collection",
        "07/09/2024 11:31:44"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:31:44"
    ],
    [
        18,
        "dist-collection",
        "07/09/2024 11:31:44"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:31:44"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:31:44"
    ],
    [
        561,
        "luz-collection",
        "07/09/2024 11:31:44"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:31:44"
    ],
    [
        394,
        "co2-collection",
        "07/09/2024 11:31:45"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:31:45"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:31:45"
    ],
    [
        690,
        "luz-collection",
        "07/09/2024 11:31:45"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:31:45"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:31:46"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:31:46"
    ],
    [
        396,
        "co2-collection",
        "07/09/2024 11:31:47"
    ],
    [
        394,
        "co2-collection",
        "07/09/2024 11:31:47"
    ],
    [
        0,
        "dist-collection",
        "07/09/2024 11:31:47"
    ],
    [
        19,
        "dist-collection",
        "07/09/2024 11:31:47"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:31:47"
    ],
    [
        447,
        "luz-collection",
        "07/09/2024 11:31:47"
    ],
    [
        477,
        "luz-collection",
        "07/09/2024 11:31:47"
    ],
    [
        544,
        "luz-collection",
        "07/09/2024 11:31:47"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:31:47"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:31:47"
    ],
    [
        394,
        "co2-collection",
        "07/09/2024 11:31:48"
    ],
    [
        395,
        "co2-collection",
        "07/09/2024 11:31:48"
    ],
    [
        19,
        "dist-collection",
        "07/09/2024 11:31:48"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:31:48"
    ],
    [
        355,
        "luz-collection",
        "07/09/2024 11:31:48"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:31:48"
    ],
    [
        395,
        "co2-collection",
        "07/09/2024 11:31:49"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:31:49"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:31:49"
    ],
    [
        445,
        "luz-collection",
        "07/09/2024 11:31:49"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:31:49"
    ],
    [
        395,
        "co2-collection",
        "07/09/2024 11:31:50"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:31:50"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:31:50"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:31:50"
    ],
    [
        198,
        "luz-collection",
        "07/09/2024 11:31:50"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:31:50"
    ],
    [
        396,
        "co2-collection",
        "07/09/2024 11:31:51"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:31:51"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:31:51"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:31:51"
    ],
    [
        190,
        "luz-collection",
        "07/09/2024 11:31:51"
    ],
    [
        259,
        "luz-collection",
        "07/09/2024 11:31:51"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:31:51"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:31:51"
    ],
    [
        396,
        "co2-collection",
        "07/09/2024 11:31:52"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:31:52"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:31:52"
    ],
    [
        450,
        "luz-collection",
        "07/09/2024 11:31:52"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:31:52"
    ],
    [
        397,
        "co2-collection",
        "07/09/2024 11:31:53"
    ],
    [
        397,
        "co2-collection",
        "07/09/2024 11:31:53"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:31:53"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:31:53"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:31:53"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:31:53"
    ],
    [
        355,
        "luz-collection",
        "07/09/2024 11:31:53"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:31:53"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:31:53"
    ],
    [
        397,
        "co2-collection",
        "07/09/2024 11:31:54"
    ],
    [
        395,
        "co2-collection",
        "07/09/2024 11:31:54"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:31:54"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:31:54"
    ],
    [
        402,
        "luz-collection",
        "07/09/2024 11:31:54"
    ],
    [
        418,
        "luz-collection",
        "07/09/2024 11:31:54"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:31:54"
    ],
    [
        397,
        "co2-collection",
        "07/09/2024 11:31:55"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:31:55"
    ],
    [
        18,
        "dist-collection",
        "07/09/2024 11:31:55"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:31:55"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:31:55"
    ],
    [
        377,
        "luz-collection",
        "07/09/2024 11:31:55"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:31:55"
    ],
    [
        397,
        "co2-collection",
        "07/09/2024 11:31:56"
    ],
    [
        19,
        "dist-collection",
        "07/09/2024 11:31:56"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:31:56"
    ],
    [
        460,
        "luz-collection",
        "07/09/2024 11:31:56"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:31:56"
    ],
    [
        396,
        "co2-collection",
        "07/09/2024 11:31:57"
    ],
    [
        397,
        "co2-collection",
        "07/09/2024 11:31:57"
    ],
    [
        18,
        "dist-collection",
        "07/09/2024 11:31:57"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:31:57"
    ],
    [
        352,
        "luz-collection",
        "07/09/2024 11:31:57"
    ],
    [
        443,
        "luz-collection",
        "07/09/2024 11:31:57"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:31:57"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:31:57"
    ],
    [
        397,
        "co2-collection",
        "07/09/2024 11:31:58"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:31:58"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:31:58"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:31:58"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:31:58"
    ],
    [
        425,
        "luz-collection",
        "07/09/2024 11:31:58"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:31:58"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:31:58"
    ],
    [
        397,
        "co2-collection",
        "07/09/2024 11:31:59"
    ],
    [
        398,
        "co2-collection",
        "07/09/2024 11:31:59"
    ],
    [
        18,
        "dist-collection",
        "07/09/2024 11:31:59"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:31:59"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:31:59"
    ],
    [
        381,
        "luz-collection",
        "07/09/2024 11:31:59"
    ],
    [
        439,
        "luz-collection",
        "07/09/2024 11:31:59"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:31:59"
    ],
    [
        397,
        "co2-collection",
        "07/09/2024 11:32:00"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:32:00"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:00"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:00"
    ],
    [
        339,
        "luz-collection",
        "07/09/2024 11:32:00"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:00"
    ],
    [
        397,
        "co2-collection",
        "07/09/2024 11:32:01"
    ],
    [
        396,
        "co2-collection",
        "07/09/2024 11:32:01"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:32:01"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:01"
    ],
    [
        375,
        "luz-collection",
        "07/09/2024 11:32:01"
    ],
    [
        453,
        "luz-collection",
        "07/09/2024 11:32:01"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:01"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:01"
    ],
    [
        396,
        "co2-collection",
        "07/09/2024 11:32:02"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:32:02"
    ],
    [
        18,
        "dist-collection",
        "07/09/2024 11:32:02"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:02"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:02"
    ],
    [
        375,
        "luz-collection",
        "07/09/2024 11:32:02"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:02"
    ],
    [
        399,
        "co2-collection",
        "07/09/2024 11:32:03"
    ],
    [
        18,
        "dist-collection",
        "07/09/2024 11:32:03"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:03"
    ],
    [
        430,
        "luz-collection",
        "07/09/2024 11:32:03"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:03"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:03"
    ],
    [
        397,
        "co2-collection",
        "07/09/2024 11:32:04"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:32:04"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:04"
    ],
    [
        357,
        "luz-collection",
        "07/09/2024 11:32:04"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:04"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:05"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:05"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:06"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:07"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:07"
    ],
    [
        445,
        "luz-collection",
        "07/09/2024 11:32:07"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:08"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:08"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:09"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:09"
    ],
    [
        397,
        "co2-collection",
        "07/09/2024 11:32:10"
    ],
    [
        396,
        "co2-collection",
        "07/09/2024 11:32:10"
    ],
    [
        396,
        "co2-collection",
        "07/09/2024 11:32:10"
    ],
    [
        18,
        "dist-collection",
        "07/09/2024 11:32:10"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:10"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:10"
    ],
    [
        449,
        "luz-collection",
        "07/09/2024 11:32:10"
    ],
    [
        397,
        "luz-collection",
        "07/09/2024 11:32:10"
    ],
    [
        360,
        "luz-collection",
        "07/09/2024 11:32:10"
    ],
    [
        356,
        "luz-collection",
        "07/09/2024 11:32:10"
    ],
    [
        440,
        "luz-collection",
        "07/09/2024 11:32:10"
    ],
    [
        380,
        "luz-collection",
        "07/09/2024 11:32:10"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:10"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:10"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:10"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:10"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:10"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:10"
    ],
    [
        397,
        "co2-collection",
        "07/09/2024 11:32:11"
    ],
    [
        397,
        "co2-collection",
        "07/09/2024 11:32:11"
    ],
    [
        397,
        "co2-collection",
        "07/09/2024 11:32:11"
    ],
    [
        397,
        "co2-collection",
        "07/09/2024 11:32:11"
    ],
    [
        397,
        "co2-collection",
        "07/09/2024 11:32:11"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:32:11"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:32:11"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:11"
    ],
    [
        437,
        "luz-collection",
        "07/09/2024 11:32:11"
    ],
    [
        385,
        "luz-collection",
        "07/09/2024 11:32:11"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:11"
    ],
    [
        398,
        "co2-collection",
        "07/09/2024 11:32:12"
    ],
    [
        396,
        "co2-collection",
        "07/09/2024 11:32:12"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:32:12"
    ],
    [
        18,
        "dist-collection",
        "07/09/2024 11:32:12"
    ],
    [
        18,
        "dist-collection",
        "07/09/2024 11:32:12"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:32:12"
    ],
    [
        18,
        "dist-collection",
        "07/09/2024 11:32:12"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:32:12"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:12"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:12"
    ],
    [
        344,
        "luz-collection",
        "07/09/2024 11:32:12"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:12"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:13"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:14"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:15"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:15"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:16"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:17"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:17"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:18"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:19"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:19"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:21"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:21"
    ],
    [
        397,
        "co2-collection",
        "07/09/2024 11:32:22"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:32:22"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:22"
    ],
    [
        435,
        "luz-collection",
        "07/09/2024 11:32:22"
    ],
    [
        438,
        "luz-collection",
        "07/09/2024 11:32:22"
    ],
    [
        446,
        "luz-collection",
        "07/09/2024 11:32:22"
    ],
    [
        394,
        "luz-collection",
        "07/09/2024 11:32:22"
    ],
    [
        368,
        "luz-collection",
        "07/09/2024 11:32:22"
    ],
    [
        376,
        "luz-collection",
        "07/09/2024 11:32:22"
    ],
    [
        388,
        "luz-collection",
        "07/09/2024 11:32:22"
    ],
    [
        379,
        "luz-collection",
        "07/09/2024 11:32:22"
    ],
    [
        455,
        "luz-collection",
        "07/09/2024 11:32:22"
    ],
    [
        452,
        "luz-collection",
        "07/09/2024 11:32:22"
    ],
    [
        349,
        "luz-collection",
        "07/09/2024 11:32:22"
    ],
    [
        364,
        "luz-collection",
        "07/09/2024 11:32:22"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:22"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:22"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:22"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:22"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:22"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:22"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:22"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:22"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:22"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:22"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:22"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:22"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:22"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:22"
    ],
    [
        398,
        "co2-collection",
        "07/09/2024 11:32:23"
    ],
    [
        398,
        "co2-collection",
        "07/09/2024 11:32:23"
    ],
    [
        398,
        "co2-collection",
        "07/09/2024 11:32:23"
    ],
    [
        400,
        "co2-collection",
        "07/09/2024 11:32:23"
    ],
    [
        400,
        "co2-collection",
        "07/09/2024 11:32:23"
    ],
    [
        397,
        "co2-collection",
        "07/09/2024 11:32:23"
    ],
    [
        399,
        "co2-collection",
        "07/09/2024 11:32:23"
    ],
    [
        398,
        "co2-collection",
        "07/09/2024 11:32:23"
    ],
    [
        397,
        "co2-collection",
        "07/09/2024 11:32:23"
    ],
    [
        398,
        "co2-collection",
        "07/09/2024 11:32:23"
    ],
    [
        398,
        "co2-collection",
        "07/09/2024 11:32:23"
    ],
    [
        397,
        "co2-collection",
        "07/09/2024 11:32:23"
    ],
    [
        394,
        "co2-collection",
        "07/09/2024 11:32:23"
    ],
    [
        399,
        "co2-collection",
        "07/09/2024 11:32:23"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:32:23"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:32:23"
    ],
    [
        18,
        "dist-collection",
        "07/09/2024 11:32:23"
    ],
    [
        18,
        "dist-collection",
        "07/09/2024 11:32:23"
    ],
    [
        18,
        "dist-collection",
        "07/09/2024 11:32:23"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:32:23"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:32:23"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:23"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:23"
    ],
    [
        403,
        "luz-collection",
        "07/09/2024 11:32:23"
    ],
    [
        346,
        "luz-collection",
        "07/09/2024 11:32:23"
    ],
    [
        442,
        "luz-collection",
        "07/09/2024 11:32:23"
    ],
    [
        411,
        "luz-collection",
        "07/09/2024 11:32:23"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:23"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:23"
    ],
    [
        393,
        "co2-collection",
        "07/09/2024 11:32:24"
    ],
    [
        389,
        "co2-collection",
        "07/09/2024 11:32:24"
    ],
    [
        395,
        "co2-collection",
        "07/09/2024 11:32:24"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:32:24"
    ],
    [
        18,
        "dist-collection",
        "07/09/2024 11:32:24"
    ],
    [
        18,
        "dist-collection",
        "07/09/2024 11:32:24"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:32:24"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:32:24"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:32:24"
    ],
    [
        18,
        "dist-collection",
        "07/09/2024 11:32:24"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:32:24"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:32:24"
    ],
    [
        18,
        "dist-collection",
        "07/09/2024 11:32:24"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:24"
    ],
    [
        442,
        "luz-collection",
        "07/09/2024 11:32:24"
    ],
    [
        392,
        "luz-collection",
        "07/09/2024 11:32:24"
    ],
    [
        336,
        "luz-collection",
        "07/09/2024 11:32:24"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:24"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:24"
    ],
    [
        393,
        "co2-collection",
        "07/09/2024 11:32:25"
    ],
    [
        18,
        "dist-collection",
        "07/09/2024 11:32:25"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:32:25"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:25"
    ],
    [
        409,
        "luz-collection",
        "07/09/2024 11:32:25"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:25"
    ],
    [
        391,
        "co2-collection",
        "07/09/2024 11:32:26"
    ],
    [
        393,
        "co2-collection",
        "07/09/2024 11:32:26"
    ],
    [
        18,
        "dist-collection",
        "07/09/2024 11:32:26"
    ],
    [
        19,
        "dist-collection",
        "07/09/2024 11:32:26"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:26"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:26"
    ],
    [
        425,
        "luz-collection",
        "07/09/2024 11:32:26"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:26"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:26"
    ],
    [
        390,
        "co2-collection",
        "07/09/2024 11:32:27"
    ],
    [
        393,
        "co2-collection",
        "07/09/2024 11:32:27"
    ],
    [
        18,
        "dist-collection",
        "07/09/2024 11:32:27"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:27"
    ],
    [
        430,
        "luz-collection",
        "07/09/2024 11:32:27"
    ],
    [
        373,
        "luz-collection",
        "07/09/2024 11:32:27"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:27"
    ],
    [
        391,
        "co2-collection",
        "07/09/2024 11:32:28"
    ],
    [
        18,
        "dist-collection",
        "07/09/2024 11:32:28"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:32:28"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:28"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:28"
    ],
    [
        336,
        "luz-collection",
        "07/09/2024 11:32:28"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:28"
    ],
    [
        394,
        "co2-collection",
        "07/09/2024 11:32:29"
    ],
    [
        392,
        "co2-collection",
        "07/09/2024 11:32:29"
    ],
    [
        18,
        "dist-collection",
        "07/09/2024 11:32:29"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:29"
    ],
    [
        350,
        "luz-collection",
        "07/09/2024 11:32:29"
    ],
    [
        448,
        "luz-collection",
        "07/09/2024 11:32:29"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:29"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:29"
    ],
    [
        391,
        "co2-collection",
        "07/09/2024 11:32:30"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:32:30"
    ],
    [
        18,
        "dist-collection",
        "07/09/2024 11:32:30"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:30"
    ],
    [
        375,
        "luz-collection",
        "07/09/2024 11:32:30"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:30"
    ],
    [
        396,
        "co2-collection",
        "07/09/2024 11:32:31"
    ],
    [
        19,
        "dist-collection",
        "07/09/2024 11:32:31"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:31"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:31"
    ],
    [
        418,
        "luz-collection",
        "07/09/2024 11:32:31"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:31"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:31"
    ],
    [
        396,
        "co2-collection",
        "07/09/2024 11:32:32"
    ],
    [
        395,
        "co2-collection",
        "07/09/2024 11:32:32"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:32:32"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:32"
    ],
    [
        446,
        "luz-collection",
        "07/09/2024 11:32:32"
    ],
    [
        365,
        "luz-collection",
        "07/09/2024 11:32:32"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:32"
    ],
    [
        394,
        "co2-collection",
        "07/09/2024 11:32:33"
    ],
    [
        18,
        "dist-collection",
        "07/09/2024 11:32:33"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:33"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:33"
    ],
    [
        349,
        "luz-collection",
        "07/09/2024 11:32:33"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:33"
    ],
    [
        394,
        "co2-collection",
        "07/09/2024 11:32:34"
    ],
    [
        393,
        "co2-collection",
        "07/09/2024 11:32:34"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:32:34"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:32:34"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:34"
    ],
    [
        374,
        "luz-collection",
        "07/09/2024 11:32:34"
    ],
    [
        444,
        "luz-collection",
        "07/09/2024 11:32:34"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:34"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:34"
    ],
    [
        394,
        "co2-collection",
        "07/09/2024 11:32:35"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:32:35"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:32:35"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:35"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:35"
    ],
    [
        412,
        "luz-collection",
        "07/09/2024 11:32:35"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:35"
    ],
    [
        395,
        "co2-collection",
        "07/09/2024 11:32:36"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:32:36"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:36"
    ],
    [
        359,
        "luz-collection",
        "07/09/2024 11:32:36"
    ],
    [
        421,
        "luz-collection",
        "07/09/2024 11:32:36"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:36"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:36"
    ],
    [
        395,
        "co2-collection",
        "07/09/2024 11:32:37"
    ],
    [
        393,
        "co2-collection",
        "07/09/2024 11:32:37"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:32:37"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:32:37"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:37"
    ],
    [
        431,
        "luz-collection",
        "07/09/2024 11:32:37"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:37"
    ],
    [
        395,
        "co2-collection",
        "07/09/2024 11:32:38"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:32:38"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:38"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:38"
    ],
    [
        339,
        "luz-collection",
        "07/09/2024 11:32:38"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:38"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:38"
    ],
    [
        395,
        "co2-collection",
        "07/09/2024 11:32:39"
    ],
    [
        394,
        "co2-collection",
        "07/09/2024 11:32:39"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:32:39"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:39"
    ],
    [
        435,
        "luz-collection",
        "07/09/2024 11:32:39"
    ],
    [
        346,
        "luz-collection",
        "07/09/2024 11:32:39"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:39"
    ],
    [
        393,
        "co2-collection",
        "07/09/2024 11:32:40"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:32:40"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:32:40"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:40"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:40"
    ],
    [
        396,
        "luz-collection",
        "07/09/2024 11:32:40"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:40"
    ],
    [
        394,
        "co2-collection",
        "07/09/2024 11:32:41"
    ],
    [
        18,
        "dist-collection",
        "07/09/2024 11:32:41"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:41"
    ],
    [
        372,
        "luz-collection",
        "07/09/2024 11:32:41"
    ],
    [
        423,
        "luz-collection",
        "07/09/2024 11:32:41"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:41"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:41"
    ],
    [
        397,
        "co2-collection",
        "07/09/2024 11:32:42"
    ],
    [
        396,
        "co2-collection",
        "07/09/2024 11:32:42"
    ],
    [
        18,
        "dist-collection",
        "07/09/2024 11:32:42"
    ],
    [
        18,
        "dist-collection",
        "07/09/2024 11:32:42"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:42"
    ],
    [
        429,
        "luz-collection",
        "07/09/2024 11:32:42"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:42"
    ],
    [
        397,
        "co2-collection",
        "07/09/2024 11:32:43"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:32:43"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:43"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:43"
    ],
    [
        342,
        "luz-collection",
        "07/09/2024 11:32:43"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:43"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:43"
    ],
    [
        396,
        "co2-collection",
        "07/09/2024 11:32:44"
    ],
    [
        396,
        "co2-collection",
        "07/09/2024 11:32:44"
    ],
    [
        18,
        "dist-collection",
        "07/09/2024 11:32:44"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:44"
    ],
    [
        444,
        "luz-collection",
        "07/09/2024 11:32:44"
    ],
    [
        343,
        "luz-collection",
        "07/09/2024 11:32:44"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:44"
    ],
    [
        396,
        "co2-collection",
        "07/09/2024 11:32:45"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:32:45"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:32:45"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:45"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:45"
    ],
    [
        389,
        "luz-collection",
        "07/09/2024 11:32:45"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:45"
    ],
    [
        397,
        "co2-collection",
        "07/09/2024 11:32:46"
    ],
    [
        18,
        "dist-collection",
        "07/09/2024 11:32:46"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:46"
    ],
    [
        368,
        "luz-collection",
        "07/09/2024 11:32:46"
    ],
    [
        387,
        "luz-collection",
        "07/09/2024 11:32:46"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:46"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:46"
    ],
    [
        396,
        "co2-collection",
        "07/09/2024 11:32:47"
    ],
    [
        396,
        "co2-collection",
        "07/09/2024 11:32:47"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:32:47"
    ],
    [
        18,
        "dist-collection",
        "07/09/2024 11:32:47"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:47"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:47"
    ],
    [
        435,
        "luz-collection",
        "07/09/2024 11:32:47"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:47"
    ],
    [
        394,
        "co2-collection",
        "07/09/2024 11:32:48"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:32:48"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:48"
    ],
    [
        354,
        "luz-collection",
        "07/09/2024 11:32:48"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:48"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:48"
    ],
    [
        394,
        "co2-collection",
        "07/09/2024 11:32:49"
    ],
    [
        394,
        "co2-collection",
        "07/09/2024 11:32:49"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:32:49"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:49"
    ],
    [
        448,
        "luz-collection",
        "07/09/2024 11:32:49"
    ],
    [
        363,
        "luz-collection",
        "07/09/2024 11:32:49"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:49"
    ],
    [
        395,
        "co2-collection",
        "07/09/2024 11:32:50"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:32:50"
    ],
    [
        18,
        "dist-collection",
        "07/09/2024 11:32:50"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:50"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:50"
    ],
    [
        424,
        "luz-collection",
        "07/09/2024 11:32:50"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:50"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:50"
    ],
    [
        394,
        "co2-collection",
        "07/09/2024 11:32:51"
    ],
    [
        394,
        "co2-collection",
        "07/09/2024 11:32:51"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:32:51"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:51"
    ],
    [
        419,
        "luz-collection",
        "07/09/2024 11:32:51"
    ],
    [
        362,
        "luz-collection",
        "07/09/2024 11:32:51"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:51"
    ],
    [
        396,
        "co2-collection",
        "07/09/2024 11:32:52"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:32:52"
    ],
    [
        19,
        "dist-collection",
        "07/09/2024 11:32:52"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:52"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:52"
    ],
    [
        428,
        "luz-collection",
        "07/09/2024 11:32:52"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:52"
    ],
    [
        395,
        "co2-collection",
        "07/09/2024 11:32:53"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:32:53"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:53"
    ],
    [
        437,
        "luz-collection",
        "07/09/2024 11:32:53"
    ],
    [
        342,
        "luz-collection",
        "07/09/2024 11:32:53"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:53"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:53"
    ],
    [
        399,
        "co2-collection",
        "07/09/2024 11:32:54"
    ],
    [
        398,
        "co2-collection",
        "07/09/2024 11:32:54"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:32:54"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:32:54"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:54"
    ],
    [
        345,
        "luz-collection",
        "07/09/2024 11:32:54"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:54"
    ],
    [
        398,
        "co2-collection",
        "07/09/2024 11:32:55"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:32:55"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:55"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:55"
    ],
    [
        404,
        "luz-collection",
        "07/09/2024 11:32:55"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:55"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:55"
    ],
    [
        397,
        "co2-collection",
        "07/09/2024 11:32:56"
    ],
    [
        398,
        "co2-collection",
        "07/09/2024 11:32:56"
    ],
    [
        18,
        "dist-collection",
        "07/09/2024 11:32:56"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:56"
    ],
    [
        422,
        "luz-collection",
        "07/09/2024 11:32:56"
    ],
    [
        370,
        "luz-collection",
        "07/09/2024 11:32:56"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:56"
    ],
    [
        398,
        "co2-collection",
        "07/09/2024 11:32:57"
    ],
    [
        18,
        "dist-collection",
        "07/09/2024 11:32:57"
    ],
    [
        18,
        "dist-collection",
        "07/09/2024 11:32:57"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:57"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:57"
    ],
    [
        426,
        "luz-collection",
        "07/09/2024 11:32:57"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:57"
    ],
    [
        397,
        "co2-collection",
        "07/09/2024 11:32:58"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:32:58"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:58"
    ],
    [
        343,
        "luz-collection",
        "07/09/2024 11:32:58"
    ],
    [
        438,
        "luz-collection",
        "07/09/2024 11:32:58"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:58"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:58"
    ],
    [
        397,
        "co2-collection",
        "07/09/2024 11:32:59"
    ],
    [
        398,
        "co2-collection",
        "07/09/2024 11:32:59"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:32:59"
    ],
    [
        18,
        "dist-collection",
        "07/09/2024 11:32:59"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:59"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:32:59"
    ],
    [
        333,
        "luz-collection",
        "07/09/2024 11:32:59"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:32:59"
    ],
    [
        397,
        "co2-collection",
        "07/09/2024 11:33:00"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:33:00"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:33:00"
    ],
    [
        349,
        "luz-collection",
        "07/09/2024 11:33:00"
    ],
    [
        422,
        "luz-collection",
        "07/09/2024 11:33:00"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:33:00"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:33:00"
    ],
    [
        397,
        "co2-collection",
        "07/09/2024 11:33:01"
    ],
    [
        397,
        "co2-collection",
        "07/09/2024 11:33:01"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:33:01"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:33:01"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:33:01"
    ],
    [
        380,
        "luz-collection",
        "07/09/2024 11:33:01"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:33:01"
    ],
    [
        399,
        "co2-collection",
        "07/09/2024 11:33:02"
    ],
    [
        19,
        "dist-collection",
        "07/09/2024 11:33:02"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:33:02"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:33:02"
    ],
    [
        422,
        "luz-collection",
        "07/09/2024 11:33:02"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:33:02"
    ],
    [
        399,
        "co2-collection",
        "07/09/2024 11:33:03"
    ],
    [
        401,
        "co2-collection",
        "07/09/2024 11:33:03"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:33:03"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:33:03"
    ],
    [
        366,
        "luz-collection",
        "07/09/2024 11:33:03"
    ],
    [
        428,
        "luz-collection",
        "07/09/2024 11:33:03"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:33:03"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:33:03"
    ],
    [
        399,
        "co2-collection",
        "07/09/2024 11:33:04"
    ],
    [
        18,
        "dist-collection",
        "07/09/2024 11:33:04"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:33:04"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:33:04"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:33:04"
    ],
    [
        335,
        "luz-collection",
        "07/09/2024 11:33:04"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:33:04"
    ],
    [
        399,
        "co2-collection",
        "07/09/2024 11:33:05"
    ],
    [
        18,
        "dist-collection",
        "07/09/2024 11:33:05"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:33:05"
    ],
    [
        350,
        "luz-collection",
        "07/09/2024 11:33:05"
    ],
    [
        446,
        "luz-collection",
        "07/09/2024 11:33:05"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:33:05"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:33:05"
    ],
    [
        399,
        "co2-collection",
        "07/09/2024 11:33:06"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:33:06"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:33:06"
    ],
    [
        398,
        "co2-collection",
        "07/09/2024 11:33:07"
    ],
    [
        399,
        "co2-collection",
        "07/09/2024 11:33:07"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:33:07"
    ],
    [
        18,
        "dist-collection",
        "07/09/2024 11:33:07"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:33:07"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:33:07"
    ],
    [
        417,
        "luz-collection",
        "07/09/2024 11:33:07"
    ],
    [
        374,
        "luz-collection",
        "07/09/2024 11:33:07"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:33:07"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:33:07"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:33:07"
    ],
    [
        399,
        "co2-collection",
        "07/09/2024 11:33:08"
    ],
    [
        398,
        "co2-collection",
        "07/09/2024 11:33:08"
    ],
    [
        18,
        "dist-collection",
        "07/09/2024 11:33:08"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:33:08"
    ],
    [
        448,
        "luz-collection",
        "07/09/2024 11:33:08"
    ],
    [
        362,
        "luz-collection",
        "07/09/2024 11:33:08"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:33:08"
    ],
    [
        398,
        "co2-collection",
        "07/09/2024 11:33:09"
    ],
    [
        18,
        "dist-collection",
        "07/09/2024 11:33:09"
    ],
    [
        19,
        "dist-collection",
        "07/09/2024 11:33:09"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:33:09"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:33:09"
    ],
    [
        343,
        "luz-collection",
        "07/09/2024 11:33:09"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:33:09"
    ],
    [
        396,
        "co2-collection",
        "07/09/2024 11:33:10"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:33:10"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:33:10"
    ],
    [
        411,
        "luz-collection",
        "07/09/2024 11:33:10"
    ],
    [
        433,
        "luz-collection",
        "07/09/2024 11:33:10"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:33:10"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:33:10"
    ],
    [
        397,
        "co2-collection",
        "07/09/2024 11:33:11"
    ],
    [
        396,
        "co2-collection",
        "07/09/2024 11:33:11"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:33:11"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:33:11"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:33:11"
    ],
    [
        375,
        "luz-collection",
        "07/09/2024 11:33:11"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:33:11"
    ],
    [
        395,
        "co2-collection",
        "07/09/2024 11:33:12"
    ],
    [
        18,
        "dist-collection",
        "07/09/2024 11:33:12"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:33:12"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:33:12"
    ],
    [
        350,
        "luz-collection",
        "07/09/2024 11:33:12"
    ],
    [
        424,
        "luz-collection",
        "07/09/2024 11:33:12"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:33:12"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:33:12"
    ],
    [
        396,
        "co2-collection",
        "07/09/2024 11:33:13"
    ],
    [
        394,
        "co2-collection",
        "07/09/2024 11:33:13"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:33:13"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:33:13"
    ],
    [
        433,
        "luz-collection",
        "07/09/2024 11:33:13"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:33:13"
    ],
    [
        396,
        "co2-collection",
        "07/09/2024 11:33:14"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:33:14"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:33:14"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:33:14"
    ],
    [
        336,
        "luz-collection",
        "07/09/2024 11:33:14"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:33:14"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:33:14"
    ],
    [
        394,
        "co2-collection",
        "07/09/2024 11:33:15"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:33:15"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:33:15"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:33:15"
    ],
    [
        409,
        "luz-collection",
        "07/09/2024 11:33:15"
    ],
    [
        377,
        "luz-collection",
        "07/09/2024 11:33:15"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:33:15"
    ],
    [
        394,
        "co2-collection",
        "07/09/2024 11:33:16"
    ],
    [
        396,
        "co2-collection",
        "07/09/2024 11:33:16"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:33:16"
    ],
    [
        18,
        "dist-collection",
        "07/09/2024 11:33:16"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:33:16"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:33:16"
    ],
    [
        367,
        "luz-collection",
        "07/09/2024 11:33:16"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:33:16"
    ],
    [
        395,
        "co2-collection",
        "07/09/2024 11:33:17"
    ],
    [
        19,
        "dist-collection",
        "07/09/2024 11:33:17"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:33:17"
    ],
    [
        353,
        "luz-collection",
        "07/09/2024 11:33:17"
    ],
    [
        436,
        "luz-collection",
        "07/09/2024 11:33:17"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:33:17"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:33:17"
    ],
    [
        393,
        "co2-collection",
        "07/09/2024 11:33:18"
    ],
    [
        393,
        "co2-collection",
        "07/09/2024 11:33:18"
    ],
    [
        18,
        "dist-collection",
        "07/09/2024 11:33:18"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:33:18"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:33:18"
    ],
    [
        446,
        "luz-collection",
        "07/09/2024 11:33:18"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:33:18"
    ],
    [
        396,
        "co2-collection",
        "07/09/2024 11:33:19"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:33:19"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:33:19"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:33:19"
    ],
    [
        357,
        "luz-collection",
        "07/09/2024 11:33:19"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:33:19"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:33:19"
    ],
    [
        395,
        "co2-collection",
        "07/09/2024 11:33:20"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:33:20"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:33:20"
    ],
    [
        420,
        "luz-collection",
        "07/09/2024 11:33:20"
    ],
    [
        418,
        "luz-collection",
        "07/09/2024 11:33:20"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:33:20"
    ],
    [
        393,
        "co2-collection",
        "07/09/2024 11:33:21"
    ],
    [
        395,
        "co2-collection",
        "07/09/2024 11:33:21"
    ],
    [
        18,
        "dist-collection",
        "07/09/2024 11:33:21"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:33:21"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:33:21"
    ],
    [
        360,
        "luz-collection",
        "07/09/2024 11:33:21"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:33:21"
    ],
    [
        393,
        "co2-collection",
        "07/09/2024 11:33:22"
    ],
    [
        19,
        "dist-collection",
        "07/09/2024 11:33:22"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:33:22"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:33:22"
    ],
    [
        428,
        "luz-collection",
        "07/09/2024 11:33:22"
    ],
    [
        342,
        "luz-collection",
        "07/09/2024 11:33:22"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:33:22"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:33:22"
    ],
    [
        392,
        "co2-collection",
        "07/09/2024 11:33:23"
    ],
    [
        392,
        "co2-collection",
        "07/09/2024 11:33:23"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:33:23"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:33:23"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:33:23"
    ],
    [
        437,
        "luz-collection",
        "07/09/2024 11:33:23"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:33:23"
    ],
    [
        394,
        "co2-collection",
        "07/09/2024 11:33:24"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:33:24"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:33:24"
    ],
    [
        334,
        "luz-collection",
        "07/09/2024 11:33:24"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:33:24"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:33:24"
    ],
    [
        393,
        "co2-collection",
        "07/09/2024 11:33:25"
    ],
    [
        393,
        "co2-collection",
        "07/09/2024 11:33:25"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:33:25"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:33:25"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:33:25"
    ],
    [
        398,
        "luz-collection",
        "07/09/2024 11:33:25"
    ],
    [
        424,
        "luz-collection",
        "07/09/2024 11:33:25"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:33:25"
    ],
    [
        392,
        "co2-collection",
        "07/09/2024 11:33:26"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:33:26"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:33:26"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:33:26"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:33:26"
    ],
    [
        406,
        "luz-collection",
        "07/09/2024 11:33:26"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:33:26"
    ],
    [
        395,
        "co2-collection",
        "07/09/2024 11:33:27"
    ],
    [
        392,
        "co2-collection",
        "07/09/2024 11:33:27"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:33:27"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:33:27"
    ],
    [
        412,
        "luz-collection",
        "07/09/2024 11:33:27"
    ],
    [
        363,
        "luz-collection",
        "07/09/2024 11:33:27"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:33:27"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:33:27"
    ],
    [
        17,
        "dist-collection",
        "07/09/2024 11:33:28"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 11:33:28"
    ],
    [
        418,
        "luz-collection",
        "07/09/2024 11:33:28"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 11:33:28"
    ],
    [
        84,
        "hum-collection",
        "07/09/2024 12:11:36"
    ],
    [
        84,
        "hum-collection",
        "07/09/2024 12:11:37"
    ],
    [
        84,
        "hum-collection",
        "07/09/2024 12:11:38"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 12:11:38"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 12:11:39"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 12:11:40"
    ],
    [
        431,
        "luz-collection",
        "07/09/2024 12:11:40"
    ],
    [
        316,
        "luz-collection",
        "07/09/2024 12:11:40"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 12:11:40"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 12:11:40"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 12:11:40"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 12:11:40"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 12:11:40"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 12:11:40"
    ],
    [
        403,
        "co2-collection",
        "07/09/2024 12:11:41"
    ],
    [
        394,
        "co2-collection",
        "07/09/2024 12:11:41"
    ],
    [
        383,
        "co2-collection",
        "07/09/2024 12:11:41"
    ],
    [
        396,
        "co2-collection",
        "07/09/2024 12:11:41"
    ],
    [
        385,
        "co2-collection",
        "07/09/2024 12:11:41"
    ],
    [
        395,
        "co2-collection",
        "07/09/2024 12:11:41"
    ],
    [
        395,
        "co2-collection",
        "07/09/2024 12:11:41"
    ],
    [
        18,
        "dist-collection",
        "07/09/2024 12:11:41"
    ],
    [
        19,
        "dist-collection",
        "07/09/2024 12:11:41"
    ],
    [
        19,
        "dist-collection",
        "07/09/2024 12:11:41"
    ],
    [
        18,
        "dist-collection",
        "07/09/2024 12:11:41"
    ],
    [
        19,
        "dist-collection",
        "07/09/2024 12:11:41"
    ],
    [
        19,
        "dist-collection",
        "07/09/2024 12:11:41"
    ],
    [
        82,
        "hum-collection",
        "07/09/2024 12:11:41"
    ],
    [
        82,
        "hum-collection",
        "07/09/2024 12:11:41"
    ],
    [
        314,
        "luz-collection",
        "07/09/2024 12:11:41"
    ],
    [
        308,
        "luz-collection",
        "07/09/2024 12:11:41"
    ],
    [
        313,
        "luz-collection",
        "07/09/2024 12:11:41"
    ],
    [
        313,
        "luz-collection",
        "07/09/2024 12:11:41"
    ],
    [
        313,
        "luz-collection",
        "07/09/2024 12:11:41"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 12:11:41"
    ],
    [
        389,
        "co2-collection",
        "07/09/2024 12:11:42"
    ],
    [
        396,
        "co2-collection",
        "07/09/2024 12:11:42"
    ],
    [
        20,
        "dist-collection",
        "07/09/2024 12:11:42"
    ],
    [
        445,
        "dist-collection",
        "07/09/2024 12:11:42"
    ],
    [
        82,
        "hum-collection",
        "07/09/2024 12:11:42"
    ],
    [
        311,
        "luz-collection",
        "07/09/2024 12:11:42"
    ],
    [
        308,
        "luz-collection",
        "07/09/2024 12:11:42"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 12:11:42"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 12:11:42"
    ],
    [
        389,
        "co2-collection",
        "07/09/2024 12:11:43"
    ],
    [
        428,
        "dist-collection",
        "07/09/2024 12:11:43"
    ],
    [
        18,
        "dist-collection",
        "07/09/2024 12:11:43"
    ],
    [
        82,
        "hum-collection",
        "07/09/2024 12:11:43"
    ],
    [
        82,
        "hum-collection",
        "07/09/2024 12:11:43"
    ],
    [
        308,
        "luz-collection",
        "07/09/2024 12:11:43"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 12:11:43"
    ],
    [
        391,
        "co2-collection",
        "07/09/2024 12:11:44"
    ],
    [
        19,
        "dist-collection",
        "07/09/2024 12:11:44"
    ],
    [
        306,
        "luz-collection",
        "07/09/2024 12:11:44"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 12:11:44"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 18:31:43"
    ],
    [
        399,
        "co2-collection",
        "07/09/2024 18:31:44"
    ],
    [
        15,
        "dist-collection",
        "07/09/2024 18:31:44"
    ],
    [
        507,
        "luz-collection",
        "07/09/2024 18:31:44"
    ],
    [
        21.4,
        "temp-collection",
        "07/09/2024 18:31:44"
    ],
    [
        411,
        "co2-collection",
        "07/09/2024 18:31:51"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 18:31:51"
    ],
    [
        367,
        "luz-collection",
        "07/09/2024 18:31:51"
    ],
    [
        21.4,
        "temp-collection",
        "07/09/2024 18:31:51"
    ],
    [
        15,
        "dist-collection",
        "07/09/2024 18:31:52"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 18:31:57"
    ],
    [
        399,
        "co2-collection",
        "07/09/2024 18:31:58"
    ],
    [
        16,
        "dist-collection",
        "07/09/2024 18:31:58"
    ],
    [
        465,
        "luz-collection",
        "07/09/2024 18:31:58"
    ],
    [
        21.4,
        "temp-collection",
        "07/09/2024 18:31:58"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 18:32:04"
    ],
    [
        21.4,
        "temp-collection",
        "07/09/2024 18:32:04"
    ],
    [
        401,
        "co2-collection",
        "07/09/2024 18:32:05"
    ],
    [
        15,
        "dist-collection",
        "07/09/2024 18:32:05"
    ],
    [
        442,
        "luz-collection",
        "07/09/2024 18:32:05"
    ],
    [
        81,
        "hum-collection",
        "07/09/2024 18:32:11"
    ],
    [
        386,
        "luz-collection",
        "07/09/2024 18:32:11"
    ],
    [
        21.4,
        "temp-collection",
        "07/09/2024 18:32:11"
    ],
    [
        413,
        "co2-collection",
        "07/09/2024 18:32:12"
    ],
    [
        15,
        "dist-collection",
        "07/09/2024 18:32:12"
    ],
    [
        79,
        "hum-collection",
        "07/09/2024 18:41:33"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 18:41:33"
    ],
    [
        416,
        "co2-collection",
        "07/09/2024 18:41:34"
    ],
    [
        407,
        "co2-collection",
        "07/09/2024 18:41:34"
    ],
    [
        16,
        "dist-collection",
        "07/09/2024 18:41:34"
    ],
    [
        79,
        "hum-collection",
        "07/09/2024 18:41:34"
    ],
    [
        570,
        "luz-collection",
        "07/09/2024 18:41:34"
    ],
    [
        519,
        "luz-collection",
        "07/09/2024 18:41:34"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 18:41:34"
    ],
    [
        414,
        "co2-collection",
        "07/09/2024 18:41:35"
    ],
    [
        16,
        "dist-collection",
        "07/09/2024 18:41:35"
    ],
    [
        78,
        "hum-collection",
        "07/09/2024 18:41:35"
    ],
    [
        577,
        "luz-collection",
        "07/09/2024 18:41:35"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 18:41:35"
    ],
    [
        15,
        "dist-collection",
        "07/09/2024 18:41:36"
    ],
    [
        78,
        "hum-collection",
        "07/09/2024 18:41:36"
    ],
    [
        575,
        "luz-collection",
        "07/09/2024 18:41:36"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 18:41:36"
    ],
    [
        412,
        "co2-collection",
        "07/09/2024 18:41:37"
    ],
    [
        16,
        "dist-collection",
        "07/09/2024 18:41:37"
    ],
    [
        79,
        "hum-collection",
        "07/09/2024 18:41:37"
    ],
    [
        569,
        "luz-collection",
        "07/09/2024 18:41:37"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 18:41:37"
    ],
    [
        409,
        "co2-collection",
        "07/09/2024 18:41:38"
    ],
    [
        16,
        "dist-collection",
        "07/09/2024 18:41:38"
    ],
    [
        79,
        "hum-collection",
        "07/09/2024 18:41:38"
    ],
    [
        22.2,
        "temp-collection",
        "07/09/2024 18:41:38"
    ],
    [
        406,
        "co2-collection",
        "07/09/2024 18:41:39"
    ],
    [
        16,
        "dist-collection",
        "07/09/2024 18:41:39"
    ],
    [
        572,
        "luz-collection",
        "07/09/2024 18:41:39"
    ]
]

# URL de la API para grabar el dato
data_url = "https://vercel-bd.vercel.app/api/data/"

# ID de colección para temp-collection
id_coleccion_temp = 11

def formatear_fecha(fecha_str):
    """Convierte la fecha de formato DD/MM/AAAA HH:MM:SS a un timestamp en segundos."""
    fecha = datetime.strptime(fecha_str, "%d/%m/%Y %H:%M:%S")
    return int(fecha.timestamp())

def grabar_dato(dato):
    """Envía el dato a la API."""
    payload = {
        'sensorValue': dato[0],  # Valor del sensor
        'timestamp': formatear_fecha(dato[2]),  # Timestamp en segundos
        'coleccion': id_coleccion_temp  # ID de la colección temp-collection
    }

    # Envío del dato a la API
    response = requests.post(data_url, json=payload)

    if response.status_code == 201:  # Created
        print(f"Dato grabado exitosamente: {dato}")
    else:
        print(f"Error al grabar el dato: {response.text}")

# Recorrer el array de JSON
for dato in array_json:
    if dato[1] == "temp-collection":
        print(f"Procesando dato de temp-collection: {dato}")
        grabar_dato(dato)
