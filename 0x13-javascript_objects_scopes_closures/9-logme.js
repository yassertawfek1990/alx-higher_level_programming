#!/usr/bin/node
let scout = 0;
exports.logMe = function (item) { console.log(`${scout++}: ${item}`); };
