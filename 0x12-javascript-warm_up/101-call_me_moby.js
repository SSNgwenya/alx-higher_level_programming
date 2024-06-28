#!/usr/bin/node
// Defining a function that executes another function x times

function callMeMoby (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
}
module.exports = { callMeMoby };
