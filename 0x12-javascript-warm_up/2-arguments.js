#!/usr/bin/node
//  prints a message depending of the number of arguments passed:
const { argv } = require('process');
if (agrv.length === 2) {
  console.log('No argument');
}
else if (agrv.length < 4) {
  console.log('Argument found');
}
else {
  console.log('Arguments found');
}
