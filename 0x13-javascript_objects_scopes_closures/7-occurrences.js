#!/usr/bin/node
// This function returns the number of occurrences in a list

exports.nbOccurences = function (list, searchElement) {
  // Initializes a counter to keep track of occurrences
  let count = 0;
  for (const element of list) {
    if (element === searchElement) {
      count++;
    }
  }
  return count;
};
