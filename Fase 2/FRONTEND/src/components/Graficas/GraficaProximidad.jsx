// Graficas.jsx
import React, { useEffect, useState } from 'react';
import ReactECharts from 'echarts-for-react';

export const GraficaProximidad = () => {
    const [option, setOption] = useState(null);

    useEffect(() => {
        fetch('/data/asset/data/life-expectancy-table.json')
            .then(response => response.json())
            .then(data => {
                const countries = ['Finland', 'France', 'Germany', 'Iceland', 'Norway', 'Poland', 'Russia', 'United Kingdom'];
                const datasetWithFilters = [];
                const seriesList = [];

                countries.forEach(country => {
                    const datasetId = 'dataset_' + country;
                    datasetWithFilters.push({
                        id: datasetId,
                        fromDatasetId: 'dataset_raw',
                        transform: {
                            type: 'filter',
                            config: {
                                and: [
                                    { dimension: 'Year', gte: 1950 },
                                    { dimension: 'Country', '=': country }
                                ]
                            }
                        }
                    });

                    seriesList.push({
                        type: 'line',
                        datasetId: datasetId,
                        showSymbol: false,
                        name: country,
                        endLabel: {
                            show: true,
                            formatter: params => `${params.value[3]}: ${params.value[0]}`
                        },
                        labelLayout: {
                            moveOverlap: 'shiftY'
                        },
                        emphasis: {
                            focus: 'series'
                        },
                        encode: {
                            x: 'Year',
                            y: 'Income',
                            label: ['Country', 'Income'],
                            itemName: 'Year',
                            tooltip: ['Income']
                        }
                    });
                });

                setOption({
                    animationDuration: 10000,
                    dataset: [
                        {
                            id: 'dataset_raw',
                            source: data
                        },
                        ...datasetWithFilters
                    ],
                    title: {
                        text: 'Income of Selected Countries since 1950'
                    },
                    tooltip: {
                        order: 'valueDesc',
                        trigger: 'axis'
                    },
                    xAxis: {
                        type: 'category',
                        nameLocation: 'middle'
                    },
                    yAxis: {
                        name: 'Income'
                    },
                    grid: {
                        right: 140
                    },
                    series: seriesList
                });
            })
            .catch(error => console.error('Error loading data:', error));
    }, []);

    return option ? <ReactECharts option={option} style={{ height: 400 }} /> : <p>Loading...</p>;
};
