const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false,
});

rl.question('Welcome to Holberton School, what is your name?\n', (input) => {
  const name = input.replace(/\n$/, '');
  console.log(`Your name is: ${name}`);
  console.log('This important software is now closing');
  rl.close();
});
