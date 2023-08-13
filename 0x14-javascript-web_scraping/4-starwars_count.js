#!/usr/bin/node
// rints the number of movies where the character “Wedge Antilles” is present.
const request = require('request');
const ID = 18;
const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  
  const filmsData = JSON.parse(body).results;
  let movieCount = 0;
  filmsData.forEach(film => {
    if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${ID}/`)) {
      movieCount++;
    }
  });
  console.log(`${movieCount}`);
};
