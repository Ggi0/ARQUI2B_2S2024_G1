import React, { useState } from 'react';
import ReactApexChart from 'react-apexcharts';

export const GraficaLineas = ({labels, ArrayData}) => {
  const [chartData, setChartData] = useState({
      series: [{
        name: "Cantidad",
        data: ArrayData
      }],
      options: {
        chart: {
          height: 350,
          type: 'line',
          zoom: {
            enabled: false
          }
        },
        dataLabels: {
          enabled: false
        },
        stroke: {
          curve: 'straight'
        },
        xaxis: {
          categories: labels,
          tickAmount : 10,
          labels: {
            rotate: -45,
          }
        }
      }
    });

return (
  <div id="chart">
    <ReactApexChart options={chartData.options} series={chartData.series} type="line" height={400} />
  </div>
)
}