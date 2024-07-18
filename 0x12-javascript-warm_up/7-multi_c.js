#!/usr/bin/node
// This script prints x times “C is fun”

const args = process.argv.slice(2);
const x = parseInt(args[0], 10);

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  // Loop to print "C is fun" x times
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
