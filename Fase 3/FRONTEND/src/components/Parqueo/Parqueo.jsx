import React, { useEffect, useState } from 'react';
import { Tajeta } from '../Historico/Tarjeta';
import '../../styles/img.css';
import { Client, Message  } from 'paho-mqtt';
import { InputOtp } from 'primereact/inputotp';
import { InputText } from "primereact/inputtext";
import { Button } from 'primereact/button';
import { APIConsultaParqueo, APIConsultaUsuario } from '../../../Api/Peticiones';


const ImgProximidad = '/data/asset/img/ubicacion.png';



export const Parqueo = () => {
    // Estados para guardar la data
    const [StatusCarro, setStatusCarro]         = useState('No ha ingresado Carro');
    const [CantCarros, setCantCarros]           = useState(0);
    const [Usuario, setUsuario]                 = useState('');
    const [Pass, setPass]                       = useState();
    // Funcion de consulta al mqtt
    const ConsultaActual = () => {
      const client = new Client('broker.emqx.io', 8083, 'subscriber-client');
      // Cuando llega un mensaje
      client.onMessageArrived = (msg) => {
        console.log("mensaje parqueo", msg); 
        // Valida si no ha ingresado carro
          if (msg != 0 && msg){
            setStatusCarro("Se ha ingresado Carro");
          }
          else{
            setStatusCarro("No ha ingresado Carro");
          }
      };
      // Cuando se conecta se mete en un loop
      client.connect({ onSuccess: () => {
          client.subscribe('arqui2_2s2024/topico_aviso_carro');
      } });
      // Si no se conecta retorna
      return () => client.disconnect();
    }

    useEffect ( () => {
      ConsultaActual();
    }, [])

    
    const MQTTPublicar = (topico, mensaje) => {
        const clientId = `cliente-publicador-${Math.random().toString(16).slice(2)}`;
        let clienteMqtt = new Client('ws://broker.emqx.io:8083/mqtt', clientId);
    
        clienteMqtt.onConnectionLost = (responseObject) => {
            if (responseObject.errorCode !== 0) {
                console.error('Conexión perdida:', responseObject.errorMessage);
            }
        };
    
        clienteMqtt.connect({
            onSuccess: () => {
                console.log("Conectado exitosamente al broker MQTT");
                const msg = new Message(mensaje);
                msg.destinationName = topico;
                clienteMqtt.send(msg);
                console.log(`Publicado: ${mensaje} en ${topico}`);
                setTimeout(() => {
                    clienteMqtt.disconnect();
                    console.log("Desconectado del broker MQTT");
                }, 500); // 0.5 segundo de retraso
            },
            onFailure: (err) => {
                console.error('Error al conectar con el broker:', err);
                if (err.errorCode) {
                    console.error('Código de error:', err.errorCode);
                }
                if (err.errorMessage) {
                    console.error('Mensaje de error:', err.errorMessage);
                }
            }
        });
    }
    
    
    
    
    
    const ValidarUsuario = async () => {
        const response = await APIConsultaUsuario(Usuario, Pass);
        console.log(response.ok)
        // Valida si la respuesta es no, manda el mensaje
        if (response.ok == false){
            alert(response.mensaje);
            MQTTPublicar("arqui2_2s2024/desbloqueo_usuario", "2");
            return;
        }
        // Si la respuesta es si, abre la talanquera
        MQTTPublicar("arqui2_2s2024/desbloqueo_usuario", "1");
        alert(response.mensaje);
    }

    const ObtenerRecuento = async () => {
        const response = await APIConsultaParqueo();
        console.log(response)
        // Valida si la respuesta es no, manda el mensaje
        if (response.ok == false){
            alert("No se ha podido actualizar");
            return;
        }
        // Si la respuesta es si, abre la talanquera
        setCantCarros(response.cantidad);
    }

    return (
        <>
            {/* Tarjetas con sus iconos, para desplegar cada uno de los modales */}
            <h2> Parqueo </h2>
            <div className="grid nested-grid">
                <div className="col-9">
                    <div className="grid">
                        <div className="col-6">
                            <Tajeta titulo='Info. de Carros' delay={200}>
                                <div className="predict-flex-container">
                                    <img
                                        src={ImgProximidad}
                                        alt="Icono de Proximidad"
                                        className='predict-imagen-tarjeta'
                                    />
                                    <h4>{StatusCarro} </h4>
                                </div>
                            </Tajeta>
                        </div>
                        <div className="col-6">
                            <Tajeta titulo='Cant. de Carros' delay={200}>
                                <div className="flex ">
                                    <h4 style={{marginInline: '10%'}}> Recuento: {CantCarros} </h4>
                                    <Button style={{marginInline: '10%'}} label="Actualizar" severity="help" text raised 
                                            onClick={ObtenerRecuento}/>
                                </div>
                            </Tajeta>
                        </div>
                        <div className="col-12">
                            <Tajeta titulo='Control de luces' delay={200}>
                                <div className="predict-flex-container">
                                <Button style={{marginInline: '2%'}} label="Apagar Luces" onClick={() => MQTTPublicar("arqui2_2s2024/prender_luces", "0")} severity="help" outlined raised />
                                <Button style={{marginInline: '2%'}} label="Encender Luces" onClick={() => MQTTPublicar("arqui2_2s2024/prender_luces", "1")} severity="Secondary" outlined raised />
                                <Button style={{marginInline: '2%'}} label="Automatico" onClick={() => MQTTPublicar("arqui2_2s2024/prender_luces", "2")} severity="info" outlined raised />

                                </div>
                            </Tajeta>
                        </div>
                    </div>
                </div>
                <div className="col-3">
                    <Tajeta titulo='Abrir talanquera' delay={200}>
                        
                        <div style={{height: '45vh'}}>
                             <h5> Ingrese el nombre de usuario</h5>  
                             <InputText id="username" value={Usuario} onChange={(e) => setUsuario(e.target.value)} />
                             <h5> Ingrese la contraseña</h5>   
                             <InputOtp value={Pass} onChange={(e) => setPass(e.value)}/>   
                             <Button 
                                style={{marginBlock: '10%'}} 
                                label="Abrir Talanquera" 
                                severity="success"
                                onClick={ValidarUsuario}
                                disabled={Usuario.trim() === '' || !Pass}
                                />
                        </div>
                    </Tajeta>
                </div>
            </div>
        </>
    )
}
