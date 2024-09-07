import React, { useMemo } from 'react';
import ReactECharts from 'echarts-for-react';

export const GraficaProximidad = ({ data }) => {
    const option = useMemo(() => {
        if (!data) return null;

        const countries = ['dist-collection'];
        const datasetWithFilters = [];
        const seriesList = [];

        countries.forEach(coleccion => {
            const datasetId = 'dataset_' + coleccion;
            datasetWithFilters.push({
                id: datasetId,
                fromDatasetId: 'dataset_raw',
                transform: {
                //    type: 'filter',
                    config: {
                        and: [
                            { dimension: 'sensor' /*  */, gte: 1 }, // Aqui van los filtros
                            { dimension: 'coleccion', '=': coleccion }
                        ]
                    }
                }
            });

            seriesList.push({
                type: 'line',
                datasetId: datasetId,
                showSymbol: false,
                name: coleccion,
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
                    x: 'timestamp',
                    y: 'sensor',
                    label: ['coleccion', 'sensor'],
                    itemName: 'timestamp',
                    tooltip: ['sensor']
                }
            });
        });

        return {
            animationDuration: 10000,
            dataset: [
                {
                    id: 'dataset_raw',
                    source: data
                },
                ...datasetWithFilters
            ],
            title: {
                text: 'sensor of Selected Countries since 1950'
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
                name: 'sensor'
            },
            grid: {
                right: 140
            },
            series: seriesList
        };
    }, [data]);

    return option ? <ReactECharts option={option} style={{ height: 400 }} /> : <p>No data available</p>;
};