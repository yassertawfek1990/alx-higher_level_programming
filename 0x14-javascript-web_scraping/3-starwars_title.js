#!/usr/bin/node
const xx = require('request');
const v = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
xx.get(v, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const b = JSON.parse(body);
    console.log(b.title);
  }
});
