import React from 'react';
import { Card } from 'primereact/card';
        
// children es palabra reservada para que el componente pueda tener hijos dentro
export const Tajeta = ({titulo, delay, children}) => {
  return (
    <div className={`fadeindown animation-duration-${delay}`}>
      <Card title={titulo}>
        {children}
      </Card>
    </div>
  )
}
