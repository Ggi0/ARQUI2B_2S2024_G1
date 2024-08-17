#include <EEPROM.h>
#include "DHT.h"

// Librerias para manejar la pantalla con comunicación I2C
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

// Definir la dirección I2C de la pantalla LCD
LiquidCrystal_I2C lcd(0x27, 16, 2);  // Dirección I2C 0x27, pantalla de 16x2

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
const int buttonPins[4] = {18, 19, 2, 3};

// Dirección de memoria EEPROM para almacenar los datos
int eepromAddress = 0;

// Variables para los pines trigPin y echoPin,
// así como para almacenar la duración y la distancia calculada.
const int trigPin = 10;
const int echoPin = 9;
long duration;

// ---------- Banderas y valores para MOSTRAR los valores -------
volatile bool lcdUpdateFlag = false;
volatile int buttonPressed = 0;

// ----------------------- INTERRUPCIONES --------------------
// Estas funciones se activan cuando se presionan los botones del teclado membrana
// Funciones de interrupción para cada botón

// botón 2 -------> DATOS ACTUALES
void button1ISR() { 
  //showSensorReadings();

  buttonPressed = 2;
  lcdUpdateFlag = true;
}

// botón 1 -----> GUARDAR DATOS
void button2ISR() { 
  // Guardar los datos en la EEPROM
  //saveDataToEEPROM(); 

  buttonPressed = 1;
  lcdUpdateFlag = true;
}

// botón 4 ------> ULTIMOS DATOS
void button3ISR() { 
  // Mostrar la última información guardada
  //readLastDataFromEEPROM();
  buttonPressed = 4;
  lcdUpdateFlag = true;
}

// botón 3 -----> TODOS LOS DATOS 
void button4ISR() { 
  // Mostrar todos los datos almacenados en la EEPROM
  //readAllDataFromEEPROM(); 
  buttonPressed = 3;
  lcdUpdateFlag = true;
}

void setup() {
  // Inicia la comunicación serie a 9600 baudios
  Serial.begin(9600);
  Serial.println("Iniciando sensores...");

  // Inicia el sensor DHT
  dht.begin();

  // Configura el pin LED como salida
  pinMode(LED_PIN, OUTPUT);

  // Configuración del sensor ultrasónico
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  // Configura los pines del teclado como entradas con resistencia pull-up interna
  for (int i = 0; i < 4; i++) {
    pinMode(buttonPins[i], INPUT_PULLUP);
  }
  Serial.println("antes de la interrupción");
  // Asocia las interrupciones a los botones
  attachInterrupt(digitalPinToInterrupt(buttonPins[0]), button1ISR, FALLING);
  attachInterrupt(digitalPinToInterrupt(buttonPins[1]), button2ISR, FALLING);
  attachInterrupt(digitalPinToInterrupt(buttonPins[2]), button3ISR, FALLING);
  attachInterrupt(digitalPinToInterrupt(buttonPins[3]), button4ISR, FALLING);
 Serial.println("DESPUES DE LA INTER");
  

  Serial.println("DHT11, LDR, MQ-135, y teclado de membrana 1x4 con EEPROM");

  // ------------- PANTALLA LCD ---------------------
  // Inicializar la pantalla LCD
  lcd.init();
  lcd.begin(16, 2);
  lcd.backlight();  // Encender la luz de fondo de la LCD
  Serial.println("Prendiendo Pantalla...");

  // Mensaje de bienvenida en la LCD
  lcd.setCursor(0, 0);  // Coloca el cursor en la primera línea
  lcd.print("Bienvenido! ACE2");
  lcd.setCursor(0, 1);  // Coloca el cursor en la segunda línea
  lcd.print("Fase 1 Grupo 1");

  delay(2000);  // Pausa para mostrar el mensaje de bienvenida
  lcd.clear();  // Limpiar la pantalla después del mensaje

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

  if (lcdUpdateFlag) {
    lcdUpdateFlag = false; // Resetear la bandera

    switch (buttonPressed) {
      case 1:
        lcd.clear();
        lcd.setCursor(0, 0);  // Primera línea
        lcd.print("Datos Guardados");
        lcd.setCursor(0, 1);  // Segunda línea
        lcd.print("Exitosamente");
        delay(1000);
        saveDataToEEPROM(); 
        break;
      case 2:
        lcd.clear();
        lcd.print("Datos ACTUALES");
        delay(1000);
        showSensorReadings();
        break;
      case 3:
        //readLastDataFromEEPROM();
        lcd.clear();
        lcd.print("Todos los Datos");
        delay(1000);
        readAllDataFromEEPROM();
        break;
      case 4:
        lcd.clear();
        lcd.setCursor(0, 0);  // Primera línea
        lcd.print("Mostrar");
        lcd.setCursor(0, 1);  // Segunda línea
        lcd.print("Datos Guardados");
        delay(1000);
        readLastDataFromEEPROM();
        break;
    }
  }


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

  // -------- menú PANTALLA LCD --------------
  // Limpiar la pantalla antes de escribir
  lcd.clear();

  // Mostrar las primeras dos opciones en la pantalla LCD
  lcd.setCursor(0, 0);  // Colocar el cursor en la primera línea
  lcd.print("1.Save 4.Mostrar");
  lcd.setCursor(0, 1);  // Colocar el cursor en la segunda línea
  lcd.print("2.Datos Actuales");

  delay(50);  // Pausa de 2 segundos para visualizar las primeras opciones
}

