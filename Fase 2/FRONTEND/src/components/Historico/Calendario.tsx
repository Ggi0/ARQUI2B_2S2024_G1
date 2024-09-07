import React, { useState } from "react";
import { Calendar } from 'primereact/calendar';

export const Calendario = () => {
  const [datetime24h, setDateTime24h] = useState(null);

  return (
    <>
    <div className="card flex flex-wrap gap-3 p-fluid">
        <div className="flex-auto">
            <label htmlFor="calendar-12h" className="font-bold block mb-2">
                Desde
            </label>
            <Calendar value={datetime24h} onChange={(e) => setDateTime24h(e.value)} showTime hourFormat="24"  showIcon  />
        </div>
        <div className="flex-auto">
            <label htmlFor="calendar-12h" className="font-bold block mb-2">
                Hasta
            </label>
            <Calendar value={datetime24h} onChange={(e) => setDateTime24h(e.value)} showTime hourFormat="24" showIcon   />
        </div>

    </div>

    </>
  )
}

