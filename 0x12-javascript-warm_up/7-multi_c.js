#!/usr/bin/node
const s = Math.floor(Number(process.argv[2]));
if (isNaN(s)) {
  console.log('Missing number of occurrences');
} else {
  for (let a = 0; a < s; a++) {
    console.log('C is fun');
  }
}
