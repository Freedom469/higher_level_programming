#!/usr/bin/node

const request = require('request');
const episode = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${episode}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error(`Error Loading movie data: ${error}`);
    return;
  }
  if (response.statusCode !== 200) {
    console.error(`Error: HTTP ${response.statusCode}`);
    return;
  }
  const name = JSON.parse(body);
  console.log(name.title);
});
