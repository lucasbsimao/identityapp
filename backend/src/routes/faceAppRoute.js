'use strinct'
module.exports = function(app){
    var faceAppCtrl = require("../controllers/faceAppController");
    app.route('/predict/:id')
        .get(faceAppCtrl.predict);
}