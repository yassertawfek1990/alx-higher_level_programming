#!/usr/bin/node
const xx = require('request');
xx.get(process.argv[2], { json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const v = {};
  body.forEach((todo) => {
    if (todo.completed) {
      if (!v[todo.userId]) {
        v[todo.userId] = 1;
      } else {
        v[todo.userId] += 1;
      }
    }
  });
  console.log(v);
});
