import taskBlock from './1-block-scoped.js';

console.log(taskBlock(true));   // should log: [false, true]
console.log(taskBlock(false));  // should log: [false, true]
