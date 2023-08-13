#!/usr/bin/node
// script that computes the number of tasks completed by user id
const request = require('request');
const url = process.argv[2];

request(url, (error, body, response) => {
  if (error) {
    console.error(error);
  }
  const todo = JSON.parse(body);
  const completed = {};
  todos.forEach((todo) => {
    if (todo.completed && completed[todo.userId] === undefined) {
      completed[todo.userId] = 1;
    } else if (todo.completed) {
      completed[todo.userId] += 1;
    }
  });
  console.log(completed);
});
