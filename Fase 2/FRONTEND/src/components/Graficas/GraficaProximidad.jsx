import React, { useEffect, useState } from 'react';
import ReactECharts from 'echarts-for-react';
import * as echarts from 'echarts'; // Importación directa de echarts

export const GraficaProximidad = () => {
    const [option, setOption] = useState(null);

    useEffect(() => {
        fetch('/data/asset/data/sensor-data.json')
            .then(response => response.json())
            .then(data => {
                // Filtrar solo los datos de "dist-collection" y la fecha "06/09/2024"
                const filteredData = data
                    .slice(1) // Eliminar el encabezado
                    .filter(item => item[1] === 'dist-collection' && item[2].substr(0, 10) === "06/09/2024") // Filtrar solo "dist-collection" de la fecha específica
                    .map(item => ({
                        sensor: item[0],
                        timestamp: item[2]
                    }));

                // Configuración de la gráfica con dataZoom
                const newOption = {
                    title: {
                        text: 'TCRT5000 Levels Over Time (dist-collection)'
                    },
                    tooltip: {
                        trigger: 'axis',
                        formatter: params => {
                            const data = params[0].data;
                            return `Timestamp: ${data.timestamp}<br/>INFRA ROJO Level: ${data.value}`;
                        }
                    },
                    toolbox: {
                        feature: {
                            dataZoom: {
                                yAxisIndex: 'none'
                            },
                            restore: {},
                            saveAsImage: {}
                        }
                    },
                    xAxis: {
                        type: 'category',
                        boundaryGap: false,
                        data: filteredData.map(item => item.timestamp),
                        name: 'Timestamp',
                        nameLocation: 'middle',
                        nameGap: 30
                    },
                    yAxis: {
                        type: 'value',
                        name: 'INFRA ROJO Level'
                    },
                    dataZoom: [
                        {
                            type: 'inside',
                            start: 0,
                            end: 10
                        },
                        {
                            start: 0,
                            end: 10
                        }
                    ],
                    series: [
                        {
                            type: 'line',
                            data: filteredData.map(item => ({
                                value: item.sensor,
                                timestamp: item.timestamp
                            })),
                            showSymbol: true,
                            emphasis: {
                                focus: 'series'
                            },
                            lineStyle: {
                                width: 2,
                                color: 'darkgray' // Línea de color gris oscuro
                            },
                            areaStyle: {
                                color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                                    {
                                        offset: 0,
                                        color: 'lightgreen' // Verde claro en la parte superior
                                    },
                                    {
                                        offset: 1,
                                        color: 'darkgray' // Gris oscuro en la parte inferior
                                    }
                                ])
                            }
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
