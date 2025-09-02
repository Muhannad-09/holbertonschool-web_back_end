const http = require('http');
const countStudents = require('./3-read_file_async');

const port = 1245;

const app = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  if (req.url === '/') {
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    res.write('This is the list of our students\n');
    const db = process.argv[2];
    countStudents(db)
      .then(() => res.end())
      .catch((err) => {
        res.end(err.toString());
      });
  } else {
    res.end('Hello Holberton School!');
  }
});

app.listen(port);

module.exports = app;
