PanelSensor panel;
int lastChangeTime = 0;
int changeDuration = 2000; // 2000 milisegundos = 2 segundos
int valorReferencia = 200; // Valor maximo de referencia

void setup() {
  size(1200, 950);  // Aumentamos un poco la altura para el label
  createNewPanel();
}

void draw() {
  background(255);
  
  // Verificar si han pasado 2 segundos
  if (millis() - lastChangeTime > changeDuration) {
    createNewPanel();
    lastChangeTime = millis();
  }
  
  // Actualizar y mostrar el panel
  panel.update();
  panel.display();
}

void createNewPanel() {
  int ballCount = int(random(1, 201)); // Número aleatorio de bolas entre 1 y 200
  int porcentaje = int((ballCount / float(valorReferencia)) * 100); // Se obtiene el porcentaje
  panel = new PanelSensor(50, 30, 400, 375, 5, porcentaje);
}
