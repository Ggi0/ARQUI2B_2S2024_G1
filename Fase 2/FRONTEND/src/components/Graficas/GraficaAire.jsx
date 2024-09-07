import React, { useEffect, useState } from 'react';
import ReactECharts from 'echarts-for-react';
import * as echarts from 'echarts'; // Importación directa de echarts

export const GraficaAire = () => {
    const [option, setOption] = useState(null);

    useEffect(() => {
        fetch('/data/asset/data/sensor-data.json')
            .then(response => response.json())
            .then(data => {
                // Filtrar solo los datos de "co2-collection"
                const filteredData = data
                    .slice(1) // Eliminar el encabezado
                    .filter(item => item[1] === 'co2-collection'); // Filtrar solo "co2-collection"

                // Extraer fechas y valores
                const date = filteredData.map(item => item[2]); // Array de fechas
                const co2Values = filteredData.map(item => item[0]); // Array de valores de CO2

                // Configuración de la gráfica
                const newOption = {
                    tooltip: {
                        trigger: 'axis',
                        position: function (pt) {
                            return [pt[0], '10%'];
                        }
                    },
                    title: {
                        left: 'center',
                        text: 'CO2 Levels Over Time'
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
                        data: date // Utilizar las fechas extraídas
                    },
                    yAxis: {
                        type: 'value',
                        boundaryGap: [0, '100%']
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
                            name: 'CO2 Levels',
                            type: 'line',
                            symbol: 'none',
                            sampling: 'lttb',
                            itemStyle: {
                                color: 'rgb(255, 70, 131)'
                            },
                            areaStyle: {
                                color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                                    {
                                        offset: 0,
                                        color: 'rgb(255, 158, 68)'
                                    },
                                    {
                                        offset: 1,
                                        color: 'rgb(255, 70, 131)'
                                    }
                                ])
                            },
                            data: co2Values // Utilizar los valores de CO2 extraídos
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
