#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2];
const data = process.argv[3];
const options = { encoding: 'utf-8' };

fs.writeFile(filePath, data, options, (error) => {
  if (error) {
    console.error(error);
  }
});
