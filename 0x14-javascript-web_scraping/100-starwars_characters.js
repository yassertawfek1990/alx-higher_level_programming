#!/usr/bin/node
const xx = require('request');
const v = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
xx(v, function (error, response, body) {
  if (!error) {
    const b = JSON.parse(body).characters;
    b.forEach((character) => {
      xx(b, function (error, response, body) {
        if (!error) {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
