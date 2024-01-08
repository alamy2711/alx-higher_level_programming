#!/usr/bin/node
const { argv } = require('process');
const size = parseInt(argv[2]);
let line = '';

if (isNaN(size)) console.log('Missing size');
else {
  for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) line += 'X';
    console.log(line);
    line = '';
  }
}
