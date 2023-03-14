#!/usr/bin/node

const Square2 = require('./5-square');

class Square extends Square2 {
  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      for (let k = 0; k < this.width; k++) {
        process.stdout.write(c);
      }
      process.stdout.write('\n');
    }
  }
}

module.exports = Square;
