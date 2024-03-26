#!/usr/bin/node
const s = require('request');
let r = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
s(r, function (error, response, body) {
  console.log(error || JSON.parse(body).title);
});
