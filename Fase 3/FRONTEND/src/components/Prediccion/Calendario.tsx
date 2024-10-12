import React, { useState } from "react";
import { Calendar } from 'primereact/calendar';

export const Calendario = ({datetime24h, setDateTime24h}) => {
  // Validacion de que solo se pueda seleccionar como maximo 8 dias despues
  let hoy = new Date();
  let diasdespues = new Date();
  diasdespues.setDate(hoy.getDate() + 8);

  return (
    <>
    <div className="card flex flex-wrap gap-3 p-fluid">
        <div className="flex-auto">
            <Calendar value={datetime24h}
                      onChange={(e) => setDateTime24h(e.value)}
                      minDate={hoy} 
                      maxDate={diasdespues}
                      showTime 
                      hourFormat="24" 
                      showIcon  />
        </div>
    </div>

    </>
  )
}

