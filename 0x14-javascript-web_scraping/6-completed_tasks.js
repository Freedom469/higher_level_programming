#!/usr/bin/node

const request = require('request');

const url = 'https://jsonplaceholder.typicode.com/todos';

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Invalid status code:', response.statusCode);
    return;
  }

  const todos = JSON.parse(body);

  const completedByUser = {};

  todos.forEach((todo) => {
    if (todo.completed) {
      if (!completedByUser[todo.userId]) {
        completedByUser[todo.userId] = 1;
      } else {
        completedByUser[todo.userId]++;
      }
    }
  });

  console.log(completedByUser);
});
