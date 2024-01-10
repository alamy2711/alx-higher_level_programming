#!/usr/bin/node
const dict = require('./101-data').dict;
const lostTotal = Object.entries(dict);
const values = Object.values(dict);
const uniqueValus = [...new Set(values)];
const newDict = {};
for (const j in uniqueValus) {
  const arr = [];
  for (const k in lostTotal) {
    if (lostTotal[k][1] === uniqueValus[j]) {
      arr.unshift(lostTotal[k][0]);
    }
  }
  newDict[uniqueValus[j]] = arr;
}
console.log(newDict);
