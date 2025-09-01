const express = require('express');
const countStudents = require('./3-read_file_async');

const databaseFile = process.argv[2]; // database.csv passed as argument

const app = express();

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  res.write('This is the list of our students\n');
  countStudents(databaseFile)
    .then(() => res.end())
    .catch((err) => {
      res.end(err.message);
    });
});

// Catch-all route for unknown endpoints (plain text)
app.use((req, res) => {
  res.status(404).send('Cannot GET ' + req.path);
});

app.listen(1245, () => {
  // eslint-disable-next-line no-console
  console.log('Express server running on port 1245');
});

module.exports = app;
