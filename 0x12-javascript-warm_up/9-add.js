#!/usr/bin/node
// prints the addition of 2 integers
const { argv } = require('process');
const a = Number(argv[2]);
const b = Number(argv[3]);

function add(a, b) => a + b;
console.log(add(a,b));
