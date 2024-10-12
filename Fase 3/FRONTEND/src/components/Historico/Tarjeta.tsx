import React from 'react';
import { Card } from 'primereact/card';
        
// children es palabra reservada para que el componente pueda tener hijos dentro
export const Tajeta = ({titulo, delay, children}) => {
  return (
    <div className={`fadeindown m-1 animation-ease-in hover:shadow-8 animation-duration-${delay}`} >
      <Card title={titulo}>
        {children}
      </Card>
    </div>
  )
}
