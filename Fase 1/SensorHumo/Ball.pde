class Ball {
  float r;   // radius
  float x, y; // location
  float xspeed, yspeed; // speed
  float maxSpeed; // maximum speed
  
  // Constructor
  Ball(float tempR, float panelWidth, float panelHeight, float maxSpeed) {
    r = tempR;
    x = random(r, panelWidth - r);
    y = random(r, panelHeight - r);
    this.maxSpeed = maxSpeed;
    xspeed = random(-maxSpeed, maxSpeed);
    yspeed = random(-maxSpeed, maxSpeed);
  }
  
  void move(float panelX, float panelY, float panelWidth, float panelHeight) {
    x += xspeed;
    y += yspeed;
    
    // Check horizontal edges
    if (x > panelWidth - r || x < r) {
      xspeed *= -1;
      x = constrain(x, r, panelWidth - r);
    }
    
    // Check vertical edges
    if (y > panelHeight - r || y < r) {
      yspeed *= -1;
      y = constrain(y, r, panelHeight - r);
    }
  }
  
  void display() {
    stroke(0);
    fill(0, 50);
    ellipse(x, y, r*2, r*2);
  }
}
