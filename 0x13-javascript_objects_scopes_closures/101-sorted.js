#!/usr/bin/node
const dict = require('./101-data');
const newDict = {};

for (const value in dict) {
  const occurrences = dict[value];
  if (!newDict[occurrences]) {
    newDict[occurrences] = [];
  }
  newDict[occurrences].push(value);
}
console.log( newDict[occurrences]);
