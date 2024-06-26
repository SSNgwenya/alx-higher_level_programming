#!/usr/bin/node
// This script prints the addition of 2 integers

function add (a, b) {
  const num1 = parseInt(a, 10);
  const num2 = parseInt(b, 10);

  if (isNaN(num1) || isNaN(num2)) {
    console.log('Invalid input. Both arguments must be integers.');
  } else {
    const result = num1 + num2;
    console.log(`The addition of ${num1} and ${num2} is: ${result}`);
  }
}
const args = process.argv.slice(2);
add(args[0], args[1]);
