#!/usr/bin/node
//  script that prints x times “C is fun”
const { argv } = require('process');
const occurence = Number(argv[2]);

if (!occurence) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < occurence; i++) {
    console.log('C is fun');
  }
}
