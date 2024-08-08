/**
 *
 */

Humedad panelHumedad;

float porcentajeHumedad = 0;

void setup() {
  size(1280, 960, P2D);
  panelHumedad = new Humedad();
}

void draw() {
  background(255);
  panelHumedad.drawHumedad(porcentajeHumedad);
  
  // Cada 20 frames, solicitar nueva información de Arduino
  // Utilización de hilos para no ralentizar el render de los marcos
  if (frameCount % 20 == 0) {
    thread("updateHumedad");
  }
}

void updateHumedad() {
  porcentajeHumedad += 1;
  porcentajeHumedad %= 100;
}
