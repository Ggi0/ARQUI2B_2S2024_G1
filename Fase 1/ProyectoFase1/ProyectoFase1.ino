#include <EEPROM.h>
#include "DHT.h"

#define DHTPIN 4      // Pin al que está conectado el pin de datos del DHT11
#define DHTTYPE DHT11 // DHT 11
#define LED_PIN 13    // Pin al que está conectado el LED

int ldrPin = A0;      // Pin analógico donde está conectado el LDR
int mq135Pin = A1;    // Pin analógico al que está conectado la salida del MQ-135
int ldrValue = 0;     // Variable para almacenar el valor del LDR
int mq135Value = 0;   // Variable para almacenar el valor del MQ-135

DHT dht(DHTPIN, DHTTYPE);

// Definimos los pines del teclado
const int buttonPins[4] = {18, 19, 20, 21};

// Variables para almacenar el estado de los botones con interrupciones
volatile bool buttonPressed[4] = {false, false, false, false};

// Dirección de memoria EEPROM para almacenar los datos
int eepromAddress = 0;

// Funciones de interrupción para cada botón
void button1ISR() { buttonPressed[0] = true; }
void button2ISR() { buttonPressed[1] = true; }
void button3ISR() { buttonPressed[2] = true; }
void button4ISR() { buttonPressed[3] = true; }

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

  Serial.println("DHT11, LDR, MQ-135, y teclado de membrana 1x4 con EEPROM");
}

void loop() {
  // Verificar si el botón 1 fue presionado
  if (buttonPressed[0]) {
    buttonPressed[0] = false; // Resetear la bandera
    // Mostrar las lecturas de los sensores
    showSensorReadings();
  }

  // Verificar si el botón 2 fue presionado
  if (buttonPressed[1]) {
    buttonPressed[1] = false; // Resetear la bandera
    // Guardar los datos en la EEPROM
    saveDataToEEPROM();
  }

  // Verificar si el botón 3 fue presionado
  if (buttonPressed[2]) {
    buttonPressed[2] = false; // Resetear la bandera
    // Mostrar la última información guardada
    readLastDataFromEEPROM();
  }

  // Verificar si el botón 4 fue presionado
  if (buttonPressed[3]) {
    buttonPressed[3] = false; // Resetear la bandera
    // Mostrar todos los datos almacenados en la EEPROM
    readAllDataFromEEPROM();
  }

  // Alterna el estado del LED
  digitalWrite(LED_PIN, HIGH);
  delay(1000); // Enciende el LED por 1 segundo
  digitalWrite(LED_PIN, LOW);
  delay(1000); // Apaga el LED por 1 segundo
}

void showSensorReadings() {
  // Lee la humedad
  float humedad = dht.readHumidity();

  // Lee la temperatura en grados Celsius (por defecto)
  float temperatura = dht.readTemperature();

  // Comprueba si alguna lectura ha fallado
  if (isnan(humedad) || isnan(temperatura)) {
    Serial.println("Error al leer del sensor DHT11");
  } else {
    // Imprime los valores en la consola serie
    Serial.print("Humedad: ");
    Serial.print(humedad);
    Serial.print(" %\t");
    Serial.print("Temperatura: ");
    Serial.print(temperatura);
    Serial.println(" °C");
  }

  // Lee el valor del sensor de luminosidad (LDR)
  ldrValue = analogRead(ldrPin);

  // Imprime el valor de la luminosidad en la consola serie
  Serial.print("Luminosidad: ");
  Serial.println(ldrValue);

  // Lee el valor del sensor MQ-135
  mq135Value = analogRead(mq135Pin);

  // Imprime el valor del sensor MQ-135 en la consola serie
  Serial.print("Valor del sensor MQ-135: ");
  Serial.println(mq135Value);
}

void saveDataToEEPROM() {
  // Lee las lecturas actuales de los sensores
  float humedad = dht.readHumidity();
  float temperatura = dht.readTemperature();
  int ldrValue = analogRead(ldrPin);
  int mq135Value = analogRead(mq135Pin);

  // Guarda los datos en la EEPROM
  EEPROM.put(eepromAddress, humedad);
  eepromAddress += sizeof(humedad);
  EEPROM.put(eepromAddress, temperatura);
  eepromAddress += sizeof(temperatura);
  EEPROM.put(eepromAddress, ldrValue);
  eepromAddress += sizeof(ldrValue);
  EEPROM.put(eepromAddress, mq135Value);
  eepromAddress += sizeof(mq135Value);

  Serial.println("Datos guardados en la EEPROM");
}

void readLastDataFromEEPROM() {
  // Variables para almacenar los datos leídos de la EEPROM
  float humedad;
  float temperatura;
  int ldrValue;
  int mq135Value;

  // Dirección de memoria de lectura (la última dirección usada)
  int address = eepromAddress - (sizeof(humedad) + sizeof(temperatura) + sizeof(ldrValue) + sizeof(mq135Value));

  // Lee los datos desde la EEPROM
  EEPROM.get(address, humedad);
  address += sizeof(humedad);
  EEPROM.get(address, temperatura);
  address += sizeof(temperatura);
  EEPROM.get(address, ldrValue);
  address += sizeof(ldrValue);
  EEPROM.get(address, mq135Value);

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
}

void readAllDataFromEEPROM() {
  // Variables para almacenar los datos leídos de la EEPROM
  float humedad;
  float temperatura;
  int ldrValue;
  int mq135Value;

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
  }

  Serial.println("-----------------------------");
}

