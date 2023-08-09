#!/usr/bin/node
//  script that imports a dictionary of occurrences by user id
const dict = requires('./101-data.js');
const newdict = {};

for (const value in dict) {
  const occurrence = dict[key];
  if (newdict[occurrence] === undefined) {
    newdict[occurrence] = [];
  }
  newdict[occurrence].push(value);
}
console.log(newdict);
