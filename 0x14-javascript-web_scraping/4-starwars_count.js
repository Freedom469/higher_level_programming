#!/usr/bin/node

// Require the 'request' library
const request = require('request');

// Set the character ID to search for
const id = '18';

// Get the URL to query from the command line arguments
const url = process.argv[2];

// Initialize a counter for the number of films containing the character
let count = 0;

// Make an HTTP GET request to the specified URL using 'request'
request.get(url, function (err, response, body) {
  if (err) {
    // Log any errors that occurred during the request
    console.log(err);
  } else {
    // Parse the response body as JSON
    const data = JSON.parse(body);

    // Iterate over each film in the 'results' array of the parsed response
    data.results.forEach((film) => {
      // Check if the 'characters' array of the film includes the given character ID
      film.characters.forEach((character) => {
        if (character.includes(id)) {
          // If the character ID is found, increment the counter
          count += 1;
        }
      });
    });

    // Log the final count of films containing the character to the console
    console.log(count);
  }
});
