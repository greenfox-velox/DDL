//Steps: 2js.text
// Create a webserver that can receive any request to any path. It should respond the path name, the request methos and the current time.
// Please rewrite the last example with express

var express = require('express');
var app = express();

app.get('*', function(req, res) {
    var date = new Date();
    res.send('Hello World!\n' + 'Date: ' + date + '\n' + 'Method: ' + req.method + '\n' + 'Path: ' + req.path);
})

app.listen(3000);
