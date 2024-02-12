#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const rg = process.argv.map(Number)
    .slice(2, process.argv.length)
    .sort((c, v) => c - v);
  console.log(rg[rg.length - 2]);
}
