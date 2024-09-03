import { SerialPort } from 'serialport';
import { DelimiterParser } from '@serialport/parser-delimiter';
import { setTimeout } from 'timers/promises';


export const arduinoConnection = async (delimiter) => {
    while (true) {
        try {
            var comPort = process.env.COM_PORT || "COM3";
            console.log(`Trying serial connection through ${comPort}.`);

            const port = new SerialPort({
                path: comPort,
                baudRate: 9600
            });
            const parser = port.pipe(new DelimiterParser({
                delimiter: delimiter
            }))
            return parser;
        } catch (error) {
            console.log("Connection failed, waiting 3s...");
            await setTimeout(3000);
        }
    }
};