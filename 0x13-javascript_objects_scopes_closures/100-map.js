#!/usr/bin/node
// script that imports an array and computes a new array.
const list = require('./100-data');
const newlist = list.map((value, index) => value * index);

console.log(list);
console.log(newlist);
