#!/usr/bin/node
// script that prints a square
const { argv } = require('process');
const size = Number(argv[2]);
const square = 'X'.repeat(size);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    console.log(square);
  }
}
