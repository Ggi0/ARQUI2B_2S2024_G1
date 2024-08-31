import React from 'react';
import useStore from '../store';

import { PrimeReactProvider, PrimeReactContext } from 'primereact/api';
import "primereact/resources/themes/lara-light-cyan/theme.css";
import 'primeflex/primeflex.css'

import'../styles/container.css';
import {Historico} from './Historico/Historico';
import {Actual} from './Actual/Actual';
import {Mas} from './Mas/Mas';

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
        return(<Mas/>);     
    }
  }
  //Lo pone dentro de un contenedor con layout definido
  return (
    <>
      <div className="contenedor">
        <h2>Hola Julian, si ves esto y le quieres meter mano para agregrle las gráficas</h2>
        <p>Estan en la ruta src/components hay tres carpetas, cada una con un archivo principal que es donde se renderiza el 
          componente, en el caso del histórico, se renderiza en un sistema de filas y columnas, ya te deje puesto donde 
          tenes que cabiarlo si queres meter las grafiicas :)
        </p>
        <ComponenteActual />
      </div>
    </>
  )
}