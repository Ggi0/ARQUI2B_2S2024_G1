import React, { useState } from 'react';
import { Tajeta } from './Tarjeta';
import { GraficaLineas } from '../Graficas/GraficaLineas';
import {GraficaProximidad} from '../Graficas/GraficaProximidad';
import { TarjetaDetalle } from './TarjetaDetalle';

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
        <div className="col">
          <Tajeta titulo='Calendarios' delay={150}>
            <p>Calendarios</p>
          </Tajeta>
        </div>
        <div className="col" onClick={() => setvisibleProximidad(true)}>
          <Tajeta titulo='Proximidad'delay={200}>
            <p></p>
          </Tajeta>
        </div>
      </div>
      <div className="grid">
        <div className="col" onClick={() => setvisibleTemperatura(true)}>
          <Tajeta titulo='Temperatura y humedad' delay={300}>
            <p></p>
          </Tajeta>
        </div>
        <div className="col" onClick={() => setvisibleLuz(true)}>
          <Tajeta titulo='Luz' delay={400}>
            <p>Luz</p>
          </Tajeta>
        </div>
        <div className="col" onClick={() => setvisibleAire(true)}>
          <Tajeta titulo='Aire' delay={500}>
            <p>Aire</p>
          </Tajeta>
        </div>
      </div>

      {/* Modales de cada una de las tarjetas */}
      <TarjetaDetalle titulo="Proximidad" visible={visibleProximidad} setVisible={setvisibleProximidad} >
        <GraficaProximidad/>
      </TarjetaDetalle>
      <TarjetaDetalle titulo="Temperatura y humedad" visible={visibleTemperatura} setVisible={setvisibleTemperatura} >
        <p> Aqui va la grafica de Temperatura y humedad</p>
      </TarjetaDetalle>
      <TarjetaDetalle titulo="Luz" visible={visibleLuz} setVisible={setvisibleLuz} >
        <p> Aqui va la grafica de Luz</p>
      </TarjetaDetalle>
      <TarjetaDetalle titulo="Aire" visible={visibleAire} setVisible={setvisibleAire} >
        <p> Aqui va la grafica de Aire</p>
      </TarjetaDetalle>

    </>
  )
}
