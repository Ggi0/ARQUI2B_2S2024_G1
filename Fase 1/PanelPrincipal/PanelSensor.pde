class PanelSensor {
  float x, y;  // Posición del panel
  float w, h;  // Ancho y alto del panel
  ArrayList<Ball> balls;  // Lista de bolas dentro del panel
  int ballCount;  // Cantidad de bolas
  
  PanelSensor(float x, float y, float w, float h, float speed, int ballCount) {
    this.x = x;
    this.y = y;
    this.w = w;
    this.h = h;
    this.ballCount = ballCount;
    
    // Inicializar la lista de bolas
    balls = new ArrayList<Ball>();
    
    // Crear la cantidad especificada de bolas
    for (int i = 0; i < ballCount; i++) {
      float radius = random(10, 30);  // Radio aleatorio entre 10 y 30
      balls.add(new Ball(radius, w, h, speed));
    }
  }
  
  void update() {
    for (Ball ball : balls) {
      ball.move(x, y, w, h);
    }
  }
  
  void display() {
    // Dibujar el marco
    stroke(0);
    fill(int(255-float(ballCount)/10));
    rect(x, y, w, h, 20);
    
    // Dibujar las bolas
    pushMatrix();
    translate(x, y);  // Trasladar el origen al inicio del panel
    for (Ball ball : balls) {
      ball.display();
    }
    popMatrix();
  }
}
