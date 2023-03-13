#!/usr/bin/node

const number = process.argv[2];

if (!number || isNaN(number)) {
  console.log('Not a number');
} else {
  const intnumber = parseInt(number);
  console.log('My number: ' + intnumber);
}
