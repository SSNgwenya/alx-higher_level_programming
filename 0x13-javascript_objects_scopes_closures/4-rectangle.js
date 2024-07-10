#!/usr/bin/node
// This class defines a Rectangle class

class Rectangle {
  // This constructor initializes the rectangle with width (w) and height (h)
  constructor (w, h) {
    // Checks if both w and h are positive integers
    if (Number.isInteger(w) && Number.isInteger(h) && w > 0 && h > 0) {
      this.width = w; // Sets width as w
      this.height = h; // Sets height as h
    } else {
      // If input is invalid, set width and height to 0
      this.width = 0;
      this.height = 0;
    }
  }

  // This method prints the rectangle using the character 'X'
  print () {
    if (this.width > 0 && this.height > 0) {
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    } else {
      console.log('This is an empty rectangle.');
    }
  }

  // This method exchanges the width and height of the rectangle
  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  // This method doubles the width and height of the rectangle
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
