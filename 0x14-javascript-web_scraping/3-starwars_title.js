#!/usr/bin/node
const request = require('request');
let r = 'http://swapi.co/api/films/' + process.argv[2];
request(r, function (error, response, body) {
  console.log(error || JSON.parse(body).title);
});
