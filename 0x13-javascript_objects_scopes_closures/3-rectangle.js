#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let c = 0; c < this.height; c++) {
      let g = '';
      for (let l = 0; l < this.width; l++) {
        g += 'X';
      }
      console.log(s);
    }
  }
}

module.exports = Rectangle;
