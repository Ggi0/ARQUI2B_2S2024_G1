import React from 'react';
import { Tajeta } from './Tarjeta';
export const Historico = () => {
  return (
    <>
      <div className="grid">
        <div className="col">
          <Tajeta titulo='Calendarios'>
            <p>Calendarios</p>
          </Tajeta>
        </div>
        <div className="col">
          <Tajeta titulo='Proximidad'>
            <p>Proximidad</p>
          </Tajeta>
        </div>
      </div>
      
      <div className="grid">
        <div className="col">
          <Tajeta titulo='Temperatura y humedad'>
            <p>Temperatura y humedad</p>
          </Tajeta>
        </div>
        <div className="col">
          <Tajeta titulo='Luz'>
            <p>Luz</p>
          </Tajeta>
        </div>
        <div className="col">
          <Tajeta titulo='Aire'>
            <p>Aire</p>
          </Tajeta>
        </div>
      </div>
    </>
  )
}
