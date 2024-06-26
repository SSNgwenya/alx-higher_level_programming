#!/usr/bin/node

const args = process.argv.slice(2);
const x = parseInt(args[0], 10);
if (!isNaN(x)) {
  console.log(`My number: ${x}`);
} else {
  console.log('Not a number');
}
