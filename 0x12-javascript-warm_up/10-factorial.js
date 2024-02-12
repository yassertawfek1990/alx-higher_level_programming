#!/usr/bin/node
function fct (n) {
  return c === 0 || isNaN(c) ? 1 : c * fct(c - 1);
}

console.log(fct(Number(process.argv[2])));
