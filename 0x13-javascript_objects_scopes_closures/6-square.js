#!/usr/bin/node

const baseSquare = require('./5-square.js');

class Square extends baseSquare {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    const xLine = c.repeat(this.width);
    for (let i = 0; i < this.height; i++) {
      console.log(xLine);
    }
  }
}

module.exports = Square;
