#!/usr/bin/node
// a function that returns the number of occurrences in a list
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  list.map(
    (x) => {
      if (x === searchElement) {
        count += 1;
        return 1;
      } else {
        return 0;
      }
    }
    );
  return count;
}
