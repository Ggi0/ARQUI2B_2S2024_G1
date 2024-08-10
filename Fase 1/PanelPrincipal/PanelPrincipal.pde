/**
 *
 */
import processing.serial.*;

Serial puertoArduino;

/*
sensores = [
  ["HUMEDAD", "90"],
  ["CO2", "99"],
  ["TEMPERATURA", "99"],
  ["DISTANCIA", "99"],
  ["LUZ", "99"]
]
*/
ArrayList<String[]> sensores = new ArrayList<String[]>();

Humedad panelHumedad;

float porcentajeHumedad = 0;

void setup() {
  size(1280, 960, P2D);
  
  puertoArduino = new Serial(this, Serial.list()[0], 9600);
  puertoArduino.bufferUntil('$');
  
  panelHumedad = new Humedad();
}

void draw() {
  background(255);
  panelHumedad.drawHumedad(porcentajeHumedad);
  
  // Cada 20 frames, solicitar nueva información de Arduino
  // Utilización de hilos para no ralentizar el render de los marcos
  if (frameCount % 200 == 0) {
    thread("updateHumedad");
  }
}

void updateHumedad() {
  //porcentajeHumedad += 1;
  //porcentajeHumedad %= 100;
  porcentajeHumedad = random(0, 100);
}

void serialEvent(Serial p){
  // puertoArduino puede ser sustituido por el objeto Serial "p"
  String datosArduino = puertoArduino.readString();
  println(datosArduino);
  
  // Si viene '#' al inicio, son Serial.println's basura
  if (datosArduino.charAt(0) == '#'){
    println("Serial.println's de Arduino ignorados");
    return;
  }
  
  // Si viene '%' al inicio, guardar el histórico de valores almacenados en la EEPROM
  if (datosArduino.charAt(0) == '%'){
    println("GUARDAR DATOS DE LA EEPROM");
    return;
  }
  
  // Si entra a este flujo, actualizar valores de sensores en tiempo real
  
  String[] datosSensores = splitTokens(datosArduino, "\n");
  
  sensores.clear();
  
  for (int i = 0; i < datosSensores.length; i++){
    String[] datoSensor = splitTokens(datosSensores[i], "/");
    if(datoSensor.length != 2) { continue; }
    
    if (datoSensor[0].equals("HUMEDAD") || datoSensor[0].equals("CO2") || datoSensor[0].equals( "TEMPERATURA") || datoSensor[0].equals("DISTANCIA") || datoSensor[0].equals("LUZ")) {
      if(datoSensor[1].charAt(datoSensor[1].length() - 1) == '$'){   
        datoSensor[1] = datoSensor[1].substring(0, datoSensor[1].length() - 1);
      }
      sensores.add(datoSensor);
    }
  }
  
  println("========= Datos guardados en el ArrayList =========");
  for (int i = 0; i < sensores.size(); i++){
     println(sensores.get(i));
  }
}
