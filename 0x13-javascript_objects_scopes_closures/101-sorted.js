#!/usr/bin/node
const dict = require('./101-data');
const newDict = {};

for (const value in dict) {
  const occurrences = data[value];
  if (!newDict[occurrences]) {
    newDict[occurrences] = [];
  }
  newDict[occurrences].push(userId);
}
console.log( newDict[occurrences]);
