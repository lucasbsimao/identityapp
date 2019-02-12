var express = require('express'),
    app = express(),
    mongoose = require('mongoose'),
    port = process.env.port || 3000;

mongoose.connect("mongodb://mongo:27018/Tododb");

routes = require('./routes/faceAppRoute');
routes(app);

app.listen(port, () => { console.log("Connection on port : " + port) });