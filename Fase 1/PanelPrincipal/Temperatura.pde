class Temperatura{

  PImage img;
  float porcentajeTemperatura = 0;
  PFont f, f2;
  int _width, _height, _posX, _posY;
  int _heightTitle, _hGap, _vGap, _rowNum, _columnNum;

  float s = 0.0;
  boolean increasing = true;
  int waitTime = 50; // Tiempo de espera entre cambios de color

  Temperatura(int heightTitle, int horizontalGap, int verticalGap, int rowNumber, int columnNumber) {
    _heightTitle = heightTitle;
    _hGap = horizontalGap;
    _vGap = verticalGap;
    _rowNum = rowNumber;
    _columnNum = columnNumber;

    updateDimensions();

    f = createFont("Arial", 35);
    f2 = createFont("Arial", 23);
    textAlign(CENTER);

    imageMode(CENTER);
    img = loadImage("temperatura.png");
    img.resize(_height, _height);
  }

  void drawTemperatura(float nuevoporcentajeTemperatura) {
    porcentajeTemperatura = nuevoporcentajeTemperatura;
 
    updateDimensions();
   
    //IMAGE
    image(img, _width / 2 + _posX, _height / 2 + _posY);
    
    //BARRA TEMPERATURA
    fill(#E80909);
    rectMode(CORNERS);
    // PUNTO MÁS ALTO EN Y: _posY + _height*0.1 > 100%
    // PUNTO MÁS BAJO EN Y: _posY + _height*0.6 > 0%
    float factorY = -0.5 * nuevoporcentajeTemperatura / 100 + 0.6;
    rect(_posX + _width / 2 - 5, _posY + _height*0.75, _posX + 5 + _width / 2, _posY + _height * factorY, 25);

    //TEXT
    fill(#0C1464);
    noStroke();
    rectMode(CENTER);

    if (_width*0.9 > 550) {
      textFont(f);
      rect(_width/2 + _posX, _height/2 + 150 + _posY, 550, 60, 28);
    } else {
      textFont(f2);
      rect(_width/2 + _posX, _height/2 + 150 + _posY, _width*0.9, 60, 28);
    }

    fill(255);
    text("Porcentaje de Temperatura: " + round(porcentajeTemperatura) + "%", _width/2 + _posX, _height/2 + 160 + _posY);
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

  void updateDimensions() {
    switch(_rowNum) {
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