void showSensorReadings() {

  Serial.println(">>>>>>>>>>>>>>>> datos actuales <<<<<<<<<<<<<<<<<<<");

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

    // Mostrar humedad y temperatura en la pantalla LCD
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("%H:");
    lcd.print(humedad);
    lcd.setCursor(0, 1);
    lcd.print("T(C):");
    lcd.print(temperatura);
    delay(3000);  // Mantener esta pantalla por 3 segundos
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

  // Mostrar valores de LDR, CO2 y distancia en la pantalla LCD
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Luz:");
  lcd.print(ldrValue);
  
  lcd.setCursor(0, 1);
  lcd.print("CO2:");
  lcd.print(mq135Value);
  lcd.print(" D(cm):");
  lcd.print(distanceCm);
  delay(3000);  // Mantener esta pantalla por 3 segundos

  lcd.clear();
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

  Serial.println("------------ Datos guardados en la EEPROM");
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
  Serial.println("------------------ Últimos datos guardados leídos de la EEPROM:");
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

    // Mostrar humedad y temperatura en la pantalla LCD
  lcd.clear();
  lcd.setCursor(0, 0);  // Primera línea
  lcd.print("H:");
  lcd.print(humedad);
  lcd.setCursor(0, 1);  // Segunda línea
  lcd.print("T(C):");
  lcd.print(temperatura);
  delay(3000);  // Mostrar por 3 segundos

  // Mostrar valores de LDR, CO2 y distancia en la pantalla LCD
  lcd.clear();
  lcd.setCursor(0, 0);  // Primera línea
  lcd.print("L:");
  lcd.print(ldrValue);
  lcd.setCursor(0, 1);  // Segunda línea
  lcd.print("CO2:");
  lcd.print(mq135Value);
  lcd.print(" D(cm):");
  lcd.print(distanceCm);
  delay(3000);  // Mostrar por 3 segundos

  lcd.clear();  // Limpiar la pantalla
}

void readAllDataFromEEPROM() {

  Serial.println("333333333333 todos los datos 33333333333333");


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

    // Mostrar humedad y temperatura en la pantalla LCD
  lcd.clear();
  lcd.setCursor(0, 0);  // Primera línea
  lcd.print("H:");
  lcd.print(humedad);
  lcd.setCursor(0, 1);  // Segunda línea
  lcd.print("T(C):");
  lcd.print(temperatura);
  delay(3000);  // Mostrar por 3 segundos

  // Mostrar valores de LDR, CO2 y distancia en la pantalla LCD
  lcd.clear();
  lcd.setCursor(0, 0);  // Primera línea
  lcd.print("L:");
  lcd.print(ldrValue);
  lcd.setCursor(0, 1);  // Segunda línea
  lcd.print("CO2:");
  lcd.print(mq135Value);
  lcd.print(" D(cm):");
  lcd.print(distanceCm);
  delay(3000);  // Mostrar por 3 segundos

  lcd.clear();  // Limpiar la pantalla
  }

  Serial.println("-----------------------------");
}