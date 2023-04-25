#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, (error, response) => {
  if (response) {
    console.log(`code: ${response.statusCode}`);
  } else {
    console.error(`Error requesting URL '${url}':`, error);
  }
});
