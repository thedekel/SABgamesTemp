//imports
var net = require("net"),
    sys = require("sys");

//globals and constarts
var port = 1337; 

//create a server
net.createServer(function(stream){
    //encoding
    stream.setEncoding("utf8");
    //function handler for connect event
    stream.on('connect', function(){
        console.log('connected');
    });
    //function handler for incoming data
    stream.on('data', function(data){
        console.log('data');
        if ((data.toString())=="ping"){
            console.log('message "ping" received');
            stream.write("pong");
        }
    });
    //function handler for disconnections
    stream.on('end', function(){
        console.log('end');
        console.log(sys.inspect(stream));
    });
}).listen(port); //listen on port given at the top
