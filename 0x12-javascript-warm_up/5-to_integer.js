#!/usr/bin/node

const args = process.argv;
const convert = parseInt(args[2]);

if (isNaN(convert)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + convert);
}
