#!/usr/bin/node

const number = parseInt(process.argv[2]);

function factorial (number) {
  if (isNaN(number)) {
    return 1;
  }

  if (number === 0 || number === 1) {
    return 1;
  }

  return number * factorial(number - 1);
}

console.log(factorial(number));
