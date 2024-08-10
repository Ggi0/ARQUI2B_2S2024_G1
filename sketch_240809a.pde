PanelGrafico panel;

void setup() {
  size(1280, 960);
  panel = new PanelGrafico(width/2 - 160, height/2 - 160); // Posición centrada
}

void draw() {
  background(255);
  panel.drawPanel();
  
  // Datos de ejemplo para el gráfico
  float[] data = {25, 50, 75, 100};
  panel.drawContent(data);
}
