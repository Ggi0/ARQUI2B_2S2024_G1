import React, { useEffect, useState } from 'react';
import ReactECharts from 'echarts-for-react';
import * as echarts from 'echarts'; // Importación directa de echarts

export const GraficaLuz = ({data}) => {
    const [option, setOption] = useState(null);

    useEffect(() => {
        if(data) {
                // Filtrar solo los datos de "co2-collection"
                const filteredData = data.slice(1) // Eliminar el encabezado
                    .filter(item => item[1] === 'luz-collection'); // Filtrar solo "co2-collection"

                // Extraer fechas únicas para el eje X
                const uniqueDates = [...new Set(filteredData.map(item => item[2]))];

                // Crear una serie de datos para el sensor de Luz
            const co2SeriesData = filteredData.map(item => {
                    let valorSensorLuz = item[0];
                    if (valorSensorLuz > 1023) {
                        valorSensorLuz = 1023;
                    }
                    valorSensorLuz = 1023 - valorSensorLuz;
                    return valorSensorLuz / 1023 * 100;
                ;}); // Asignar todos los valores del sensor de Luz

                // Configuración de la gráfica
                const newOption = {
                    title: {
                    text: 'Light Levels Over Time (lum/m2)'
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
                        data: ['Light Levels']
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
                            name: 'Light Levels',
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
            }
    }, [data]);

    return option ? <ReactECharts option={option} style={{ height: 400 }} /> : <p>Loading...</p>;
};
