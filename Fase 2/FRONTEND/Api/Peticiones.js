import axios from "axios";

const configuracion = {
    baseURL: 'http://127.0.0.1:5000',
    headers: {
        'Content-Type': 'application/json'
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
