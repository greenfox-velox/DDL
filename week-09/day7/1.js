//Steps: 1js.text
// Create a webserver that can receive any request to any path. It should respond the path name, the request methos and the current time.

var http = require('http');

var server = http.createServer(function(req, res) {
    res.writeHead(200, {'Content-Type' : 'text/plain'})
    var date = new Date();
    res.end('Hello World!\n' + 'Date: ' + date + '\n' + 'Method: ' + req.method + '\n' + 'URL: ' + req.url);
});

server.listen(3000, '127.0.0.1')
