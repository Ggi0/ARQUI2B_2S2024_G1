class Humedad {
  ParticleSystem[] particles = new ParticleSystem[5];
  float porcentajeHumedad = 0;
  PFont f;
  int widthPanelH, heightPanelH;
  
  Humedad(){
    // Ancho y alto de panel calculado para dejar espacio para 4 marcos en pantalla
    widthPanelH = width / 2 - 10;
    heightPanelH = height / 2 - 5;
    
    for (int i = 0; i < particles.length; i++){
      particles[i] = new ParticleSystem(new PVector(widthPanelH * i / 5, 0), porcentajeHumedad, i);
    }
    
    f = createFont("Arial", 40);
    textFont(f);
    
    rectMode(CENTER);
    textAlign(CENTER);
  }

  void drawHumedad(float nuevoPorcentHumedad){
    porcentajeHumedad = nuevoPorcentHumedad;
    
    // Actualizando particulas
    for (int i = 0; i < particles.length; i++){
      particles[i].addParticle(porcentajeHumedad, widthPanelH);
      particles[i].run();
    }
    
    //Text
    widthPanelH = width / 2;
    heightPanelH = height / 2;
    
    //fill(#0C1464, percentageH * 100 / 100 + 155);
    fill(#0C1464);
    rect(widthPanelH/2, heightPanelH/2 - 15, 550, 60, 28);
    
    fill(255);
    text("Porcentaje de Humedad: " + round(porcentajeHumedad) + "%", widthPanelH/2, heightPanelH/2);
  }
}
