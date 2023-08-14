#!/usr/bin/node
// gets the contents of a webpage and stores it in a file
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  fs.writeFile(filePath, body, { encoding: 'utf-8'} , error => {
    if (error) {
      console.error(error);
    } else {
      console.log(`${filePath}`);
    }
  });
});
