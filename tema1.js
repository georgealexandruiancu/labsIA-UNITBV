var nj = require('numjs');

var w1 = [0,1,0]
var x1 = [2,1,-1]
var d1 = -1
var x2 = [0, -1, -1]
var d2 = 1

function fActivare(net){
    f = ((2 * (2.71 ** net)) / ((1+(2.71**net))*2))
    console.log(f) 
}
fActivare(10);