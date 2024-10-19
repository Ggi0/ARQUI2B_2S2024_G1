import serial
import time
import paho.mqtt.client as mqtt
import json
# Escrituras a BD
import requests
import calendar

import smbus

# DATOS RECIBIDOS DE ARDUINO
# Sensores
temperatura = 0
humedad = 0
luminosidad = 0
aire = 0
ultrasonico = 0
dist_estacionar = 0
entrada_dist = 0

# Uso de la Talanquera
talanquera_uso = "0"

# DATOS ENVIADOS A ARDUINO
# Usuario Correcto
abrir_talanquera = "cerrar_t"

# Prender Luces
prender_luces = "apagar_luces"

# Inicializa el bus I2C
bus = smbus.SMBus(1)
arduino_address = 0x08  # Direcci�n I2C del Arduino



# Distribucion de colecciones
colecciones = {
    'co2': 7,
    'dist': 8,
    'hum': 9,
    'luz': 10, 
    'temp': 11
}

# URL BD
URL_BD = 'http://34.29.61.196:8000/api/data/'

def escribir_a_BD(coleccion, valor):
    time_tuple = time.gmtime()
    timestamp = calendar.timegm(time_tuple)
    new_bd_entry = {
        'coleccion': coleccion,
        'sensorValue': valor,
        'timestamp': timestamp
    }

    post_response = requests.post(URL_BD, json=new_bd_entry)
    if post_response.status_code == 201:
        print(f'Escritura a BD exitosa. Response: {post_response.json()}')
    else:
        print(f'Escritura a BD fallida. Code: {post_response.status_code}, Response: {post_response.json()}')


# MQTT Publisher para enviar los datos de los sensores al broker
def enviar_datos_mqtt(client):
    datos = {
        'temperatura': temperatura,
        'humedad': humedad,
        'luminosidad': luminosidad,
        'aire': aire,
        'ultrasonico': ultrasonico
    }
    
    # Convertir el diccionario a una cadena JSON
    datos_json = json.dumps(datos)
    
    # Publicar el JSON en el topico de MQTT
    client.publish('arqui2_2s2024/topico_sensores', payload=datos_json, qos=0, retain=False)

def aviso_carro(client):
    client.publish('arqui2_2s2024/topico_aviso_carro', payload=talanquera_uso, qos=0, retain=False)

def desbloqueo(client):
    client.subscribe("arqui2_2s2024/desbloqueo_usuario")

def luces(client):
    client.subscribe("arqui2_2s2024/prender_luces")


# Clasificacion de datos recibidos por Arduino
def clasificacion(inicial, valor):
    global temperatura, humedad, luminosidad, aire, ultrasonico, dist_estacionar, entrada_dist, talanquera_uso, abrir_talanquera, prender_luces

    if inicial == 'T':
        temperatura = float(valor)
        print(f"Temperatura: {temperatura} C")
        escribir_a_BD(colecciones.get('temp'), temperatura)

    elif inicial == 'H':
        humedad = float(valor)
        print(f"Humedad: {humedad}%")
        escribir_a_BD(colecciones.get('hum'), humedad)

    elif inicial == 'L':
        luminosidad = float(valor)
        print(f"Luminosidad: {luminosidad}")
        escribir_a_BD(colecciones.get('luz'), luminosidad)

    elif inicial == 'A':
        aire = float(valor)
        print(f"Calidad del aire: {aire}")
        escribir_a_BD(colecciones.get('co2'), aire)

    elif inicial == 'U':
        ultrasonico = float(valor)
        print(f"Distancia ultrasonico: {ultrasonico} cm")
        escribir_a_BD(colecciones.get('dist'), ultrasonico)

    elif inicial == 'D':
        if entrada_dist == 1:
            dist_estacionar = float(valor)
            print(f"Distancia para estacionar: {dist_estacionar} cm")
        else:
            entrada_dist = 1

    elif inicial == 'E':
        talanquera_uso = valor
        print(f"Uso de la talanquera: {talanquera_uso}")

    #elif inicial == 'x':
        #abrir_talanquera = '0'
    
    elif inicial == 'n':
        abrir_talanquera = '0'

    elif inicial == 'm':
        prender_luces = '0'

