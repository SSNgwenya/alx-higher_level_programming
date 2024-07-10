// 6-square.js

const Square = require('./5-square');

class EnhancedSquare extends Square {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    // Prints the square using character c
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = EnhancedSquare;
