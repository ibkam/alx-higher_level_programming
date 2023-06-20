#!/usr/bin/node
//  prints two arguments passed to it, in the following format: “ is ”
const { argv } = require('process');
const argv1 = argv[2];
const argv2 = argv[3];
console.log(argv1 + ' is ' + argv2)
