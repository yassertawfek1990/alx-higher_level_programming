#!/usr/bin/node
const xx = require('request');
xx(process.argv[2], function (error, response, body) {
  if (!error) {
    const v = JSON.parse(body).results;
    console.log(v.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  }
});
