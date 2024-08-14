class Luz {

  PImage img;
  float porcentajeLuz = 0;
  PFont f, f2;
  int _width, _height, _posX, _posY;
  int _heightTitle, _hGap, _vGap, _rowNum, _columnNum;

  float s = 0.0;
  boolean increasing = true;
  int waitTime = 50; // Tiempo de espera entre cambios de color

  Luz(int heightTitle, int horizontalGap, int verticalGap, int rowNumber, int columnNumber) {
    _heightTitle = heightTitle;
    _hGap = horizontalGap;
    _vGap = verticalGap;
    _rowNum = rowNumber;
    _columnNum = columnNumber;

    updateDimensions();

    f = createFont("Arial", 38);
    f2 = createFont("Arial", 28);
    textAlign(CENTER);

    imageMode(CENTER);
    img = loadImage("nube.png");
    img.resize(_height, _height);
  }

  void drawLuz(float nuevoporcentajeLuz) {
    porcentajeLuz = nuevoporcentajeLuz;
 
    updateDimensions();
    

    pushMatrix();
    translate(_width/2 + _posX + -160, _height/2 + -60 + _posY);
    rotate(frameCount / 400.0);
    star(0, 0, 110, 130, 60);
    popMatrix();

    //IMAGE
    image(img, _width / 2 + _posX, _height / 2 + _posY);

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
    text("Porcentaje de Luz: " + round(porcentajeLuz) + "%", _width/2 + _posX, _height/2 + 160 + _posY);
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

  void star(float x, float y, float radius1, float radius2, int npoints) {
    float angle = TWO_PI / npoints;
    float halfAngle = angle / 2.0;
    
    float r, g, b;

    // Asignar color según el porcentaje de luz
    // Fórmula considerando que el porcentaje de luz oscila entre 0 a 100
    r = 155 * porcentajeLuz / 100 + 100;
    g = 155 * porcentajeLuz / 100 + 100;
    b = 0;
    
    fill(constrain(r, 0, 255), constrain(g, 0, 255), b); // Asegura que los valores estén entre 0 y 255
    
    beginShape();
    for (float a = 0; a < TWO_PI; a += angle) {
      float sx = x + cos(a) * radius2;
      float sy = y + sin(a) * radius2;
      vertex(sx, sy);
      sx = x + cos(a + halfAngle) * radius1;
      sy = y + sin(a + halfAngle) * radius1;
      vertex(sx, sy);
    }
    endShape(CLOSE);
  }
}
