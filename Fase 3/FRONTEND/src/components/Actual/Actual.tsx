import React, { useEffect, useState } from 'react';
import { Tajeta } from '../Historico/Tarjeta';
import '../../styles/img.css';
import { Client } from 'paho-mqtt';

const ImgAire = '/data/asset/img/Aire.png';
const ImgLuz = '/data/asset/img/Luz.png';
const ImgTemperatura = '/data/asset/img/Temperatura.png';
const ImgHumedad = '/data/asset/img/Temperatura.png';
const ImgProximidad = '/data/asset/img/proximidad.png';


export const Actual = () => {
    // Estados para guardar la data
    const [DataHumedad, setDataHumedad]         = useState(0);
    const [DataTemperatura, setDataTemperatura] = useState(0);
    const [DataDistancia, setDataDistancia]     = useState(0);
    const [DataLuz, setDataLuz]                 = useState(0);
    const [DataAire, setDataAire]               = useState(0);
 
    // Funcion de consulta al mqtt
    const ConsultaActual = () => {
      const client = new Client('broker.emqx.io', 8083, 'subscriber-client');
      // Cuando llega un mensaje
      client.onMessageArrived = (msg) => {
          const respuestaMQTT = JSON.parse(msg.payloadString)
          setDataHumedad(respuestaMQTT.humedad);
          setDataTemperatura(respuestaMQTT.temperatura);
          setDataDistancia(respuestaMQTT.distancia);
          setDataLuz(respuestaMQTT.luz);
          setDataAire(respuestaMQTT.aire);
      };
      // Cuando se conecta se mete en un loop
      client.connect({ onSuccess: () => {
          client.subscribe('arqui2_2s2024/topico_sensores');
      } });
      // Si no se conecta retorna
      return () => client.disconnect();
    }

    useEffect ( () => {
      ConsultaActual();
    }, [])

    return (
        <>
            {/* Tarjetas con sus iconos, para desplegar cada uno de los modales */}
          
            <div className="grid">
                <div className="col">
                    <Tajeta titulo='Humedad' delay={300}>
                        <div className="predict-flex-container">
                            <img
                                src={ImgHumedad}
                                alt="Icono de Proximidad"
                                className='predict-imagen-tarjeta'
                            />
                            <h1> Valor: {DataHumedad} </h1>
                        </div>
                    </Tajeta>
                </div>
                <div className="col">
                    <Tajeta titulo='Temperatura' delay={300}>
                        <div className="predict-flex-container">
                            <img
                                src={ImgTemperatura}
                                alt="Icono de Proximidad"
                                className='predict-imagen-tarjeta'
                            />
                            <h1> Valor: {DataTemperatura} </h1>
                        </div>
                    </Tajeta>
                </div>                
                <div className="col">
                    <Tajeta titulo='Proximidad' delay={200}>
                        <div className="predict-flex-container">
                            <img
                                src={ImgProximidad}
                                alt="Icono de Proximidad"
                                className='predict-imagen-tarjeta'
                            />
                            <h1> Valor: {DataDistancia} </h1>
                        </div>
                    </Tajeta>
                </div>
            </div>
            <div className="grid">
                <div className="col">
                    <Tajeta titulo='Luz' delay={400}>
                        <div className="predict-flex-container">
                            <img
                                src={ImgLuz}
                                alt="Icono de Proximidad"
                                className='predict-imagen-tarjeta'
                            />
                            <h1> Valor: {DataLuz} </h1>
                        </div>
                    </Tajeta>
                </div>
                <div className="col">
                    <Tajeta titulo='Aire' delay={500}>
                        <div className="predict-flex-container"> 
                            <img
                                src={ImgAire}
                                alt="Icono de Proximidad"
                                className='predict-imagen-tarjeta'
                            />
                            <h1> Valor: {DataAire} </h1>
                        </div>
                    </Tajeta>
                </div>
            </div>
        </>
    )
}
