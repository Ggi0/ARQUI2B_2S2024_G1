import express from 'express';
import { arduinoConnection } from './arduino/connection.js';
import { getSensorDocs } from './firebase/getDocs.js';
import { addSensorValue } from './firebase/insertDoc.js';

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
 * Getting all documents from Firebase DB
 */
const getAllDocs = async () => {
    const documents = await getSensorDocs();
    console.log("== DOCUMENTS FROM FIREBASE DB (arduino-collection) ==")
    documents.forEach(doc => {
        console.log(`${doc.id} => ${JSON.stringify(doc.data())}`);
    })
}

/**
 * Establishing connection with Arduino
 */
const setArduinoConnection = async () => {
    const parser = await arduinoConnection('$');

    parser.on('open', () => {
        console.log('Opened Serial Port.');
    })
 
    parser.on('data', async (arduinoData) => {
        // Si viene '#' al inicio, son Serial.println's basura
        if (arduinoData.toString().charAt(0) == '#') {
            return;
        }

        var sensorValues = arduinoData.toString().split('\n');

        for(const sensorValue of sensorValues){
            var sensorData = sensorValue.split('/');
            if (sensorData.length != 2 ||
                sensorData[0] != "HUMEDAD" && sensorData[0] != "CO2" && sensorData[0] !=  "TEMPERATURA" && sensorData[0] != "DISTANCIA" && sensorData[0] != "LUZ") {
              continue;
            }
            
            await addNewSensorValue(sensorData);
        }
    })
}

var counter = 0;
// Adding a new document to the Firebase DB
const addNewSensorValue = async (sensorData) => {
    try {
        const response = await addSensorValue(sensorData);
        counter++;
        console.log(`New DB entry. ID: ${response.id}. Escritura No.${counter}`);
    } catch (error) {
        console.log(error.message);
    }
  }