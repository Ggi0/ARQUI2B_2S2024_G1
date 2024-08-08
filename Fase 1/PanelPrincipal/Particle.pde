class Particle {
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
    stroke(255, lifespan);
    
    if ( factor >= maxAcceleration * 5 / 6) {
      blue = #1460D8;
    } else if (factor >= maxAcceleration * 3 / 6) {
        blue = #75A0E3;
    } else {
        blue = #9CC0FC;
    }
    fill(blue, lifespan);
    ellipse(position.x, position.y, 10, 10);
  }

  // Determina si la partícula debe eliminarse
  boolean isDead() {
    return (lifespan < 0.0);
  }
}
