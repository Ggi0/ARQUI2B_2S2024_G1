import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import firestore
from google.cloud.firestore_v1 import aggregation
from google.cloud.firestore_v1.base_query import FieldFilter
from datetime import datetime
import json


class BaseData:
    def __init__(self):
        # Toma los datos generales
        self.credenciales = credentials.Certificate("clave.json")
        # inicializa la base de datos
        firebase_admin.initialize_app(self.credenciales)
        # Obtén una referencia a la base de datos
        self.db = firestore.client()
        # Diccionario que va a funcionar como base de datos
        self.diccionario = []
    
    def _abrir_json(self):
        try:
            with open("database.json", "r") as archivo:
                self.diccionario = json.load(archivo)
        except:
            print ("El archivo no se pudo abrir")

    def _escribir_json(self):
        # Escribir el diccionario en un archivo JSON
        with open("database.json", "w") as archivo:
            json.dump(self.diccionario, archivo, indent=4)  # indent es opcional, solo es para hacerlo más legible

    # Formateo de fechas
    def formateo_fechas(self, timestamp):
        # Convertir el timestamp de milisegundos a segundos y luego a datetime
        data_stamp = datetime.fromtimestamp(timestamp / 1000)
        # Formatear el datetime al formato DD/MM/AAAA HH:MM:SS
        fecha_formateada = data_stamp.strftime("%d/%m/%Y %H:%M:%S")
        return fecha_formateada
    
    def obtener_longitud_db(self):
        # Manejador de las colecciones
        longitud_colecciones = 0
        # Obtiene de la base de datos el conjunto de colecciones 
        colecciones = self.db.collections()
        # Itera las colecciones para agregar 
        for coleccion in colecciones:
            # Colecciones no contables
            if coleccion.id == "arduino-collection" or coleccion.id == "counter-collection":
                continue
            # Obtiene la tabla de cada una de las colecciones haciendo un query dummy
            consulta = self.db.collection(coleccion.id).where(filter=FieldFilter("timestamp", ">", 0))
            agregacion = aggregation.AggregationQuery(consulta)
            # `alias` to provides a key for accessing the aggregate query results
            longitud = agregacion.count(alias="all").get()[0][0].value
            print(f"longitud de la colección {coleccion.id}...: {longitud}")
            longitud_colecciones += longitud

        return(longitud_colecciones)
    
    # Seccion para cambio rapido, barre todo en caso tenga timestamp en lugar de fecha y hora
    def _formateo_fecha_general(self):
        self._abrir_json()
        for dict_i in self.diccionario[1:]:
            dict_i[2] = self.formateo_fechas(dict_i[2])
        self._escribir_json()

    def ordenar_por_fecha(self):
        # Extraer el encabezado
        header = self.diccionario[0]
        # Ordenar el resto de los datos por la columna de fechas
        sorted_data = sorted(self.diccionario[1:], key=lambda x: datetime.strptime(x[2], "%d/%m/%Y %H:%M:%S"))
        # Volver a agregar el encabezado
        sorted_data.insert(0, header)
        self.diccionario = sorted_data
        self._escribir_json()

    # Consulta general de datos
    def consulta_general(self):
        # Abre el json de base de datos y valida si es local
        self._abrir_json()
        # Valida la longitud obtenida de la bases
        longitud_bd = self.obtener_longitud_db()
        # Si las longitudes son iguales, no hubieron cambios
        if longitud_bd == (len(self.diccionario) - 1): # Sin encabezado
            print("============ No han ocurrido cambios ==============")
            self.ordenar_por_fecha()
            return self.diccionario

        print("============ Han ocurrido Cambios ==============")
        print(longitud_bd , (len(self.diccionario) - 1))
        # Si hay cambios, hace la consulta general y limpia el diccionario
        self.diccionario = []
        # Obtiene de la base de datos el conjunto de colecciones 
        colecciones = self.db.collections()
        # Itera las colecciones para agregar 
        for coleccion in colecciones:
            '''
            colecciones válidas:
                * co2-collection
                * dist-collection
                * hum-collection
                * luz-collection
                * temp-collection
            '''
            # valida que no sea el de arduino, brincando a la siguiente iteracion
            if coleccion.id == "arduino-collection" or coleccion.id == "counter-collection":
                continue
            # Obtiene la tabla de cada una de las colecciones
            data_coleccion = self.db.collection(coleccion.id).get()
            self.diccionario += [
                [ temp.to_dict()["sensorValue"], coleccion.id , self.formateo_fechas(temp.to_dict()["timestamp"]) ]
                for temp in data_coleccion
            ]

        # Guarda el encabezado
        encabezado = [ "sensor", "coleccion", "timestamp" ]
        # Valida que ya posea encabezado
        if self.diccionario[0] != encabezado:
            self.diccionario.insert(0, encabezado)
        # Reordena el diccionario y lo escribe
        self.ordenar_por_fecha()
        # Escribe el json
        self._escribir_json()
        return(self.diccionario)
