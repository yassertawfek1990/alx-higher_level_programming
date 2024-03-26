#!/usr/bin/node
const xx = require('request');
xx.get(process.argv[2]).on('response', function (response) {
  console.log(`code: ${response.statusCode}`);
});
