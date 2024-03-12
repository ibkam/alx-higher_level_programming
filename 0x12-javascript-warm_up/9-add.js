#!/usr/bin/node
// prints the addition of 2 integers
const { argv } = require('process');
const a = Number(argv[2]);
const b = Number(argv[3]);
let sum = 0;
function add (a, b) {
  sum = (a + b);
  console.log(sum);
}
add(a, b);
