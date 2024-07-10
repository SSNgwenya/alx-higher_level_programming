#!/usr/bin/node
// This class defines a square and inherits from Rectangle of 4-rectangle.js

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    // Since Square inherits from Rectangle, we call super() to invoke the constructor of Rectangle
    super(size, size);
  }
}

module.exports = Square;
