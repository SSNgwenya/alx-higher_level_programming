#!/usr/bin/node
// This script prints the addition of 2 integers

function add(a, b) {
    console.log(a + b);
}

// Example usage:
const firstInt = parseInt(process.argv[2], 10);
const secondInt = parseInt(process.argv[3], 10);

add(firstInt, secondInt);
