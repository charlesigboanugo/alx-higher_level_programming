#!/usr/bin/node
const limit = parseInt(process.argv[2]);
let times = 0;

if (limit === undefined || isNaN(limit)) {
  console.log('Missing number of occurrences');
} else {
  for (times = 0; times < limit; times++) {
    console.log('C is fun');
  }
}
