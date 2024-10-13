import paho.mqtt.client as mqtt

# Configuración del cliente MQTT
broker = 'broker.emqx.io'
port = 1883
topic = 'arqui2_2s2024/topico_prueba'

def on_connect(client, userdata, flags, rc):
    print(f'Conectado con el código {rc}')
    client.subscribe(topic)

def on_message(client, userdata, msg):
    print(f'Mensaje recibido: {msg.payload.decode()}')

# Crear el cliente MQTT
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, port, 60)
client.loop_forever()
