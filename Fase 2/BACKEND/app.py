# importa la base de datos
from controlador_db import BaseData

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
    base.ordenar_por_fecha()
    data = base.diccionario #Comentar para pruebas
    #data = base.consulta_general() 
    return data

if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)