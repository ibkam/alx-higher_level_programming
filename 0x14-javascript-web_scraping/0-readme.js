#!/usr/bin/node
// script that reads and prints the content of a file.
const fs = require('fs')
async function readfilecontent {
  try {
    const content = await fs.promise.readfile(filepath, 'utf-8');
    console.log(content)
  } catch (error) {
    console.log(error);
  }
}
if (process.argv.length < 3) {
  console.log(error);
} else {
  const filepath = process.argv[2];
  readfilecontent(filepath);
}
