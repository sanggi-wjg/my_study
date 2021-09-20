const express = require('express')
const app = express()
const port = 8010

var fs = require('fs');

app.use('/static', express.static(__dirname + '/static'));

app.get('/', (req, res) => {
    fs.createReadStream('rtc_main.html').pipe(res);
})

app.listen(port, () => {
    console.log(`Example app listening at http://localhost:${port}`)
})