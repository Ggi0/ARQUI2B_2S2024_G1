# importa la base de datos
from controlador_db import BaseData

# Librerias de Flask
from flask import Flask
app = Flask(__name__)

@app.route("/consulta_general")
def hello_world():
    base = BaseData()
    data = base.consulta_general()
    return data

if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)