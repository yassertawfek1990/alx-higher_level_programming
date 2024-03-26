#!/usr/bin/node
const x = require('request');
const id = process.argv[2];
const v = `https://swapi-api.alx-tools.com/api/films/${id}`;
x.get(v, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const b = JSON.parse(body);
    const z = b.characters;
    for (const a of z) {
      x.get(a, (error, response, body) => {
        if (error) {
          console.log(error);
        } else {
          const g = JSON.parse(body);
          console.log(g.name);
        }
      });
    }
  }
});
