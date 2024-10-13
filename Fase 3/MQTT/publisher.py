import paho.mqtt.client as mqtt
import time
import random
import json

class Publisher:
    def __init__(self):
        # Configuración del cliente MQTT
        self.broker = 'broker.emqx.io'
        self.puerto = 1883
        self.topico = 'arqui2_2s2024/topico_sensores'
        self.cliente = mqtt.Client()
        self.cliente.connect(self.broker, self.puerto, 60)
        # Mantener la conexión en segundo plano
        self.cliente.loop_start()

    def publicar(self, tem, hum, dist, luz, aire):
        data = {
            "temperatura" : tem,
            "humedad" : hum,
            "distancia" : dist,
            "luz" : luz,
            "aire" : aire,
        }
        self.cliente.publish(self.topico, json.dumps(data))
    
    def desconectar(self):
        # Finalizar la conexión
        self.cliente.loop_stop()
        self.cliente.disconnect()


pub = Publisher()

try:
    while True:
        # Publicar un mensaje cada 3 segundos
        random_number1 = random.randint(1, 100)
        random_number2 = random.randint(1, 10)
        random_number3 = random.randint(1, 1000)
        random_number4 = random.randint(1, 500)
        random_number5 = random.randint(1, 300)
        pub.publicar(random_number1, random_number2, random_number3, random_number4, random_number5)
        time.sleep(3)
except KeyboardInterrupt:
    print("Interrumpido por el usuario")

pub.desconectar()

