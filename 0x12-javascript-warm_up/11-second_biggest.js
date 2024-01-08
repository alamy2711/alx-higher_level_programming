#!/usr/bin/node
const { argv } = require('process');

if (argv.length === 2 || argv.length === 3) console.log(0);
else {
  let second = 0;
  let first = argv[2];
  for (let i = 2; i < argv.length; i++) {
    if (first < argv[i]) {
      if (second < first) second = first;
      first = argv[i];
    }
  }
  console.log(second);
}
