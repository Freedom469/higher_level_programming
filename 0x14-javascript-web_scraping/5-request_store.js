#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filename = process.argv[3];

request(url, function (err, res, body) {
  if (err) {
    console.log(err);
    return;
  }

  fs.writeFile(filename, body, 'utf8', function (err) {
    if (err) {
      console.log(err);
    }
  });
});
