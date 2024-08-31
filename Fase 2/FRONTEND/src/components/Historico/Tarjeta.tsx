import React from 'react';
import { Card } from 'primereact/card';
        
// children es palabra reservada para que el componente pueda tener hijos dentro
export const Tajeta = ({titulo, children}) => {
  return (
    <Card title={titulo}> 
      {children}
    </Card>
  )
}
