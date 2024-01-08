#!/usr/bin/node
const { argv } = require('process');

console.log(factorial(parseInt(argv[2])));

function factorial (n) {
  if (isNaN(n) || n === 1 || n === 0) return 1;

  return n * factorial(n - 1);
}
