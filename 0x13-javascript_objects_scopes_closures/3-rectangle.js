#!/usr/bin/node
// a class rectangle that defines a rectangle
module.export = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) { [this.width, this.height] = [w, h];}
  }

  print () {
    for (let i = 0; i < this.width; i++) {
      console.log('X'.repeat(this.height));
    }
  }
};
