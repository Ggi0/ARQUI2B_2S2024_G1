import React from 'react'
import '../../styles/TablaFuturista.css'; // Importar los estilos

export const TabIntegrantes = () => {
  const miembros = [
    { nombre: 'Santiago Julián Barrera Reyes', rol: '201905584' },
    { nombre: 'Evelio Marcos Jousué Cruz Solíz', rol: '202010040' },
    { nombre: 'Elías Abraham Vasquez Soto', rol: '201900131' },
    { nombre: 'Giovanni Saul Concohá Cax', rol: '202100229' },
    { nombre: 'Jemima Solmaira Chavajay Quiejú', rol: '201801521' }
  ];

  return (
    <div className="tabla-futurista-container">
      <table className="tabla-futurista">
        <thead>
          <tr>
            <th>Nombre</th>
            <th>Carne</th>
          </tr>
        </thead>
        <tbody>
          {miembros.map((miembro, index) => (
            <tr key={index}>
              <td>{miembro.nombre}</td>
              <td>{miembro.rol}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};