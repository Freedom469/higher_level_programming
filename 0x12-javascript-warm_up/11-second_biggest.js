#!/usr/bin/node

const len = process.argv.length;

const argv = process.argv;

if (len === 2 || len === 3) {
  console.log('0');
} else {
  let max = argv[2];
  let max2 = argv[2];

  for (let i = 3; i < len; i++) {
    if (argv[i] > max) {
      max2 = max;
      max = argv[i];
    } else if (argv[i] > max2) {
      max2 = argv[i];
    }
  }

  console.log(max2);
}