def send_two_numbers(command, high_number, low_number):
    global arduino_address
    # Asegurarse de que los n�meros estan dentro del rango de un byte (0-255)
    
    comandos_luces = {
    "prender_luces": bytes([]),
    "apagar_luces": bytes([0]),
    "luces_automaticas": bytes([2])
    }

    comandos_talanquera = {
    "cerrar_t": bytes([0]),
    "abrir_t": bytes([1])
    }

    #comando = prender_luces
    #luz_byte = comandos_luces.get(comando)
    #print (luz_byte)

    ##comando = abrir_talanquera
    #t_byte = comandos_talanquera.get(comando)
    #print(t_byte)
   
    #luz_byte = bytes([100])
    #luz_byte = luz_byte & 0xFF
    #t_byte = t_byte & 0xFF
    
    if prender_luces == "prender_luces":
            bus.write_i2c_block_data(arduino_address, 0, [1, 0])
    if prender_luces == "apagar_luces":
            bus.write_i2c_block_data(arduino_address, 0, [0, 0])

    # Enviar los dos bytes (uno para el high byte y otro para el low byte) con un comando
    bus.write_i2c_block_data(arduino_address, 0, [0, 0])



# Conexion al broker MQTT
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    # Suscripcion
    client.subscribe("pruebaJemima/")
    # Publicacion inicial de estado
    client.publish('raspberryJemima/status', payload="Conectado", qos=0, retain=False)

def on_message(client, userdata, msg):
    global abrir_talanquera 
    global prender_luces 
    if msg.topic == "arqui2_2s2024/desbloqueo_usuario":
        abrir_talanquera = msg.payload.decode('utf-8') 
        if abrir_talanquera == "1":
            abrir_talanquera = "abrir_t"
        elif abrir_talanquera == "0":
            abrir_talanquera == "cerrar_t"

        print(f"Mensaje recibido talanquera: {abrir_talanquera}")


    elif msg.topic == "arqui2_2s2024/prender_luces":
        prender_luces = msg.payload.decode('utf-8') 
        if prender_luces == "1":
            prender_luces = "prender_luces"
        elif prender_luces == "0":
            prender_luces = "apagar_luces"
        elif prender_luces == "2":
            prender_luces = "luces_automaticas"
        print(f"Mensaje recibido luces: {prender_luces}")
    else:
        print(f"{msg.topic} {msg.payload}")

# Configuracion del cliente MQTT
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.will_set('raspberry/status', b'{"status": "Off"}')
client.connect("broker.emqx.io", 1883, 60)

# Iniciar el bucle de procesamiento de mensajes MQTT
client.loop_start()  # Usamos loop_start() para no bloquear el codigo mientras enviamos y recibimos mensajes MQTT

# Comunicacion con Arduino
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
time.sleep(2)

# Bucle principal para leer datos del puerto serial y enviarlos por MQTT
try:
    while True:
        
        if ser.in_waiting > 0:
            
            line = ser.readline().decode('utf-8').rstrip()
            print(f"Respuesta de Arduino: {line}")
            if len(line) > 1:  # Comprobamos que la linea no esta vacia
                inicial = line[0]
                valor = line[1:]
                if inicial == "z":
                    print(valor)
                else:
                    try:
                        clasificacion(inicial, valor)
                    except ValueError as err:
                        print(err)
                
                
                
                
                # Despues de clasificar y actualizar las variables de los sensores, enviamos los datos por MQTT
                enviar_datos_mqtt(client)
                aviso_carro(client)
                desbloqueo(client)
                luces(client)

                send_two_numbers(prender_luces,0,0)
                print(prender_luces)
                time.sleep(1)

            else:
                print("Linea vacia o invalida recibida.")
except KeyboardInterrupt:
    print("Interrupcion manual por el usuario")

ser.close()
client.loop_stop()  # Detenemos el loop de MQTT al finalizar


