import React from 'react';
import useStore from '../store';

import { PrimeReactProvider, PrimeReactContext } from 'primereact/api';
import "primereact/resources/themes/lara-light-cyan/theme.css";
import 'primeflex/primeflex.css'

import'../styles/container.css';
import {Historico} from './Historico/Historico';
import {Actual} from './Actual/Actual';
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
      default:
        return(<TabIntegrantes/>);     
    }
  }
  //Lo pone dentro de un contenedor con layout definido
  return (
    <>
      <div className="contenedor">
        <h1>ARQUITECTURA DE COMPUTADORES Y ENSAMBLADORES 2</h1>
        <ComponenteActual />
      </div>
    </>
  )
}