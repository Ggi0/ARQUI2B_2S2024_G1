import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import firestore
from datetime import datetime

class BaseData:
    def __init__(self):
        # Toma los datos generales
        self.credenciales = credentials.Certificate("C:\\Users\\Marcos Josué Cruz\\Documents\\ARQUI2\\ARQUI2B_2S2024_G1\\Fase 2\\BACKEND\\arqui2-db-firebase-adminsdk-137on-dbfa694095.json")
        # inicializa la base de datos
        firebase_admin.initialize_app(self.credenciales)
        # Obtén una referencia a la base de datos
        self.db = firestore.client()
        # Diccionario que va a funcionar como base de datos
        self.diccionario = []
    
    # Formateo de fechas
    def formateo_fechas(self, timestamp):
        # Convertir el timestamp de milisegundos a segundos y luego a datetime
        data_stamp = datetime.fromtimestamp(timestamp / 1000)
        # Formatear el datetime al formato DD/MM/AAAA HH:MM:SS
        fecha_formateada = data_stamp.strftime("%d/%m/%Y %H:%M:%S")
        return fecha_formateada
    
    # Consulta general de datos
    def consulta_general(self):
        # Obtiene de la base de datos el conjunto de colecciones 
        colecciones = self.db.collections()
        # Itera las colecciones para agregar 
        for coleccion in colecciones:
            '''
            colecciones:
                * co2-collection
                * dist-collection
                * hum-collection
                * luz-collection
                * temp-collection
            '''
            # valida que no sea el de arduino, brincando a la siguiente iteracion
            if coleccion.id == "arduino-collection":
                continue
            # Obtiene la tabla de cada una de las colecciones
            data_coleccion = self.db.collection(coleccion.id).get()
            self.diccionario += [
                [ temp.to_dict()["sensorValue"], coleccion.id , self.temp.to_dict()["timestamp"] ]
                for temp in data_coleccion
            ]
        # Guarda el encabezado
        encabezado = [ "sensor", "coleccion", "timestamp" ]
        self.diccionario.insert(0, encabezado)
        return(self.diccionario)

