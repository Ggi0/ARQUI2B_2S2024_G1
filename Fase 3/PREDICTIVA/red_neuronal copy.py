# Cosas de redes neuronales
import tensorflow as tf
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
# Validaciones de tiempo
from datetime import datetime, timedelta

# Cosas de django
import os
import django
import pickle

# Configura el entorno de Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "apidb.settings")
django.setup()

# Cambia la importación relativa a una absoluta
from app_api.models import Coleccion, Data

# Asegúrate de que existe la carpeta 'modelos'
if not os.path.exists('modelos'):
    os.makedirs('modelos')

def crear_modelo(coleccion_buscada):
    # Obtiene los valores de los datos y sensores
    array_datos_co2 = Data.objects.filter(coleccion=coleccion_buscada)
    array_tiempos = [temp.timestamp for temp in array_datos_co2]
    array_valores = [temp.sensorValue for temp in array_datos_co2]

    # Convierte a array de numpy
    entrada_tiempo = np.array(array_tiempos).reshape(-1, 1)
    salida_valor = np.array(array_valores, dtype=float).reshape(-1, 1)

    # Normalización de los tiempos y valores de los sensores
    scaler_tiempos = StandardScaler()
    scaler_valores = StandardScaler()

    entrada_tiempo = scaler_tiempos.fit_transform(entrada_tiempo)
    salida_valor = scaler_valores.fit_transform(salida_valor)

    # Divide los datos en conjuntos de entrenamiento y prueba
    entrada_tiempo_train, entrada_tiempo_test, salida_valor_train, salida_valor_test = train_test_split(
        entrada_tiempo, salida_valor, test_size=0.2, random_state=42
    )

    # Crea las capas de la red neuronal
    modelo = tf.keras.Sequential([
        tf.keras.layers.Dense(128, activation='relu', input_shape=[1]),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(32, activation='relu'),
        tf.keras.layers.Dense(1)
    ])

    # Configura el modelo
    modelo.compile(optimizer='adam', loss='mse')

    # Inicia el entrenamiento
    print(f"Comenzando entrenamiento para {coleccion_buscada.nombre}...")
    modelo.fit(entrada_tiempo_train, salida_valor_train, 
               epochs=500, batch_size=32, 
               validation_data=(entrada_tiempo_test, salida_valor_test),
               verbose=1)
    print(f"Finalizó entrenamiento para {coleccion_buscada.nombre}...")

    # Guarda el modelo entrenado
    modelo.save(f'modelos/modelo_{coleccion_buscada.nombre}.keras')
    
    # Guarda los escaladores
    with open(f'modelos/scaler_tiempos_{coleccion_buscada.nombre}.pkl', 'wb') as f:
        pickle.dump(scaler_tiempos, f)
    with open(f'modelos/scaler_valores_{coleccion_buscada.nombre}.pkl', 'wb') as f:
        pickle.dump(scaler_valores, f)
    
    print(f"Modelo y escaladores guardados para {coleccion_buscada.nombre}")

def probar_modelo(coleccion_buscada, fecha_prediccion):
    # Carga el modelo entrenado
    modelo_cargado = tf.keras.models.load_model(f'modelos/modelo_{coleccion_buscada.nombre}.keras')
    
    # Carga los escaladores
    with open(f'modelos/scaler_tiempos_{coleccion_buscada.nombre}.pkl', 'rb') as f:
        scaler_tiempos = pickle.load(f)
    with open(f'modelos/scaler_valores_{coleccion_buscada.nombre}.pkl', 'rb') as f:
        scaler_valores = pickle.load(f)
    
    # Normaliza el dato de entrada para la predicción 
    timestamp_test = np.array([fecha_prediccion]).reshape(-1, 1)
    timestamp_test_normalizado = scaler_tiempos.transform(timestamp_test)
    
    # Realiza la predicción
    resultado = modelo_cargado.predict(timestamp_test_normalizado)
    
    # Desnormaliza el resultado de la predicción para interpretarlo correctamente
    resultado_original = scaler_valores.inverse_transform(resultado)
    
    return(float(resultado_original[0][0]))


def solicitar_prediccion(id_coleccion, fecha_prediccion):
    # Valida que la colección sea existente
    if not Coleccion.objects.filter(id=id_coleccion).exists():
        return ("La coleecion buscada no existe", 0)
    # Valida la pureza de los datos
    if not str(fecha_prediccion).isdigit():
        return ("La fecha no es numerica", 0)
    # Valida que la fecha sea un timestamp valido
    fecha_a_validar = datetime.fromtimestamp(int(fecha_prediccion))
    fecha_actual = datetime.now()
    fecha_limite = fecha_actual + timedelta(days=10)
    if not (fecha_actual <= fecha_a_validar <= fecha_limite):
        pass
        #return ("La fecha no esta en el rango de los proximos 10 dias", 0)

    # Si todo sale bien, busca la coleccion y la fecha
    coleccion_buscada = Coleccion.objects.get(id=id_coleccion)
    return ("Solicitud Exitosa", probar_modelo(coleccion_buscada, fecha_prediccion))




if __name__ == '__main__':
    # Obtiene las colecciones
    colecciones = [Coleccion.objects.get(id=i) for i in range(7, 12)]

    # Crea el modelo para cada una de las colecciones
    for coleccion in colecciones:
        crear_modelo(coleccion)
