#!/usr/bin/node

const request = require('request');

const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const films = JSON.parse(body);
  const charactersURL = films.results[id].characters;

  for (const charURL of charactersURL) {
    request(String(charURL), function (error, response, body) {
      if (error) {
        console.error(error);
      }
      const charInfo = JSON.parse(body);
      console.log(charInfo.name);
    });
  }
});
