class Particle {
  PVector _origin;
  PVector position;
  PVector velocity;
  PVector acceleration;
  float lifespan;
  float factor;
  float maxAcceleration;
  color blue;

  Particle(PVector origin, float newFactor, float maxAcc, int widthPanelH) {
    factor = newFactor;
    maxAcceleration = maxAcc;
    acceleration = new PVector(0, factor);
    velocity = new PVector(random(-1, 1), random(-2, 0));
    position = origin.copy();
    _origin = origin.copy();
    
    // Relación considerando: size(640, 360) ->  lifespan = 255.0
    lifespan = widthPanelH * 255.0 / 640.0;
    if (lifespan > 255){
      lifespan = 255;
    }
  }

  void run() {
    update();
    display();
  }

  // Actualizar posición de partícula
  void update() {
    velocity.add(acceleration);
    position.add(velocity);
    lifespan -= 1.0;
  }

  // Display partícula
  void display() {
    if ( factor >= maxAcceleration * 2 / 3) {         // a partir del 66.67% de humedad
      blue = #1460D8;
    } else if (factor >= maxAcceleration * 1 / 3) {   // a partir de 33.33% de humedad
      blue = #75A0E3;
    } else {                                          // color inicial (muy ligero)
      blue = #9CC0FC;
    }
    
    if (position.array()[1] < _origin.array()[1]) {
      noStroke();
      fill(blue, 0);
    } else {
      stroke(255);
      fill(blue, lifespan);
    }
    ellipse(position.x, position.y, 10, 10);
  }

  // Determina si la partícula debe eliminarse
  boolean isDead() {
    return (lifespan < 0.0);
  }
  
  PVector getPosition(){
    return position;
  }
}
