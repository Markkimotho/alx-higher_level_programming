#!/usr/bin/node

const numOfTimes = parseInt(process.argv[2]);
if (isNaN(numOfTimes)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < numOfTimes; i++) {
    console.log('C is fun');
  }
}
