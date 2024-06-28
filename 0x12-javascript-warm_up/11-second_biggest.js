#!/usr/bin/node
// This script searches for the second biggest integer in the list of arguments

function findSecondBiggest (numbers) {
  if (numbers.length < 2) {
    return 0;
  }

  let first = -Infinity;
  let second = -Infinity;

  for (const num of numbers) {
    if (num > first) {
      second = first;
      first = num;
    } else if (num > second && num < first) {
      second = num;
    }
  }

  return second;
}

const args = process.argv.slice(2).map(Number);

const result = findSecondBiggest(args);

console.log(result);
