#!/usr/bin/node
// computes and prints a factorial
const { argv } = require('process');
const n = argv[2];
function factorial (n) {
  return n === 0 || isNaN(n) ? 1 : n * factorial(n-1);
}
console.log(factorial(Number(n)));
