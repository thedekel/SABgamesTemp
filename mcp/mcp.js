//imports
var http = require("http"),
    net = require("net"),
    util = require("util"),
    fs = require("fs"),
    ejs = require("ejs"),
    mongo = require("mongodb");
//global variables
var webPort = 8000,
    socPort = 1337;

//handle the web server
http.createServer(function(req, res){
    
}).listen(webPort);

//handle web socket communications
net.createServer(function(stream){
    //set encoding of socket streams
    stream.setEncoding("utf8");
    //handle new connections
    stream.on('connect', function(){

    });
    //handle incoming data
    stream.on('data', function(){

    });
    //handle disconnections
    stream.on('end', function(){

    });
}).listen(socPort);
