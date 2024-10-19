import React, { useEffect, useState } from 'react';
import { Tajeta } from '../Historico/Tarjeta';
import { Calendario } from './Calendario';
import '../../styles/img.css';
import { Button } from 'primereact/button';
import { APIConsultaPrediccion } from '../../../Api/Peticiones';

const ImgAire = '/data/asset/img/Aire.png';
const ImgLuz = '/data/asset/img/Luz.png';
const ImgTemperatura = '/data/asset/img/Temperatura.png';
const ImgHumedad = '/data/asset/img/tacita.png';
const ImgProximidad = '/data/asset/img/proximidad.png';


export const Prediccion = () => {
    // Estado para el boton de busqueda
    const [BtnBusqueda, SetBtnBusqueda]         = useState("Consultar")
    const [BtnDisabled, SetBtnDisabled]         = useState(false)
    // Estados para guardar la data
    const [DataHumedad, setDataHumedad]         = useState(0);
    const [DataTemperatura, setDataTemperatura] = useState(0);
    const [DataDistancia, setDataDistancia]     = useState(0);
    const [DataLuz, setDataLuz]                 = useState(0);
    const [DataAire, setDataAire]               = useState(0);

    // Estados para la hora
    const [datetime24h, setDateTime24h] = useState(null);


    // Funcion que consulta a la api de las predicciones
    const ConsultarPredicciones = async () => {
        // Valida que se seleccione una fecha
        if (datetime24h === null){
            return;
        }
        const fechaSolicitada = Math.floor(datetime24h.getTime() / 1000)
        // Setea los botones a nulo e indica que esta buscand
        SetBtnBusqueda("Buscando..")
        SetBtnDisabled(true)
        const response = await APIConsultaPrediccion(fechaSolicitada);
        console.log(response)
        // Recorre el arreglo y setea los valores
        response.map((x) => {
            if (x.sensor === 'hum-collection'){
                setDataHumedad(Math.round(x.valor * 100) / 100 )  
            }
            else if (x.sensor === 'temp-collection'){
                setDataTemperatura(Math.round(x.valor * 100) / 100 )  
            }
            else if (x.sensor === 'dist-collection'){
                setDataDistancia(Math.round(x.valor * 100) / 100 )  
            }
            else if (x.sensor === 'luz-collection'){
                setDataLuz(Math.round(x.valor * 100) / 100 )  
            }
            else if (x.sensor === 'co2-collection'){
                setDataAire(Math.round(x.valor * 100) / 100 )  
            }
        })
        SetBtnDisabled(false)
        SetBtnBusqueda("Consultar")
    }

    return (
        <>
            {/* Tarjetas con sus iconos, para desplegar cada uno de los modales */}
            
            <div className="grid">
                <div className="col-5" style={{'display': 'flex', 'flexDirection': 'row'}}>
                    <Calendario datetime24h={datetime24h} setDateTime24h={setDateTime24h} ></Calendario>
                    <Button style={{'marginInline': '2%'}} onClick={ConsultarPredicciones} disabled={datetime24h === null || BtnDisabled}> {BtnBusqueda} </Button>
                </div>
            </div>

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
