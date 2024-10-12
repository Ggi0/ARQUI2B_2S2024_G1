import React from 'react';
import useStore from '../store';

import { PrimeReactProvider, PrimeReactContext } from 'primereact/api';
import "primereact/resources/themes/lara-light-cyan/theme.css";
import 'primeflex/primeflex.css'
import { TypeAnimation } from 'react-type-animation';

import'../styles/container.css';
import {Historico} from './Historico/Historico';
import {Actual} from './Actual/Actual';
import { Prediccion } from './Prediccion/Prediccion';
import {TabIntegrantes} from './Mas/TabIntegrantes';

export const Contenedor = () => {
  // Toma el estado de zustan y controla que componente renderizar.
  const activeComponent = useStore((state) => state.activeComponent);
  const ComponenteActual = () => {
    switch (activeComponent){
      case "Historico":
        return(<Historico/>);
      case "Actual":
        return(<Actual/>);
      case "Prediccion":
        return(<Prediccion/>);
      default:
        return(<TabIntegrantes/>);     
    }
  }
  //Lo pone dentro de un contenedor con layout definido
  return (
    <>
      <div className="contenedor">
        <h1>
        <TypeAnimation
          sequence={[
            // Same substring at the start will only be typed once, initially
            'Arquitectura de computadores y ensambladores 2, Proyecto Unico',
            1000,
            'Arquitectura de computadores y ensambladores 2, Control de acceso vehicular',
            1000,
            'Arquitectura de computadores y ensambladores 2, Fase 2',
            1000,
            'Arquitectura de computadores y ensambladores 2, Fase 2: Ahora es personal',
            1000,
          ]}
          speed={50}
          style={{ fontSize: '1em' }}
          repeat={Infinity}
        />
        </h1>
        <ComponenteActual />
      </div>
    </>
  )
}