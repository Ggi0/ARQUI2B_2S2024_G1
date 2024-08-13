#include <EEPROM.h>
#include "DHT.h"

#define DHTPIN 4       // Pin al que está conectado el pin de datos del DHT11
#define DHTTYPE DHT11  // DHT 11
#define LED_PIN 13     // Pin al que está conectado el LED

int ldrPin = A0;       // Pin analógico donde está conectado el LDR
int mq135Pin = A1;     // Pin analógico al que está conectado la salida del MQ-135

int ldrValue = 0;      // Variable para almacenar el valor del LDR
int mq135Value = 0;    // Variable para almacenar el valor del MQ-135
float humedad = 0;     // Variable para almacenar el valor de la humedad
float temperatura = 0; // Variable para almacenar el valor de la temperatura
int distanceCm = 0;    // Variable para almacenar la distancia en Cm

DHT dht(DHTPIN, DHTTYPE);

// Definimos los pines del teclado
const int buttonPins[4] = {18, 19, 21, 20};

// Dirección de memoria EEPROM para almacenar los datos
int eepromAddress = 0;

// Variables para los pines trigPin y echoPin,
// así como para almacenar la duración y la distancia calculada.
const int trigPin = 9;
const int echoPin = 10;
long duration;

// Funciones de interrupción para cada botón
void button1ISR() { 
  showSensorReadings();
}

void button2ISR() { 
  // Guardar los datos en la EEPROM
  saveDataToEEPROM(); 
}

void button3ISR() { 
  // Mostrar la última información guardada
  readLastDataFromEEPROM(); 
}

void button4ISR() { 
  // Mostrar todos los datos almacenados en la EEPROM
  readAllDataFromEEPROM(); 
}

void setup() {
  // Inicia la comunicación serie a 9600 baudios
  Serial.begin(9600);
  Serial.println("Iniciando sensores...");

  // Inicia el sensor DHT
  dht.begin();

  // Configura el pin LED como salida
  pinMode(LED_PIN, OUTPUT);

  // Configura los pines del teclado como entradas con resistencia pull-up interna
  for (int i = 0; i < 4; i++) {
    pinMode(buttonPins[i], INPUT_PULLUP);
  }

  // Asocia las interrupciones a los botones
  attachInterrupt(digitalPinToInterrupt(buttonPins[0]), button1ISR, FALLING);
  attachInterrupt(digitalPinToInterrupt(buttonPins[1]), button2ISR, FALLING);
  attachInterrupt(digitalPinToInterrupt(buttonPins[2]), button3ISR, FALLING);
  attachInterrupt(digitalPinToInterrupt(buttonPins[3]), button4ISR, FALLING);

  // Configuración del sensor ultrasónico
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  Serial.println("DHT11, LDR, MQ-135, y teclado de membrana 1x4 con EEPROM");
}

void loop() {
  // Enviando los valores de los sensores a Processing
  sendSensorReadingsToProcessing();
  // Caracter "trigger" que arranca serialEvent() de Processing
  Serial.print("$");

  // Caracter para que Processing ignore cualquier Serial.print
  Serial.println("#");

  // Alterna el estado del LED
  digitalWrite(LED_PIN, HIGH);
  delay(1000); // Enciende el LED por 1 segundo
  digitalWrite(LED_PIN, LOW);
  delay(1000); // Apaga el LED por 1 segundo

  // Caracter "trigger" que arranca serialEvent() de Processing
  Serial.println("$");
}

void sendSensorReadingsToProcessing() {
  // Lee la humedad
  humedad = dht.readHumidity();

  // Lee la temperatura en grados Celsius (por defecto)
  temperatura = dht.readTemperature();

  if (!isnan(humedad)){
    Serial.print("HUMEDAD/");
    Serial.println(humedad);
  }
  if (!isnan(temperatura)){
    Serial.print("TEMPERATURA/");
    Serial.println(temperatura);
  }

  // Lee el valor del sensor de luminosidad (LDR)
  ldrValue = analogRead(ldrPin);

  // Imprime el valor de la luminosidad en la consola serie
  Serial.print("LUZ/");
  Serial.println(ldrValue);

  // Lee el valor del sensor MQ-135
  mq135Value = analogRead(mq135Pin);

  // Imprime el valor del sensor MQ-135 en la consola serie
  Serial.print("CO2/");
  Serial.println(mq135Value);

  // Lógica para el sensor HC-SR04
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  distanceCm = duration * 0.034 / 2;
  Serial.print("DISTANCIA/");
  Serial.println(distanceCm);
}

