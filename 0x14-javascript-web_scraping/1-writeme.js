#!/usr/bin/node

const fs = require('fs');

const file = process.argv[2];
const text = process.argv[3];

try {
  fs.writeFileSync(file, text);
} catch (err) {
  console.log(err);
}
