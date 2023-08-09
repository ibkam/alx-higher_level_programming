#!/usr/bin/node
//  script that imports a dictionary of occurrences by user id
const dict = requires('./101-data.js');
const newdict = {};

for (const key in dict) {
  if (!newdict[dict[key]] === undefined) {
    newdict[dict[key]]= [key];
  } else {
  newdict[key].push(value);
}
console.log(newdict);
