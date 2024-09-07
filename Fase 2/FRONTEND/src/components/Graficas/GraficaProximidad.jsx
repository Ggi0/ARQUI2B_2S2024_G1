import React, { useEffect, useState } from 'react';
import ReactECharts from 'echarts-for-react';

export const GraficaProximidad = () => {
    const [option, setOption] = useState(null);

    useEffect(() => {
        fetch('/data/asset/data/sensor-data.json')
            .then(response => response.json())
            .then(data => {
                // Convertir el JSON y filtrar solo "co2-collection"
                const filteredData = data
                    .slice(1) // Eliminar el encabezado
                    .filter(item => item[1] === 'co2-collection' && item[2].substr(0, 10) == "06/09/2024" ) // Filtrar solo "co2-collection"
                    .map(item => ({
                        sensor: item[0],
                        timestamp: item[2]
                    }));

                setOption({
                    title: {
                        text: 'CO2 Levels Over Time (co2-collection)'
                    },
                    tooltip: {
                        trigger: 'axis',
                        formatter: params => {
                            const data = params[0].data;
                            return `Timestamp: ${data.timestamp}<br/>CO2 Level: ${data.value}`;
                        }
                    },
                    xAxis: {
                        type: 'category',
                        name: 'Timestamp',
                        data: filteredData.map(item => item.timestamp),
                        nameLocation: 'middle',
                        nameGap: 30
                    },
                    yAxis: {
                        type: 'value',
                        name: 'CO2 Level'
                    },
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
                                width: 2
                            }
                        }
                    ]
                });
            })
            .catch(error => console.error('Error loading data:', error));
    }, []);

    return option ? <ReactECharts option={option} style={{ height: 400 }} /> : <p>Loading...</p>;
};
