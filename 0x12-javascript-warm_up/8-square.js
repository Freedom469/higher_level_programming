#!/usr/bin/node

const x = process.argv[2];

if (isNaN(x)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i++) {
    let output = '';

    for (let i = 0; i < x; i++) {
      output += 'X';
    }
    console.log(output);
  }
}
