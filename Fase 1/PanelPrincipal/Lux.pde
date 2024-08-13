/**
 * Reflection 
 * by Simon Greenwold. 
 * 
 * Vary the specular reflection component of a material
 * using a timed cycle.
 */
 
final color PAPER = color(125, 155, 185);

float s = 0.0;
boolean increasing = true;
int waitTime = 50; // Tiempo de espera entre cambios de color

void setup() {
  size(850, 478, P3D);
  noStroke();
  colorMode(RGB, 1);
  fill(0.4);
}

void draw() {
  PImage img;
  img = loadImage("nubes.jpg");
  background(img);

  translate(width / 2, height / 2);
  // Set the specular color of lights that follow
  lightSpecular(1, 1, 1);
  directionalLight(0.8, 0.8, 0.8, 0, 0, -1);
  
  // Actualiza el valor de 's' para cambiar el color
  if (increasing) {
    s += 0.01; // Aumenta el valor de 's'
    if (s >= 1.0) {
      increasing = false; // Inicia la disminución cuando 's' alcanza su máximo
    }
  } else {
    s -= 0.01; // Disminuye el valor de 's'
    if (s <= 0.0) {
      increasing = true; // Inicia el aumento cuando 's' alcanza su mínimo
    }
  }
  
  // Configura el color especular (rojo a anaranjado)
  specular(s, 0.5 * s, 0); 
  
  // Dibuja la esfera
  sphere(120);
  
  // Espera un poco antes de la siguiente actualización
  delay(waitTime);
}
