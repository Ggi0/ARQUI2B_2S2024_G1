import React, { useState } from 'react';
import { Tajeta } from './Tarjeta';
import {GraficaProximidad} from '../Graficas/GraficaProximidad';
import { GraficaAire } from '../Graficas/GraficaAire';
import { GraficaLuz } from '../Graficas/GraficaLuz';
import { GraficaTempAndHum } from '../Graficas/GraficaTempAndHum';
import { TarjetaDetalle } from './TarjetaDetalle';
import { Calendario } from './Calendario';
import '../../styles/img.css';
import DataJSON from '../../../public/data/asset/data/sensor-data.json';

const ImgAire        = '/data/asset/img/Aire.png';
const ImgCalendar    = '/data/asset/img/calendar.png';
const ImgLuz         = '/data/asset/img/Luz.png';
const ImgTemperatura = '/data/asset/img/Temperatura.png';
const ImgProximidad  = '/data/asset/img/proximidad.png';


export const Historico = () => {
  // Estados para manejar la visibilidad de los modales
  const [visibleProximidad, setvisibleProximidad]   = useState(false);
  const [visibleTemperatura, setvisibleTemperatura] = useState(false);
  const [visibleLuz, setvisibleLuz]                 = useState(false);
  const [visibleAire, setvisibleAire]               = useState(false);
  
  return (
    <>
    {/* Tarjetas con sus iconos, para desplegar cada uno de los modales */}
      <div className="grid">
        <div className="col" onClick={() => setvisibleTemperatura(true)}>
          <Tajeta titulo='Temperatura y humedad' delay={300}>
            <div className="flex-container">
              <img 
                src={ImgTemperatura} 
                alt="Icono de Proximidad" 
                style={{ width: '150px', height: '150px' }} 
              />
            </div>
          </Tajeta>
        </div>
      </div>
      <div className="grid">
        <div className="col" onClick={() => setvisibleProximidad(true)}>
          <Tajeta titulo='Proximidad'delay={200}>
            <div className="flex-container">
              <img 
                src={ImgProximidad} 
                alt="Icono de Proximidad" 
                style={{ width: '150px', height: '150px' }} 
              />
            </div>
          </Tajeta>
        </div>
        <div className="col" onClick={() => setvisibleLuz(true)}>
          <Tajeta titulo='Luz' delay={400}>
            <div className="flex-container">
              <img 
                src={ImgLuz} 
                alt="Icono de Proximidad" 
                style={{ width: '150px', height: '150px' }} 
              />
            </div>
          </Tajeta>
        </div>
        <div className="col" onClick={() => setvisibleAire(true)}>
          <Tajeta titulo='Aire' delay={500}>
            <div className="flex-container">
              <img 
                src={ImgAire} 
                alt="Icono de Proximidad" 
                style={{ width: '150px', height: '150px' }} 
              />
            </div>
          </Tajeta>
        </div>
      </div>

      {/* Modales de cada una de las tarjetas */}
      <TarjetaDetalle titulo="Proximidad" visible={visibleProximidad} setVisible={setvisibleProximidad} >
        <GraficaProximidad data = {DataJSON}/>
      </TarjetaDetalle>
      <TarjetaDetalle titulo="Temperatura y humedad" visible={visibleTemperatura} setVisible={setvisibleTemperatura} >
        <GraficaTempAndHum data = {DataJSON}/>
      </TarjetaDetalle>
      <TarjetaDetalle titulo="Luz" visible={visibleLuz} setVisible={setvisibleLuz} >
        <GraficaLuz data = {DataJSON}/>
      </TarjetaDetalle>
      <TarjetaDetalle titulo="Aire" visible={visibleAire} setVisible={setvisibleAire} >
        <GraficaAire data = {DataJSON}/>
      </TarjetaDetalle>

    </>
  )
}
