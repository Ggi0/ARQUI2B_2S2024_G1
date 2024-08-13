// Declaración del ángulo inicial
float theta = 0.0;

// Declaración del panel
PanelOla panel;

// Variables para el porcentaje aleatorio y el temporizador
float porcentajeAleatorio;
int intervaloActualizacion = 2000; // Intervalo de actualización en milisegundos
int tiempoUltimaActualizacion;

void setup() {
  size(1200, 900);
  tiempoUltimaActualizacion = millis(); // Captura el tiempo actual
  porcentajeAleatorio = random(0, 100); // Genera un porcentaje aleatorio entre 0 y 100
  panel = new PanelOla(50, 50, 450, 400, (int) porcentajeAleatorio);
}

void draw() {
  background(255);
  // Verifica si ha pasado el intervalo de actualización
  if (millis() - tiempoUltimaActualizacion > intervaloActualizacion) {
    porcentajeAleatorio = random(0, 100); // Genera un nuevo porcentaje aleatorio entre 0 y 100
    tiempoUltimaActualizacion = millis(); // Actualiza el tiempo de la última actualización
    panel.actualizarParametros((int) porcentajeAleatorio); // Actualiza los parámetros del panel
  }
  panel.dibujar();
  panel.actualizar();
}
