import React, { useEffect, useState } from 'react';
import ReactECharts from 'echarts-for-react';
import * as echarts from 'echarts'; // Importación directa de echarts

export const GraficaTempAndHum = ({ data }) => {
    const [option, setOption] = useState(null);

    useEffect(() => {
        if (data) {
            // Filtrar los datos para cada tipo de colección
            const tempData = data.slice(1).filter(item => item[1] === 'temp-collection'); // Filtrar "temp-collection"
            const humData = data.slice(1).filter(item => item[1] === 'hum-collection'); // Filtrar "hum-collection"

            // Extraer fechas únicas para el eje X
            const uniqueDates = [...new Set(tempData.map(item => item[2]))];

            // Extraer valores para cada serie
            const tempValues = tempData.map(item => item[0]); // Valores de temperatura
            const humValues = humData.map(item => item[0]);   // Valores de humedad

            // Configuración de la gráfica
            const newOption = {
                tooltip: {
                    trigger: 'axis',
                    axisPointer: {
                        type: 'cross',
                        crossStyle: {
                            color: '#999'
                        }
                    }
                },
                toolbox: {
                    feature: {
                        dataView: { show: true, readOnly: false },
                        magicType: { show: true, type: ['line', 'bar'] },
                        restore: { show: true },
                        saveAsImage: { show: true }
                    }
                },
                legend: {
                    data: ['Temperature', 'Humidity']
                },
                xAxis: [
                    {
                        type: 'category',
                        data: uniqueDates, // Usar las fechas únicas del JSON
                        axisPointer: {
                            type: 'shadow'
                        }
                    }
                ],
                yAxis: [
                    {
                        type: 'value',
                        name: 'Temperature (°C)',
                        min: 0,
                        max: 40, // Ajustar según los datos de temperatura
                        interval: 5,
                        axisLabel: {
                            formatter: '{value} °C'
                        }
                    },
                    {
                        type: 'value',
                        name: 'Humidity (%)',
                        min: 0,
                        max: 100, // Ajustar según los datos de humedad
                        interval: 10,
                        axisLabel: {
                            formatter: '{value} %'
                        }
                    }
                ],
                dataZoom: [
                    {
                        type: 'inside',
                        start: 0,
                        end: 100
                    },
                    {
                        start: 0,
                        end: 100
                    }
                ],
                series: [
                    {
                        name: 'Temperature',
                        type: 'bar',
                        yAxisIndex: 0,
                        itemStyle: {
                            color: new echarts.graphic.LinearGradient(
                                0, 0, 0, 1,
                                [
                                    { offset: 0, color: '#005187' }, // Amarillo
                                    { offset: 1, color: '#84B6F4' }  // Naranja
                                ]
                            )
                        },
                        tooltip: {
                            valueFormatter: function (value) {
                                return value + ' °C';
                            }
                        },
                        data: tempValues // Utilizar los valores de temperatura extraídos del JSON
                    },
                    {
                        name: 'Humidity',
                        type: 'bar',
                        yAxisIndex: 1,
                        itemStyle: {
                            color: new echarts.graphic.LinearGradient(
                                0, 0, 0, 1,
                                [
                                    { offset: 0, color: '#FFE135' }, // Amarillo más claro
                                    { offset: 1, color: '#FE2020' }  // Naranja más oscuro
                                ]
                            )
                        },
                        tooltip: {
                            valueFormatter: function (value) {
                                return value + ' %';
                            }
                        },
                        data: humValues // Utilizar los valores de humedad extraídos del JSON
                    }
                ]
            };

            // Establecer la configuración en el estado
            setOption(newOption);
        }
    }, [data]); // Se ejecuta cada vez que cambie el prop data

    return option ? <ReactECharts option={option} style={{ height: 400 }} /> : <p>Cargando...</p>;
};
