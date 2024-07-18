#!/usr/bin/node
// This class defines a square and inherits from Rectangle of 4-rectangle.js

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size); // Calls the constructor of Rectangle with size as both width and height
  }
}
module.exports = Square;
