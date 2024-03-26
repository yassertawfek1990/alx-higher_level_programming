#!/usr/bin/node
const xx = require('fs');
xx.writeFile(process.argv[2], process.argv[3], error => {
  if (error) console.log(error);
});
