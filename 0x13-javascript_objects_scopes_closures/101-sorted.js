#!/usr/bin/node
//  script that imports a dictionary of occurrences by user id
const dict = requires('./101-data.js');
const newdict = {};

for (const key in dict) {
  const occurrence = dict[key];
  if (!newdict[occurrence] ){
    newdict[occurrence] = [];
  }
  newdict[key].push(value);
}
console.log(newdict);
