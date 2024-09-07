import React, { useEffect, useState } from 'react';
import ReactECharts from 'echarts-for-react';
import * as echarts from 'echarts'; // Importación directa de echarts

export const GraficaLuz = () => {
    const [option, setOption] = useState(null);

    useEffect(() => {
        fetch('/data/asset/data/sensor-data.json')
            .then(response => response.json())
            .then(data => {
                // Filtrar solo los datos de "co2-collection"
                const filteredData = data.slice(1) // Eliminar el encabezado
                    .filter(item => item[1] === 'co2-collection'); // Filtrar solo "co2-collection"

                // Extraer fechas únicas para el eje X
                const uniqueDates = [...new Set(filteredData.map(item => item[2]))];

                // Crear una serie de datos para el sensor de CO2
                const co2SeriesData = filteredData.map(item => item[0]); // Asignar todos los valores del sensor de CO2

                // Configuración de la gráfica
                const newOption = {
                    title: {
                        text: 'Stacked Area Chart - CO2 Levels'
                    },
                    tooltip: {
                        trigger: 'axis',
                        axisPointer: {
                            type: 'cross',
                            label: {
                                backgroundColor: '#6a7985'
                            }
                        }
                    },
                    legend: {
                        data: ['CO2 Levels']
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
                    grid: {
                        left: '3%',
                        right: '4%',
                        bottom: '3%',
                        containLabel: true
                    },
                    xAxis: [
                        {
                            type: 'category',
                            boundaryGap: false,
                            data: uniqueDates // Usar todas las fechas únicas como eje X
                        }
                    ],
                    yAxis: [
                        {
                            type: 'value',
                            boundaryGap: [0, '100%']
                        }
                    ],
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
                            name: 'CO2 Levels',
                            type: 'line',
                            stack: 'Total',
                            emphasis: {
                                focus: 'series'
                            },
                            symbol: 'none',
                            sampling: 'lttb',
                            itemStyle: {
                                color: 'rgb(255, 105, 180)' // Color de línea en rosado
                            },
                            areaStyle: {
                                color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                                    {
                                        offset: 0,
                                        color: 'rgb(255, 182, 193)' // Color inicial rosado claro
                                    },
                                    {
                                        offset: 1,
                                        color: 'rgb(255, 140, 0)' // Color final anaranjado
                                    }
                                ])
                            },
                            data: co2SeriesData // Usar los datos del sensor de CO2
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
