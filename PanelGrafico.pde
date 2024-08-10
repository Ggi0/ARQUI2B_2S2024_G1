class PanelGrafico {
  int x, y;  // Posición del panel
  int size;  // Tamaño del panel (ancho = alto = size)
  
  PanelGrafico(int posX, int posY) {
    // Calcula el tamaño del panel basado en 1/4 de la pantalla
    size = min(width, height) / 2;
    x = posX;
    y = posY;
  }
  
  void drawPanel() {
    // Dibujar un rectángulo como marco del panel
    fill(200); // Color de fondo del panel
    stroke(0); // Color del borde del panel
    strokeWeight(2);
    rect(x, y, size, size);
    
    // Aquí podrías agregar más código para dibujar gráficos específicos dentro del panel
  }
  
  void drawContent(float[] data) {
    // Ejemplo de dibujo de contenido simple: un gráfico de barras
    int numBars = data.length;
    float barWidth = size / numBars;
    
    for (int i = 0; i < numBars; i++) {
      float barHeight = map(data[i], 0, 100, 0, size);
      fill(100, 150, 255);
      rect(x + i * barWidth, y + size - barHeight, barWidth - 2, barHeight);
    }
  }
}
