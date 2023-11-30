#!/usr/bin/node

const dict = require('./101-data').dict;
const d = {};

for (const k in dict) {
  if (!(dict[k] in d)) {
    d[dict[k]] = [k];
  } else {
    d[dict[k]].push(k);
  }
}

console.log(d);
