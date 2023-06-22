#!/usr/bin/node
// prints My number: <first argument converted in integer>const { argv } = require('process');
const { argv } = require('process');
const convert = Number(argv[2]);

if(isNaN(convert)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${convert}`);
}
