#!/usr/bin/node
// a class rectangle that defines a rectangle
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) { [this.width, this.height] = [w, h];}
  }

  print () {
    let s = '';
    for (let i = 0; i < this.width; i++) {
      for (let i = 0; i < this.height; i++) {
        s +='X';
      }
      console.log(s);
    }
  }
};
