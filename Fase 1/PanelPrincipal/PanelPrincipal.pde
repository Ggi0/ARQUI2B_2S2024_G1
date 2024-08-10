/**
 *
 */
import processing.serial.*;

Serial puertoArduino;

Humedad panelHumedad;

/*
sensores = {
  "HUMEDAD": "90",
  "CO2": "99",
  "TEMPERATURA": "99",
  "DISTANCIA": "99",
  "LUZ": "99"
}
*/
FloatDict sensores = new FloatDict();

ArrayList<FloatDict> valoresEEPROM = new ArrayList<FloatDict>();

void setup() {
  size(1280, 960, P2D);
  
  puertoArduino = new Serial(this, Serial.list()[0], 9600);
  puertoArduino.bufferUntil('$');
  
  inicializarSensores();
  
  rectMode(CENTER);
  panelHumedad = new Humedad();
}

void draw() {
  background(255);
  fill(200);
  rect(width/4, height/4, panelHumedad.getWidth(), panelHumedad.getHeight(), 28);
  
  panelHumedad.drawHumedad(sensores.get("HUMEDAD"));
  panelHumedad.drawHumedad(sensores.get("HUMEDAD"));
  panelHumedad.drawHumedad(sensores.get("HUMEDAD"));
  panelHumedad.drawHumedad(sensores.get("HUMEDAD"));
  panelHumedad.drawHumedad(sensores.get("HUMEDAD"));
  
  
  // Cada 20 frames, solicitar nueva información de Arduino
  // Utilización de hilos para no ralentizar el render de los marcos
  if (frameCount % 10 == 0) {
    //sensores.add("HUMEDAD", 1);
    //sensores.set("HUMEDAD", sensores.get("HUMEDAD")%100);
  }
}

void serialEvent(Serial p){
  // puertoArduino puede ser sustituido por el objeto Serial "p"
  String datosArduino = puertoArduino.readString();
  
  println("================== Datos recibidos de Arduino ==================");
  println(datosArduino);
  
  // Si viene '#' al inicio, son Serial.println's basura
  if (datosArduino.charAt(0) == '#'){
    println("> Datos de Arduino ignorados");
    return;
  }
  
  // Si viene '%' al inicio, guardar el histórico de valores almacenados en la EEPROM
  if (datosArduino.charAt(0) == '%'){
    valoresEEPROM.add(sensores);
    println("=========== Datos de sensores guardados en la EEPROM ==========");
    println(valoresEEPROM);
    return;
  }
  
  // Si entra a este flujo, actualizar valores de sensores en tiempo real
  
  inicializarSensores();
  
  String[] datosSensores = splitTokens(datosArduino, "\n");
  
  for (int i = 0; i < datosSensores.length; i++){
    String[] datoSensor = splitTokens(datosSensores[i], "/");
    if(datoSensor.length != 2) { continue; }
    
    if (datoSensor[0].equals("HUMEDAD") || datoSensor[0].equals("CO2") || datoSensor[0].equals( "TEMPERATURA") || datoSensor[0].equals("DISTANCIA") || datoSensor[0].equals("LUZ")) {
      if(datoSensor[1].charAt(datoSensor[1].length() - 1) == '$'){   
        datoSensor[1] = datoSensor[1].substring(0, datoSensor[1].length() - 1);
      }
      sensores.set(datoSensor[0], float(datoSensor[1]));
    }
  }
  
  println("=============== Datos de sensores actualizados ================");
  println(sensores);
}

void inicializarSensores(){
  sensores.set("HUMEDAD", 0.0);
  sensores.set("CO2",0.0);
  sensores.set("TEMPERATURA",0.0);
  sensores.set("DISTANCIA",0.0);
  sensores.set("LUZ",0.0);
}
