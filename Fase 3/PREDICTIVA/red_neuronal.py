import tensorflow as tf
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from datetime import datetime, timedelta
import os
import django
import pickle
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau
from tensorflow.keras.optimizers import Nadam
from tensorflow.keras.regularizers import l2

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "apidb.settings")
django.setup()

from app_api.models import Coleccion, Data

if not os.path.exists('modelos'):
    os.makedirs('modelos')

def crear_secuencias(X, y, longitud_secuencia):
    X_seq, y_seq = [], []
    for i in range(len(X) - longitud_secuencia):
        X_seq.append(X[i:(i + longitud_secuencia)])
        y_seq.append(y[i + longitud_secuencia])
    return np.array(X_seq), np.array(y_seq)

def crear_modelo(coleccion_buscada):
    array_datos_co2 = Data.objects.filter(coleccion=coleccion_buscada).order_by('timestamp')
    array_tiempos = [temp.timestamp for temp in array_datos_co2]
    array_valores = [temp.sensorValue for temp in array_datos_co2]

    # Convertir timestamps a características más útiles
    fechas = [datetime.fromtimestamp(ts) for ts in array_tiempos]
    entrada_tiempo = np.array([(d.hour * 3600 + d.minute * 60 + d.second) / 86400 for d in fechas]).reshape(-1, 1)
    entrada_dia_semana = np.array([d.weekday() for d in fechas]).reshape(-1, 1)
    entrada_dia_anio = np.array([d.timetuple().tm_yday for d in fechas]).reshape(-1, 1)

    salida_valor = np.array(array_valores, dtype=float).reshape(-1, 1)

    # Normalización
    scaler_tiempo = MinMaxScaler()
    scaler_dia_semana = MinMaxScaler()
    scaler_dia_anio = MinMaxScaler()
    scaler_valores = MinMaxScaler()

    entrada_tiempo = scaler_tiempo.fit_transform(entrada_tiempo)
    entrada_dia_semana = scaler_dia_semana.fit_transform(entrada_dia_semana)
    entrada_dia_anio = scaler_dia_anio.fit_transform(entrada_dia_anio)
    salida_valor = scaler_valores.fit_transform(salida_valor)

    # Combinar características
    X = np.hstack((entrada_tiempo, entrada_dia_semana, entrada_dia_anio))
    y = salida_valor

    # Crear secuencias
    longitud_secuencia = 24  # Ajusta según la naturaleza de tus datos
    X_seq, y_seq = crear_secuencias(X, y, longitud_secuencia)

    # División de datos
    X_train, X_test, y_train, y_test = train_test_split(X_seq, y_seq, test_size=0.2, random_state=42)

    # Modelo
    modelo = tf.keras.Sequential([
        tf.keras.layers.LSTM(128, return_sequences=True, input_shape=(longitud_secuencia, 3)),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.LSTM(64, return_sequences=False),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(32, activation='relu', kernel_regularizer=l2(0.01)),
        tf.keras.layers.Dense(1)
    ])

    # Optimizador Nadam
    optimizer = Nadam(learning_rate=0.001)
    modelo.compile(optimizer=optimizer, loss='mse', metrics=['mae'])

    early_stopping = EarlyStopping(monitor='val_loss', patience=50, restore_best_weights=True)
    reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.2, patience=20, min_lr=1e-6)

    print(f"Comenzando entrenamiento para {coleccion_buscada.nombre}...")
    history = modelo.fit(
        X_train, y_train, 
        epochs=500,
        batch_size=32,
        validation_data=(X_test, y_test),
        callbacks=[early_stopping, reduce_lr],
        verbose=1
    )
    print(f"Finalizó entrenamiento para {coleccion_buscada.nombre}...")

    modelo.save(f'modelos/modelo_{coleccion_buscada.nombre}.keras')
    
    # Guardar escaladores
    with open(f'modelos/scaler_tiempo_{coleccion_buscada.nombre}.pkl', 'wb') as f:
        pickle.dump(scaler_tiempo, f)
    with open(f'modelos/scaler_dia_semana_{coleccion_buscada.nombre}.pkl', 'wb') as f:
        pickle.dump(scaler_dia_semana, f)
    with open(f'modelos/scaler_dia_anio_{coleccion_buscada.nombre}.pkl', 'wb') as f:
        pickle.dump(scaler_dia_anio, f)
    with open(f'modelos/scaler_valores_{coleccion_buscada.nombre}.pkl', 'wb') as f:
        pickle.dump(scaler_valores, f)
    
    print(f"Modelo y escaladores guardados para {coleccion_buscada.nombre}")

    # Evaluación del modelo
    test_loss, test_mae = modelo.evaluate(X_test, y_test, verbose=0)
    print(f"Test MAE: {test_mae}")

    return history, longitud_secuencia

