#!/usr/bin/node
// Status Of Get request

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const content = JSON.parse(body);
    console.log(content.title);
  }
});
