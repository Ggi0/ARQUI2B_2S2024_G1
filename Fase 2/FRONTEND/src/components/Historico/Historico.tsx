import React from 'react';
import { Tajeta } from './Tarjeta';
import { GraficaLineas } from '../Graficas/GraficaLineas';
import {GraficaProximidad} from '../Graficas/GraficaProximidad';

export const Historico = () => {
  return (
    <>
      <div className="grid">
        <div className="col">
          <Tajeta titulo='Calendarios' delay={100}>
            <p>Calendarios</p>
          </Tajeta>
        </div>
        <div className="col">
          <Tajeta titulo='Proximidad'delay={200}>
            <p></p>
          </Tajeta>
        </div>
      </div>
      
      <div className="grid">
        <div className="col">
          <Tajeta titulo='Temperatura y humedad' delay={300}>
            <GraficaProximidad/>
          </Tajeta>
        </div>
        <div className="col">
          <Tajeta titulo='Luz' delay={400}>
            <p>Luz</p>
          </Tajeta>
        </div>
        <div className="col">
          <Tajeta titulo='Aire' delay={500}>
            <p>Aire</p>
          </Tajeta>
        </div>
      </div>
    </>
  )
}
