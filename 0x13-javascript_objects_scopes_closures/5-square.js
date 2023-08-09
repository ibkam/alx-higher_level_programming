#!/usr/bin/node
// class Square that defines a square
module.exports = class square extends require('./4-rectangle.js') {
  constructor (size) {
    super(size, size)
  }
};
