import express from 'express';
import { arduinoConnection } from './arduino/connection.js';
import { getSensorDocs } from './firebase/getDocs.js';

import { addSensorValue } from '../firebase/insertDoc.js';

const app = express();

app.set('port', process.env.PORT || 8080);

app.get('/', (req, res) => {
    res.json({'message': 'App is running OK'})
})

app.get('/getDocs', (req, res) => {
    res.json({'message': 'Getting documents from database, see console.'});
    getAllDocs();
});

app.listen(app.get('port'), () => {
    console.log(`Server listening on port ${app.get('port')}`);
    setArduinoConnection();
})

/**
 * Getting all documentos from Firebase DB
 */
const getAllDocs = async () => {
    const documents = await getSensorDocs();
    documents.forEach(doc => {
        console.log(`${doc.id} => ${doc.data()}`);
    })
}

/**
 * 
 */
const setArduinoConnection = async () => {
    const parser = await arduinoConnection('$');
    
    parser.on('open', () => {
        console.log('Opened Serial Port.');
    })

    parser.on('data', (arduinoData) => {
        // Si viene '#' al inicio, son Serial.println's basura
        if (arduinoData[0] == '#') {
            return;
        }
        
        console.log("=== Datos recibidos de Arduino ===");
        console.log(arduinoData);

        var sensorValues = arduinoData.split('\n');
        sensorValues.forEach(sensorValue => {
            var sensorData = sensorValue.split('/');
            if (sensorData.length != 2 ||
                sensorData[0] != "HUMEDAD" && sensorData[0] != "CO2" && sensorData[0] !=  "TEMPERATURA" && sensorData[0] != "DISTANCIA" && sensorData[0] != "LUZ") {
              return;
            }
            
            addNewSensorValue(sensorData);
        })
    })
}

const addNewSensorValue = async () => {
    try {
        const response = await addSensorValue(sensorData);
        console.log(`New DB entry. ID: ${response.id}`);
    } catch (error) {
        console.log(error.message);
    }
  }