#!/usr/bin/node

const request = require('request');

// Function to fetch characters of a Star Wars movie by ID
function getCharacters (movieId) {
  return new Promise((resolve, reject) => {
    const url = `https://swapi.dev/api/films/${movieId}/`;

    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        const film = JSON.parse(body);
        const characters = film.characters;
        resolve(characters);
      }
    });
  });
}

// Function to get character name from URL
function getCharacterName (characterUrl) {
  return new Promise((resolve, reject) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        const character = JSON.parse(body);
        resolve(character.name);
      }
    });
  });
}
