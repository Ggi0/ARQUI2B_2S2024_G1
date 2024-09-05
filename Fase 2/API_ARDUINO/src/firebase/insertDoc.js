import { db } from './firebase.js';
import { collection, addDoc } from "firebase/firestore";

const tempCollection = collection(db, "temp-collection");
const co2Collection = collection(db, "co2-collection");
const humCollection = collection(db, "hum-collection");
const distCollection = collection(db, "dist-collection");
const luzCollection = collection(db, "luz-collection");

/**
 * Carga individual de medida de sensor, para insertarlo a la DB
 */
export async function addSensorValue(sensorData) {
    if (!Array.isArray(sensorData) ||
        sensorData.length != 2 ||
        sensorData[0] != "HUMEDAD" && sensorData[0] != "CO2" && sensorData[0] !=  "TEMPERATURA" && sensorData[0] != "DISTANCIA" && sensorData[0] != "LUZ") {
            throw new Error('La información recibida no es la correcta');
    }

    var collection;
    if(sensorData[0] == "HUMEDAD"){
        collection = humCollection;
    } else if(sensorData[0] == "CO2"){
        collection = co2Collection;
    } else if(sensorData[0] == "TEMPERATURA"){
        collection = tempCollection;
    } else if(sensorData[0] == "DISTANCIA"){
        collection = distCollection;
    } else {
        collection = luzCollection;
    }

    try {
        const newSensorValue = {
            sensorId: sensorData[0],
            timestamp: Date.now(),
            sensorValue: parseFloat(sensorData[1])
        };

        const response = await insert(collection, newSensorValue);
        return response;
    } catch (error) {
        throw new Error(error);
    }
}

/**
 * Recibe valor de sensor en JSON para insertarlo a la DB
 */
const insert = async (collection, newSensorValue) => {
    try {
        const response = await addDoc(collection, newSensorValue);
        return response;
    } catch (error) {
        throw new Error(error);
    }
}