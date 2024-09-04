import { SerialPort } from 'serialport';
import { DelimiterParser } from '@serialport/parser-delimiter';
import { setTimeout } from 'timers/promises';


export const arduinoConnection = async (delimiter) => {
    var tryConnection = true;
    var comPort = process.env.COM_PORT || "COM3";

    while (tryConnection) {
        try {
            tryConnection = false;
            process.stdout.write(`Trying serial connection through ${comPort}... `);

            var port = new SerialPort({
                path: comPort, 
                baudRate: 9600
            });
            port.on('error', () => {
                tryConnection = true;
            })

            // Giving time to connect
            await setTimeout(2000);

            if (tryConnection){
                // The connection with Arduino failed, trying again
                console.log("Failed, waiting 3s.");
                await setTimeout(1000);
                continue;
            }

            // If the prograam execution reaches this code, the connection with Arduino was established
            console.log("Done!");
            await setTimeout(1000);

            const parser = port.pipe(new DelimiterParser({
                delimiter: delimiter
            }))

            return parser;
            
        } catch (error) {
            throw new Error(error);
        }
    }
};