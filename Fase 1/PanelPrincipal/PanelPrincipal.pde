/**
 *
 */
import processing.serial.*;

Serial puertoArduino;

FloatDict sensores = new FloatDict();

// Declaración del ángulo inicial
float theta = 0.0;
/*
sensores = {
 "HUMEDAD": 90.0,
 "CO2": 99.0,
 "TEMPERATURA": 99.0,
 "DISTANCIA": 99.0,
 "LUZ": 99.0
 }
 */

/* Arreglo dinámico para guardar histórico de valores en EEPROM */
ArrayList<FloatDict> valoresEEPROM = new ArrayList<FloatDict>();

/* Paneles de cada uno de los sensores */
Humedad     panelHumedad;
Luz         panelLuz;
Temperatura panelTemperatura;
Humo        panelHumo; 
Proximidad  panelProximidad; // Reemplazar por panel de Sensor E

/* Diseño de la ventana */
int heightTitle = 100;
int verticalGap, horizontalGap;
color panelColor = 200; // gris
PFont fontTitle;

void setup() {
  size(1280, 960, P2D);
  windowMove(100, 20);
  fontTitle = createFont("Courier New", 40);

  // OJO
  // Descomentar cuando se esté usando el ARDUINO
  puertoArduino = new Serial(this, Serial.list()[0], 9600);
  puertoArduino.bufferUntil('$');

  inicializarSensores();

  verticalGap = 15;
  horizontalGap = 15;

  /*
  * PARÁMETROS
   * Tamaño del título, espaciado horizontal entre paneles, espaciado vertical entre paneles, num fila, num columna
   */
  // 1° FILA
  panelHumedad     = new Humedad(heightTitle, horizontalGap, verticalGap, 1, 1);
  panelLuz         = new Luz(heightTitle, horizontalGap, verticalGap, 1, 2);
  // 2° FILA
  panelTemperatura = new Temperatura(heightTitle, horizontalGap, verticalGap, 2, 1);
  panelHumo        = new Humo(heightTitle, horizontalGap, verticalGap, 2, 2);
  panelProximidad  = new Proximidad(heightTitle, horizontalGap, verticalGap, 2, 3);
}

void draw() {
  /* FONDO */
  drawBackground();
  drawTitle();

  /* PANELES 1° FILA (2 columnas) */
  //HUMEDAD
  drawBackgroundPanel(panelHumedad.getPosX(), panelHumedad.getPosY(), panelHumedad.getWidth(), panelHumedad.getHeight());
  panelHumedad.drawHumedad(sensores.get("HUMEDAD"));
  
  // Luz
  drawBackgroundPanel(panelLuz.getPosX(), panelLuz.getPosY(), panelLuz.getWidth(), panelLuz.getHeight());
  panelLuz.drawLuz(sensores.get("LUZ"));

  /* PANELES 2° FILA (3 columnas) */
  // SENSOR C
  drawBackgroundPanel(panelTemperatura.getPosX(), panelTemperatura.getPosY(), panelTemperatura.getWidth(), panelTemperatura.getHeight());
  panelTemperatura.drawTemperatura(sensores.get("TEMPERATURA"));

  // SENSOR D
  drawBackgroundPanel(panelHumo.getPosX(), panelHumo.getPosY(), panelHumo.getWidth(), panelHumo.getHeight());
  panelHumo.drawHumo(sensores.get("CO2"));

  // SENSOR E
  drawBackgroundPanel(panelProximidad.getPosX(), panelProximidad.getPosY(), panelProximidad.getWidth(), panelProximidad.getHeight());
  panelProximidad.drawProximidad(sensores.get("DISTANCIA"));

  // Cada 20 frames, actualiza la información del porcentaje de humedad
  /*if (frameCount % 15 == 0) {
    // OJO
    // Comentar cuando se esté usando el ARDUINO
    sensores.add("HUMEDAD", 1);
    sensores.set("HUMEDAD", sensores.get("HUMEDAD")%100);
    
    sensores.add("LUZ", 1);
    sensores.set("LUZ", sensores.get("LUZ")%100);
    
    sensores.add("TEMPERATURA", 1);
    sensores.set("TEMPERATURA", sensores.get("TEMPERATURA")%100);
    
    sensores.add("CO2", 1);
    sensores.set("CO2", sensores.get("CO2")%100);
    
    sensores.add("DISTANCIA", 1);
    sensores.set("DISTANCIA", sensores.get("DISTANCIA")%100);
  }*/
}

void drawBackground() {
  float scale = 100.0 / width; // tomando en cuenta que el máximo del stroke es de 255
  for (int i = 0; i < width; i++) {
    stroke(i * scale); // setea los colores de las líneas de 0 (negro) a 255 (blanco);
    line(i, 0, i, height); // dibuja líneas verticales por toda la pantalla
  }
}

void drawTitle() {
  fill(#82F2A8);
  noStroke();
  rectMode(CENTER);
  rect(width/2, heightTitle/2, width - horizontalGap * 2 - 200, heightTitle - verticalGap * 2, 28);
  textAlign(CENTER);
  textFont(fontTitle);
  for (int i = 4; i >= 0; i--) {
    fill(0, 0, 0, 255*(4-i)/4);
    text("Sensores Grupo 1 - FASE 1", width/2 - i, heightTitle/2 + 10 - i);
  }
  fill(0);
  text("Sensores Grupo 1 - FASE 1", width/2, heightTitle/2 + 10);
}

void drawBackgroundPanel(int posX, int posY, int _width, int _height) {
  fill(panelColor);
  rectMode(CORNER);
  strokeWeight(6);
  stroke(255);
  rect(posX, posY, _width, _height, 28);
  strokeWeight(1);
}

/* Sección que se dispara desde Arduino */
void serialEvent(Serial p) {
  // puertoArduino puede ser sustituido por el objeto Serial "p"
  String datosArduino = puertoArduino.readString();

  println("================== Datos recibidos de Arduino ==================");
  println(datosArduino);

  // Si viene '#' al inicio, son Serial.println's basura
  if (datosArduino.charAt(0) == '#') {
    println("> Datos de Arduino ignorados");
    return;
  }

  // Si viene '%' al inicio, guardar el histórico de valores almacenados en la EEPROM
  if (datosArduino.charAt(0) == '%') {
    valoresEEPROM.add(sensores);
    println("=========== Datos de sensores guardados en la EEPROM ==========");
    println(valoresEEPROM);
    return;
  }

  // Si entra a este flujo, actualizar valores de sensores en tiempo real

  inicializarSensores();

  String[] datosSensores = splitTokens(datosArduino, "\n");

  for (int i = 0; i < datosSensores.length; i++) {
    String[] datoSensor = splitTokens(datosSensores[i], "/");
    if (datoSensor.length != 2) {
      continue;
    }

    if (datoSensor[0].equals("HUMEDAD") || datoSensor[0].equals("CO2") || datoSensor[0].equals( "TEMPERATURA") || datoSensor[0].equals("DISTANCIA") || datoSensor[0].equals("LUZ")) {
      if (datoSensor[1].charAt(datoSensor[1].length() - 1) == '$') {
        datoSensor[1] = datoSensor[1].substring(0, datoSensor[1].length() - 1);
      }
      sensores.set(datoSensor[0], float(datoSensor[1]));
    }
  }

  println("=============== Datos de sensores actualizados ================");
  println(sensores);
}

void inicializarSensores() {
  sensores.set("HUMEDAD", 0.0);
  sensores.set("CO2", 0.0);
  sensores.set("TEMPERATURA", 0.0);
  sensores.set("DISTANCIA", 0.0);
  sensores.set("LUZ", 1023);
}
