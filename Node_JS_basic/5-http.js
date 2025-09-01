const http = require('http');
const countStudents = require('./3-read_file_async');

const databaseFile = process.argv[2]; // database.csv passed as argument

const app = http.createServer((req, res) => {
  res.setHeader('Content-Type', 'text/plain');

  if (req.url === '/') {
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    res.write('This is the list of our students\n');
    countStudents(databaseFile)
      .then(() => res.end())
      .catch((err) => {
        res.end(err.message);
      });
  } else {
    res.statusCode = 404;
    res.end('Not Found');
  }
});

app.listen(1245, () => {
  // eslint-disable-next-line no-console
  console.log('Server running on port 1245');
});

module.exports = app;
