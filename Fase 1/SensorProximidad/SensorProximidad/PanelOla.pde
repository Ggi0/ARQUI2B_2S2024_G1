class PanelOla {
  // Valores de referencia para multiplicarlos
  float velocidadReferencia = 0.004;
  float amplitudReferencia = 1.5;
  float periodoReferencia = 0.002;
  float x, y, w, h, velocidad, amplitud, periodo, porcentaje;
  
  PanelOla(float x, float y, float w, float h, int porcentaje) {
    this.x = x;
    this.y = y;
    this.w = w;
    this.h = h;
    this.porcentaje = porcentaje;
    this.velocidad = velocidadReferencia * porcentaje;
    this.amplitud = amplitudReferencia * porcentaje;
    this.periodo = periodoReferencia * porcentaje;
  }

  void dibujar() {
    // Dibujar marco
    stroke(0);
    fill(0);
    rect(x, y, w, h, 20);

    // Dibujar olas dentro del marco
    float angle = theta;
    stroke(66, 186, 61);  // Color verde para la línea
    noFill();
    beginShape(); // Inicia la forma para conectar puntos
    for (int i = 0; i <= w; i += 10) {
      float yPos = y + h/2 + sin(angle) * amplitud; // Amplitud controla la altura de la onda
      vertex(x + i, yPos); // Define un vértice de la forma
      angle += periodo; // El periodo controla la distancia entre las olas
    }
    endShape(); // Termina la forma y conecta todos los puntos
    // Dibujar el label
    fill(0);
    textAlign(CENTER, TOP);
    textSize(24);
    text("Porcentaje de distancia: " + porcentaje + "%", x + w/2, y + h + 10);
  }

  void actualizar() {
    theta += velocidad;
  }

  void actualizarParametros(int porcentaje) {
    this.porcentaje = porcentaje;
    this.velocidad = velocidadReferencia * porcentaje;
    this.amplitud = amplitudReferencia * porcentaje;
    this.periodo = periodoReferencia * porcentaje;
  }
}