def probar_modelo(coleccion_buscada, fecha_prediccion):
    # Carga el modelo entrenado y los escaladores
    modelo_cargado = tf.keras.models.load_model(f'modelos/modelo_{coleccion_buscada.nombre}.keras')
    
    with open(f'modelos/scaler_tiempo_{coleccion_buscada.nombre}.pkl', 'rb') as f:
        scaler_tiempo = pickle.load(f)
    with open(f'modelos/scaler_dia_semana_{coleccion_buscada.nombre}.pkl', 'rb') as f:
        scaler_dia_semana = pickle.load(f)
    with open(f'modelos/scaler_dia_anio_{coleccion_buscada.nombre}.pkl', 'rb') as f:
        scaler_dia_anio = pickle.load(f)
    with open(f'modelos/scaler_valores_{coleccion_buscada.nombre}.pkl', 'rb') as f:
        scaler_valores = pickle.load(f)
    
    # Preprocesa la fecha de predicción
    fecha_dt = datetime.fromtimestamp(fecha_prediccion)
    tiempo_del_dia = (fecha_dt.hour * 3600 + fecha_dt.minute * 60 + fecha_dt.second) / 86400
    dia_semana = fecha_dt.weekday()
    dia_anio = fecha_dt.timetuple().tm_yday

    # Normaliza las características
    tiempo_normalizado = scaler_tiempo.transform([[tiempo_del_dia]])
    dia_semana_normalizado = scaler_dia_semana.transform([[dia_semana]])
    dia_anio_normalizado = scaler_dia_anio.transform([[dia_anio]])

    # Combina las características
    X_pred = np.hstack((tiempo_normalizado, dia_semana_normalizado, dia_anio_normalizado))

    # Obtén los datos históricos para formar la secuencia
    datos_historicos = Data.objects.filter(coleccion=coleccion_buscada, timestamp__lt=fecha_prediccion).order_by('-timestamp')[:24]
    
    if len(datos_historicos) < 24:
        return "No hay suficientes datos históricos para hacer una predicción precisa."

    X_hist = []
    for dato in reversed(datos_historicos):
        fecha_hist = datetime.fromtimestamp(dato.timestamp)
        tiempo_hist = (fecha_hist.hour * 3600 + fecha_hist.minute * 60 + fecha_hist.second) / 86400
        dia_semana_hist = fecha_hist.weekday()
        dia_anio_hist = fecha_hist.timetuple().tm_yday
        
        tiempo_norm = scaler_tiempo.transform([[tiempo_hist]])
        dia_semana_norm = scaler_dia_semana.transform([[dia_semana_hist]])
        dia_anio_norm = scaler_dia_anio.transform([[dia_anio_hist]])
        
        X_hist.append(np.hstack((tiempo_norm, dia_semana_norm, dia_anio_norm)).flatten())

    X_hist = np.array(X_hist)
    X_pred = np.vstack((X_hist, X_pred.flatten())).reshape(1, 25, 3)

    # Realiza la predicción
    resultado = modelo_cargado.predict(X_pred)
    
    # Desnormaliza el resultado
    resultado_original = scaler_valores.inverse_transform(resultado)
    
    return float(resultado_original[0][0])



