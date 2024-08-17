class Humo {

  float porcentajeHumo = 0;
  PFont f, f2;
  int _width, _height, _posX, _posY;
  int _heightTitle, _hGap, _vGap, _rowNum, _columnNum;

  float s = 0.0;
  boolean increasing = true;
  int waitTime = 50; // Tiempo de espera entre cambios de color
  
  PanelSensor panel;
  int lastChangeTime = 0;
  int changeDuration = 2000; // 2000 milisegundos = 2 segundos
  int valorReferencia = 200; // Valor maximo de referencia

  Humo(int heightTitle, int horizontalGap, int verticalGap, int rowNumber, int columnNumber) {
    _heightTitle = heightTitle;
    _hGap = horizontalGap;
    _vGap = verticalGap;
    _rowNum = rowNumber;
    _columnNum = columnNumber;

    updateDimensions();

    f = createFont("Arial", 35);
    f2 = createFont("Arial", 23);
    textAlign(CENTER);
    
    createNewPanel();
  }

  void drawHumo(float nuevoPorcentajeHumo) {
    porcentajeHumo = nuevoPorcentajeHumo;
 
    updateDimensions();
    
    // Verificar si han pasado 2 segundos
    if (millis() - lastChangeTime > changeDuration) {
      createNewPanel();
      lastChangeTime = millis();
    }
    
    // Actualizar y mostrar el panel
    panel.update();
    panel.display();
    
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
    text("Porcentaje de CO2: " + round(porcentajeHumo) + "%", _width/2 + _posX, _height/2 + 160 + _posY);
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
  
  void createNewPanel() {
    int porcentaje = Math.round(porcentajeHumo);
    panel = new PanelSensor(_posX, _posY, _width, _height, 5, porcentaje);
  }
  
}
