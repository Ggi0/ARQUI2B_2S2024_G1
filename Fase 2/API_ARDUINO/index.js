const express = require('express');
const app = express();

app.set('port', process.env.PORT || 4000);

app.get('/', (req, res) => {
    res.json(
        {
            'Title': 'Hola mundo!'
        }
    )
})

app.listen(app.get('port'), () => {
    console.log(`Server listening on port ${app.get('port')}`)
})