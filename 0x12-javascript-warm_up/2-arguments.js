#!/usr/bin/node
//  prints a message depending of the number of arguments passed:
const process = require('process');
const argv  = process.argv;
if (agrv.length === 2) {
  console.log('No argument');
}
else if (agrv.length < 4) {
  console.log('Argument found');
}
else {
  console.log('Arguments found');
}
