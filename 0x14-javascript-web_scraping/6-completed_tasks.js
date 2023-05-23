#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }

  const completedTodos = {};
  const todosObj = JSON.parse(body);
  for (const todo of todosObj) {
    if (todo.completed) {
      if (completedTodos[todo.userId]) {
        completedTodos[todo.userId]++;
      } else {
        completedTodos[todo.userId] = 1;
      }
    }
  }
  console.log(completedTodos);
});
