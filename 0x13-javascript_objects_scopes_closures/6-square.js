#!/usr/bin/node
module.exports = class Square extends require('./5-square.js') {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let d = 0; d < this.height; d++) console.log(c.repeat(this.width));
    }
  }
};
