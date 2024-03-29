#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, function (error, response) {
  if (error) {
    console.error(error);
  }
  const statusCode = response && response.statusCode;
  console.log('code:', statusCode);
});
