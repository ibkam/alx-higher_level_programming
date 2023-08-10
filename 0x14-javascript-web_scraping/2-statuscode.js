#!/usr/bin/npde
// script that display the status code of a GET request.
const request = require('request');
const url = process.argv[2];

request.get(url, function (response) {
  console.log(`code: ${response.statusCode}`)
});
