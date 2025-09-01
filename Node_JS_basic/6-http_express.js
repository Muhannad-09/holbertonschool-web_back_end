const express = require('express');

const app = express();

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

// Catch-all route for unknown endpoints (return plain text)
app.use((req, res) => {
  res.status(404).send('Cannot GET ' + req.path);
});

app.listen(1245, () => {
  // eslint-disable-next-line no-console
  console.log('Express server running on port 1245');
});

module.exports = app;
