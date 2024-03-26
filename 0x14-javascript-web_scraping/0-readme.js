#!/usr/bin/node
const xx = require('fs');
xx.readFile(process.argv[2], 'utf8', function (error, content) {
  console.log(error || content);
});
