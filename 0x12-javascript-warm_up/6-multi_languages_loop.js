#!/usr/bin/node
// This script prints 3 lines: (like 1-multi_languages.js) but by using an array of string and a loop

// array of strings
const messages = [
  'C is fun',
  'Python is cool',
  'JavaScript is amazing'
];

for (let i = 0; i < messages.length; i++) {
  console.log(messages[i]);
}
