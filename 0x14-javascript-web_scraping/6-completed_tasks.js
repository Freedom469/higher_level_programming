#!/usr/bin/node

const request = require('request');

request(process.argv[2], (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }

  const json = JSON.parse(body);
  const re = {};

  for (let i = 0; i < json.length; i++) {
    if (json[i].completed === true) {
      if (re[json[i].userId] === undefined) {
        re[json[i].userId] = 0;
      }

      re[json[i].userId]++;
    }
  }

  console.log(re);
});
