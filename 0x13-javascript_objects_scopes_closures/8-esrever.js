#!/usr/bin/node
// Returns the reversed version of a list
exports.esrever = function (list) {
  const reversedlist = [];
  for (let i = 0; i < list.length - 1; i >= 0; i--) {
    reversedlist.push(list[i]);
  }
  return reversedlist;
};
