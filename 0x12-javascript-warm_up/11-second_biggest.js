#!/usr/bin/node
const { argv } = require('process');

if (argv.length <= 3) {
    console.log(0);
} else {
    let first = Number(argv[2]);
    let second = Number(argv[3]);

    for (let i = 3; i < argv.length; i++) {
        const currentNumber = Number(argv[i]);

        if (currentNumber > first) {
            second = first;
            first = currentNumber;
        } else if (currentNumber > second && currentNumber < first) {
            second = currentNumber;
        }
    }

    console.log(second);
}
