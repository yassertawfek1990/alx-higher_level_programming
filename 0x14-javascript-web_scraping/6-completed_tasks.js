#!/usr/bin/node
const xx = require('request');
xx(process.argv[2], function (error, response, body) {
  if (!error) {
    const v = JSON.parse(body);
    let b = {};
    v.forEach((todo) => {
      if (todo.completed && b[todo.userId] === undefined) {
        b[todo.userId] = 1;
      } else if (todo.completed) {
        b[todo.userId] += 1;
      }
    });
    console.log(b);
  }
});
