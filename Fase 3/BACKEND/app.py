# importa la base de datos
from controlador_db import BaseData

# importa el controlador de predicciones
from predictor import Predictor

# Librerias de Flask
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Controlador de base de datos
base = BaseData()

@app.route("/consulta_general")
def general():
    base._abrir_json()
    #base.ordenar_por_fecha()
    #data = base.diccionario #Comentar para pruebas
    
    data = base.consulta_general() 
    return data

@app.route("/consulta_prediccion/<timestamp>")
def predecir(timestamp):
    nuevo = Predictor()
    data = nuevo.ObtenerPredicciones(timestamp)
    return data

if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)