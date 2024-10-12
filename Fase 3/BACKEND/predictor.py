import requests

class Predictor:
    def __init__(self):
        self.ruta_api = "http://34.29.61.196:8000/api/"

    def ObtenerPredicciones(self, fecha_timestamp):
        # Obtinene la respuesta para cada una de las colecciones
        array_respuestas = []
        array_colecciones = requests.get(self.ruta_api + "colecciones").json()
        # Itera sobre todas las colecciones
        for temp in array_colecciones:
            ruta = self.ruta_api + f"Prediccion?fecha_timestamp={fecha_timestamp}&id_coleccion={temp["id"]}"
            respuesta = requests.get(ruta).json()
            temp_data = {
                "sensor": temp["nombre"],
                "valor": respuesta["resultado"],
                "mensaje": respuesta["mensaje"]
            }
            array_respuestas.append(temp_data)
        return(array_respuestas)

if __name__ == '__main__':
    nuevo = Predictor()
    nuevo.ObtenerPredicciones(1728693536)