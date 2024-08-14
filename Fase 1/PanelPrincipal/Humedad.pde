class Humedad {
  ParticleSystem[] particles = new ParticleSystem[6];
  PImage img;
  float porcentajeHumedad = 0;
  PFont f, f2;
  int _width, _height, _posX, _posY;
  int _heightTitle, _hGap, _vGap, _rowNum, _columnNum;
  
  Humedad(int heightTitle, int horizontalGap, int verticalGap, int rowNumber, int columnNumber){
    _heightTitle = heightTitle;
    _hGap = horizontalGap;
    _vGap = verticalGap;
    _rowNum = rowNumber;
    _columnNum = columnNumber;
    
    updateDimensions();    
    
    int i;
    for (i = 0; i < particles.length - 1; i++){
      particles[i] = new ParticleSystem(new PVector(_width * i / particles.length + _posX, _posY + 10), porcentajeHumedad, i);
    }
    particles[i] = new ParticleSystem(new PVector(_width + _posX, _posY + 10), porcentajeHumedad, i);
    
    f = createFont("Arial", 38);
    f2 = createFont("Arial", 28);
    textAlign(CENTER);
    
    imageMode(CENTER);
    img = loadImage("sombrilla.png");
    img.resize(_height, _height);
  }

  void drawHumedad(float nuevoPorcentHumedad){    
    porcentajeHumedad = nuevoPorcentHumedad;
    
    updateDimensions();
    
    // Actualizando particulas
    for (int i = 0; i < particles.length; i++){
      particles[i].addParticle(porcentajeHumedad, _width, _posX, _posY + 10);
      particles[i].run(nuevoPorcentHumedad, _width, _posX, _hGap, _height, _posY, _vGap);
    }
    
    //IMAGE
    image(img, _width / 2 + _posX, _height / 2 + _posY);
    
    //TEXT
    fill(#0C1464);
    noStroke();
    rectMode(CENTER);
    
    if (_width*0.9 > 550) {
     textFont(f);
     rect(_width/2 + _posX, _height/2 + 150 + _posY, 550, 60, 28);
    }
    else {
     textFont(f2);
     rect(_width/2 + _posX, _height/2 + 150 + _posY, _width*0.9, 60, 28);
    }
    
    fill(255);
    text("Porcentaje de Humedad: " + round(porcentajeHumedad) + "%", _width/2 + _posX, _height/2 + 160 + _posY);
  }
  
  int getWidth() {
    updateDimensions();
    return _width;
  }
  
  int getHeight() {
    updateDimensions();
    return _height;
  }
  
  int getPosX() {
    updateDimensions();
    return _posX;
  }
  
  int getPosY() {
    updateDimensions();
    return _posY;
  }
  
  void updateDimensions(){
    switch(_rowNum){
      case 1:
          // PRIMERA FILA -> grid: 2 columnas
          _width = int(width / 2 - 1.5 * _hGap);
        break;
      case 2:
          // SEGUNDA FILA -> grid: 3 columnas
          _width = (width - _hGap) / 3 - _hGap;
        break;
    }
    
    int heightContent = height - _heightTitle;
    int heightRow = heightContent / 2;
    
    _height = heightRow - _vGap;
    _posX = _hGap * _columnNum + _width * (_columnNum - 1);
    _posY = heightTitle + _vGap * (_rowNum - 1) + _height * (_rowNum - 1);
  }
}
