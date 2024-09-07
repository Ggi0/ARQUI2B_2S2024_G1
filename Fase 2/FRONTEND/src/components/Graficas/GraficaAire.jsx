import React, { useEffect, useState } from 'react';
import ReactECharts from 'echarts-for-react';

export const GraficaAire = () => {
    const [option, setOption] = useState(null);

    useEffect(() => {
        fetch('/data/asset/data/sensor-data.json')
            .then(response => response.json())
            .then(data => {
                // Filtrar solo los datos de "co2-collection"
                const filteredData = data
                    .slice(1) // Eliminar el encabezado
                    .filter(item => item[1] === 'co2-collection') // Filtrar solo "co2-collection"
                    .map(item => [item[2], item[0]]); // Mapeo de datos [timestamp, sensor]

                // Configuración de la gráfica
                const newOption = {
                    xAxis: {
                        type: 'category',
                        boundaryGap: false,
                        data: filteredData.map(item => item[0]) // Asignar los timestamps al eje X
                    },
                    yAxis: {
                        type: 'value',
                        boundaryGap: [0, '30%']
                    },
                    visualMap: {
                        type: 'piecewise',
                        show: false,
                        dimension: 0,
                        seriesIndex: 0,
                        pieces: [
                            {
                                gt: 1,
                                lt: 3,
                                color: 'rgba(0, 0, 180, 0.4)'
                            },
                            {
                                gt: 5,
                                lt: 7,
                                color: 'rgba(0, 0, 180, 0.4)'
                            }
                        ]
                    },
                    series: [
                        {
                            type: 'line',
                            smooth: 0.6,
                            symbol: 'none',
                            lineStyle: {
                                color: '#5470C6',
                                width: 5
                            },
                            markLine: {
                                symbol: ['none', 'none'],
                                label: { show: false },
                                data: [{ xAxis: 1 }, { xAxis: 3 }, { xAxis: 5 }, { xAxis: 7 }]
                            },
                            areaStyle: {},
                            data: filteredData // Utilizar los datos filtrados para la gráfica
                        }
                    ]
                };

                // Establecer la configuración en el estado
                setOption(newOption);
            })
            .catch(error => console.error('Error loading data:', error));
    }, []);

    return option ? <ReactECharts option={option} style={{ height: 400 }} /> : <p>Loading...</p>;
};
