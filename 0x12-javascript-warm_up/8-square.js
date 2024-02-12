#!/usr/bin/node
const z = Math.floor(Number(process.argv[2]));
if (isNaN(z)) {
  console.log('Missing size');
} else {
  for (let q = 0; q < z; q++) {
    let w = '';
    for (let s = 0; s < z; s++) w += 'X';
    console.log(w);
  }
}
