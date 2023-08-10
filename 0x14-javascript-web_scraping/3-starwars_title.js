#!/usr/bin/node
// prints the title of a Star Wars movie where the episode number matches a given integer.
const request = require('request');

const moviID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieid}`;
request.get(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  console.log(JSON.parse(body).title);
});
