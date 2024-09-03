import { db } from './firebase.js';
import { collection, addDoc } from "firebase/firestore";

const collectionReference = collection(db, "arduino-collection");

/**
 * Carga individual de medida de sensor, para insertarlo a la DB
 */
export async function addSensorValue(sensorData) {
    if (!Array.isArray(sensorData) ||
        sensorData.length != 2 ||
        sensorData[0] != "HUMEDAD" && sensorData[0] != "CO2" && sensorData[0] !=  "TEMPERATURA" && sensorData[0] != "DISTANCIA" && sensorData[0] != "LUZ") {
            throw new Error('La información recibida no es la correcta');
    }

    try {
        const newSensorValue = {
            sensorId: sensorData[0],
            timestamp: Date.now(),
            sensorValue: sensorData[1]
        };

        const response = await insert(newSensorValue);
        return response;
    } catch (error) {
        throw new Error(error);
    }
}

/**
 * Recibe valor de sensor en JSON para insertarlo a la DB
 */
const insert = async (newSensorValue) => {
    try {
        const response = await addDoc(collectionReference, newSensorValue);
        return response;
    } catch (error) {
        throw new Error(error);
    }
}