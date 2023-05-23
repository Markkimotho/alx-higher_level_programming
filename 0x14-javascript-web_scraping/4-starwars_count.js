#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const films = JSON.parse(body);
  let charCount = 0;
  for (const result of films.results) {
    for (const character of result.characters) {
      if (character.includes(18)) {
        charCount++;
      }
    }
  }
  console.log(charCount);
});
