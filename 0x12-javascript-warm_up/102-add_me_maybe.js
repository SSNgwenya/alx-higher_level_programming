#!/usr/bin/node
// Defining a function that increase a number and calls another function

function addMeMaybe (number, theFunction) {
  number++;
  theFunction(number);
}
module.exports = { addMeMaybe };
