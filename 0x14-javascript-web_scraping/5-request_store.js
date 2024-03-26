#!/usr/bin/node
const vv = require('fs');
const xx = require('request');
xx(process.argv[2]).pipe(vv.createWriteStream(process.argv[3]));
