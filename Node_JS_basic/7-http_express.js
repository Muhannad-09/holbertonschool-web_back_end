const express = require('express');
const countStudents = require('./3-read_file_async');

const databaseFile = process.argv[2];

const app = express();

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  try {
    const output = await countStudents(databaseFile);
    res.send(`This is the list of our students\n${output}`);
  } catch (err) {
    res.send(err.message);
  }
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
