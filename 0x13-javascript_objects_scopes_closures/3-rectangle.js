#!/usr/bin/node
// This Class defines the Rectangle

class Rectangle {
  constructor (w, h) {
    // Checking if both w and h are positive integers
    if (Number.isInteger(w) && Number.isInteger(h) && w > 0 && h > 0) {
      this.width = w; // Setting width
      this.height = h; // Setting height
    } else {
      // If input is invalid, width and height are set to 0
      this.width = 0;
      this.height = 0;
    }
  }

  // Method of printing the rectangle using the character 'X'
  print () {
    if (this.width > 0 && this.height > 0) {
      // This loop prints each row of the rectangle
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    } else {
      // Message to print if the rectangle is invalid
      console.log('This is an empty rectangle.');
    }
  }
}

// Exporting the Rectangle class to be used in other files
module.exports = Rectangle;