def probar_modelo(coleccion_buscada, fecha_prediccion):
    # Carga el modelo entrenado y los escaladores
    modelo_cargado = tf.keras.models.load_model(f'modelos/modelo_{coleccion_buscada.nombre}.keras')
    
    with open(f'modelos/scaler_tiempo_{coleccion_buscada.nombre}.pkl', 'rb') as f:
        scaler_tiempo = pickle.load(f)
    with open(f'modelos/scaler_dia_semana_{coleccion_buscada.nombre}.pkl', 'rb') as f:
        scaler_dia_semana = pickle.load(f)
    with open(f'modelos/scaler_dia_anio_{coleccion_buscada.nombre}.pkl', 'rb') as f:
        scaler_dia_anio = pickle.load(f)
    with open(f'modelos/scaler_valores_{coleccion_buscada.nombre}.pkl', 'rb') as f:
        scaler_valores = pickle.load(f)
    
    # Preprocesa la fecha de predicción
    fecha_dt = datetime.fromtimestamp(int(fecha_prediccion))
    tiempo_del_dia = (fecha_dt.hour * 3600 + fecha_dt.minute * 60 + fecha_dt.second) / 86400
    dia_semana = fecha_dt.weekday()
    dia_anio = fecha_dt.timetuple().tm_yday

    # Normaliza las características
    tiempo_normalizado = scaler_tiempo.transform([[tiempo_del_dia]])
    dia_semana_normalizado = scaler_dia_semana.transform([[dia_semana]])
    dia_anio_normalizado = scaler_dia_anio.transform([[dia_anio]])

    # Combina las características
    X_pred = np.hstack((tiempo_normalizado, dia_semana_normalizado, dia_anio_normalizado))

    # Obtén los datos históricos para formar la secuencia
    datos_historicos = Data.objects.filter(coleccion=coleccion_buscada, timestamp__lt=fecha_prediccion).order_by('-timestamp')[:23]
    
    if len(datos_historicos) < 23:
        return "No hay suficientes datos históricos para hacer una predicción precisa."

    X_hist = []
    for dato in reversed(datos_historicos):
        fecha_hist = datetime.fromtimestamp(dato.timestamp)
        tiempo_hist = (fecha_hist.hour * 3600 + fecha_hist.minute * 60 + fecha_hist.second) / 86400
        dia_semana_hist = fecha_hist.weekday()
        dia_anio_hist = fecha_hist.timetuple().tm_yday
        
        tiempo_norm = scaler_tiempo.transform([[tiempo_hist]])
        dia_semana_norm = scaler_dia_semana.transform([[dia_semana_hist]])
        dia_anio_norm = scaler_dia_anio.transform([[dia_anio_hist]])
        
        X_hist.append(np.hstack((tiempo_norm, dia_semana_norm, dia_anio_norm)).flatten())

    X_hist = np.array(X_hist)
    X_pred = np.vstack((X_hist, X_pred.flatten())).reshape(1, 24, 3)

    # Realiza la predicción
    resultado = modelo_cargado.predict(X_pred)
    
    # Desnormaliza el resultado
    resultado_original = scaler_valores.inverse_transform(resultado)
    
    return float(resultado_original[0][0])


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



'''
if __name__ == '__main__':
    colecciones = [Coleccion.objects.get(id=i) for i in range(10, 12)]
    for coleccion in colecciones:
        history, _ = crear_modelo(coleccion)
        
        # Visualización del entrenamiento (opcional, requiere matplotlib)
        import matplotlib.pyplot as plt
        plt.figure(figsize=(12, 6))
        plt.plot(history.history['loss'], label='Training Loss')
        plt.plot(history.history['val_loss'], label='Validation Loss')
        plt.title(f'Training and Validation Loss for {coleccion.nombre}')
        plt.xlabel('Epoch')
        plt.ylabel('Loss')
        plt.legend()
        plt.savefig(f'modelos/training_history_{coleccion.nombre}.png')
        plt.close()
'''