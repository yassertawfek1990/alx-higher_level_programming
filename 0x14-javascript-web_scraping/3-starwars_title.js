#!/usr/bin/node
const xx = require('request');
let v = 'http://swapi.co/api/films/' + process.argv[2];
xx(v, function (error, response, body) {
  console.log(error || JSON.parse(body).title);
});