void showSensorReadings() {
  // Comprueba si alguna lectura ha fallado
  if (isnan(humedad) || isnan(temperatura)) {
    Serial.println("Error al leer del sensor DHT11");
  } else {
    // Imprime los valores en la consola serie
    Serial.print("LCDHumedad: ");
    Serial.print(humedad);
    Serial.print(" %\t");
    Serial.print("LCDTemperatura: ");
    Serial.print(temperatura);
    Serial.println(" °C");
  }

  // Imprime el valor de la luminosidad en la consola serie
  Serial.print("LCDLuminosidad: ");
  Serial.println(ldrValue);

  // Imprime el valor del sensor MQ-135 en la consola serie
  Serial.print("LCDValor del sensor MQ-135: ");
  Serial.println(mq135Value);

  Serial.print("LCDDistancia: ");
  Serial.print(distanceCm);
  Serial.println(" cm");
}

void saveDataToEEPROM() {
  // Guarda los datos en la EEPROM
  EEPROM.put(eepromAddress, humedad);
  eepromAddress += sizeof(humedad);
  EEPROM.put(eepromAddress, temperatura);
  eepromAddress += sizeof(temperatura);
  EEPROM.put(eepromAddress, ldrValue);
  eepromAddress += sizeof(ldrValue);
  EEPROM.put(eepromAddress, mq135Value);
  eepromAddress += sizeof(mq135Value);
  EEPROM.put(eepromAddress, distanceCm); // Guardar la distancia
  eepromAddress += sizeof(distanceCm);

  Serial.println("Datos guardados en la EEPROM");
}

void readLastDataFromEEPROM() {
  // Variables para almacenar los datos leídos de la EEPROM
  float humedad;
  float temperatura;
  int ldrValue;
  int mq135Value;
  int distanceCm;

  // Dirección de memoria de lectura (la última dirección usada)
  int address = eepromAddress - (sizeof(humedad) + sizeof(temperatura) + sizeof(ldrValue) + sizeof(mq135Value) + sizeof(distanceCm));

  // Lee los datos desde la EEPROM
  EEPROM.get(address, humedad);
  address += sizeof(humedad);
  EEPROM.get(address, temperatura);
  address += sizeof(temperatura);
  EEPROM.get(address, ldrValue);
  address += sizeof(ldrValue);
  EEPROM.get(address, mq135Value);
  address += sizeof(mq135Value);
  EEPROM.get(address, distanceCm); // Leer la distancia

  // Imprime los datos leídos en la consola serie
  Serial.println("Últimos datos guardados leídos de la EEPROM:");
  Serial.print("Humedad: ");
  Serial.print(humedad);
  Serial.println(" %");
  Serial.print("Temperatura: ");
  Serial.print(temperatura);
  Serial.println(" °C");
  Serial.print("Luminosidad: ");
  Serial.println(ldrValue);
  Serial.print("Valor del sensor MQ-135: ");
  Serial.println(mq135Value);
  Serial.print("Distancia: ");
  Serial.println(distanceCm);
}

void readAllDataFromEEPROM() {
  // Variables para almacenar los datos leídos de la EEPROM
  float humedad;
  float temperatura;
  int ldrValue;
  int mq135Value;
  int distanceCm;

  // Dirección de memoria de lectura
  int address = 0;

  // Lee todos los datos desde la EEPROM
  Serial.println("Todos los datos almacenados en la EEPROM:");

  while (address < eepromAddress) {
    // Lee los datos desde la EEPROM
    EEPROM.get(address, humedad);
    address += sizeof(humedad);
    EEPROM.get(address, temperatura);
    address += sizeof(temperatura);
    EEPROM.get(address, ldrValue);
    address += sizeof(ldrValue);
    EEPROM.get(address, mq135Value);
    address += sizeof(mq135Value);
    EEPROM.get(address, distanceCm); // Leer la distancia
    address += sizeof(distanceCm);

    // Imprime los datos leídos en la consola serie
    Serial.println("-----------------------------");
    Serial.print("Humedad: ");
    Serial.print(humedad);
    Serial.println(" %");
    Serial.print("Temperatura: ");
    Serial.print(temperatura);
    Serial.println(" °C");
    Serial.print("Luminosidad: ");
    Serial.println(ldrValue);
    Serial.print("Valor del sensor MQ-135: ");
    Serial.println(mq135Value);
    Serial.print("Distancia: ");
    Serial.println(distanceCm);
  }

  Serial.println("-----------------------------");
}
