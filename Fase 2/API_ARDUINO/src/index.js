import express from 'express';
import { getTestDocs } from './firebase/getDocs.js';

// const express = require('express');
const app = express();

// import {getTestDocs} from './getDocs'; 


// const { SerialPort } = require('serialport');
// const { DelimiterParser } = require('@serialport/parser-delimiter');

// const { setTimeout } = require('timers/promises');
// const yourFunction = async () => {
//     await setTimeout(5000);
//     console.log("Waited 5s");
  
//     await setTimeout(5000);
//     console.log("Waited an additional 5s");
//   };

// while (true) {
//     try {
//         console.log('Trying connection...')

//         const port = new SerialPort({
//             path: "COM3",
//             baudRate: 9600
//         });
//         const parser = port.pipe(new DelimiterParser({delimiter: '\n'}))
        
//         parserSerial.on('open', () => {
//             console.log('Opened Serial Port.');
//         })
    
//         parser.on('data', (line) => {
//             console.log(line);
//         })

//         break;
//     } catch (error) {
//         await delay(3000);
//     }
// }


app.set('port', process.env.PORT || 8080);

app.get('/', (req, res) => {
    res.json({'Title': 'Hola mundo!'})
})

app.get('/getDocs', (req, res) => {
    getAllDocs();
    res.json({'Title': 'getting Docs, see console...'});
});

app.listen(app.get('port'), () => {
    console.log(`Server listening on port ${app.get('port')}`)
})

async function getAllDocs() {
    const documents = await getTestDocs();
    documents.forEach(doc => {
        console.log(doc.id);
        console.log(doc.data());
    })
}