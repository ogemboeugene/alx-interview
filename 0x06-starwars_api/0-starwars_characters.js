#!/usr/bin/node
const request = require('request');

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, (error, response, body) => {
  if (error || response.statusCode !== 200) {
    console.error('Error:', error || `Unexpected status code: ${response.statusCode}`);
    return;
  }

  const filmData = JSON.parse(body);
  const characters = filmData.characters;

  // Function to make a request and return a promise
  const makeCharacterRequest = (characterUrl) => {
    return new Promise((resolve, reject) => {
      request(characterUrl, (error, response, body) => {
        if (error || response.statusCode !== 200) {
          reject(error || `Unexpected status code: ${response.statusCode}`);
        } else {
          resolve(JSON.parse(body));
        }
      });
    });
  };

  // Iterate through characters sequentially and print their names
  (async () => {
    for (const character of characters) {
      try {
        const characterData = await makeCharacterRequest(character);
        console.log(characterData.name);
      } catch (error) {
        console.error('Error fetching character:', error);
      }
    }
  })();
});
