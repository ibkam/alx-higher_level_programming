#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  list.forEach((x) => {
    if (x === searchElement) {
      count += 1;
    }
  });
  return count;
};
