#!/usr/bin/node

const xx = require('request');
const id = process.argv[2];
const v = `https://swapi-api.alx-tools.com/api/films/${id}`;

xx.get(v, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const b = JSON.parse(body);
    const z = b.characters;
    // console.log(characters);
    for (const a of z) {
      xx.get(a, (error, response, body) => {
        if (error) {
          console.log(error);
        } else {
          const d = JSON.parse(body);
          console.log(d.name);
        }
      });
    }
  }
});
