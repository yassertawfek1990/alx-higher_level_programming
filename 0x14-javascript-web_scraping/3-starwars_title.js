#!/usr/bin/node
const s = require('request');
let r = 'http://swapi.co/api/films/' + process.argv[2];
s(r, function (error, response, body) {
  console.log(error || JSON.parse(body).title);
});
