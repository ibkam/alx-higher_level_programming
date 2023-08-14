#!/usr/bin/node
// prints all characters of a Star Wars movie:
const request = require('request');
const { argv } = require('process');

const url = 'https://swapi-api.alx-tools.com/api/films/';
function MakeRequest (url) {
  return new Promise(function (resolve, reject) {
    request(url, (error, response, body) => {
      if (!error && response.statusCode === 200) {
        resolve(body);
      } else {
        reject(error);
      }
    });
  });
}

asy function main () {
  const movie = await MakeRequest(url + argv[2]);
  const characters = JSON.parse(movie).characters;
  characters.forEach(async function (element) {
    const character = await MakeRequest(element);
    const CharacterName = JSON.parse(character).name;
    console.log (CharacterName);
  });
}

main();
