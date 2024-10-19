import axios from "axios";

const configuracion = {
    baseURL: 'https://b4e8-2800-98-1111-1327-00-7.ngrok-free.app',
    headers: {
        'Content-Type': 'application/json',
        'ngrok-skip-browser-warning': 'true' 
    }
}

const cliente = axios.create(configuracion)

export const APIConsultaGeneral = async () => {
    try {
        const response = await cliente.get('/consulta_general');
        console.log(response.data);
        return(response.data); // Aquí imprimes los datos que retornó la API
    } catch (error) {
        console.error("Error al hacer la solicitud:", error);
        window.alert(" Ha ocurrido un error al pedir los datos al servidor");
        return(false);
    }
}

export const APIConsultaPrediccion = async (fecha) => {
    try {
        const response = await cliente.get('/consulta_prediccion/' + fecha);
        return(response.data); // Aquí imprimes los datos que retornó la API
    } catch (error) {
        console.error("Error al hacer la solicitud:", error);
        window.alert(" Ha ocurrido un error al pedir la prediccion al servidor");
        return(false);
    }
}

export const APIConsultaUsuario = async (user, pass) => {
    try {
        const response = await cliente.get('/consulta_usuario/' + user + "/" + pass);
        return(response.data); // Aquí imprimes los datos que retornó la API
    } catch (error) {
        console.error("Error al hacer la solicitud:", error);
        window.alert(" Ha ocurrido un error al pedir la prediccion al servidor");
        return(false);
    }
}
 
export const APIConsultaParqueo = async () => {
    try {
        const response = await cliente.get('/consulta_cant_talanquera');
        return(response.data); // Aquí imprimes los datos que retornó la API
    } catch (error) {
        console.error("Error al hacer la solicitud:", error);
        window.alert(" Ha ocurrido un error al pedir la prediccion al servidor");
        return(false);
    }
}
