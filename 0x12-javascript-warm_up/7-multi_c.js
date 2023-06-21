#!/usr/bin/node
//  script that prints x times “C is fun”
const { argv } = require('process');
const occurence = Number(argv[2]);
for ( let i = 0; i < occurence; i++) {
  console.log('C is fun');
}
if isNaN(occurence) {
  console.log('Missing number of occurrences');
}
