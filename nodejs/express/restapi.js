var express = require("express");
var app = express();

var router = express.Router();

router.get("/user/:id", function(req, res){
    res.send(req.params.id);
});

router.post("/user", function(req, res){
    res.send("");
});

app.use("/api",router);

var server = app.listen(3000, () => {
    console.log("Server running at http://localhost:" + server.address().port);
});