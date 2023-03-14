#!/usr/bin/node

const firstArg = process.argv[2];
const secondArg = process.argv[3];
const concatArg = firstArg + ' is ' + secondArg;
console.log(concatArg);
