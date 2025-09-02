const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();
const port = 1245;

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  res.write('This is the list of our students\n');
  const db = process.argv[2];

  countStudents(db)
    .then(() => res.end())
    .catch((err) => res.end(err.message));
});

app.listen(port);
module.exports = app;
