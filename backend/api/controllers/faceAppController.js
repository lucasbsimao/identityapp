'use strict'

var http = require('http');

exports.predict = (req,res) => {
    var options = {
        hostname: "mlalgorithm",
        port: 5000,
        path: '/predict/'+req.params.id,
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    };

    var clReq = http.request(options, (clRes) => {
        clRes.setEncoding('utf8');
        
        var response = "";

        clRes.on('data', (data) => {
            response += data;
        });

        clRes.on('end', () => {
            res.json(response);
        });
    });
    clReq.end();
}